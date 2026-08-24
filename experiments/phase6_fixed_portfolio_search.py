from __future__ import annotations

import csv
import json
import sys
from math import comb
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.baselines import random_unique_tickets
from src.data_loader import load_and_validate
from src.evaluator import payout_matrix
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_COUNT = 30000
CANDIDATE_SEED = 260824
MAX_N = 1200
BOTTOM_K = 24
AVG_WEIGHT = 0.01


def load():
    rows = load_and_validate(ROOT / "data")
    draws = [tuple(int(r[f"n{i}"]) for i in range(1, 21)) for r in rows]
    dates = [r["date"] for r in rows]
    assert len(draws) == 195
    return draws, dates


def fixed_portfolio_bound():
    rules = RuleSet()
    total_draws = comb(70, 20)
    ev = 0.0
    probs = {}
    for hits in range(11):
        p = comb(10, hits) * comb(60, 20 - hits) / total_draws
        probs[hits] = p
        ev += p * rules.gross_for_hits(hits)
    all_tickets = comb(70, 10)
    constant_all_ticket_payout = sum(
        comb(20, hits) * comb(50, 10 - hits) * rules.gross_for_hits(hits)
        for hits in range(11)
    )
    return {
        "gross_ev_per_1_azn_ticket": ev,
        "universal_fixed_portfolio_maximin_ratio": ev,
        "all_distinct_tickets": all_tickets,
        "all_ticket_portfolio_constant_payout_per_draw": constant_all_ticket_payout,
        "all_ticket_portfolio_ratio": constant_all_ticket_payout / all_tickets,
        "hit_probabilities": probs,
    }


def greedy_free_n(payouts: np.ndarray):
    candidate_count, draw_count = payouts.shape
    cumulative = np.zeros(draw_count, dtype=np.float32)
    used = np.zeros(candidate_count, dtype=bool)
    selected = []
    checkpoints = []
    best = None
    means = payouts.mean(axis=1)

    for n in range(1, MAX_N + 1):
        k = min(BOTTOM_K, draw_count)
        worst = np.argpartition(cumulative, k - 1)[:k]
        score = payouts[:, worst].mean(axis=1) + AVG_WEIGHT * means
        score[used] = -1e9
        idx = int(np.argmax(score))
        used[idx] = True
        selected.append(idx)
        cumulative += payouts[idx]

        if n >= 20:
            rec = {
                "N": n,
                "min_ratio": float(cumulative.min() / n),
                "avg_ratio": float(cumulative.mean() / n),
                "min_payout": float(cumulative.min()),
                "worst_index": int(cumulative.argmin()),
            }
            if best is None or (rec["min_ratio"], rec["avg_ratio"]) > (
                best["min_ratio"],
                best["avg_ratio"],
            ):
                best = rec
        if n <= 20 or n % 20 == 0:
            checkpoints.append(
                {
                    "N": n,
                    "min_ratio": float(cumulative.min() / n),
                    "avg_ratio": float(cumulative.mean() / n),
                }
            )
    return selected, best, checkpoints


def evaluate(tickets, draws, dates):
    totals = payout_matrix(tickets, draws, RuleSet()).sum(axis=0)
    ratios = totals / len(tickets)
    return {
        "N": len(tickets),
        "min_ratio": float(ratios.min()),
        "avg_ratio": float(ratios.mean()),
        "median_ratio": float(np.median(ratios)),
        "profitable_share": float(np.mean(ratios > 1.0)),
        "min_payout": float(totals.min()),
        "min_pl": float(totals.min() - len(tickets)),
        "avg_pl": float(totals.mean() - len(tickets)),
        "worst_date": dates[int(np.argmin(ratios))],
        "best_ratio": float(ratios.max()),
        "best_date": dates[int(np.argmax(ratios))],
    }


def write_tickets(path: Path, tickets):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ticket_id", *[f"n{i}" for i in range(1, 11)]])
        for i, ticket in enumerate(tickets, 1):
            w.writerow([i, *ticket])


def main():
    draws, dates = load()
    exposed_draws, formerly_sealed = draws[:160], draws[160:]
    exposed_dates, formerly_sealed_dates = dates[:160], dates[160:]

    candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)
    matrix = payout_matrix(candidates, exposed_draws, RuleSet()).astype(np.float32)
    selected, best, checkpoints = greedy_free_n(matrix)
    tickets = [candidates[i] for i in selected[: best["N"]]]

    result = {
        "fixed_portfolio_bound": fixed_portfolio_bound(),
        "search": {
            "candidate_count": CANDIDATE_COUNT,
            "candidate_seed": CANDIDATE_SEED,
            "max_n": MAX_N,
            "bottom_k": BOTTOM_K,
            "avg_weight": AVG_WEIGHT,
            "selected_N": best["N"],
            "fit_160": evaluate(tickets, exposed_draws, exposed_dates),
            "formerly_sealed_35": evaluate(tickets, formerly_sealed, formerly_sealed_dates),
            "checkpoints": checkpoints,
        },
        "holdout_opened": True,
        "holdout_note": (
            "The final 35 rows were opened exactly once after freezing the search rule "
            "and exact 662-ticket portfolio. They must never again be called untouched holdout."
        ),
    }
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "results" / "phase6_fixed_portfolio_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    write_tickets(ROOT / "results" / "phase6_overfit_candidate_662.csv", tickets)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
