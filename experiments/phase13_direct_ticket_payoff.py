from __future__ import annotations

import json
import sys
from dataclasses import dataclass
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
TRAIN_START = 20
POOL_SIZE = 5_000
POOL_SEED = 424242  # deliberately reuse Phase-12 universe; no new favorable pool seed
MIN_N = 19
MAX_N = 400
CAL_WINDOW = 32
RIDGE = 50.0
RANDOM_REPLICATES = 20
FAIR_P = 20.0 / 70.0
MODEL_NAMES = ("ridge_cap15", "ridge_cap5", "ridge_profit_ticket", "empirical_cap15")


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
        assert len(vals) == 20 and len(set(vals)) == 20
        X[i, np.asarray(vals) - 1] = 1
        draws.append(vals)
    assert len(draws) == 195
    return df, X, draws


def zscore(v):
    v = np.asarray(v, dtype=float)
    sd = float(v.std())
    return (v - v.mean()) / (sd if sd > 1e-9 else 1.0)


def pool_incidence(pool):
    M = np.zeros((len(pool), 70), dtype=np.float64)
    for i, ticket in enumerate(pool):
        M[i, np.asarray(ticket, dtype=int) - 1] = 1.0
    return M


def static_features(pool):
    rows = []
    for ticket in pool:
        a = np.asarray(ticket, dtype=float)
        s = set(int(x) for x in ticket)
        gaps = np.diff(a)
        q = [np.mean((a >= lo) & (a <= hi)) for lo, hi in ((1,17),(18,35),(36,52),(53,70))]
        rows.append([
            (a.mean() - 35.5) / 20.0,
            a.std() / 20.0,
            np.mean(a <= 35),
            np.mean((a.astype(int) % 2) == 1),
            *q,
            sum(1 for x in s if x + 1 in s) / 9.0,
            (a.max() - a.min()) / 69.0,
            (gaps.std() if len(gaps) else 0.0) / 10.0,
        ])
    return np.asarray(rows, dtype=np.float64)


def number_gap_score(X, t):
    g = np.zeros(70, dtype=float)
    for j in range(70):
        hits = np.flatnonzero(X[:t, j])
        gap = t - int(hits[-1]) if len(hits) else min(t, 50)
        g[j] = min(gap, 50) / 50.0
    return zscore(g)


def pair_residual(X, t, window=40):
    H = X[max(0, t-window):t].astype(float)
    if len(H) < 8:
        return np.zeros((70,70), dtype=float)
    c = H.sum(axis=0)
    C = H.T @ H
    exp = np.outer(c, c) / max(len(H), 1)
    R = (C - exp) / np.sqrt(exp + 5.0)
    np.fill_diagonal(R, 0.0)
    return R


def ticket_features(M, static, X, t):
    cols = []
    for w in (5, 10, 20, 40, 80):
        H = X[max(0, t-w):t]
        f = H.mean(axis=0) if len(H) else np.full(70, FAIR_P)
        z = zscore(f - FAIR_P)
        mean = (M @ z) / 10.0
        second = (M @ (z*z)) / 10.0
        cols += [mean, np.sqrt(np.maximum(0.0, second - mean*mean))]

    gap = number_gap_score(X, t)
    gap_mean = (M @ gap) / 10.0
    gap_second = (M @ (gap*gap)) / 10.0
    cols += [gap_mean, np.sqrt(np.maximum(0.0, gap_second-gap_mean*gap_mean))]

    if t:
        prev = X[t-1].astype(float)
        cols.append((M @ prev) / 10.0)
    else:
        cols.append(np.zeros(len(M)))
    if t >= 2:
        cols.append((M @ X[t-2].astype(float)) / 10.0)
    else:
        cols.append(np.zeros(len(M)))

    R = pair_residual(X, t, 40)
    # Average residual among the 45 unordered pairs inside a 10-number ticket.
    pair_internal = ((M @ R) * M).sum(axis=1) / 90.0
    cols.append(zscore(pair_internal))

    if t:
        context = zscore(R[X[t-1].astype(bool)].sum(axis=0))
        cols.append((M @ context) / 10.0)
    else:
        cols.append(np.zeros(len(M)))

    # Closeness of ticket structure to rolling draw-level structure.
    hist = X[max(0,t-20):t]
    if len(hist):
        nums = np.arange(1,71)
        draw_low = hist[:,:35].sum(axis=1).mean() / 20.0
        draw_odd = hist[:,(nums % 2)==1].sum(axis=1).mean() / 20.0
        draw_mean_num = ((hist * nums[None,:]).sum(axis=1) / 20.0).mean()
    else:
        draw_low, draw_odd, draw_mean_num = 0.5, 0.5, 35.5

    # static columns: mean_num, std_num, low35, odd, q1..q4, runs, range, gapstd
    cols.append(-np.abs(static[:,2] - draw_low))
    cols.append(-np.abs(static[:,3] - draw_odd))
    cols.append(-np.abs((static[:,0]*20.0 + 35.5) - draw_mean_num) / 20.0)

    F = np.column_stack([np.ones(len(M)), *cols, *[static[:,j] for j in range(static.shape[1])]])
    return F.astype(np.float64)


