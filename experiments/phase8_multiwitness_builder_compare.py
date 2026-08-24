from __future__ import annotations

import json
import random
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.baselines import random_unique_tickets
from src.data_loader import load_and_validate
from src.evaluator import payout_matrix
from src.rules import RuleSet, validate_ticket

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_COUNT = 12_000
CANDIDATE_SEED = 260824
PAYOUT = np.array([0, 1, 0, 0, 0, 2, 5, 15, 150, 1500, 100000], dtype=np.float32)


def load_draws():
    rows = load_and_validate(ROOT / "data")
    draws = [tuple(int(r[f"n{i}"]) for i in range(1, 21)) for r in rows]
    assert len(draws) == 195
    return draws


def incidence(tickets):
    a = np.zeros((len(tickets), 70), dtype=np.uint8)
    for i, ticket in enumerate(tickets):
        t = validate_ticket(ticket)
        a[i, np.asarray(t, dtype=int) - 1] = 1
    return a


def cyclic_tickets(n):
    steps = [1, 3, 9, 11, 13, 17, 19, 23, 27, 29, 31, 33, 37, 41, 43, 47, 51, 53, 57, 59, 61, 63, 67]
    out, seen = [], set()
    for step in steps:
        for start in range(70):
            t = tuple(sorted((((start + i * step) % 70) + 1) for i in range(10)))
            if t not in seen:
                seen.add(t)
                out.append(t)
                if len(out) >= n:
                    return out
    return out


def evaluate(tickets, draws):
    totals = payout_matrix(tickets, draws, RuleSet()).sum(axis=0)
    ratios = totals / len(tickets)
    return {
        "N": len(tickets),
        "min": float(ratios.min()),
        "p10": float(np.quantile(ratios, 0.10)),
        "avg": float(ratios.mean()),
        "profitable_share": float(np.mean(ratios > 1.0)),
    }


def build_greedy(pm, *, max_n=900, bottom_k=24, cap=None):
    utility = np.minimum(pm, cap) if cap is not None else pm
    cumulative_utility = np.zeros(pm.shape[1], dtype=np.float32)
    cumulative_real = np.zeros(pm.shape[1], dtype=np.float32)
    used = np.zeros(pm.shape[0], dtype=bool)
    means = utility.mean(axis=1)
    selected = []
    best = None

    for n in range(1, max_n + 1):
        k = min(bottom_k, pm.shape[1])
        worst = np.argpartition(cumulative_utility, k - 1)[:k]
        score = utility[:, worst].mean(axis=1) + 0.01 * means
        score[used] = -1e30
        idx = int(np.argmax(score))
        used[idx] = True
        selected.append(idx)
        cumulative_utility += utility[idx]
        cumulative_real += pm[idx]

        if n >= 80:
            ratio = cumulative_real / n
            rec = {
                "N": n,
                "min": float(ratio.min()),
                "p05": float(np.quantile(ratio, 0.05)),
                "avg": float(ratio.mean()),
            }
            key = (rec["min"], rec["p05"], rec["avg"])
            if best is None or key > best[0]:
                best = (key, rec)

    assert best is not None
    return selected[: best[1]["N"]], best[1]


def local_descent(ticket_incidence, draw, max_steps=40):
    current = np.zeros(70, dtype=bool)
    current[np.asarray(draw, dtype=int) - 1] = True
    hits = ticket_incidence[:, current].sum(axis=1).astype(np.int16)
    payout = float(PAYOUT[hits].sum())

    for _ in range(max_steps):
        ins = np.where(~current)[0]
        local_best = payout
        best_out = best_in = None
        best_hits = None

        for out_number in np.where(current)[0]:
            candidate_hits = hits[None, :] - ticket_incidence[:, out_number][None, :] + ticket_incidence[:, ins].T
            values = PAYOUT[candidate_hits].sum(axis=1)
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

    return tuple((np.where(current)[0] + 1).tolist()), payout


def multiple_adversaries(tickets, seed, *, count=4, starts=12):
    ti = incidence(tickets)
    rng = np.random.default_rng(seed)
    found = {}
    for _ in range(starts):
        draw = tuple(sorted((rng.choice(70, 20, replace=False) + 1).tolist()))
        witness, payout = local_descent(ti, draw)
        found[witness] = min(payout, found.get(witness, float("inf")))

    ranked = sorted((payout, draw) for draw, payout in found.items())
    chosen = []
    for payout, draw in ranked:
        if all(len(set(draw) & set(existing)) <= 17 for _, existing in chosen):
            chosen.append((payout, draw))
        if len(chosen) >= count:
            break
    if len(chosen) < count:
        for item in ranked:
            if item not in chosen:
                chosen.append(item)
            if len(chosen) >= count:
                break

    return [
        {"payout": payout, "ratio": payout / len(tickets), "draw": list(draw)}
        for payout, draw in chosen
    ]


