# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 7 — adversarial portfolio search + walk-forward real-draw track`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N is a free integer optimization variable**; round-number grids are controls only.
- Physical/video investigation is deprioritized. Working assumption: lototron unchanged.
- The old final 35-row holdout was consumed once in Phase 6 and is no longer fresh validation.

## Exact universal fixed-portfolio result — CLOSED

For any fixed 10-number ticket, exact gross mean payout across all possible 20-of-70 draws is **0.5985557942634199 AZN per 1 AZN stake**.

Therefore every fixed N-ticket portfolio satisfies:

`min_draw_return_ratio <= 0.5985557942634199`.

The bound is achieved by the all-ticket portfolio of `C(70,10)=396,704,524,216` distinct tickets. So no fixed ticket list at any N can guarantee break-even/profit against every mathematically possible draw.

This does **not** close the real-draw problem: persistent real-world profit would require predictive/non-uniform information or an adaptive/conditional process.

## Phase 6 — strongest historical “always plus” anti-example

Free-N maximin fit on the first 160 already-exposed real draws selected **N=662**.

Fit:
- minimum return **1.64048**;
- worst P/L **+424 AZN**;
- profitable **160/160**.

One-time next-35 check after freezing the portfolio:
- profitable **0/35**;
- minimum return **0.37613**;
- average return **0.505999**.

Verdict: extreme finite-history overfit.

## Phase 7 — adversarial finder implemented

See:
- `src/adversarial.py`
- `experiments/phase7_cutting_plane.py`
- `results/PHASE7_ADVERSARIAL_START.md`
- `results/phase7_cutting_plane_checkpoint.json`

The adversarial finder performs multi-start steepest one-out/one-in swap descent over valid 20-of-70 draws. Each result is a concrete low-payout witness, not a global-minimum proof.

### Attack on the Phase-6 N=662 portfolio

Historical minima:
- fitted first 160: **1.64048** return;
- all 195 real draws: **0.37613** return.

Adversarial search found:
- 97-AZN witness with 25-start deterministic run: return **0.14653**;
- independent heavier multi-start run: **94 AZN**, return about **0.1420**;
- independent 100,000-random-draw scan followed by local descent: **96 AZN**, return **0.1450**.

Conclusion: the real archive missed a very large weak region in the fitted ticket geometry. The ~14–15% adversarial return is reproducible across search variants.

## Cutting-plane checkpoint

Each iteration fits a free-N portfolio against the first 160 real draws plus all prior adversarial witnesses, then generates a new witness.

First five completed iterations:

| iter | constraints | N | fitted constraint min | real-195 min | new adversarial return |
|---:|---:|---:|---:|---:|---:|
| 0 | 160 | 662 | 1.6405 | 0.3761 | 0.1465 |
| 1 | 161 | 560 | 1.5964 | 0.3750 | 0.1482 |
| 2 | 162 | 733 | 1.5593 | 0.3615 | 0.1678 |
| 3 | 163 | 484 | 1.5661 | 0.3347 | 0.1405 |
| 4 | 164 | 728 | 1.5742 | 0.3503 | 0.1717 |

The adversarial column is not expected to be monotonic because both portfolio building and adversarial minimization are currently heuristic. The key fact is that every rebuilt portfolio still admits a concrete valid witness paying only about **14–17%** of stake despite appearing >150% guaranteed on its fitted constraint set.

## Current objective

Continue searching by different methods/stages for persistent positive performance on **real unseen draws**, while using adversarial search to prevent fake historical guarantees.

### Track A — adversarial/maximin coverage

- strengthen the adversarial finder;
- keep a growing witness bank;
- rebuild free-N portfolios against multiple adversaries, not just history;
- compare different portfolio builders against the same witness bank;
- approach the exact universal ceiling 0.5985557943 as closely as practical for finite N.

Track A cannot itself yield universal >1 profit; its output is robust portfolio geometry/components.

### Track B — real-draw walk-forward strategy

- rolling/nested walk-forward across historical rows;
- portfolio may change before each draw using only prior information;
- test materially different conditional/dynamic rules, not only frequency signals;
- N remains free at every step;
- future draws after a method is frozen become fresh validation.

## NEXT ACTION

1. Upgrade adversarial search to combine bulk random/population seeding with local descent and keep several distinct low-payout witnesses per portfolio.
2. Continue cutting-plane for longer sequences using a witness bank, not one witness per iteration only.
3. Compare alternative portfolio constructors: bottom-k greedy, capped-payout robust greedy, diversity/intersection penalties, and LP/ILP relaxation if practical.
4. Record best finite-N adversarial floor and explicit worst-draw witnesses for each constructor.
5. Start Track B rolling walk-forward dynamic portfolio experiments separately.
6. Do not return to machine/video research unless a later strategy explicitly requires it.
7. Keep all failed approaches, seeds and reproducible outputs in the repo.

No autonomous recurring task is enabled for this repository.