def solve_ridge(xtx, xty, penalty=RIDGE):
    reg = np.eye(xtx.shape[0]) * penalty
    reg[0,0] = 0.0
    return np.linalg.solve(xtx + reg, xty)


def choose_n_from_prior(curves, t):
    prior = [s for s in range(max(WARMUP, t-CAL_WINDOW), t) if s in curves]
    if not prior:
        return MIN_N
    best = None
    for n in range(MIN_N, MAX_N+1):
        ratios = np.asarray([curves[s][n-1] / n for s in prior], dtype=float)
        avg = float(ratios.mean())
        q20 = float(np.quantile(ratios, 0.20))
        recent = float(ratios[-min(10,len(ratios)):].mean())
        downside = float(np.maximum(0.0, 1.0-ratios).mean())
        obj = 0.45*avg + 0.30*q20 + 0.25*recent - 0.15*downside
        key = (obj, q20, avg)
        if best is None or key > best[0]:
            best = (key, n)
    return int(best[1])


def aggregate(records):
    cost = int(sum(r["N"] for r in records))
    payout = float(sum(r["payout"] for r in records))
    capped = float(sum(r["capped15"] for r in records))
    return {
        "targets": len(records),
        "cost": cost,
        "payout": payout,
        "net_pl": payout-cost,
        "roi": payout/cost if cost else 1.0,
        "capped15_roi": capped/cost if cost else 1.0,
        "profitable_share": float(np.mean([r["payout"] > r["N"] for r in records])),
        "N_min": int(min(r["N"] for r in records)),
        "N_median": float(np.median([r["N"] for r in records])),
        "N_max": int(max(r["N"] for r in records)),
    }