def strong_random_scan_attack(tickets, seed, *, samples=30_000, keep=24, batch=1000):
    ti = incidence(tickets)
    rng = np.random.default_rng(seed)
    best = []

    for start in range(0, samples, batch):
        size = min(batch, samples - start)
        draw_matrix = np.zeros((size, 70), dtype=np.uint8)
        draws = []
        for i in range(size):
            d0 = np.sort(rng.choice(70, 20, replace=False))
            draw_matrix[i, d0] = 1
            draws.append(tuple((d0 + 1).tolist()))
        hits = ti @ draw_matrix.T
        values = PAYOUT[hits].sum(axis=0)
        idx = np.argpartition(values, keep - 1)[:keep]
        best.extend((float(values[i]), draws[int(i)]) for i in idx)
        best = sorted(best, key=lambda x: x[0])[:keep]

    local = {}
    for _, draw in best:
        witness, payout = local_descent(ti, draw)
        local[witness] = min(payout, local.get(witness, float("inf")))
    payout, witness = min((p, d) for d, p in local.items())
    return {
        "payout": payout,
        "ratio": payout / len(tickets),
        "draw": list(witness),
        "unique_local_minima": len(local),
        "sample_min": best[0][0],
    }


def main():
    draws = load_draws()
    candidates = random_unique_tickets(CANDIDATE_COUNT, CANDIDATE_SEED)
    base = payout_matrix(candidates, draws, RuleSet()).astype(np.float32)
    witness_bank = []
    result = {"candidate_count": CANDIDATE_COUNT, "seed": CANDIDATE_SEED, "bank_rounds": [], "builders": []}

    # Grow one common bank: four rounds, four independent adversarial witnesses per round.
    for round_index in range(4):
        full = np.concatenate([base, payout_matrix(candidates, witness_bank, RuleSet())], axis=1) if witness_bank else base
        selected, fit = build_greedy(full, max_n=900, bottom_k=32)
        portfolio = [candidates[i] for i in selected]
        adversarial = multiple_adversaries(portfolio, 82000 + round_index, count=4, starts=10)
        existing = set(witness_bank)
        for a in adversarial:
            witness = tuple(a["draw"])
            if witness not in existing:
                witness_bank.append(witness)
                existing.add(witness)
        result["bank_rounds"].append({
            "round": round_index,
            "constraints_before": full.shape[1],
            "N": len(portfolio),
            "fit": fit,
            "real": evaluate(portfolio, draws),
            "new_adversarial_ratios": [a["ratio"] for a in adversarial],
        })

    full = np.concatenate([base, payout_matrix(candidates, witness_bank, RuleSet())], axis=1)
    specs = [
        ("worst8", 8, None),
        ("bottom24", 24, None),
        ("bottom64", 64, None),
        ("cap15_bottom24", 24, 15),
        ("cap30_bottom24", 24, 30),
    ]
    built = {}

    for j, (name, bottom_k, cap) in enumerate(specs):
        selected, fit = build_greedy(full, max_n=1000, bottom_k=bottom_k, cap=cap)
        portfolio = [candidates[i] for i in selected]
        adversarial = multiple_adversaries(portfolio, 90000 + j, count=5, starts=14)
        record = {
            "name": name,
            "N": len(portfolio),
            "fit": fit,
            "real": evaluate(portfolio, draws),
            "adversarial_min": min(a["ratio"] for a in adversarial),
            "worst_adversarial_witness": min(adversarial, key=lambda a: a["ratio"]),
        }
        result["builders"].append(record)
        built[name] = portfolio

    first_best = max(result["builders"], key=lambda r: r["adversarial_min"])
    matched_n = first_best["N"]
    for j, (name, portfolio) in enumerate([
        ("random_sameN", random_unique_tickets(matched_n, 99117)),
        ("cyclic_sameN", cyclic_tickets(matched_n)),
    ]):
        adversarial = multiple_adversaries(portfolio, 93000 + j, count=5, starts=16)
        result["builders"].append({
            "name": name,
            "N": len(portfolio),
            "fit": None,
            "real": evaluate(portfolio, draws),
            "adversarial_min": min(a["ratio"] for a in adversarial),
            "worst_adversarial_witness": min(adversarial, key=lambda a: a["ratio"]),
        })

    # Strong independent attack on the apparent best greedy portfolio and a same-N random control.
    bottom64 = built["bottom64"]
    random_control = random_unique_tickets(len(bottom64), 99117)
    result["strong_attack"] = {
        "bottom64": strong_random_scan_attack(bottom64, 123456),
        "random_sameN": strong_random_scan_attack(random_control, 123457),
    }
    result["best_by_strong_attack"] = "bottom64_but_near_random"

    out = ROOT / "results" / "phase8_multiwitness_builder_compare.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
