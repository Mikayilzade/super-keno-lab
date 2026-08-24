# Phase 2 — robust complementary search

Date: 2026-08-24

Status: **NOT SUCCESS — materially more stable than Phase 1, still negative on unseen/diagnostic draws.**

## Frozen method

Phase 2 deliberately removes the main Phase 1 failure mode: selecting tickets because of one spectacular historical 8+/9+/10-hit event.

Method:
- deterministic candidate pool: **6,000** unique random tickets, seed `20260824`;
- portfolio size **N is free** and selected from every prefix, not a round-number grid;
- selection utility caps each ticket's per-draw contribution at **15 AZN** during search;
- each training draw is expanded with **3 perturbation draws**, each swapping **2 of the 20 drawn numbers**;
- greedy selection targets the bottom **15%** of current smoothed scenarios;
- chronological fold-stability prior rewards tickets that contribute across multiple training periods rather than one row;
- actual uncapped payout table is used only when evaluating a frozen portfolio.

The frozen configuration was selected using training-only expanding walk-forward checks. The final 35-row holdout was not read or scored.

## Training-only configuration selection

Five predeclared robust configurations were compared using:
1. fit on first 60 training rows -> score next 30;
2. fit on first 90 training rows -> score next 30.

Primary configuration-selection key: worst next-block minimum payout/cost ratio, then worst 10th-percentile ratio, then average ratio.

Winner:
`cap=15, variants=3, swaps=2, bottom_frac=0.15, alpha=0.03`

Its two internal forward checks were:

| Fit rows | Selected N | Next-block min ratio | Next-block p10 ratio | Next-block avg ratio |
|---:|---:|---:|---:|---:|
| 60 | 142 | 0.282 | 0.309 | 0.506 |
| 90 | 270 | 0.307 | 0.384 | 0.529 |

N changed naturally with the data; no round-number target was imposed.

## Leave-30-out stability inside the first 120 rows

With the configuration already frozen, each 30-row chronological block was omitted in turn.

| Omitted block | Selected N | Min ratio | p10 ratio | Avg ratio |
|---:|---:|---:|---:|---:|
| 1 | 244 | 0.279 | 0.368 | 0.487 |
| 2 | 292 | 0.366 | 0.397 | 0.523 |
| 3 | 215 | 0.279 | 0.356 | 0.773 |
| 4 | 192 | 0.333 | 0.354 | 0.568 |

This is much less spectacular than Phase 1, but importantly it is far less dependent on one exact historical row.

## Final Phase 2 portfolio fitted on all 120 training rows

The frozen search selected **N = 203** tickets.

Training:
- minimum payout/cost ratio: **0.5862**;
- 10th percentile ratio: **0.6256**;
- average payout/cost ratio: **1.1734**;
- worst P/L: **-84 AZN**;
- profitable draws: **42.5%**;
- worst date: **2026-02-18**.

Unlike the Phase 1 overfit portfolio, Phase 2 does **not** claim historical guaranteed profit.

The exact 203-ticket frozen portfolio is saved in `results/phase2_candidate_203.csv`.

## Reused 40-row diagnostic block

Important: these 40 rows were already exposed by Phase 1, so this is **not a new untouched test**. It is only a diagnostic comparison.

Phase 2, N=203:
- minimum payout/cost ratio: **0.2759**;
- 10th percentile ratio: **0.3719**;
- average payout/cost ratio: **0.7393**;
- worst P/L: **-147 AZN**;
- average P/L: **-52.93 AZN**;
- profitable draws: **12.5%**;
- worst date: **2026-05-29**.

Phase 1 overfit portfolio, N=370, on the same block:
- minimum ratio: **0.2378**;
- average ratio: **0.6136**;
- profitable draws: **5%**.

So the robust method improves the reused diagnostic floor, average return and profitable-draw share, but it is still far from persistent positive performance.

## Fair-random negative control

The frozen 203-ticket portfolio was also tested against **500 newly generated uniform random 20-of-70 draws** that were not used by selection.

Phase 2:
- min ratio: **0.256**;
- q05 ratio: **0.330**;
- average ratio: **0.584**;
- profitable draws: **8.4%**.

Median of 20 ordinary random 203-ticket portfolios on the same synthetic draws:
- min ratio: **~0.251**;
- q05 ratio: **~0.330**;
- average ratio: **~0.551**;
- profitable draws: **~8.0%**.

Conclusion: portfolio geometry alone does not manufacture an edge under a fair synthetic generator. The next meaningful gains must come from a real empirical/regime signal in the draw process, with the robust portfolio layer used to convert that signal into coverage.

## Holdout

The final **35 draws (2026-07-20 .. 2026-08-23)** remain sealed and were not scored in Phase 2.

## Next direction

Do not open the 35-row holdout yet.

Phase 3 should shift emphasis from pure coverage optimization to **walk-forward empirical signal discovery**, while retaining the Phase 2 robust portfolio engine:
- previous-draw overlap and lag structure;
- rolling hot/cold signals with shrinkage;
- pair/triple co-occurrence stability;
- range/parity/run/gap regime features;
- change-point/regime detection;
- candidate pools conditioned on signals available *before* each draw;
- nested walk-forward tests where both the signal and portfolio are rebuilt only from past data.

Only if a signal-conditioned method materially beats the random and Phase 2 controls across internal forward windows should a candidate be frozen for the final 35-row holdout.
