from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import load_and_validate

ROOT = Path(__file__).resolve().parents[1]
SEED = 20260824
SIMS = 1000
P = 20 / 70


def incidence(rows):
    x = np.zeros((len(rows), 70), dtype=np.int8)
    for i, row in enumerate(rows):
        nums = [int(row[f"n{j}"]) for j in range(1, 21)]
        x[i, np.asarray(nums) - 1] = 1
    return x


def sim_matrix(n, rng):
    x = np.zeros((n, 70), dtype=np.int8)
    for i in range(n):
        x[i, rng.choice(70, 20, replace=False)] = 1
    return x


def max_change_stat(x, w):
    best = (-1.0, -1)
    for t in range(w, len(x) - w + 1):
        a = x[t - w : t].mean(axis=0)
        b = x[t : t + w].mean(axis=0)
        stat = float(np.sum((a - b) ** 2))
        if stat > best[0]:
            best = (stat, t)
    return best


def mc_p(values, observed):
    values = np.asarray(values)
    return float((np.sum(values >= observed) + 1) / (len(values) + 1))


def main():
    rows = load_and_validate(ROOT / "data")
    assert len(rows) == 195

    # Final holdout rows 160..194 remain sealed. Phase 4 uses only exposed rows 0..159.
    exposed = rows[:160]
    x = incidence(exposed)
    xd, xv = x[:120], x[120:160]

    counts = x.sum(axis=0)
    expected = len(x) * P
    observed_range = int(counts.max() - counts.min())
    observed_maxdev = float(np.max(np.abs(counts - expected)))
    observed_chi = float(np.sum((counts - expected) ** 2 / (len(x) * P * (1 - P))))

    rng = np.random.default_rng(SEED)
    ranges, maxdevs, chis = [], [], []
    cp_sims = {10: [], 15: [], 20: [], 30: []}
    for _ in range(SIMS):
        sim = sim_matrix(len(x), rng)
        c = sim.sum(axis=0)
        ranges.append(int(c.max() - c.min()))
        maxdevs.append(float(np.max(np.abs(c - len(sim) * P))))
        chis.append(float(np.sum((c - len(sim) * P) ** 2 / (len(sim) * P * (1 - P)))))
        for w in cp_sims:
            cp_sims[w].append(max_change_stat(sim, w)[0])

    dates = [row["date"] for row in exposed]
    cp = {}
    for w, simulated in cp_sims.items():
        stat, t = max_change_stat(x, w)
        cp[str(w)] = {
            "stat": stat,
            "cut_index": int(t),
            "left_last_date": dates[t - 1],
            "right_first_date": dates[t],
            "mc_p": mc_p(simulated, stat),
        }

    design_counts = xd.sum(axis=0)
    diagnostic_counts = xv.sum(axis=0)
    cold_order = np.argsort(design_counts)

    result = {
        "holdout_opened": False,
        "rows_used": 160,
        "design_rows": 120,
        "diagnostic_rows": 40,
        "seed": SEED,
        "fair_simulations": SIMS,
        "marginal_frequency": {
            "expected_count_per_number": expected,
            "min_number": int(np.argmin(counts) + 1),
            "min_count": int(counts.min()),
            "max_number": int(np.argmax(counts) + 1),
            "max_count": int(counts.max()),
            "range": observed_range,
            "range_mc_p": mc_p(ranges, observed_range),
            "max_abs_deviation": observed_maxdev,
            "max_abs_deviation_mc_p": mc_p(maxdevs, observed_maxdev),
            "global_chi_like": observed_chi,
            "global_chi_like_mc_p": mc_p(chis, observed_chi),
        },
        "coldest_design_numbers": [
            {
                "number": int(i + 1),
                "design_count": int(design_counts[i]),
                "diagnostic_count": int(diagnostic_counts[i]),
            }
            for i in cold_order[:10]
        ],
        "change_point_scan": cp,
        "notes": [
            "Maximum single-number deviation is a flagged lead, not a proven physical bias.",
            "Number 4 is the extreme low-frequency number in the first 160 exposed rows.",
            "Its independent 40-row diagnostic persistence is weak and below the signal gate.",
            "The strongest 10-row change-point hint is near 2026-06-02; longer windows do not support a stable regime boundary.",
            "No final holdout row was inspected or scored.",
        ],
    }
    out = ROOT / "results" / "phase4_physical_regime_audit.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