def main():
    df, X, draws = load_rows()
    pool = random_unique_tickets(POOL_SIZE, POOL_SEED)
    M = pool_incidence(pool)
    static = static_features(pool)
    rules = RuleSet()

    # Exact payouts of every fixed-pool ticket on every historical draw.
    raw_pm = payout_matrix(pool, draws, rules).astype(np.float64)
    cap15_pm = np.minimum(raw_pm, 15.0)
    cap5_pm = np.minimum(raw_pm, 5.0)
    profit_pm = (raw_pm > 1.0).astype(np.float64)

    # Build sufficient statistics only from historical labels available before each target.
    sample_F = ticket_features(M, static, X, TRAIN_START)
    d = sample_F.shape[1]
    xtx = np.zeros((d,d), dtype=np.float64)
    xty15 = np.zeros(d, dtype=np.float64)
    xty5 = np.zeros(d, dtype=np.float64)
    xtyp = np.zeros(d, dtype=np.float64)
    empirical_sum = np.zeros(POOL_SIZE, dtype=np.float64)
    empirical_n = 0

    def add_training_target(s):
        nonlocal xtx, xty15, xty5, xtyp, empirical_sum, empirical_n
        F = ticket_features(M, static, X, s)
        xtx += F.T @ F
        xty15 += F.T @ cap15_pm[:,s]
        xty5 += F.T @ cap5_pm[:,s]
        xtyp += F.T @ profit_pm[:,s]
        empirical_sum += cap15_pm[:,s]
        empirical_n += 1

    for s in range(TRAIN_START, WARMUP):
        add_training_target(s)

    curves = {name:{} for name in MODEL_NAMES}
    records = {name:[] for name in MODEL_NAMES}
    random_records = {name:[[] for _ in range(RANDOM_REPLICATES)] for name in MODEL_NAMES}
    tier_payout = {name:{str(h):0.0 for h in range(11)} for name in MODEL_NAMES}

    for t in range(WARMUP, len(draws)):
        F = ticket_features(M, static, X, t)
        betas = {
            "ridge_cap15": solve_ridge(xtx, xty15),
            "ridge_cap5": solve_ridge(xtx, xty5),
            "ridge_profit_ticket": solve_ridge(xtx, xtyp),
        }
        scores = {name:F @ beta for name,beta in betas.items()}
        scores["empirical_cap15"] = empirical_sum / max(empirical_n,1)

        for mi, name in enumerate(MODEL_NAMES):
            order = np.argsort(-scores[name], kind="stable")[:MAX_N]
            raw_curve = np.cumsum(raw_pm[order,t])
            capped_curve = np.cumsum(cap15_pm[order,t])
            curves[name][t] = capped_curve
            n = choose_n_from_prior(curves[name], t)
            chosen = order[:n]
            payout = float(raw_curve[n-1])
            capped = float(capped_curve[n-1])
            hits = (M[chosen] @ X[t].astype(float)).astype(int)
            for h in range(11):
                count = int(np.sum(hits == h))
                tier_payout[name][str(h)] += count * rules.gross_for_hits(h)
            rec = {
                "t": t,
                "date": str(df.loc[t,"date"].date()),
                "N": n,
                "payout": payout,
                "capped15": capped,
                "ratio": payout/n,
            }
            records[name].append(rec)

            # Matched-N random selection from the exact same fixed universe.
            for r in range(RANDOM_REPLICATES):
                rng = np.random.default_rng(13_000_000 + mi*1_000_000 + r*10_007 + t)
                idx = rng.choice(POOL_SIZE, n, replace=False)
                rp = float(raw_pm[idx,t].sum())
                rc = float(cap15_pm[idx,t].sum())
                random_records[name][r].append({"t":t,"N":n,"payout":rp,"capped15":rc})

        # Only after target t is fully frozen/scored does it become training data.
        add_training_target(t)

    result = {
        "method": {
            "pool_size": POOL_SIZE,
            "pool_seed": POOL_SEED,
            "pool_note": "same fixed universe as Phase 12; no new pool seed selected",
            "warmup": WARMUP,
            "train_start": TRAIN_START,
            "ridge": RIDGE,
            "N_policy": f"free integer {MIN_N}..{MAX_N}, chosen from prior capped15 prefix curves only",
            "random_replicates": RANDOM_REPLICATES,
            "models": list(MODEL_NAMES),
            "no_future_leakage": True,
        },
        "models": {},
    }

    for name in MODEL_NAMES:
        strat = aggregate(records[name])
        rnd = [aggregate(x) for x in random_records[name]]
        rois = np.asarray([x["roi"] for x in rnd], dtype=float)
        blocks = []
        for a,b in ((0,40),(40,80),(80,125)):
            sb = aggregate(records[name][a:b])
            rbrois = np.asarray([aggregate(run[a:b])["roi"] for run in random_records[name]])
            blocks.append({
                "rows": [WARMUP+a, WARMUP+b],
                "dates": [records[name][a]["date"], records[name][b-1]["date"]],
                "strategy": sb,
                "random_roi_mean": float(rbrois.mean()),
                "strategy_above_random_mean": bool(sb["roi"] > rbrois.mean()),
            })
        high = sum(v for h,v in tier_payout[name].items() if int(h) >= 8)
        result["models"][name] = {
            "strategy": strat,
            "random": {
                "roi_mean": float(rois.mean()),
                "roi_std": float(rois.std(ddof=1)),
                "roi_p05": float(np.quantile(rois,0.05)),
                "roi_p95": float(np.quantile(rois,0.95)),
                "best_roi": float(rois.max()),
                "replicates_beating_strategy": int(np.sum(rois >= strat["roi"])),
                "empirical_one_sided_p": float((np.sum(rois >= strat["roi"])+1)/(RANDOM_REPLICATES+1)),
            },
            "blocks": blocks,
            "payout_by_hit_tier": tier_payout[name],
            "share_payout_from_8plus": float(high / strat["payout"] if strat["payout"] else 0.0),
            "records": records[name],
        }

    # Promotion is predefined and intentionally strict.
    promoted = []
    for name, rec in result["models"].items():
        positive_blocks = sum(1 for b in rec["blocks"] if b["strategy"]["net_pl"] > 0)
        beats_blocks = sum(1 for b in rec["blocks"] if b["strategy_above_random_mean"])
        if (
            rec["strategy"]["net_pl"] > 0
            and rec["strategy"]["roi"] > rec["random"]["roi_mean"]
            and beats_blocks >= 2
            and positive_blocks >= 2
        ):
            promoted.append(name)
    result["decision"] = {"promoted": promoted, "any_gate_passed": bool(promoted)}

    out = ROOT / "results" / "phase13_direct_ticket_payoff.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    lines = [
        "# Phase 13 — direct ticket-payoff ranking with deterministic execution",
        "",
        "Date: 2026-08-25",
        "",
        f"Fixed universe: **{POOL_SIZE} tickets**, seed `{POOL_SEED}` reused from Phase 12. N free **{MIN_N}..{MAX_N}**. Each model compared with **{RANDOM_REPLICATES} matched-N random replicas** from the same universe.",
        "",
        "| model | ROI | P/L | random mean ROI | blocks > random | positive blocks | 8+ payout share |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, rec in result["models"].items():
        beats = sum(1 for b in rec["blocks"] if b["strategy_above_random_mean"])
        pos = sum(1 for b in rec["blocks"] if b["strategy"]["net_pl"] > 0)
        lines.append(
            f"| {name} | {rec['strategy']['roi']:.4f} | {rec['strategy']['net_pl']:.0f} | {rec['random']['roi_mean']:.4f} | {beats}/3 | {pos}/3 | {rec['share_payout_from_8plus']:.1%} |"
        )
    lines += [
        "",
        f"Promotion gate passed: **{bool(promoted)}**. Promoted: `{promoted}`.",
        "",
        "The models are trained on ticket payout/capped utility directly, not number-hit probability. Training for target t ends at t-1. N is chosen only from prior capped prefix curves. Rare 8+ payout concentration is reported explicitly.",
    ]
    (ROOT / "results" / "PHASE13_DIRECT_TICKET_PAYOFF.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(json.dumps({k:{"strategy":v["strategy"],"random":v["random"],"blocks":v["blocks"]} for k,v in result["models"].items()}, indent=2))
    print(result["decision"])


if __name__ == "__main__":
    main()
