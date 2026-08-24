from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, hstack, vstack


@dataclass(frozen=True)
class FractionalSolution:
    target_n: int
    floor: float
    weights: np.ndarray
    support: int
    status: str


def solve_fractional_distinct_relaxation(payout_matrix: np.ndarray, target_n: int) -> FractionalSolution:
    """Maximize the minimum payout ratio over scenarios for N distinct tickets.

    Variables are fractional ticket shares w_i and floor t.  Sum(w)=1 and
    0 <= w_i <= 1/N, which is the natural LP relaxation of selecting N distinct
    tickets uniformly (each selected ticket would have weight exactly 1/N).
    """
    pm = np.asarray(payout_matrix, dtype=np.float64)
    if pm.ndim != 2:
        raise ValueError("payout_matrix must be 2-D [tickets, scenarios]")
    ticket_count, scenario_count = pm.shape
    if not (1 <= target_n <= ticket_count):
        raise ValueError("target_n must be between 1 and ticket_count")

    # -P^T w + t <= 0  <=>  P^T w >= t for every scenario.
    a_left = -csr_matrix(pm.T)
    a_ub = hstack([a_left, np.ones((scenario_count, 1), dtype=np.float64)], format="csr")
    b_ub = np.zeros(scenario_count, dtype=np.float64)

    a_eq = csr_matrix(np.concatenate([np.ones(ticket_count), [0.0]])[None, :])
    b_eq = np.array([1.0], dtype=np.float64)

    c = np.zeros(ticket_count + 1, dtype=np.float64)
    c[-1] = -1.0
    bounds = [(0.0, 1.0 / target_n)] * ticket_count + [(0.0, None)]

    result = linprog(
        c,
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
        options={"presolve": True},
    )
    if not result.success:
        raise RuntimeError(f"LP failed for N={target_n}: {result.message}")

    weights = np.asarray(result.x[:-1], dtype=np.float64)
    weights[weights < 1e-12] = 0.0
    weights /= weights.sum()
    return FractionalSolution(
        target_n=target_n,
        floor=float(result.x[-1]),
        weights=weights,
        support=int(np.count_nonzero(weights)),
        status=str(result.message),
    )


def _portfolio_metrics(pm: np.ndarray, indices: Sequence[int]) -> dict:
    idx = np.asarray(indices, dtype=int)
    ratios = pm[idx].sum(axis=0) / len(idx)
    return {
        "N": int(len(idx)),
        "min": float(np.min(ratios)),
        "p05": float(np.quantile(ratios, 0.05)),
        "p10": float(np.quantile(ratios, 0.10)),
        "avg": float(np.mean(ratios)),
    }


def round_fractional_solution(
    payout_matrix: np.ndarray,
    solution: FractionalSolution,
    *,
    seed: int,
    random_rounds: int = 24,
) -> tuple[list[int], dict]:
    """Round LP weights into N distinct tickets and retain the best finite-bank floor.

    Includes deterministic top-weight rounding plus randomized weighted sampling
    without replacement.  The returned object is an actual distinct-ticket list.
    """
    pm = np.asarray(payout_matrix, dtype=np.float64)
    w = solution.weights
    n = solution.target_n
    if np.count_nonzero(w) < n:
        raise RuntimeError("fractional support is smaller than target N")

    candidates: list[np.ndarray] = []
    top = np.argpartition(-w, n - 1)[:n]
    candidates.append(np.sort(top))

    rng = np.random.default_rng(seed)
    p = w / w.sum()
    for _ in range(random_rounds):
        draw = rng.choice(len(w), size=n, replace=False, p=p)
        candidates.append(np.sort(draw))

    best_idx = None
    best_metrics = None
    best_key = None
    seen = set()
    for idx in candidates:
        key_tuple = tuple(int(x) for x in idx)
        if key_tuple in seen:
            continue
        seen.add(key_tuple)
        m = _portfolio_metrics(pm, idx)
        key = (m["min"], m["p05"], m["p10"], m["avg"])
        if best_key is None or key > best_key:
            best_key = key
            best_idx = idx
            best_metrics = m

    assert best_idx is not None and best_metrics is not None
    best_metrics = dict(best_metrics)
    best_metrics["fractional_floor"] = solution.floor
    best_metrics["fractional_support"] = solution.support
    best_metrics["round_candidates_checked"] = len(seen)
    return [int(x) for x in best_idx], best_metrics
