from __future__ import annotations

# Workflow trigger checkpoint: Phase 9 LP experiment.
import csv
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.phase8_multiwitness_builder_compare import (
    build_greedy,
    evaluate,
    multiple_adversaries,
    strong_random_scan_attack,
)
from src.baselines import random_unique_tickets
from src.data_loader import load_and_validate
from src.evaluator import payout_matrix
from src.lp_maximin import round_fractional_solution, solve_fractional_distinct_relaxation
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_COUNT = 12_000
CANDIDATE_SEED = 260824
INITIAL_NS = [337, 509, 683, 863, 1061]


def load_draws():
    rows = load_and_validate(ROOT / "data")
    draws = [tuple(int(r[f"n{i}"]) for i in range(1, 21)) for r in rows]
    assert len(draws) == 195
    return draws


def build_phase8_bank(candidates, base_pm):
    witness_bank: list[tuple[int, ...]] = []
    rounds = []
    for round_index in range(4):
        full = (
            np.concatenate(
                [base_pm, payout_matrix(candidates, witness_bank, RuleSet()).astype(np.float32)],
                axis=1,
            )
            if witness_bank
            else base_pm
        )
        selected, fit = build_greedy(full, max_n=900, bottom_k=32)
        portfolio = [candidates[i] for i in selected]
        adversarial = multiple_adversaries(
            portfolio, 82000 + round_index, count=4, starts=10
        )
        existing = set(witness_bank)
        added = []
        for a in adversarial:
            witness = tuple(a["draw"])
            if witness not in existing:
                witness_bank.append(witness)
                existing.add(witness)
                added.append(witness)
        rounds.append(
            {
                "round": round_index,
                "constraints_before": int(full.shape[1]),
                "N": len(portfolio),
                "fit": fit,
                "added": [list(x) for x in added],
            }
        )
    return witness_bank, rounds


def constraint_matrix(candidates, base_pm, witnesses):
    if not witnesses:
        return base_pm.astype(np.float64)
    wpm = payout_matrix(candidates, witnesses, RuleSet()).astype(np.float32)
    return np.concatenate([base_pm, wpm], axis=1).astype(np.float64)


def solve_round_attack(candidates, pm, n, seed, attack_starts=8, round_trials=18):
    sol = solve_fractional_distinct_relaxation(pm, n)
    indices, rounded = round_fractional_solution(
        pm, sol, seed=seed, random_rounds=round_trials
    )
    portfolio = [candidates[i] for i in indices]
    attacks = multiple_adversaries(
        portfolio, seed + 700_000, count=3, starts=attack_starts
    )
    adversarial_min = min(a["ratio"] for a in attacks)
    return {
        "N": n,
        "fractional_floor": sol.floor,
        "fractional_support": sol.support,
        "rounded": rounded,
        "adversarial_min": adversarial_min,
        "attacks": attacks,
        "indices": indices,
        "portfolio": portfolio,
    }


def write_portfolio(path: Path, portfolio):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ticket_id", *[f"n{i}" for i in range(1, 11)]])
        for i, ticket in enumerate(portfolio, 1):
            w.writerow([i, *ticket])


def strip_large(record):
    out = {k: v for k, v in record.items() if k not in {"indices", "portfolio"}}
    return out


