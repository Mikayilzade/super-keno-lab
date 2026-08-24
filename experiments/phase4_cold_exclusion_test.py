from __future__ import annotations

import json
import random
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
SEARCH_SEED = 20260944
CONFIG = RobustConfig(cap=15, variants=3, swaps=2, bottom_frac=0.15, alpha=0.03)


def restricted_tickets(n, excluded, seed):
    rng = random.Random(seed)
    universe = [x for x in range(1, 71) if x not in set(excluded)]
    seen, out = set(), []
    while len(out) < n:
        ticket = tuple(sorted(rng.sample(universe, 10)))
        if ticket not in seen:
            seen.add(ticket)
            out.append(ticket)
    return out


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
        "min_pl": float(m.min_pl),
        "avg_pl": float(m.avg_pl),
        "worst_date": dates[m.worst_index],
    }


def main():
    rows = load_and_validate(ROOT / "data")
    draws = [tuple(int(r[f"n{i}"]) for i in range(1, 21)) for r in rows]
    dates = [r["date"] for r in rows]
    design, diagnostic = draws[:120], draws[120:160]
    dd, dv = dates[:120], dates[120:160]

    cases = {
        "unrestricted": [],
        "avoid_4": [4],
        "avoid_design_bottom3": [4, 19, 64],
        "avoid_design_bottom5": [4, 19, 64, 1, 38],
    }
    result = {"holdout_opened": False, "cases": {}}
    for name, excluded in cases.items():
        if excluded:
            candidates = restricted_tickets(CANDIDATE_COUNT, excluded, CANDIDATE_SEED)
        else:
            candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)
        portfolio, best, _ = robust_search(
            design, candidates, CONFIG, seed=SEARCH_SEED, max_n=700
        )
        result["cases"][name] = {
            "excluded": excluded,
            "search_best": best,
            "design": evaluate(portfolio, design, dd),
            "diagnostic": evaluate(portfolio, diagnostic, dv),
        }

    out = ROOT / "results" / "phase4_cold_exclusion_test.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
