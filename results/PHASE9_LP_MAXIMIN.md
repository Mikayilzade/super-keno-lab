# Phase 9 — LP/fractional maximin + rounding

Date: 2026-08-24

Status: **COMPUTED — see JSON for complete reproducibility.**

## Final LP-rounded portfolio

- N: **1106** distinct tickets
- fractional finite-bank floor: **0.957675**
- fractional support: **1219** tickets
- rounded finite-bank min: **0.432188**
- real-195 min: **0.432188**
- strong adversarial witnessed return: **0.225136**

## Controls

- bottom-64 free-N control: N=1120, strong adversarial return **0.219643**
- random control seed 99117: strong adversarial return **0.221519**
- random control seed 99173: strong adversarial return **0.223327**

The LP value is a relaxation on the finite witness bank, not a guarantee over all possible draws. The rounded portfolio is a concrete list of unique tickets and is independently attacked afterward.

## Decision rule

If LP-rounded adversarial performance does not materially separate from same-N random controls, do not keep refining fixed-portfolio geometry. Move the main effort to rolling walk-forward / adaptive portfolio selection, retaining the adversarial oracle as a robustness gate.
