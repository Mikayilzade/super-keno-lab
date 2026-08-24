from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
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
CANDIDATES = 320
CAL_WINDOW = 32
RECENT_META = 18
MIN_N = 19
MAX_N = 320
PAYOUT_CAP_FOR_RANKING = 15.0


@dataclass(frozen=True)
class Config:
    name: str
    family: str
    beta: float
    freq_window: int = 40
    pair_window: int = 20


CONFIGS = [
    Config("hot_b06", "hot", 0.6, 40, 20),
    Config("hot_b10", "hot", 1.0, 80, 20),
    Config("cold_b06", "cold", 0.6, 40, 20),
    Config("cold_b10", "cold", 1.0, 80, 20),
    Config("pair_b07", "pair", 0.7, 40, 20),
    Config("pair_b11", "pair", 1.1, 40, 40),
    Config("revert_b07", "reversion", 0.7, 40, 20),
    Config("ensemble_b06", "ensemble", 0.6, 80, 20),
    Config("ensemble_b10", "ensemble", 1.0, 80, 20),
]


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
    s = float(v.std())
    return (v - v.mean()) / (s if s > 1e-9 else 1.0)


def frequency_score(X, t, window, cold=False):
    H = X[max(0, t - window):t]
    f = H.mean(axis=0)
    return -zscore(f) if cold else zscore(f)


def pair_score(X, dates, t, window):
    if t < 2 or (dates[t - 1] - dates[t - 2]).days != 1:
        return np.zeros(70, dtype=float)
    H = X[max(0, t - window):t].astype(float)
    if len(H) < 8:
        return np.zeros(70, dtype=float)
    c = H.sum(0)
    C = H.T @ H
    exp = np.outer(c, c) / max(len(H), 1)
    R = (C - exp) / np.sqrt(exp + 5.0)
    np.fill_diagonal(R, 0.0)
    context = X[t - 1].astype(bool)
    return zscore(R[context].sum(axis=0))


def reversion_score(X, t):
    if t < 1:
        return np.zeros(70, dtype=float)
    groups = [(0, 17), (17, 35), (35, 52), (52, 70)]
    prev = X[t - 1]
    score = np.zeros(70, dtype=float)
    for a, b in groups:
        expected = 20.0 * (b - a) / 70.0
        observed = float(prev[a:b].sum())
        # If a group was overrepresented, mildly downweight it next time; vice versa.
        score[a:b] = expected - observed
    return zscore(score)


def signal_for(config, X, dates, t):
    if config.family == "hot":
        return frequency_score(X, t, config.freq_window, cold=False)
    if config.family == "cold":
        return frequency_score(X, t, config.freq_window, cold=True)
    if config.family == "pair":
        return pair_score(X, dates, t, config.pair_window)
    if config.family == "reversion":
        return reversion_score(X, t)
    if config.family == "ensemble":
        cold = frequency_score(X, t, config.freq_window, cold=True)
        pair = pair_score(X, dates, t, config.pair_window)
        rev = reversion_score(X, t)
        return zscore(0.35 * cold + 0.45 * pair + 0.20 * rev)
    raise ValueError(config.family)


def weighted_unique_tickets(score, n, beta, seed):
    rng = np.random.default_rng(seed)
    s = zscore(score)
    weights = np.exp(np.clip(beta * s, -4.0, 4.0))
    weights = weights / weights.sum()
    seen = set()
    out = []
    attempts = 0
    while len(out) < n and attempts < n * 100:
        attempts += 1
        t = tuple(sorted((rng.choice(70, 10, replace=False, p=weights) + 1).tolist()))
        if t not in seen:
            seen.add(t)
            out.append(t)
    if len(out) < n:
        # Deterministic random fill keeps the experiment total and reproducible.
        for t in random_unique_tickets(n * 2, seed + 991):
            if t not in seen:
                seen.add(t)
                out.append(t)
                if len(out) >= n:
                    break
    return out[:n]


