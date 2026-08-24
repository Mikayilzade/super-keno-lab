# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 7 — adversarial portfolio search + walk-forward real-draw track`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N is a free integer optimization variable**; round-number grids are controls only.
- Physical/video investigation is no longer a priority. Working assumption: lototron unchanged.
- Current official rules/payouts are snapshotted; scorer/evaluator, baselines and robust search are reproducible.

## Exact universal fixed-portfolio result — CLOSED

See `research/FIXED_PORTFOLIO_MAXIMIN_BOUND.md`.

For any fixed 10-number ticket, exact gross mean payout across all possible 20-of-70 draws is:

**0.5985557942634199 AZN per 1 AZN stake.**

Therefore for every fixed N-ticket portfolio:

`min_draw_return_ratio <= 0.5985557942634199`.

The bound is achieved exactly by taking all `C(70,10)=396,704,524,216` different tickets: every possible draw then pays `237,449,791,580 AZN`, ratio **0.5985557942634199**.

Conclusion: **no fixed ticket list at any N can guarantee break-even or profit against every mathematically possible draw under current rules.**

This does not close the actual-real-draw problem; a persistent real-world edge would require predictive/non-uniform information or an adaptive/conditional process.

## Phase 1 — historical overfit anti-example

Naive matrix selected **N=370**, achieved 120/120 profitable design draws with minimum P/L +137 AZN, then collapsed on the next 40 exposed rows: min return 0.2378, average return 0.6136, profitable 5%.

## Phase 2 — robust complementary portfolio

Frozen robust search selected **N=203**. Reused 40-row diagnostic: min return 0.2759, average return 0.7393, worst P/L -147 AZN, profitable 12.5%.

A fair-generator control showed portfolio geometry alone does not create an edge.

## Phase 3 — empirical signals

No signal gate passed. Previous-draw repeat/avoid, raw hot/cold, fixed pairs and simple structural persistence failed. Contextual pair score remained only a weak lead.

## Phases 4–5 — operational/physical branch

Physical lototron evidence was documented, but no actionable machine/set edge was confirmed. User has now explicitly deprioritized this branch and instructed the project to treat the lototron as unchanged.

## Phase 6 — direct search for an “always plus” historical list

See:
- `results/PHASE6_FIXED_PORTFOLIO_PIVOT.md`
- `experiments/phase6_fixed_portfolio_search.py`
- `results/phase6_candidate_662_indices.json`

A new free-N greedy maximin fit used the first **160 previously exposed real draws**, 30,000 deterministic candidate tickets, seed `260824`, and continuous N search through 1200.

Best fitted portfolio: **N=662**.

Fit on those 160 draws:
- worst payout **1086 AZN** on 662 AZN cost;
- worst P/L **+424 AZN**;
- minimum return **1.64048**;
- profitable draws **160/160**.

This is exactly the type of historical list the project was asked to search for.

### One-time forward check on the original final 35 rows

The algorithm and exact 662-ticket portfolio were frozen first; then the formerly sealed 35 rows were opened once.

Result:
- profitable draws **0/35**;
- worst payout **249 AZN**;
- worst P/L **-413 AZN**;
- minimum return **0.37613**;
- average return **0.505999**;
- best return **0.75831**.

Verdict: **extreme finite-history overfit**. 100% profitability on a known archive is not a sufficient criterion.

The final 35 rows are now **consumed** and must never again be called untouched holdout.

## Current objective

Continue searching by different methods/stages for persistent positive performance on **real unseen draws**, while keeping the exact impossibility of universal fixed >1 return in view.

Two tracks run conceptually in parallel:

### Track A — adversarial/maximin coverage

Purpose: construct strong finite-N portfolios and force them to face newly generated worst-case draws instead of only historical rows.

- build candidate portfolio with free N;
- search the 20-of-70 draw space for a low-payout adversarial witness;
- add witness as a constraint;
- rebuild portfolio;
- repeat until the floor stabilizes;
- compare achieved floor with exact universal ceiling 0.5985557942634199.

This track cannot produce universal positive profit, but it prevents fake historical guarantees and may produce highly balanced portfolio components useful in conditional strategies.

### Track B — real-draw walk-forward strategy

Purpose: find a process that changes/selects the portfolio before each draw using only information available at that time.

- nested rolling walk-forward evaluation across the 195 historical rows;
- test multiple materially different methods, not only frequency signals;
- allow conditional selection among several prebuilt complementary portfolios;
- N remains free at every step;
- future draws after a method is frozen become the next truly fresh validation set.

## NEXT ACTION — Phase 7

1. Implement an adversarial draw finder for an arbitrary fixed portfolio using 70-bit masks + multi-start swap/local search.
2. Verify it finds much worse draws than the 195-history archive for Phase-1/2/6 portfolios.
3. Build a cutting-plane loop: portfolio -> adversarial witnesses -> rebuilt free-N portfolio -> new witnesses.
4. Record best finite-N floor and concrete worst-draw witnesses at each iteration.
5. In parallel, redesign the historical evaluation as rolling walk-forward because the old holdout is spent.
6. Test conditional/dynamic portfolio families separately from fixed-list coverage.
7. Do not return to machine/video research unless a later strategy explicitly needs it.
8. Keep all failures and exact reproducibility seeds/results in the repo.

No autonomous recurring task is enabled for this repository.
