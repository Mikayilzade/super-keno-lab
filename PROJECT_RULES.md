# Project rules

This repository is the dedicated laboratory for Azerbaijan Super Keno strategy research.

## Isolation

- `Mikayilzade/loto-research` is a separate broad lottery-research project.
- Do not delete, move, rewrite, or repurpose files in `loto-research` from this project.
- Data copied here is an independent working copy.
- All Super Keno strategy experiments, code, checkpoints and conclusions belong here.

## Primary objective

Search for a reproducible ticket-selection / portfolio process whose net result remains positive across **real unseen Super Keno draws**.

Portfolio size **N is a free integer variable**. It does not have to be round. A useful construction may contain 347, 662, 12,342 or any other number of distinct tickets.

Different methods and multi-stage methods are explicitly allowed. The project should keep testing materially different portfolio constructions, predictive rules, conditional portfolios and adversarial stress tests rather than getting stuck on one family.

## Exact fixed-portfolio limitation

Under the current snapshotted 1-AZN payout table, the universal fixed-portfolio problem is solved exactly: every fixed ticket has gross mean payout `0.5985557942634199`, so for every fixed N-ticket portfolio there exists at least one mathematically possible 20-of-70 draw with return ratio at most that value.

The bound is achieved by the portfolio of all `C(70,10)=396,704,524,216` distinct tickets, whose payout is constant across every possible draw. Therefore **no fixed ticket list can guarantee break-even or positive profit against every mathematically possible draw** under the current rules.

See `research/FIXED_PORTFOLIO_MAXIMIN_BOUND.md`.

This does **not** close the real-draw problem. Persistent profit on actual future draws would require a non-uniform/predictive effect, a conditional/adaptive selection rule, or another real-world edge.

## Current working assumption

Do not spend project time trying to prove machine/lototron changes. Treat the lototron as unchanged unless a later strategy specifically requires another assumption.

## Evidence rules

- Never use future draws when building a rule claimed to predict an earlier draw.
- Report average result and worst result; optimize the worst unseen-draw floor as a primary metric.
- Keep fixed historical-fit portfolios as anti-overfitting benchmarks, not proof of an edge.
- Record failed approaches as well as successful ones to avoid repeating work.
- Compare strategies against random/simple controls of the same N.
- Current official rules, ticket price and payout table must remain dated/sourced.
- Keep real-money execution out of the research loop until an explicit later decision; current work is simulation/backtesting only.

## Evaluation after Phase 6

The original final 35-draw holdout was opened once after freezing the Phase-6 662-ticket candidate. It is now **consumed** and must never again be called untouched holdout.

Future historical work must use nested/rolling walk-forward evaluation. Truly fresh validation requires future draws collected after a strategy is frozen.

## Data integrity

Every accepted draw must contain exactly 20 unique integers in 1..70. Deduplicate by date, official draw number when present, and sorted 20-number combination. Conflicts are flagged, never guessed.
