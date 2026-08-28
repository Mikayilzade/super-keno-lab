#!/usr/bin/env python3
"""Infer finite ticket-cap candidates from controlled sold-% transitions.

Research-only helper for 1001 Sevinc. It does NOT place bets or make network calls.

Model:
- displayed sold percentage is an integer generated from M/C;
- C = total predetermined ticket cap;
- M = sold tickets before a controlled block;
- k = known additional tickets bought during that block;
- external sales during the observation window must be zero/negligible for an exact inference.

The solver supports floor and nearest-integer display models and intersects multiple
observations. A single percentage transition generally does NOT identify C; two or
more controlled transitions can narrow it sharply.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Observation:
    cumulative_added: int
    displayed_percent: int


def interval_for_display(C: int, pct: int, mode: str) -> tuple[int, int]:
    """Inclusive integer M interval that renders as pct for a given cap C."""
    if mode == "floor":
        lo = math.ceil(pct * C / 100)
        hi = math.ceil((pct + 1) * C / 100) - 1
    elif mode == "nearest":
        # half-up nearest integer: pct-0.5 <= 100*M/C < pct+0.5
        lo = math.ceil((pct - 0.5) * C / 100)
        hi = math.ceil((pct + 0.5) * C / 100) - 1
    else:
        raise ValueError(f"unsupported mode: {mode}")
    return max(0, lo), min(C, hi)


def feasible_caps(
    observations: Iterable[Observation],
    c_min: int = 1,
    c_max: int = 100_000,
    mode: str = "floor",
) -> list[tuple[int, int, int]]:
    """Return (C, base_M_lo, base_M_hi) consistent with all observations."""
    obs = list(observations)
    if not obs:
        raise ValueError("at least one observation is required")
    if obs[0].cumulative_added != 0:
        raise ValueError("first observation must have cumulative_added=0")

    out: list[tuple[int, int, int]] = []
    for C in range(c_min, c_max + 1):
        base_lo, base_hi = 0, C
        feasible = True
        for o in obs:
            lo, hi = interval_for_display(C, o.displayed_percent, mode)
            lo -= o.cumulative_added
            hi -= o.cumulative_added
            base_lo = max(base_lo, lo)
            base_hi = min(base_hi, hi, C - o.cumulative_added)
            if base_lo > base_hi:
                feasible = False
                break
        if feasible:
            out.append((C, base_lo, base_hi))
    return out


def parse_obs(values: list[str]) -> list[Observation]:
    out = []
    for v in values:
        k, p = v.split(":", 1)
        out.append(Observation(int(k), int(p)))
    out.sort(key=lambda x: x.cumulative_added)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--obs",
        nargs="+",
        required=True,
        help="observations as cumulative_added:displayed_percent, e.g. 0:33 17:34 66:35",
    )
    ap.add_argument("--c-min", type=int, default=1)
    ap.add_argument("--c-max", type=int, default=100_000)
    ap.add_argument("--mode", choices=["floor", "nearest"], default="floor")
    ap.add_argument("--show", type=int, default=25)
    args = ap.parse_args()

    obs = parse_obs(args.obs)
    caps = feasible_caps(obs, args.c_min, args.c_max, args.mode)
    print(f"mode={args.mode} observations={obs}")
    print(f"feasible_cap_count={len(caps)}")
    if caps:
        values = [x[0] for x in caps]
        print(f"cap_range={min(values)}..{max(values)}")
        print("first_candidates:")
        for row in caps[: args.show]:
            print(row)


if __name__ == "__main__":
    main()
