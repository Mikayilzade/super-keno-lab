from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.adversarial import local_swap_adversary
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


def load_draws():
    rows = load_and_validate(ROOT / 'data')
    return [tuple(int(r[f'n{i}']) for i in range(1, 21)) for r in rows]


def greedy_free_n(payouts: np.ndarray):
    cumulative = np.zeros(payouts.shape[1], dtype=np.float32)
    used = np.zeros(payouts.shape[0], dtype=bool)
    means = payouts.mean(axis=1)
    selected = []
    best = None

    for n in range(1, MAX_N + 1):
        k = min(BOTTOM_K, payouts.shape[1])
        worst = np.argpartition(cumulative, k - 1)[:k]
        score = payouts[:, worst].mean(axis=1) + AVG_WEIGHT * means
        score[used] = -1e9
        idx = int(np.argmax(score))
        used[idx] = True
        selected.append(idx)
        cumulative += payouts[idx]

        if n >= 20:
            rec = {
                'N': n,
                'min_ratio': float(cumulative.min() / n),
                'avg_ratio': float(cumulative.mean() / n),
                'min_payout': float(cumulative.min()),
            }
            if best is None or (rec['min_ratio'], rec['avg_ratio']) > (
                best['min_ratio'], best['avg_ratio']
            ):
                best = rec
    return selected, best


def main(iterations=5, adversary_starts=25):
    draws = load_draws()
    historical = draws[:160]
    all_real = draws
    candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)
    base_matrix = payout_matrix(candidates, historical, RuleSet()).astype(np.float32)
    witnesses = []
    results = []

    for iteration in range(iterations):
        if witnesses:
            witness_matrix = payout_matrix(candidates, witnesses, RuleSet()).astype(np.float32)
            constraints = np.concatenate([base_matrix, witness_matrix], axis=1)
        else:
            constraints = base_matrix

        selected, best = greedy_free_n(constraints)
        portfolio = [candidates[i] for i in selected[: best['N']]]

        historical_totals = payout_matrix(portfolio, historical, RuleSet()).sum(axis=0)
        real_totals = payout_matrix(portfolio, all_real, RuleSet()).sum(axis=0)
        adversary = local_swap_adversary(
            portfolio,
            seed=9000 + iteration,
            starts=adversary_starts,
            max_steps=30,
        )
        adversarial_ratio = adversary['payout'] / len(portfolio)

        results.append({
            'iteration': iteration,
            'constraints': len(historical) + len(witnesses),
            'N': len(portfolio),
            'constraint_min_ratio': best['min_ratio'],
            'history160_min_ratio': float(historical_totals.min() / len(portfolio)),
            'real195_min_ratio': float(real_totals.min() / len(portfolio)),
            'adversarial_payout': adversary['payout'],
            'adversarial_ratio': adversarial_ratio,
            'adversarial_draw': list(adversary['draw']),
            'adversary_steps': adversary['steps'],
        })
        witnesses.append(adversary['draw'])

    payload = {
        'candidate_count': CANDIDATE_COUNT,
        'candidate_seed': CANDIDATE_SEED,
        'max_n': MAX_N,
        'bottom_k': BOTTOM_K,
        'avg_weight': AVG_WEIGHT,
        'adversary_starts': adversary_starts,
        'note': 'Adversarial ratios are heuristic witnessed upper bounds on the true portfolio minimum, not global-minimum certificates.',
        'results': results,
        'witnesses': [list(w) for w in witnesses],
    }
    out = ROOT / 'results' / 'phase7_cutting_plane_checkpoint.json'
    out.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
