from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data_loader import load_and_validate

ROOT = Path(__file__).resolve().parents[1]
NUMBER_FIELDS = [f"n{i}" for i in range(1, 21)]
EXPOSED_ROWS = 160
CURRENT_SCHEDULE_EVIDENCE_FROM = date(2025, 11, 26)
DIAGNOSTIC_START = date(2026, 5, 23)
WEEKDAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def draw_numbers(row):
    return tuple(int(row[f]) for f in NUMBER_FIELDS)


def official_code(d: date) -> int:
    iso = d.isocalendar()
    return int(f"{iso.year % 100:02d}{iso.week:02d}{iso.weekday}")


def freq_vector(rows):
    out = np.zeros(70, dtype=float)
    for row in rows:
        for n in draw_numbers(row):
            out[n - 1] += 1.0
    return out


def corr(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if np.std(a) == 0 or np.std(b) == 0:
        return None
    return float(np.corrcoef(a, b)[0, 1])


def main():
    all_rows = load_and_validate(ROOT / "data")
    rows = all_rows[:EXPOSED_ROWS]
    assert len(rows) == EXPOSED_ROWS
    assert rows[-1]["date"] == "2026-07-19"

    dated = [(date.fromisoformat(r["date"]), r) for r in rows]

    known = 0
    mismatches = []
    for d, row in dated:
        raw = row["official_draw"].strip()
        if not raw:
            continue
        known += 1
        observed = int(raw)
        expected = official_code(d)
        if observed != expected:
            mismatches.append({"date": d.isoformat(), "observed": observed, "expected": expected})

    number4_blocks = []
    for start in range(0, EXPOSED_ROWS, 20):
        block = dated[start : start + 20]
        number4_blocks.append({
            "rows": [start, start + len(block) - 1],
            "start": block[0][0].isoformat(),
            "end": block[-1][0].isoformat(),
            "draws": len(block),
            "number4_count": sum(4 in draw_numbers(r) for _, r in block),
        })

    number4_weekday = []
    for wd, name in enumerate(WEEKDAY_NAMES):
        group = [(d, r) for d, r in dated if d.weekday() == wd]
        count = sum(4 in draw_numbers(r) for _, r in group)
        number4_weekday.append({
            "weekday": name,
            "draws": len(group),
            "number4_count": count,
            "number4_rate": count / len(group),
        })

    current = [(d, r) for d, r in dated if d >= CURRENT_SCHEDULE_EVIDENCE_FROM]
    design = [(d, r) for d, r in current if d < DIAGNOSTIC_START]
    diagnostic = [(d, r) for d, r in current if d >= DIAGNOSTIC_START]

    def tf_diff(group):
        tue_fri = [r for d, r in group if d.weekday() in (1, 4)]
        other = [r for d, r in group if d.weekday() not in (1, 4)]
        return (
            freq_vector(tue_fri) / len(tue_fri) - freq_vector(other) / len(other),
            len(tue_fri),
            len(other),
        )

    design_diff, design_tf, design_other = tf_diff(design)
    diagnostic_diff, diagnostic_tf, diagnostic_other = tf_diff(diagnostic)

    weekday_corrs = {}
    for wd, name in enumerate(WEEKDAY_NAMES):
        left = [r for d, r in design if d.weekday() == wd]
        right = [r for d, r in diagnostic if d.weekday() == wd]
        weekday_corrs[name] = {
            "design_draws": len(left),
            "diagnostic_draws": len(right),
            "frequency_profile_corr": corr(freq_vector(left) / len(left), freq_vector(right) / len(right)),
        }

    result = {
        "scope": {
            "exposed_rows": EXPOSED_ROWS,
            "holdout_opened": False,
            "latest_used": rows[-1]["date"],
        },
        "official_draw_code": {
            "known_ids": known,
            "matches": known - len(mismatches),
            "mismatches": mismatches,
            "formula": "YYWWD using ISO week-year/week/weekday",
        },
        "number4_by_20row_blocks": number4_blocks,
        "number4_by_weekday": number4_weekday,
        "current_schedule_sanity_check": {
            "known_from": CURRENT_SCHEDULE_EVIDENCE_FROM.isoformat(),
            "period_rows": len(current),
            "design_rows": len(design),
            "diagnostic_rows": len(diagnostic),
            "tue_fri_design_draws": design_tf,
            "other_design_draws": design_other,
            "tue_fri_diagnostic_draws": diagnostic_tf,
            "other_diagnostic_draws": diagnostic_other,
            "tue_fri_vs_other_frequency_difference_corr_design_to_diagnostic": corr(design_diff, diagnostic_diff),
            "weekday_profile_correlations": weekday_corrs,
        },
    }

    out = ROOT / "results" / "phase5_operational_regime_audit.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
