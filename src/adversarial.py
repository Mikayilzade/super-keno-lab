from __future__ import annotations

import numpy as np

from .rules import RuleSet, validate_ticket


def ticket_incidence(tickets):
    tickets = [validate_ticket(t) for t in tickets]
    matrix = np.zeros((len(tickets), 70), dtype=np.uint8)
    for i, ticket in enumerate(tickets):
        matrix[i, np.asarray(ticket, dtype=int) - 1] = 1
    return matrix


def portfolio_payout_from_incidence(ticket_incidence_matrix, draw, rules=RuleSet()):
    draw0 = np.asarray(sorted(int(x) - 1 for x in draw), dtype=int)
    if len(draw0) != 20 or len(set(draw0.tolist())) != 20 or draw0.min() < 0 or draw0.max() >= 70:
        raise ValueError('draw must contain exactly 20 unique integers in 1..70')
    hits = ticket_incidence_matrix[:, draw0].sum(axis=1)
    lookup = np.asarray([rules.gross_for_hits(i) for i in range(11)], dtype=np.float32)
    return float(lookup[hits].sum())


def local_swap_adversary(
    tickets,
    *,
    seed: int,
    starts: int = 25,
    max_steps: int = 30,
    rules=RuleSet(),
):
    """Heuristic minimizer over valid 20-of-70 draws.

    Uses many random starts and steepest 1-out/1-in swap descent. The returned
    draw is a concrete payout witness, not a proof that the global minimum was
    found.
    """
    incidence = ticket_incidence(tickets)
    lookup = np.asarray([rules.gross_for_hits(i) for i in range(11)], dtype=np.float32)
    rng = np.random.default_rng(seed)
    best_payout = float('inf')
    best_draw = None
    best_steps = 0

    for _ in range(starts):
        current = np.zeros(70, dtype=bool)
        current[rng.choice(70, 20, replace=False)] = True
        hits = incidence[:, current].sum(axis=1).astype(np.int16)
        payout = float(lookup[hits].sum())
        steps = 0

        while steps < max_steps:
            outs = np.where(current)[0]
            ins = np.where(~current)[0]
            local_best = payout
            best_out = best_in = None
            best_hits = None

            for out_number in outs:
                candidate_hits = (
                    hits[None, :]
                    - incidence[:, out_number][None, :]
                    + incidence[:, ins].T
                )
                values = lookup[candidate_hits].sum(axis=1)
                j = int(np.argmin(values))
                value = float(values[j])
                if value < local_best - 1e-9:
                    local_best = value
                    best_out = int(out_number)
                    best_in = int(ins[j])
                    best_hits = candidate_hits[j].copy()

            if best_out is None:
                break

            current[best_out] = False
            current[best_in] = True
            hits = best_hits
            payout = local_best
            steps += 1

        if payout < best_payout:
            best_payout = payout
            best_draw = tuple((np.where(current)[0] + 1).tolist())
            best_steps = steps

    return {
        'draw': best_draw,
        'payout': best_payout,
        'steps': best_steps,
        'starts': starts,
        'seed': seed,
    }
