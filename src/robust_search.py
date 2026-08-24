from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Sequence
import numpy as np

from .evaluator import payout_matrix
from .rules import RuleSet


@dataclass(frozen=True)
class RobustConfig:
    cap: float = 15.0
    variants: int = 3
    swaps: int = 2
    bottom_frac: float = 0.15
    alpha: float = 0.03


def perturb_draws(draws: Sequence[Sequence[int]], variants: int, swaps: int, seed: int):
    rng = random.Random(seed)
    out = []
    origin = []
    for i, draw in enumerate(draws):
        base = set(draw)
        out.append(tuple(sorted(base)))
        origin.append(i)
        for _ in range(variants):
            current = set(base)
            removed = rng.sample(sorted(current), swaps)
            current.difference_update(removed)
            outside = [x for x in range(1, 71) if x not in current]
            current.update(rng.sample(outside, swaps))
            out.append(tuple(sorted(current)))
            origin.append(i)
    return out, origin


def robust_search(
    draws,
    candidates,
    config: RobustConfig,
    seed: int,
    max_n: int = 700,
    min_n: int = 20,
):
    scenarios, origins = perturb_draws(draws, config.variants, config.swaps, seed)
    utility = payout_matrix(candidates, scenarios, RuleSet()).astype(np.float32)
    utility = np.minimum(utility, config.cap)

    n_folds = 4 if len(draws) >= 80 else 3
    fold_of_origin = np.minimum(
        np.arange(len(draws)) * n_folds // len(draws), n_folds - 1
    )
    fold_scenario = np.asarray([fold_of_origin[i] for i in origins])

    global_mean = utility.mean(axis=1)
    fold_means = np.stack(
        [utility[:, fold_scenario == f].mean(axis=1) for f in range(n_folds)],
        axis=1,
    )
    prior = (
        fold_means.min(axis=1)
        + 0.15 * fold_means.mean(axis=1)
        - 0.05 * fold_means.std(axis=1)
    )

    cumulative = np.zeros(utility.shape[1], dtype=np.float32)
    used = np.zeros(len(candidates), dtype=bool)
    selected = []
    checkpoints = []
    best = None
    bottom_n = max(16, int(round(utility.shape[1] * config.bottom_frac)))

    for n in range(1, max_n + 1):
        bottom = np.argpartition(cumulative, bottom_n - 1)[:bottom_n]
        score = (
            utility[:, bottom].mean(axis=1)
            + config.alpha * global_mean
            + 0.05 * prior
        )
        score[used] = -1e9
        idx = int(np.argmax(score))
        used[idx] = True
        selected.append(idx)
        cumulative += utility[idx]

        if n >= min_n:
            ratio = cumulative / n
            fold_ratio = [
                float(cumulative[fold_scenario == f].mean() / n)
                for f in range(n_folds)
            ]
            record = {
                "N": n,
                "q10": float(np.quantile(ratio, 0.10)),
                "q05": float(np.quantile(ratio, 0.05)),
                "min_fold_mean": min(fold_ratio),
                "mean": float(ratio.mean()),
            }
            checkpoints.append(record)
            key = (
                record["q10"],
                record["q05"],
                record["min_fold_mean"],
                record["mean"],
            )
            if best is None or key > best[0]:
                best = (key, record)

    assert best is not None
    best_n = best[1]["N"]
    return [candidates[i] for i in selected[:best_n]], best[1], checkpoints
