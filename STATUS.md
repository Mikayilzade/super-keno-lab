# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 9 — LP/maximin relaxation + Track B walk-forward start`

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

## Phase 6 — strongest historical always-plus anti-example

Free-N fit on first 160 exposed real draws selected **N=662** and was profitable 160/160 with minimum return **1.64048**, then failed 0/35 on the next frozen block; minimum return **0.37613**, average **0.505999**.

Verdict: extreme finite-history overfit.

## Phase 7 — adversarial finder + first cutting-plane

See `results/PHASE7_ADVERSARIAL_START.md`.

The N=662 historical portfolio was attacked down from real-history minimum 0.376 to reproducible adversarial witnesses around **0.142–0.147**. Five one-witness cutting-plane iterations still left 14–17% adversarial-return holes.

Verdict: real history misses large weak regions in fitted portfolio geometry.

## Phase 8 — multi-witness bank + builder comparison

See:
- `experiments/phase8_multiwitness_builder_compare.py`
- `results/phase8_multiwitness_builder_compare.json`
- `results/PHASE8_MULTIWITNESS_AND_BUILDERS.md`

Setup:
- all 195 rows treated as exposed geometry constraints;
- 12,000 deterministic candidate tickets, seed `260824`;
- four adversarial-bank rounds, four distinct witnesses added per round;
- N free.

Shared-bank builder progression:

| round | N | fitted min | weakest new adversarial return |
|---:|---:|---:|---:|
| 0 | 898 | 0.7082 | 0.1971 |
| 1 | 891 | 0.6846 | 0.1987 |
| 2 | 847 | 0.7166 | 0.1960 |
| 3 | 705 | 0.5872 | 0.1957 |

### Same-bank builder comparison

- worst-8 greedy: N=829, fitted min 0.9614, adversarial 0.1942;
- bottom-24: N=893, adversarial 0.1937;
- bottom-64 / CVaR-like: N=863, initial adversarial 0.2109;
- cap-15 bottom-24: N=716, adversarial 0.1774;
- cap-30 bottom-24: N=854, adversarial 0.1991;
- random same-N control: N=863, adversarial 0.2005;
- cyclic control: N=847, a valid adversarial draw produced **0 payout**.

Worst-8 is another overfit warning: nearly break-even fitted floor but only ~19% under attack.

### Stronger independent attack

Bottom-64 N=863 was attacked using 30,000 additional random valid draws, retaining weak seeds and locally descending them:
- bottom-64 strongest witness: **170/863 = 0.19699**;
- same-N random control: **168/863 = 0.19467**.

Difference is only ~0.23 percentage points. Current greedy/CVaR/capped builders therefore **do not materially beat random portfolio geometry** under stronger adversarial search.

Verdict: **NO ADVERSARIAL EDGE YET. Stop tuning bottom-k constants.**

## Current objective

Continue searching by materially different methods/stages for persistent positive performance on **real unseen draws**, while retaining the adversarial oracle as a mandatory anti-overfit gate.

### Track A — robust portfolio components

Track A cannot produce universal >1 return, but should seek substantially better finite-N geometry than random and create robust components for conditional strategies.

### Track B — actual-profit process

Portfolio may change/select before each draw using only information available then. This is the only route still compatible with persistent real-world profit under the exact fixed-list impossibility result.

## NEXT ACTION — Phase 9

1. Formulate a **fractional maximin / linear-programming relaxation** over a finite candidate-ticket pool and the current adversarial witness bank.
2. Optimize ticket weights directly instead of greedy prefix order.
3. Round/sparsify fractional weights into distinct-ticket portfolios with free N.
4. Attack LP-rounded portfolios with the strong adversarial finder and add new witnesses in a cutting-plane loop.
5. Compare LP-rounded portfolios against matched-N random and Phase-8 bottom-64 controls.
6. Start **Track B rolling walk-forward** dynamic/conditional portfolio experiments separately using only past information at each historical step.
7. Do not spend further phases on bottom-k parameter tuning unless LP results show a concrete reason.
8. Keep all failures, seeds, exact witnesses and reproducible outputs in the repo.

No autonomous recurring task is enabled for this repository.
