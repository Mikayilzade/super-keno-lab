from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.phase14_draw_structure import (
    CAL_WINDOW,
    MAX_N,
    MIN_N,
    POOL_SEED,
    POOL_SIZE,
    TRAIN_START,
    WARMUP,
    aggregate,
    context,
    draw_structure,
    load_rows,
    ticket_structure,
)
from src.baselines import random_unique_tickets
from src.evaluator import payout_matrix
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
RANDOM_REPLICATES = 20
RIDGE = 25.0
KNN_K = 8

GROUPS = {
    "quadrants": [0, 1, 2, 3],
    "balance": [4, 5],
    "mean_location": [6],
    "dispersion_span_gaps": [7, 9, 10],
    "runs": [8],
}

PREDICTORS = ("expanding_mean", "rolling20", "ridge", "knn")


def choose_n(curves, t):
    prior = [s for s in range(max(WARMUP, t - CAL_WINDOW), t) if s in curves]
    if not prior:
        return MIN_N
    best = None
    for n in range(MIN_N, MAX_N + 1):
        ratios = np.asarray([curves[s][n - 1] / n for s in prior], dtype=float)
        avg = float(ratios.mean())
        q20 = float(np.quantile(ratios, 0.20))
        recent = float(ratios[-min(10, len(ratios)):].mean())
        downside = float(np.maximum(0.0, 1.0 - ratios).mean())
        objective = 0.45 * avg + 0.30 * q20 + 0.25 * recent - 0.15 * downside
        key = (objective, q20, avg)
        if best is None or key > best[0]:
            best = (key, n)
    return int(best[1])


def ridge_predict_group(S, t, dims):
    idx = range(TRAIN_START, t)
    A = np.vstack([context(S, s) for s in idx])
    Y = S[np.asarray(list(idx))][:, dims]
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


def predict_group(S, t, dims, predictor):
    if predictor == "expanding_mean":
        return S[:t, dims].mean(axis=0)
    if predictor == "rolling20":
        return S[max(0, t - 20):t, dims].mean(axis=0)
    if predictor == "ridge":
        return ridge_predict_group(S, t, dims)
    if predictor == "knn":
        current = context(S, t)
        candidates = []
        for s in range(TRAIN_START, t):
            candidates.append((float(np.mean((context(S, s) - current) ** 2)), s))
        candidates.sort()
        idx = [s for _, s in candidates[: min(KNN_K, len(candidates))]]
        if not idx:
            return S[:t, dims].mean(axis=0)
        return S[idx][:, dims].mean(axis=0)
    raise ValueError(predictor)


def group_scale(S, t, dims):
    sd = S[:t, dims].std(axis=0)
    return np.maximum(sd, 0.03)


def score_tickets(ticket_struct, target_group, dims, scale):
    diff = (ticket_struct[:, dims] - target_group[None, :]) / scale[None, :]
    return -np.mean(diff * diff, axis=1)


def rmse_scaled(pred, actual, scale):
    z = (np.asarray(pred) - np.asarray(actual)) / scale
    return float(np.sqrt(np.mean(z * z)))


def forecastability(S, dims):
    errors = {p: [] for p in PREDICTORS}
    per_target = []
    for t in range(WARMUP, len(S)):
        scale = group_scale(S, t, dims)
        actual = S[t, dims]
        rec = {"t": t}
        for p in PREDICTORS:
            pred = predict_group(S, t, dims, p)
            e = rmse_scaled(pred, actual, scale)
            errors[p].append(e)
            rec[p] = e
        per_target.append(rec)

    baseline = np.asarray(errors["expanding_mean"], dtype=float)
    out = {}
    for p in PREDICTORS:
        e = np.asarray(errors[p], dtype=float)
        blocks = []
        for a, b in ((0, 40), (40, 80), (80, 125)):
            eb = e[a:b]
            bb = baseline[a:b]
            skill = 1.0 - float(np.mean(eb * eb) / np.mean(bb * bb))
            blocks.append({
                "rmse_mean": float(eb.mean()),
                "mse_skill_vs_expanding": skill,
            })
        out[p] = {
            "rmse_mean": float(e.mean()),
            "mse_skill_vs_expanding": 1.0 - float(np.mean(e * e) / np.mean(baseline * baseline)),
            "blocks": blocks,
            "positive_skill_blocks": int(sum(1 for x in blocks if x["mse_skill_vs_expanding"] > 0)),
        }
    return out, per_target


