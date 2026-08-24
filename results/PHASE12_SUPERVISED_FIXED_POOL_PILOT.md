# Phase 12 — supervised walk-forward probability model + fixed ticket universe

Date: 2026-08-24

Status: **NO EDGE.**

## Why this is materially different

Phase 10/11 generated a new stochastic candidate-ticket pool at every target, and seed robustness showed that this sampling variance could create a false weak lead.

Phase 12 therefore removed that mechanism:

- one fixed universe of **5,000 distinct tickets**, seed `424242`;
- no per-target ticket-generation seed;
- a supervised expanding walk-forward model predicts a score/probability for each of the 70 numbers;
- every fixed ticket is ranked deterministically by the sum of its predicted number probabilities;
- N remains free over every integer **19..300**;
- N at target `t` is chosen only from realized prefix performance on the preceding 32 scored targets;
- matched-random control uses the exact selected N.

## Predictor

A ridge-regularized linear probability model (`lambda=20`) is refit before every target. Training examples are number-by-draw observations from earlier targets only.

Features available before target:
- rolling number frequency: 5 / 10 / 20 / 40 / 80 draws;
- gap since last appearance;
- previous-draw membership;
- contextual pair residual score;
- previous-draw group mean-reversion feature.

No future target information is used in feature generation or training.

## Result — 125 strict one-step targets

Strategy:
- cost: **9232 AZN**
- payout: **4932 AZN**
- net P/L: **-4300 AZN**
- ROI: **0.53423**
- profitable targets: **9.6%**
- N range: **19..277**, median **28**

Matched random using the same N schedule:
- cost: **9232 AZN**
- payout: **5204 AZN**
- net P/L: **-4028 AZN**
- ROI: **0.56369**

The supervised model is worse than its matched-random control.

## Chronological blocks

| rows | strategy ROI | random ROI | strategy P/L |
|---|---:|---:|---:|
| 70..109 | 0.45101 | 0.51808 | -1989 AZN |
| 110..149 | 0.59803 | 0.58994 | -1390 AZN |
| 150..194 | 0.57183 | 0.59833 | -921 AZN |

Only the middle block marginally beats random; all three blocks are strongly negative in absolute P/L.

## Verdict

A straightforward supervised per-number probability model does not extract a usable next-draw edge from the current features/history. Do not tune ridge constants or minor feature windows as the next phase merely to improve this result.

Next work should use a qualitatively different target/representation, for example predicting **draw-level structures or conditional ticket payoff directly**, or exploiting cross-sectional ranking with strong seed-averaged execution and nested model selection. Every future adaptive strategy must report both control-ticket randomness and strategy-construction randomness.
