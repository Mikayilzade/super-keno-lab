from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.baselines import random_unique_tickets
from src.data_loader import load_and_validate
from src.evaluator import metrics_from_payouts, payout_matrix
from src.robust_search import RobustConfig, robust_search
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_COUNT = 6000
CANDIDATE_SEED = 20260824

CONFIGS = [
    RobustConfig(cap=15, variants=3, swaps=2, bottom_frac=0.15, alpha=0.03),
    RobustConfig(cap=30, variants=3, swaps=2, bottom_frac=0.15, alpha=0.03),
    RobustConfig(cap=150, variants=3, swaps=2, bottom_frac=0.15, alpha=0.03),
    RobustConfig(cap=15, variants=3, swaps=1, bottom_frac=0.15, alpha=0.03),
    RobustConfig(cap=15, variants=5, swaps=2, bottom_frac=0.20, alpha=0.03),
]


def load():
    rows = load_and_validate(ROOT / "data")
    draws = [tuple(int(r[f"n{i}"]) for i in range(1, 21)) for r in rows]
    dates = [r["date"] for r in rows]
    assert len(draws) == 195
    return draws, dates


def evaluate(tickets, draws, dates):
    totals = payout_matrix(tickets, draws, RuleSet()).sum(axis=0)
    m = metrics_from_payouts(totals, len(tickets), RuleSet())
    ratios = totals / len(tickets)
    return {
        "N": len(tickets),
        "min_ratio": float(ratios.min()),
        "p10_ratio": float(np.quantile(ratios, 0.10)),
        "avg_ratio": float(ratios.mean()),
        "profitable_share": float(np.mean(ratios > 1.0)),
        "min_pl": m.min_pl,
        "avg_pl": m.avg_pl,
        "worst_date": dates[m.worst_index],
    }


def config_dict(c):
    return {
        "cap": c.cap,
        "variants": c.variants,
        "swaps": c.swaps,
        "bottom_frac": c.bottom_frac,
        "alpha": c.alpha,
    }


def main():
    draws, dates = load()
    train, validation = draws[:120], draws[120:160]
    dt, dv = dates[:120], dates[120:160]
    candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)

    walkforward = []
    for ci, config in enumerate(CONFIGS):
        windows = []
        for end, next_end in ((60, 90), (90, 120)):
            portfolio, best, _ = robust_search(
                train[:end],
                candidates,
                config,
                seed=20260824 + end + ci * 100,
                max_n=550,
            )
            ev = evaluate(portfolio, train[end:next_end], dt[end:next_end])
            windows.append({"fit_end": end, "search_best": best, "evaluation": ev})
        score = [
            min(w["evaluation"]["min_ratio"] for w in windows),
            min(w["evaluation"]["p10_ratio"] for w in windows),
            float(np.mean([w["evaluation"]["avg_ratio"] for w in windows])),
        ]
        walkforward.append(
            {"config": config_dict(config), "windows": windows, "score": score}
        )

    best_index = max(
        range(len(walkforward)),
        key=lambda i: tuple(walkforward[i]["score"]),
    )
    frozen = CONFIGS[best_index]

    portfolio, search_best, _ = robust_search(
        train,
        candidates,
        frozen,
        seed=20260824 + 120,
        max_n=700,
    )

    result = {
        "candidate_count": CANDIDATE_COUNT,
        "candidate_seed": CANDIDATE_SEED,
        "config_selection": walkforward,
        "frozen_config_index": best_index,
        "frozen_config": config_dict(frozen),
        "frozen_search_best": search_best,
        "train": evaluate(portfolio, train, dt),
        "validation_reused_diagnostic": evaluate(portfolio, validation, dv),
        "holdout_opened": False,
        "selected_tickets": [list(t) for t in portfolio],
    }

    out = ROOT / "results" / "phase2_results.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
