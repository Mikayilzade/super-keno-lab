# Phase 10 — rolling walk-forward adaptive portfolio search

Date: 2026-08-24

Status: **NO GATE PASSED**

## Strict walk-forward protocol

- warmup: 70 draws
- scored targets: 125
- candidate pool per family/target: 320
- N: free integer prefix 19..320
- selection at target t uses only rows before t
- meta-family selection uses only realized prior target outcomes
- abstention uses only prior realized outcomes

## Overall

- meta, no abstention: ROI **0.4559**, net P/L **-1967.00 AZN**
- meta + abstention: played **17 / 125**, ROI **0.4366**, net P/L **-360.00 AZN**
- matched random, same abstention: ROI **0.6839**, net P/L **-202.00 AZN**
- best individual family by ROI: **ensemble_b06**, ROI **0.7147**

## Risk

- meta + abstention max drawdown: **360.00 AZN**
- max losing streak: **13** played/target rows
- played N range: **19 .. 124**, median **22.0**

## Gate

- positive net: **False**
- beats same-cost random ROI: **False**
- positive chronological blocks: **0 / 3**
- final gate: **False**

Complete per-target trace and every family result are in `results/phase10_walkforward_adaptive.json`.
