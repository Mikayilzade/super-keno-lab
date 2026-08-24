# Phase 13 — direct ticket-payoff ranking with deterministic execution

Date: 2026-08-25

Status: **NO EDGE — direct ticket-payoff ranking rejected as a primary route.**

## Setup

- Strict walk-forward over **125** targets after 70-draw warmup.
- Fixed universe: **5,000 distinct tickets**, seed `424242` reused from Phase 12; no new favorable pool seed.
- N free on every target: **19..400**.
- N selected only from prior capped-payout prefix curves.
- Four predefined direct-payoff models, with no post-result retuning:
  - ridge on payout capped at 15;
  - ridge on payout capped at 5;
  - ridge on whether a ticket pays >1 AZN;
  - expanding empirical capped-payoff per ticket.
- Ticket-level features use only information available before the target draw: rolling number-score aggregates/dispersion, gaps, previous-draw overlap, contextual pair interactions, ticket structure and rolling structural closeness.
- Each method compared with **20 matched-N random replicas** drawn from the exact same fixed ticket universe.
- Rare 8+ payout contribution reported separately.

## Results

| model | ROI | P/L (AZN) | random mean ROI | blocks > random | positive blocks | 8+ payout share |
|---|---:|---:|---:|---:|---:|---:|
| ridge_cap15 | **0.48423** | **-16,320** | 0.56454 | 0/3 | 0/3 | 6.85% |
| ridge_cap5 | **0.48945** | **-13,380** | 0.53920 | 0/3 | 0/3 | 9.36% |
| ridge_profit_ticket | **0.48882** | **-13,209** | 0.53403 | 0/3 | 0/3 | 7.13% |
| empirical_cap15 | **0.51876** | **-11,312** | 0.54457 | 2/3 | 0/3 | 11.07% |

### ridge_cap15
- cost: 31,642 AZN
- payout: 15,322 AZN
- N range: 19..400, median 334
- all **20/20** random replicas beat the strategy overall
- chronological strategy ROIs: 0.4679 / 0.4999 / 0.4763

### ridge_cap5
- cost: 26,207 AZN
- payout: 12,827 AZN
- N range: 19..397, median 208
- 19/20 random replicas beat the strategy
- chronological strategy ROIs: 0.4540 / 0.5259 / 0.4618

### ridge_profit_ticket
- cost: 25,840 AZN
- payout: 12,631 AZN
- N range: 19..397, median 190
- all **20/20** random replicas beat the strategy
- chronological strategy ROIs: 0.4821 / 0.4904 / 0.4987

### empirical_cap15
- cost: 23,506 AZN
- payout: 12,194 AZN
- N range: 19..400, median 92
- chronological strategy ROIs: 0.5719 / 0.5562 / 0.4718
- it beat the random mean in the first two blocks but failed in the most recent block and remained strongly negative overall.

## Interpretation

Directly predicting robust ticket payoff did **not** solve the failure of per-number prediction. The learned rankings are actually worse than matched random for the three ridge objectives, and the simple empirical-payoff ranking shows no persistent positive P/L.

The failure is not explained by dependence on one rare jackpot: only about 7–11% of payout came from 8+ hit tickets for these methods.

Promotion gate: **none**.

## Decision

Do not tune ridge constants, payout caps or nearby feature windows as the next phase merely to improve these numbers.

Pivot to **Phase 14: draw-level regime/structure prediction**. Instead of ranking numbers or tickets directly, predict coarse properties of the next 20-number draw (range/quadrant balance, parity, sum, overlap/run structure, dispersion/regime uncertainty), then condition among deterministic/prebuilt portfolio components. N remains free and every conditioned choice must beat same-cost random in repeated chronological walk-forward blocks.