def choose_prefix(tickets, past_draws):
    pm = payout_matrix(tickets, past_draws, RuleSet()).astype(np.float64)
    capped = np.minimum(pm, PAYOUT_CAP_FOR_RANKING)
    recent_weight = np.linspace(0.65, 1.35, pm.shape[1])
    ticket_score = (capped * recent_weight[None, :]).mean(axis=1)
    order = np.argsort(-ticket_score, kind="stable")
    ordered = pm[order]
    cumulative = ordered.cumsum(axis=0)

    best = None
    upper = min(MAX_N, len(tickets))
    for n in range(MIN_N, upper + 1):
        ratio = cumulative[n - 1] / n
        avg = float(ratio.mean())
        q20 = float(np.quantile(ratio, 0.20))
        recent = float(ratio[-min(10, len(ratio)):].mean())
        downside = float(np.mean(np.maximum(0.0, 1.0 - ratio)))
        objective = 0.45 * avg + 0.30 * q20 + 0.25 * recent - 0.15 * downside
        rec = {
            "N": n,
            "objective": objective,
            "cal_avg_ratio": avg,
            "cal_q20_ratio": q20,
            "cal_recent_ratio": recent,
            "cal_min_ratio": float(ratio.min()),
        }
        if best is None or (objective, q20, avg) > (
            best[0]["objective"], best[0]["cal_q20_ratio"], best[0]["cal_avg_ratio"]
        ):
            best = (rec, order[:n])
    assert best is not None
    rec, idx = best
    return [tickets[int(i)] for i in idx], rec


def score_portfolio(portfolio, draw):
    payout = float(payout_matrix(portfolio, [draw], RuleSet()).sum())
    cost = len(portfolio)
    return {
        "N": cost,
        "payout": payout,
        "pl": payout - cost,
        "ratio": payout / cost if cost else 1.0,
        "profitable": bool(payout > cost),
    }


def max_drawdown(pl_values):
    equity = np.cumsum(np.asarray(pl_values, dtype=float))
    if len(equity) == 0:
        return 0.0
    running = np.maximum.accumulate(np.r_[0.0, equity])
    dd = running[1:] - equity
    return float(dd.max())


def max_losing_streak(pl_values):
    best = cur = 0
    for x in pl_values:
        if x < 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return int(best)


def aggregate(records):
    played = [r for r in records if r["N"] > 0]
    cost = float(sum(r["N"] for r in played))
    payout = float(sum(r["payout"] for r in played))
    pls = [float(r["pl"]) for r in records]
    ns = [r["N"] for r in played]
    return {
        "targets": len(records),
        "played": len(played),
        "abstained": len(records) - len(played),
        "total_cost": cost,
        "total_payout": payout,
        "net_pl": payout - cost,
        "roi": payout / cost if cost else 1.0,
        "profitable_share_of_played": float(np.mean([r["pl"] > 0 for r in played])) if played else 0.0,
        "max_drawdown": max_drawdown(pls),
        "max_losing_streak": max_losing_streak(pls),
        "N_min": int(min(ns)) if ns else 0,
        "N_median": float(np.median(ns)) if ns else 0.0,
        "N_max": int(max(ns)) if ns else 0,
    }


def meta_score(history):
    if len(history) < 6:
        return -1e9
    h = history[-RECENT_META:]
    ratios = np.asarray([x["ratio"] for x in h], dtype=float)
    pls_per_ticket = np.asarray([x["pl"] / max(x["N"], 1) for x in h], dtype=float)
    weights = np.linspace(0.7, 1.3, len(h))
    wr = float(np.average(ratios, weights=weights))
    consistency = float(np.mean(ratios > 1.0))
    downside = float(np.mean(np.maximum(0.0, 1.0 - ratios)))
    return wr + 0.20 * consistency - 0.25 * downside + 0.10 * float(pls_per_ticket.mean())


