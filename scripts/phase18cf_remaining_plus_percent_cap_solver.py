#!/usr/bin/env python3
"""Recover/narrow a finite-pool cap from an exact remaining count and displayed sold%.

1001 Sevinc first-party guidance says the product surface exposes how many tickets
remain for the draw to take place. If that count is R and the true target pool cap
is C, then sold M = C - R. A displayed integer sold percentage constrains C even
when the percentage is rounded or truncated.

N for Super Keno portfolio optimization is unrelated and remains free.
"""

from __future__ import annotations

import argparse
import math


def compatible(c: int, remaining: int, pct: int, mode: str) -> bool:
    sold = c - remaining
    if sold < 0 or c <= 0:
        return False
    x = 100.0 * sold / c
    if mode == "round":
        # conventional half-up display assumption
        return math.floor(x + 0.5) == pct
    if mode == "floor":
        return math.floor(x) == pct
    if mode == "ceil":
        return math.ceil(x) == pct
    raise ValueError(mode)


def solve(remaining: int, pct: int, cmax: int, mode: str):
    return [c for c in range(max(remaining, 1), cmax + 1) if compatible(c, remaining, pct, mode)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--remaining", type=int, required=True)
    ap.add_argument("--pct", type=int, required=True, help="displayed integer sold percent")
    ap.add_argument("--cmax", type=int, default=100000)
    ap.add_argument("--mode", choices=["round", "floor", "ceil", "all"], default="all")
    args = ap.parse_args()

    modes = ["round", "floor", "ceil"] if args.mode == "all" else [args.mode]
    for mode in modes:
        vals = solve(args.remaining, args.pct, args.cmax, mode)
        if vals:
            print(f"{mode}: {len(vals)} caps; min={vals[0]} max={vals[-1]}")
            if len(vals) <= 30:
                print("  ", vals)
        else:
            print(f"{mode}: no compatible caps <= {args.cmax}")


if __name__ == "__main__":
    main()
