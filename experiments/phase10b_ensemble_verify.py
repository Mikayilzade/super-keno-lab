from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.phase10_walkforward_adaptive import (
    CAL_WINDOW,
    CANDIDATES,
    CONFIGS,
    WARMUP,
    choose_prefix,
    load_rows,
    score_portfolio,
    signal_for,
    weighted_unique_tickets,
)
from src.baselines import random_unique_tickets
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
RANDOM_REPLICATES = 40


def hit_tier_breakdown(portfolio, draw):
    d = set(draw)
    counts = {str(k): 0 for k in range(11)}
    payout_by_tier = {str(k): 0.0 for k in range(11)}
    rules = RuleSet()
    for ticket in portfolio:
        h = len(set(ticket) & d)
        counts[str(h)] += 1
        payout_by_tier[str(h)] += rules.gross_for_hits(h)
    return counts, payout_by_tier


def aggregate(records):
    cost = float(sum(r["N"] for r in records))
    payout = float(sum(r["payout"] for r in records))
    return {
        "targets": len(records),
        "cost": cost,
        "payout": payout,
        "net_pl": payout - cost,
        "roi": payout / cost if cost else 1.0,
        "profitable_share": float(np.mean([r["payout"] > r["N"] for r in records])),
        "max_target_payout": float(max(r["payout"] for r in records)),
        "max_target_ratio": float(max(r["ratio"] for r in records)),
        "N_min": int(min(r["N"] for r in records)),
        "N_median": float(np.median([r["N"] for r in records])),
        "N_max": int(max(r["N"] for r in records)),
    }