def main():
    df, X, draws = load_rows()
    dates = df["date"].tolist()
    outcomes = {c.name: [] for c in CONFIGS}
    meta_all = []
    meta_abstain = []
    random_all = []
    random_abstain = []
    trace = []

    for t in range(WARMUP, len(draws)):
        past = draws[max(0, t - CAL_WINDOW):t]
        proposals = {}
        for ci, config in enumerate(CONFIGS):
            signal = signal_for(config, X, dates, t)
            pool = weighted_unique_tickets(
                signal, CANDIDATES, config.beta, seed=1_000_000 + t * 101 + ci
            )
            portfolio, cal = choose_prefix(pool, past)
            realized = score_portfolio(portfolio, draws[t])
            realized.update({"date": str(df.loc[t, "date"].date()), "t": t, "config": config.name, **cal})
            proposals[config.name] = (portfolio, realized)

        # Selection is based only on already realized earlier targets.
        scores = {name: meta_score(hist) for name, hist in outcomes.items()}
        selected_name = max(scores, key=scores.get)
        selected_portfolio, selected_realized = proposals[selected_name]

        meta_rec = dict(selected_realized)
        meta_rec["selected_by_meta_score"] = scores[selected_name]
        meta_all.append(meta_rec)

        # Abstention gate is also based only on prior realized records for the selected config.
        hist = outcomes[selected_name][-RECENT_META:]
        if len(hist) >= 8:
            hist_ratios = np.asarray([r["ratio"] for r in hist], dtype=float)
            weighted_mean = float(np.average(hist_ratios, weights=np.linspace(0.7, 1.3, len(hist))))
            lower_half = float(np.median(hist_ratios))
            confidence = weighted_mean + 0.25 * lower_half
        else:
            confidence = -1e9

        play = confidence > 1.28 and scores[selected_name] > 1.10
        if play:
            abstain_rec = dict(selected_realized)
        else:
            abstain_rec = {
                "date": str(df.loc[t, "date"].date()),
                "t": t,
                "config": "ABSTAIN",
                "N": 0,
                "payout": 0.0,
                "pl": 0.0,
                "ratio": 1.0,
                "profitable": False,
            }
        meta_abstain.append(abstain_rec)

        # Same-cost random controls are generated before seeing target, using deterministic seeds.
        rnd = random_unique_tickets(len(selected_portfolio), 2_000_000 + t)
        rr = score_portfolio(rnd, draws[t])
        rr.update({"date": str(df.loc[t, "date"].date()), "t": t})
        random_all.append(rr)
        if play:
            rra = dict(rr)
        else:
            rra = {"date": rr["date"], "t": t, "N": 0, "payout": 0.0, "pl": 0.0, "ratio": 1.0, "profitable": False}
        random_abstain.append(rra)

        trace.append({
            "t": t,
            "date": str(df.loc[t, "date"].date()),
            "selected": selected_name,
            "selected_N": selected_realized["N"],
            "selected_ratio": selected_realized["ratio"],
            "selected_pl": selected_realized["pl"],
            "meta_score_before_target": scores[selected_name],
            "abstention_confidence_before_target": confidence,
            "played_by_abstention": play,
            "random_ratio": rr["ratio"],
        })

        # Only now, after all decisions for t are frozen, append realized outcomes to meta history.
        for config in CONFIGS:
            outcomes[config.name].append(proposals[config.name][1])

    family_summary = {name: aggregate(recs) for name, recs in outcomes.items()}
    overall = {
        "meta_no_abstention": aggregate(meta_all),
        "meta_with_abstention": aggregate(meta_abstain),
        "matched_random_no_abstention": aggregate(random_all),
        "matched_random_with_same_abstention": aggregate(random_abstain),
    }

    # Chronological block audit; thresholds/method were not retuned per block.
    block_edges = [WARMUP, min(WARMUP + 40, len(draws)), min(WARMUP + 80, len(draws)), len(draws)]
    blocks = []
    for a, b in zip(block_edges[:-1], block_edges[1:]):
        ia, ib = a - WARMUP, b - WARMUP
        blocks.append({
            "rows": [a, b],
            "dates": [str(df.loc[a, "date"].date()), str(df.loc[b - 1, "date"].date())],
            "meta_no_abstention": aggregate(meta_all[ia:ib]),
            "meta_with_abstention": aggregate(meta_abstain[ia:ib]),
            "matched_random": aggregate(random_all[ia:ib]),
        })

    best_family = max(family_summary, key=lambda k: family_summary[k]["roi"])
    result = {
        "method": {
            "warmup": WARMUP,
            "candidate_pool": CANDIDATES,
            "calibration_window": CAL_WINDOW,
            "meta_history": RECENT_META,
            "N_policy": f"free integer prefix N from {MIN_N}..{MAX_N}",
            "families": [c.__dict__ for c in CONFIGS],
            "no_future_leakage": True,
            "decision_order": "build proposals from rows < t; select family and abstention from realized outcomes < t; only then score row t",
        },
        "family_summary": family_summary,
        "best_family_by_roi": best_family,
        "overall": overall,
        "blocks": blocks,
        "trace": trace,
    }

    # Conservative verdict: positive ROI must beat matched random and repeat across blocks.
    meta = overall["meta_with_abstention"]
    rnd = overall["matched_random_with_same_abstention"]
    positive_blocks = sum(1 for b in blocks if b["meta_with_abstention"]["net_pl"] > 0)
    result["gate"] = {
        "positive_net": meta["net_pl"] > 0,
        "beats_same_cost_random_roi": meta["roi"] > rnd["roi"],
        "positive_blocks": positive_blocks,
        "passed": bool(meta["net_pl"] > 0 and meta["roi"] > rnd["roi"] and positive_blocks >= 2),
    }

    out = ROOT / "results" / "phase10_walkforward_adaptive.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    md = f"""# Phase 10 — rolling walk-forward adaptive portfolio search\n\nDate: 2026-08-24\n\nStatus: **{'GATE PASSED' if result['gate']['passed'] else 'NO GATE PASSED'}**\n\n## Strict walk-forward protocol\n\n- warmup: {WARMUP} draws\n- scored targets: {len(draws) - WARMUP}\n- candidate pool per family/target: {CANDIDATES}\n- N: free integer prefix {MIN_N}..{MAX_N}\n- selection at target t uses only rows before t\n- meta-family selection uses only realized prior target outcomes\n- abstention uses only prior realized outcomes\n\n## Overall\n\n- meta, no abstention: ROI **{overall['meta_no_abstention']['roi']:.4f}**, net P/L **{overall['meta_no_abstention']['net_pl']:.2f} AZN**\n- meta + abstention: played **{overall['meta_with_abstention']['played']} / {overall['meta_with_abstention']['targets']}**, ROI **{overall['meta_with_abstention']['roi']:.4f}**, net P/L **{overall['meta_with_abstention']['net_pl']:.2f} AZN**\n- matched random, same abstention: ROI **{overall['matched_random_with_same_abstention']['roi']:.4f}**, net P/L **{overall['matched_random_with_same_abstention']['net_pl']:.2f} AZN**\n- best individual family by ROI: **{best_family}**, ROI **{family_summary[best_family]['roi']:.4f}**\n\n## Risk\n\n- meta + abstention max drawdown: **{overall['meta_with_abstention']['max_drawdown']:.2f} AZN**\n- max losing streak: **{overall['meta_with_abstention']['max_losing_streak']}** played/target rows\n- played N range: **{overall['meta_with_abstention']['N_min']} .. {overall['meta_with_abstention']['N_max']}**, median **{overall['meta_with_abstention']['N_median']:.1f}**\n\n## Gate\n\n- positive net: **{result['gate']['positive_net']}**\n- beats same-cost random ROI: **{result['gate']['beats_same_cost_random_roi']}**\n- positive chronological blocks: **{positive_blocks} / {len(blocks)}**\n- final gate: **{result['gate']['passed']}**\n\nComplete per-target trace and every family result are in `results/phase10_walkforward_adaptive.json`.\n"""
    (ROOT / "results" / "PHASE10_WALKFORWARD_ADAPTIVE.md").write_text(md, encoding="utf-8")
    print(json.dumps({"overall": overall, "gate": result["gate"], "best_family": best_family}, indent=2))


if __name__ == "__main__":
    main()
