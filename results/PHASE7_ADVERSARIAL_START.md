# Phase 7 — adversarial maximin start

Date: 2026-08-24

Status: **IN PROGRESS — adversarial finder validated; first cutting-plane iterations completed.**

## Purpose

The project no longer treats a portfolio that is positive on all known draws as sufficient evidence. Phase 6 demonstrated an extreme historical fit: 662 tickets were positive on all first 160 real draws, but failed on every next 35 draw.

Phase 7 therefore attacks each fitted portfolio with newly generated valid 20-of-70 draws designed to minimize its payout.

## Adversarial finder

Implementation: `src/adversarial.py`.

Method:
- represent a portfolio as a ticket-by-number incidence matrix;
- start from multiple random valid 20-number draws;
- repeatedly evaluate every one-out / one-in swap;
- take the steepest payout-reducing swap;
- retain the lowest local minimum across starts.

The result is a **concrete low-payout witness**, not a proof of the global minimum.

## First attack on the Phase-6 662-ticket portfolio

The Phase-6 portfolio had:
- minimum return on first 160 fitted real draws: **1.64048**;
- minimum return across all 195 known real draws: **0.37613**.

The new adversarial finder found a valid draw with payout only **97 AZN** for 662 AZN cost:

- adversarial return ratio: **0.14653**;
- draw: `3,4,5,6,8,11,16,21,29,32,38,42,45,49,54,56,60,61,62,68`.

An independent heavier run also found a 94-AZN witness (ratio about **0.1420**), confirming that the 195-draw archive was nowhere near the true weak region of the fitted portfolio.

## Cutting-plane loop

Experiment: `experiments/phase7_cutting_plane.py`.
Checkpoint: `results/phase7_cutting_plane_checkpoint.json`.

Each iteration:
1. fit a free-N portfolio against the original first 160 real draws plus all prior adversarial witnesses;
2. find a new low-payout adversarial draw for the frozen portfolio;
3. add that witness to the next iteration.

First five completed iterations:

| iter | constraints | N | fitted constraint min | real-195 min | new adversarial return |
|---:|---:|---:|---:|---:|---:|
| 0 | 160 | 662 | 1.6405 | 0.3761 | 0.1465 |
| 1 | 161 | 560 | 1.5964 | 0.3750 | 0.1482 |
| 2 | 162 | 733 | 1.5593 | 0.3615 | 0.1678 |
| 3 | 163 | 484 | 1.5661 | 0.3347 | 0.1405 |
| 4 | 164 | 728 | 1.5742 | 0.3503 | 0.1717 |

The non-monotonic adversarial column is expected at this stage because both the portfolio builder and adversarial minimizer are heuristic. The important result is that every rebuilt portfolio still has a concrete valid draw paying only roughly **14–17%** of cost despite looking >150% guaranteed on its fitted constraint set.

## Interpretation

This gives a much stronger anti-overfit mechanism than historical holdouts alone. A portfolio is no longer allowed to call itself robust because it covers hundreds of past draws; it must also survive draws actively constructed against its ticket geometry.

The exact universal fixed-list ceiling remains **0.5985557943**, so Track A cannot reach guaranteed profit >1 across all mathematically possible draws. Its purpose is to find balanced portfolio components and expose structural weaknesses before those components enter conditional or adaptive strategies.

## Next action

1. strengthen adversarial search with population/random-sample seeding plus local descent, reducing sensitivity to random starts;
2. run longer cutting-plane sequences and retain multiple adversarial witnesses per portfolio rather than one;
3. compare different portfolio builders (greedy bottom-k, capped payout, diversity constraints, LP/ILP relaxations) against the same witness bank;
4. start Track B rolling walk-forward separately: dynamic/conditional portfolio selection before each historical draw;
5. future real draws after a method is frozen are the only fresh validation source now that the old holdout is consumed.
