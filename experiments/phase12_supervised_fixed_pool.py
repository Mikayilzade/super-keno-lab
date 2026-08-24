from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.baselines import random_unique_tickets
from src.evaluator import payout_matrix
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
WARMUP = 70
MIN_N = 19
MAX_N = 300
CAL_WINDOW = 32
POOL_SIZE = 5_000
POOL_SEED = 424242
RIDGE = 20.0


def load_rows():
    parts = sorted(DATA.glob("super_keno_draws_part_*.csv"))
    df = pd.concat([pd.read_csv(p) for p in parts], ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    nums = [f"n{i}" for i in range(1, 21)]
    X = np.zeros((len(df), 70), dtype=np.int8)
    draws = []
    for i, row in df.iterrows():
        vals = tuple(sorted(row[nums].astype(int).tolist()))
        X[i, np.asarray(vals) - 1] = 1
        draws.append(vals)
    assert len(draws) == 195
    return df, X, draws


def zscore(v):
    v = np.asarray(v, dtype=float)
    s = float(v.std())
    return (v - v.mean()) / (s if s > 1e-9 else 1.0)


def pair_context(X, t, window=20):
    if t < 2:
        return np.zeros(70, dtype=float)
    H = X[max(0, t - window):t].astype(float)
    c = H.sum(axis=0)
    C = H.T @ H
    expected = np.outer(c, c) / max(len(H), 1)
    residual = (C - expected) / np.sqrt(expected + 5.0)
    np.fill_diagonal(residual, 0.0)
    return zscore(residual[X[t - 1].astype(bool)].sum(axis=0))


def features_at(X, t):
    columns = []
    for window in (5, 10, 20, 40, 80):
        H = X[max(0, t - window):t]
        freq = H.mean(axis=0) if len(H) else np.full(70, 20 / 70)
        columns.append(freq - 20 / 70)

    gap = np.zeros(70, dtype=float)
    for number in range(70):
        hits = np.flatnonzero(X[:t, number])
        g = t - hits[-1] if len(hits) else min(t, 40)
        gap[number] = min(g, 40) / 40

    previous = X[t - 1].astype(float) if t else np.zeros(70)
    reversion = np.zeros(70, dtype=float)
    if t:
        for a, b in ((0, 17), (17, 35), (35, 52), (52, 70)):
            reversion[a:b] = 20 * (b - a) / 70 - X[t - 1, a:b].sum()

    return np.column_stack(
        columns + [gap, previous, pair_context(X, t), zscore(reversion)]
    )


def ridge_fit(features, y, penalty=RIDGE):
    mean = features.mean(axis=0)
    sd = features.std(axis=0)
    sd[sd < 1e-8] = 1.0
    A = (features - mean) / sd
    y_mean = float(y.mean())
    beta = np.linalg.solve(
        A.T @ A + penalty * np.eye(A.shape[1]),
        A.T @ (y - y_mean),
    )
    return mean, sd, y_mean, beta


def ticket_payout(ticket, draw):
    hits = len(set(ticket) & set(draw))
    return RuleSet().gross_for_hits(hits)


def aggregate(records):
    cost = int(sum(r["N"] for r in records))
    payout = float(sum(r["payout"] for r in records))
    return {
        "cost": cost,
        "payout": payout,
        "net_pl": payout - cost,
        "roi": payout / cost,
        "profitable_share": float(np.mean([r["payout"] > r["N"] for r in records])),
        "N_min": int(min(r["N"] for r in records)),
        "N_median": float(np.median([r["N"] for r in records])),
        "N_max": int(max(r["N"] for r in records)),
    }


def main():
    df, X, draws = load_rows()
    feature_tensor = [features_at(X, t) for t in range(len(draws))]

    pool = random_unique_tickets(POOL_SIZE, POOL_SEED)
    incidence = np.zeros((POOL_SIZE, 70), dtype=np.uint8)
    for i, ticket in enumerate(pool):
        incidence[i, np.asarray(ticket) - 1] = 1

    realized_curves = {}
    records = []
    random_records = []

    for t in range(WARMUP, len(draws)):
        historical_targets = range(20, t)
        train_X = np.vstack([feature_tensor[s] for s in historical_targets])
        train_y = np.concatenate([X[s].astype(float) for s in historical_targets])
        mean, sd, y_mean, beta = ridge_fit(train_X, train_y)

        target_X = (feature_tensor[t] - mean) / sd
        probabilities = np.clip(y_mean + target_X @ beta, 0.05, 0.55)

        ticket_scores = incidence @ probabilities
        order = np.argsort(-ticket_scores, kind="stable")[:MAX_N]
        ticket_values = np.asarray(
            [ticket_payout(pool[int(i)], draws[t]) for i in order], dtype=float
        )
        cumulative = np.cumsum(ticket_values)
        realized_curves[t] = cumulative

        prior_targets = [
            s for s in range(max(WARMUP, t - CAL_WINDOW), t) if s in realized_curves
        ]
        best = None
        for n in range(MIN_N, MAX_N + 1):
            ratios = (
                np.asarray([realized_curves[s][n - 1] / n for s in prior_targets])
                if prior_targets
                else np.asarray([0.0])
            )
            avg = float(ratios.mean())
            q20 = float(np.quantile(ratios, 0.20))
            recent = float(ratios[-min(10, len(ratios)):].mean())
            downside = float(np.maximum(0.0, 1.0 - ratios).mean())
            objective = 0.45 * avg + 0.30 * q20 + 0.25 * recent - 0.15 * downside
            key = (objective, q20, avg)
            if best is None or key > best[0]:
                best = (key, n)

        n = int(best[1])
        payout = float(cumulative[n - 1])
        records.append({"t": t, "N": n, "payout": payout, "ratio": payout / n})

        random_portfolio = random_unique_tickets(n, 8_000_000 + t)
        random_payout = float(
            payout_matrix(random_portfolio, [draws[t]], RuleSet()).sum()
        )
        random_records.append(
            {"t": t, "N": n, "payout": random_payout, "ratio": random_payout / n}
        )

    blocks = []
    for a, b in ((0, 40), (40, 80), (80, 125)):
        blocks.append(
            {
                "rows": [WARMUP + a, WARMUP + b],
                "strategy": aggregate(records[a:b]),
                "matched_random": aggregate(random_records[a:b]),
            }
        )

    result = {
        "method": {
            "pool_size": POOL_SIZE,
            "pool_seed": POOL_SEED,
            "ridge_penalty": RIDGE,
            "features": [
                "freq5", "freq10", "freq20", "freq40", "freq80",
                "gap", "previous_hit", "pair_context", "group_reversion",
            ],
            "N_policy": "free integer 19..300 chosen from trailing 32 realized target curves",
            "no_future_leakage": True,
        },
        "strategy": aggregate(records),
        "matched_random": aggregate(random_records),
        "blocks": blocks,
        "records": records,
    }

    out = ROOT / "results" / "phase12_supervised_fixed_pool.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("strategy", "matched_random", "blocks")}, indent=2))


if __name__ == "__main__":
    main()