def main():
    df, X, draws = load_rows()
    dates = df["date"].tolist()
    config = next(c for c in CONFIGS if c.name == "ensemble_b06")

    strategy = []
    random_runs = [[] for _ in range(RANDOM_REPLICATES)]
    tier_payout_total = {str(k): 0.0 for k in range(11)}
    target_rows = []

    for t in range(WARMUP, len(draws)):
        past = draws[max(0, t - CAL_WINDOW):t]
        signal = signal_for(config, X, dates, t)
        pool = weighted_unique_tickets(
            signal, CANDIDATES, config.beta, seed=1_000_000 + t * 101 + 7
        )
        portfolio, cal = choose_prefix(pool, past)
        rec = score_portfolio(portfolio, draws[t])
        rec.update({"t": t, "date": str(df.loc[t, "date"].date()), **cal})
        strategy.append(rec)

        counts, tier_payout = hit_tier_breakdown(portfolio, draws[t])
        for k, v in tier_payout.items():
            tier_payout_total[k] += float(v)
        target_rows.append({
            "t": t,
            "date": rec["date"],
            "N": rec["N"],
            "payout": rec["payout"],
            "ratio": rec["ratio"],
            "hits": counts,
            "payout_by_tier": tier_payout,
        })

        for r in range(RANDOM_REPLICATES):
            rnd = random_unique_tickets(len(portfolio), 3_000_000 + r * 100_003 + t)
            rr = score_portfolio(rnd, draws[t])
            rr.update({"t": t, "date": rec["date"]})
            random_runs[r].append(rr)

    strategy_summary = aggregate(strategy)
    random_summaries = [aggregate(x) for x in random_runs]
    random_rois = np.asarray([x["roi"] for x in random_summaries])
    random_pl = np.asarray([x["net_pl"] for x in random_summaries])

    edges = [WARMUP, min(WARMUP + 40, len(draws)), min(WARMUP + 80, len(draws)), len(draws)]
    blocks = []
    for a, b in zip(edges[:-1], edges[1:]):
        ia, ib = a - WARMUP, b - WARMUP
        s = aggregate(strategy[ia:ib])
        rroi = np.asarray([aggregate(run[ia:ib])["roi"] for run in random_runs])
        blocks.append({
            "rows": [a, b],
            "dates": [str(df.loc[a, "date"].date()), str(df.loc[b - 1, "date"].date())],
            "strategy": s,
            "random_roi_mean": float(rroi.mean()),
            "random_roi_p10": float(np.quantile(rroi, 0.10)),
            "random_roi_p90": float(np.quantile(rroi, 0.90)),
            "strategy_above_random_mean": bool(s["roi"] > rroi.mean()),
        })

    high_tier = sum(v for k, v in tier_payout_total.items() if int(k) >= 8)
    total_payout = strategy_summary["payout"]
    result = {
        "frozen_method": "ensemble_b06 from Phase 10; no parameter retuning",
        "random_replicates": RANDOM_REPLICATES,
        "strategy": strategy_summary,
        "random": {
            "roi_mean": float(random_rois.mean()),
            "roi_std": float(random_rois.std(ddof=1)),
            "roi_p05": float(np.quantile(random_rois, 0.05)),
            "roi_p95": float(np.quantile(random_rois, 0.95)),
            "best_roi": float(random_rois.max()),
            "worst_roi": float(random_rois.min()),
            "net_pl_mean": float(random_pl.mean()),
            "replicates_beating_strategy": int(np.sum(random_rois >= strategy_summary["roi"])),
            "empirical_one_sided_p": float((np.sum(random_rois >= strategy_summary["roi"]) + 1) / (RANDOM_REPLICATES + 1)),
        },
        "payout_concentration": {
            "by_hit_tier": tier_payout_total,
            "payout_from_8plus": float(high_tier),
            "share_from_8plus": float(high_tier / total_payout if total_payout else 0.0),
            "largest_target_payout": strategy_summary["max_target_payout"],
        },
        "blocks": blocks,
        "targets": target_rows,
    }

    positive_blocks = sum(1 for b in blocks if b["strategy"]["net_pl"] > 0)
    beats_random_blocks = sum(1 for b in blocks if b["strategy_above_random_mean"])
    result["decision"] = {
        "strategy_positive": strategy_summary["net_pl"] > 0,
        "beats_random_overall": strategy_summary["roi"] > random_rois.mean(),
        "beats_random_blocks": beats_random_blocks,
        "positive_blocks": positive_blocks,
        "promote_to_next_stage": bool(
            strategy_summary["roi"] > random_rois.mean()
            and beats_random_blocks >= 2
            and result["random"]["empirical_one_sided_p"] <= 0.10
        ),
    }

    out = ROOT / "results" / "phase10b_ensemble_verify.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    md = f"""# Phase 10B — frozen ensemble_b06 verification\n\nDate: 2026-08-24\n\nThe Phase-10 best family was frozen without retuning and replayed across the same strict walk-forward targets. Each target was compared with {RANDOM_REPLICATES} deterministic same-N random portfolios.\n\n## Frozen strategy\n\n- ROI: **{strategy_summary['roi']:.4f}**\n- net P/L: **{strategy_summary['net_pl']:.2f} AZN**\n- cost: **{strategy_summary['cost']:.0f} AZN**\n- profitable targets: **{strategy_summary['profitable_share']:.1%}**\n- N range: **{strategy_summary['N_min']}..{strategy_summary['N_max']}**, median **{strategy_summary['N_median']:.1f}**\n\n## Same-N random distribution\n\n- mean ROI: **{random_rois.mean():.4f}**\n- 5–95% ROI: **{np.quantile(random_rois,0.05):.4f} .. {np.quantile(random_rois,0.95):.4f}**\n- best random replicate ROI: **{random_rois.max():.4f}**\n- random replicates >= strategy: **{result['random']['replicates_beating_strategy']} / {RANDOM_REPLICATES}**\n- empirical one-sided p: **{result['random']['empirical_one_sided_p']:.4f}**\n\n## Concentration\n\n- payout from 8+ hit tickets: **{high_tier:.0f} AZN**\n- share of all payout from 8+: **{result['payout_concentration']['share_from_8plus']:.1%}**\n- largest one-target payout: **{strategy_summary['max_target_payout']:.0f} AZN**\n\n## Chronological robustness\n\n- blocks above same-N random mean: **{beats_random_blocks} / {len(blocks)}**\n- positive-P/L blocks: **{positive_blocks} / {len(blocks)}**\n\n## Decision\n\nPromote as a signal lead: **{result['decision']['promote_to_next_stage']}**.\n\nPromotion does not mean profitable. It only means the frozen ensemble shows repeatable separation from same-cost random and deserves a more targeted next-stage model.\n"""
    (ROOT / "results" / "PHASE10B_ENSEMBLE_VERIFY.md").write_text(md, encoding="utf-8")
    print(json.dumps({"strategy": strategy_summary, "random": result["random"], "decision": result["decision"]}, indent=2))


if __name__ == "__main__":
    main()