def main():
    draws = load_draws()
    candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)
    base_pm = payout_matrix(candidates, draws, RuleSet()).astype(np.float32)

    witnesses, bank_rounds = build_phase8_bank(candidates, base_pm)
    pm = constraint_matrix(candidates, base_pm, witnesses)

    initial_scan = []
    initial_full = []
    for j, n in enumerate(INITIAL_NS):
        rec = solve_round_attack(
            candidates, pm, n, seed=910_000 + j, attack_starts=8, round_trials=16
        )
        initial_full.append(rec)
        initial_scan.append(strip_large(rec))

    best = max(
        initial_full,
        key=lambda r: (
            r["adversarial_min"],
            r["rounded"]["min"],
            r["rounded"]["p05"],
        ),
    )
    current_n = best["N"]

    cutting_rounds = []
    for round_index in range(3):
        pm = constraint_matrix(candidates, base_pm, witnesses)
        neighbor_ns = sorted(
            {
                max(120, current_n - 37),
                current_n,
                min(1200, current_n + 41),
            }
        )
        candidates_this_round = []
        for j, n in enumerate(neighbor_ns):
            rec = solve_round_attack(
                candidates,
                pm,
                n,
                seed=920_000 + round_index * 100 + j,
                attack_starts=7,
                round_trials=18,
            )
            candidates_this_round.append(rec)

        chosen = max(
            candidates_this_round,
            key=lambda r: (
                r["adversarial_min"],
                r["rounded"]["min"],
                r["rounded"]["p05"],
            ),
        )
        current_n = chosen["N"]

        # Add a stronger, diverse batch of witnesses for the chosen actual portfolio.
        new_attacks = multiple_adversaries(
            chosen["portfolio"],
            950_000 + round_index,
            count=4,
            starts=16,
        )
        existing = set(witnesses)
        added = []
        for a in new_attacks:
            witness = tuple(a["draw"])
            if witness not in existing:
                witnesses.append(witness)
                existing.add(witness)
                added.append(witness)

        cutting_rounds.append(
            {
                "round": round_index,
                "constraints_before": int(pm.shape[1]),
                "tested": [strip_large(x) for x in candidates_this_round],
                "chosen_N": current_n,
                "chosen_quick_adversarial_min": chosen["adversarial_min"],
                "added_witnesses": [list(x) for x in added],
                "added_witness_ratios": [a["ratio"] for a in new_attacks],
            }
        )

    # Final LP fit/rounding on the full grown witness bank.
    final_pm = constraint_matrix(candidates, base_pm, witnesses)
    final_solution = solve_fractional_distinct_relaxation(final_pm, current_n)
    final_indices, final_rounded = round_fractional_solution(
        final_pm,
        final_solution,
        seed=999_001,
        random_rounds=32,
    )
    final_portfolio = [candidates[i] for i in final_indices]

    final_strong = strong_random_scan_attack(
        final_portfolio, 777_001, samples=30_000, keep=24
    )

    random_controls = []
    for j, seed in enumerate((99117, 99173)):
        p = random_unique_tickets(current_n, seed)
        random_controls.append(
            {
                "seed": seed,
                "real": evaluate(p, draws),
                "strong_attack": strong_random_scan_attack(
                    p, 778_000 + j, samples=30_000, keep=24
                ),
            }
        )

    # Free-N broad-tail greedy control on the same final bank.
    g_idx, g_fit = build_greedy(final_pm.astype(np.float32), max_n=1200, bottom_k=64)
    greedy_portfolio = [candidates[i] for i in g_idx]
    greedy_strong = strong_random_scan_attack(
        greedy_portfolio, 779_001, samples=30_000, keep=24
    )

    result = {
        "candidate_count": CANDIDATE_COUNT,
        "candidate_seed": CANDIDATE_SEED,
        "base_real_draws": 195,
        "phase8_bank_rounds": bank_rounds,
        "initial_witnesses": 16,
        "initial_scan": initial_scan,
        "cutting_rounds": cutting_rounds,
        "final_witness_count": len(witnesses),
        "final_lp": {
            "N": current_n,
            "fractional_floor": final_solution.floor,
            "fractional_support": final_solution.support,
            "rounded_fit": final_rounded,
            "real": evaluate(final_portfolio, draws),
            "strong_attack": final_strong,
        },
        "bottom64_control": {
            "N": len(greedy_portfolio),
            "fit": g_fit,
            "real": evaluate(greedy_portfolio, draws),
            "strong_attack": greedy_strong,
        },
        "random_controls": random_controls,
        "interpretation_note": (
            "LP floors are finite-bank relaxation values. Rounded portfolios are actual distinct-ticket lists. "
            "Strong adversarial attacks are concrete heuristic witnesses, not global-minimum certificates."
        ),
    }

    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    (results_dir / "phase9_lp_maximin.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    write_portfolio(results_dir / f"phase9_lp_portfolio_{current_n}.csv", final_portfolio)

    md = f"""# Phase 9 — LP/fractional maximin + rounding\n\nDate: 2026-08-24\n\nStatus: **COMPUTED — see JSON for complete reproducibility.**\n\n## Final LP-rounded portfolio\n\n- N: **{current_n}** distinct tickets\n- fractional finite-bank floor: **{final_solution.floor:.6f}**\n- fractional support: **{final_solution.support}** tickets\n- rounded finite-bank min: **{final_rounded['min']:.6f}**\n- real-195 min: **{result['final_lp']['real']['min']:.6f}**\n- strong adversarial witnessed return: **{final_strong['ratio']:.6f}**\n\n## Controls\n\n- bottom-64 free-N control: N={len(greedy_portfolio)}, strong adversarial return **{greedy_strong['ratio']:.6f}**\n- random control seed 99117: strong adversarial return **{random_controls[0]['strong_attack']['ratio']:.6f}**\n- random control seed 99173: strong adversarial return **{random_controls[1]['strong_attack']['ratio']:.6f}**\n\nThe LP value is a relaxation on the finite witness bank, not a guarantee over all possible draws. The rounded portfolio is a concrete list of unique tickets and is independently attacked afterward.\n\n## Decision rule\n\nIf LP-rounded adversarial performance does not materially separate from same-N random controls, do not keep refining fixed-portfolio geometry. Move the main effort to rolling walk-forward / adaptive portfolio selection, retaining the adversarial oracle as a robustness gate.\n"""
    (results_dir / "PHASE9_LP_MAXIMIN.md").write_text(md, encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
