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
TRAIN_START = 15
POOL_SIZE = 5_000
POOL_SEED = 424242
MIN_N = 19
MAX_N = 400
CAL_WINDOW = 32
RIDGE = 25.0
RANDOM_REPLICATES = 20
VALID_MODELS = ("ridge_structure", "rolling20_structure", "knn_structure")
ALL_MODELS = VALID_MODELS + ("oracle_structure",)


def load_rows():
    parts = sorted(DATA.glob("super_keno_draws_part_*.csv"))
    df = pd.concat([pd.read_csv(p) for p in parts], ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    nums = [f"n{i}" for i in range(1, 21)]
    draws = [tuple(sorted(r[nums].astype(int).tolist())) for _, r in df.iterrows()]
    assert len(draws) == 195
    return df, draws


def draw_structure(nums):
    a = np.asarray(nums, dtype=float)
    s = set(int(x) for x in nums)
    gaps = np.diff(a)
    q = [np.mean((a >= lo) & (a <= hi)) for lo, hi in ((1,17),(18,35),(36,52),(53,70))]
    return np.asarray([
        *q,
        np.mean((a.astype(int) % 2) == 1),
        np.mean(a <= 35),
        (a.mean() - 35.5) / 20.0,
        a.std() / 20.0,
        sum(1 for x in s if x + 1 in s) / max(len(a) - 1, 1),
        (a.max() - a.min()) / 69.0,
        (gaps.std() if len(gaps) else 0.0) / 10.0,
    ], dtype=float)


def context(S, t):
    pieces = []
    for lag in (1,2,3):
        pieces.append(S[t-lag] if t >= lag else np.zeros(S.shape[1]))
    for w in (5,10,20,40):
        H = S[max(0,t-w):t]
        pieces.append(H.mean(axis=0) if len(H) else np.zeros(S.shape[1]))
    for w in (10,20):
        H = S[max(0,t-w):t]
        pieces.append(H.std(axis=0) if len(H) else np.zeros(S.shape[1]))
    return np.concatenate(pieces)


def ridge_predict(S, t):
    idx = range(TRAIN_START, t)
    A = np.vstack([context(S, s) for s in idx])
    Y = np.vstack([S[s] for s in idx])
    mean = A.mean(axis=0)
    sd = A.std(axis=0)
    sd[sd < 1e-8] = 1.0
    Z = (A - mean) / sd
    y_mean = Y.mean(axis=0)
    beta = np.linalg.solve(
        Z.T @ Z + RIDGE * np.eye(Z.shape[1]),
        Z.T @ (Y - y_mean),
    )
    return y_mean + ((context(S, t) - mean) / sd) @ beta


def rolling_predict(S, t):
    return S[max(0,t-20):t].mean(axis=0)


def knn_predict(S, t, k=8):
    current = context(S, t)
    candidates = []
    for s in range(TRAIN_START, t):
        c = context(S, s)
        candidates.append((float(np.mean((c-current)**2)), s))
    candidates.sort()
    idx = [s for _, s in candidates[:min(k, len(candidates))]]
    return S[idx].mean(axis=0) if idx else rolling_predict(S, t)


def ticket_structure(pool):
    return np.vstack([draw_structure(t) for t in pool])


def score_by_structure(ticket_struct, predicted):
    weights = np.asarray([2,2,2,2,1.25,1.0,1.5,0.8,0.7,0.5,0.5], dtype=float)
    diff = (ticket_struct - predicted[None,:]) * weights[None,:]
    return -np.sum(diff * diff, axis=1)


def choose_n(curves, t):
    prior = [s for s in range(max(WARMUP,t-CAL_WINDOW), t) if s in curves]
    if not prior:
        return MIN_N
    best = None
    for n in range(MIN_N, MAX_N+1):
        ratios = np.asarray([curves[s][n-1] / n for s in prior], dtype=float)
        avg = float(ratios.mean())
        q20 = float(np.quantile(ratios, 0.20))
        recent = float(ratios[-min(10,len(ratios)):].mean())
        downside = float(np.maximum(0.0, 1.0-ratios).mean())
        objective = 0.45*avg + 0.30*q20 + 0.25*recent - 0.15*downside
        key = (objective, q20, avg)
        if best is None or key > best[0]:
            best = (key, n)
    return int(best[1])


def aggregate(records):
    cost = int(sum(x["N"] for x in records))
    payout = float(sum(x["payout"] for x in records))
    capped = float(sum(x["capped15"] for x in records))
    return {
        "targets": len(records),
        "cost": cost,
        "payout": payout,
        "net_pl": payout-cost,
        "roi": payout/cost,
        "capped15_roi": capped/cost,
        "profitable_share": float(np.mean([x["payout"] > x["N"] for x in records])),
        "N_min": int(min(x["N"] for x in records)),
        "N_median": float(np.median([x["N"] for x in records])),
        "N_max": int(max(x["N"] for x in records)),
    }


def main():
    df, draws = load_rows()
    S = np.vstack([draw_structure(d) for d in draws])
    pool = random_unique_tickets(POOL_SIZE, POOL_SEED)
    ticket_struct = ticket_structure(pool)
    raw = payout_matrix(pool, draws, RuleSet()).astype(np.float64)
    cap15 = np.minimum(raw, 15.0)

    curves = {m:{} for m in ALL_MODELS}
    records = {m:[] for m in ALL_MODELS}
    random_records = {m:[[] for _ in range(RANDOM_REPLICATES)] for m in VALID_MODELS}
    prediction_errors = {m:[] for m in VALID_MODELS}

    for t in range(WARMUP, len(draws)):
        predictions = {
            "ridge_structure": ridge_predict(S, t),
            "rolling20_structure": rolling_predict(S, t),
            "knn_structure": knn_predict(S, t),
            "oracle_structure": S[t],
        }
        for mi, model in enumerate(ALL_MODELS):
            predicted = predictions[model]
            order = np.argsort(-score_by_structure(ticket_struct, predicted), kind="stable")[:MAX_N]
            raw_curve = np.cumsum(raw[order,t])
            capped_curve = np.cumsum(cap15[order,t])
            curves[model][t] = capped_curve
            n = choose_n(curves[model], t)
            records[model].append({
                "t": t,
                "date": str(df.loc[t,"date"].date()),
                "N": n,
                "payout": float(raw_curve[n-1]),
                "capped15": float(capped_curve[n-1]),
                "ratio": float(raw_curve[n-1] / n),
            })
            if model in VALID_MODELS:
                prediction_errors[model].append(float(np.sqrt(np.mean((predicted-S[t])**2))))
                for r in range(RANDOM_REPLICATES):
                    rng = np.random.default_rng(14_000_000 + mi*1_000_000 + r*10_007 + t)
                    idx = rng.choice(POOL_SIZE, n, replace=False)
                    random_records[model][r].append({
                        "t": t,
                        "N": n,
                        "payout": float(raw[idx,t].sum()),
                        "capped15": float(cap15[idx,t].sum()),
                    })

    result = {
        "method": {
            "pool_size": POOL_SIZE,
            "pool_seed": POOL_SEED,
            "models": list(VALID_MODELS),
            "oracle_diagnostic": True,
            "N_policy": f"free integer {MIN_N}..{MAX_N}",
            "no_future_leakage_for_valid_models": True,
        },
        "models": {},
    }

    for model in ALL_MODELS:
        strategy = aggregate(records[model])
        blocks = []
        for a,b in ((0,40),(40,80),(80,125)):
            block = {"rows":[WARMUP+a,WARMUP+b], "strategy": aggregate(records[model][a:b])}
            if model in VALID_MODELS:
                random_rois = np.asarray([aggregate(run[a:b])["roi"] for run in random_records[model]])
                block["random_roi_mean"] = float(random_rois.mean())
                block["above_random"] = bool(block["strategy"]["roi"] > random_rois.mean())
            blocks.append(block)
        rec = {"strategy": strategy, "blocks": blocks}
        if model in VALID_MODELS:
            rois = np.asarray([aggregate(run)["roi"] for run in random_records[model]])
            rec["random"] = {
                "roi_mean": float(rois.mean()),
                "roi_p05": float(np.quantile(rois,0.05)),
                "roi_p95": float(np.quantile(rois,0.95)),
                "replicates_beating_strategy": int(np.sum(rois >= strategy["roi"])),
            }
            rec["prediction_rmse_mean"] = float(np.mean(prediction_errors[model]))
        result["models"][model] = rec

    promoted = []
    for model in VALID_MODELS:
        rec = result["models"][model]
        beats = sum(1 for b in rec["blocks"] if b["above_random"])
        positive = sum(1 for b in rec["blocks"] if b["strategy"]["net_pl"] > 0)
        if rec["strategy"]["net_pl"] > 0 and rec["strategy"]["roi"] > rec["random"]["roi_mean"] and beats >= 2 and positive >= 2:
            promoted.append(model)
    result["decision"] = {
        "valid_promoted": promoted,
        "oracle_note": "oracle_structure uses target structure and is diagnostic only, never a valid strategy",
    }

    out = ROOT / "results" / "phase14_draw_structure.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