def oracle_economic_value(df, draws, S, pool, ticket_struct, raw, cap15, name, dims):
    curves = {}
    records = []
    random_runs = [[] for _ in range(RANDOM_REPLICATES)]

    for t in range(WARMUP, len(draws)):
        scale = group_scale(S, t, dims)
        scores = score_tickets(ticket_struct, S[t, dims], dims, scale)
        order = np.argsort(-scores, kind="stable")[:MAX_N]
        raw_curve = np.cumsum(raw[order, t])
        capped_curve = np.cumsum(cap15[order, t])
        curves[t] = capped_curve
        n = choose_n(curves, t)
        records.append({
            "t": t,
            "date": str(df.loc[t, "date"].date()),
            "N": n,
            "payout": float(raw_curve[n - 1]),
            "capped15": float(capped_curve[n - 1]),
        })
        for r in range(RANDOM_REPLICATES):
            rng = np.random.default_rng(15_000_000 + 1_000_000 * list(GROUPS).index(name) + r * 10_007 + t)
            idx = rng.choice(POOL_SIZE, n, replace=False)
            random_runs[r].append({
                "t": t,
                "N": n,
                "payout": float(raw[idx, t].sum()),
                "capped15": float(cap15[idx, t].sum()),
            })

    strategy = aggregate(records)
    random_summaries = [aggregate(x) for x in random_runs]
    random_rois = np.asarray([x["roi"] for x in random_summaries], dtype=float)
    blocks = []
    for a, b in ((0, 40), (40, 80), (80, 125)):
        s = aggregate(records[a:b])
        rr = np.asarray([aggregate(run[a:b])["roi"] for run in random_runs], dtype=float)
        blocks.append({
            "strategy": s,
            "random_roi_mean": float(rr.mean()),
            "oracle_lift_vs_random": float(s["roi"] - rr.mean()),
        })
    return {
        "strategy": strategy,
        "random_roi_mean": float(random_rois.mean()),
        "random_roi_p05": float(np.quantile(random_rois, 0.05)),
        "random_roi_p95": float(np.quantile(random_rois, 0.95)),
        "oracle_lift_vs_random": float(strategy["roi"] - random_rois.mean()),
        "random_replicates_beating_oracle": int(np.sum(random_rois >= strategy["roi"])),
        "blocks": blocks,
    }


def combo_oracle(df, draws, S, pool, ticket_struct, raw, cap15, groups):
    dims = sorted(set(d for g in groups for d in GROUPS[g]))
    curves = {}
    records = []
    for t in range(WARMUP, len(draws)):
        scale = group_scale(S, t, dims)
        scores = score_tickets(ticket_struct, S[t, dims], dims, scale)
        order = np.argsort(-scores, kind="stable")[:MAX_N]
        raw_curve = np.cumsum(raw[order, t])
        capped_curve = np.cumsum(cap15[order, t])
        curves[t] = capped_curve
        n = choose_n(curves, t)
        records.append({"t": t, "N": n, "payout": float(raw_curve[n - 1]), "capped15": float(capped_curve[n - 1])})
    return {"groups": list(groups), "dims": dims, "strategy": aggregate(records)}


def main():
    df, draws = load_rows()
    S = np.vstack([draw_structure(d) for d in draws])
    pool = random_unique_tickets(POOL_SIZE, POOL_SEED)
    ticket_struct = ticket_structure(pool)
    raw = payout_matrix(pool, draws, RuleSet()).astype(np.float64)
    cap15 = np.minimum(raw, 15.0)

    result = {
        "method": {
            "pool_size": POOL_SIZE,
            "pool_seed": POOL_SEED,
            "groups": GROUPS,
            "predictors": list(PREDICTORS),
            "N_policy": f"free integer {MIN_N}..{MAX_N} selected only from earlier capped15 curves",
            "oracle_is_diagnostic_only": True,
            "valid_forecastability_is_strict_walk_forward": True,
        },
        "groups": {},
    }

    for name, dims in GROUPS.items():
        forecast, _ = forecastability(S, dims)
        oracle = oracle_economic_value(df, draws, S, pool, ticket_struct, raw, cap15, name, dims)
        best_predictor = max(
            PREDICTORS,
            key=lambda p: (forecast[p]["positive_skill_blocks"], forecast[p]["mse_skill_vs_expanding"]),
        )
        result["groups"][name] = {
            "dims": dims,
            "oracle": oracle,
            "forecastability": forecast,
            "best_predictor_by_predeclared_rule": best_predictor,
            "best_forecast_skill": forecast[best_predictor]["mse_skill_vs_expanding"],
            "best_positive_skill_blocks": forecast[best_predictor]["positive_skill_blocks"],
        }

    # Diagnostic combinations are selected only from oracle lift and are never treated as valid strategy evidence.
    ranked = sorted(
        GROUPS,
        key=lambda g: result["groups"][g]["oracle"]["oracle_lift_vs_random"],
        reverse=True,
    )
    result["diagnostic_combinations"] = [
        combo_oracle(df, draws, S, pool, ticket_struct, raw, cap15, ranked[:2]),
        combo_oracle(df, draws, S, pool, ticket_struct, raw, cap15, ranked[:3]),
    ]

    table = []
    for name in GROUPS:
        rec = result["groups"][name]
        table.append({
            "group": name,
            "oracle_roi": rec["oracle"]["strategy"]["roi"],
            "random_roi_mean": rec["oracle"]["random_roi_mean"],
            "oracle_lift": rec["oracle"]["oracle_lift_vs_random"],
            "best_predictor": rec["best_predictor_by_predeclared_rule"],
            "forecast_skill": rec["best_forecast_skill"],
            "positive_skill_blocks": rec["best_positive_skill_blocks"],
            "value_x_positive_skill": rec["oracle"]["oracle_lift_vs_random"] * max(0.0, rec["best_forecast_skill"]),
        })
    result["value_forecastability_table"] = table

    candidates = [
        r for r in table
        if r["oracle_lift"] >= 0.10 and r["forecast_skill"] > 0 and r["positive_skill_blocks"] >= 2
    ]
    result["decision"] = {
        "promising_groups": [r["group"] for r in candidates],
        "promotion_rule": "oracle lift >= 0.10, positive forecast MSE skill overall, and positive skill in >=2/3 blocks",
    }

    out = ROOT / "results" / "phase15_oracle_factor_decomposition.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"table": table, "decision": result["decision"], "combinations": result["diagnostic_combinations"]}, indent=2))


if __name__ == "__main__":
    main()
