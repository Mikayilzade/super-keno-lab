# Phase 8 — multi-witness adversarial bank and builder comparison

Date: 2026-08-24

Status: **NO ADVERSARIAL EDGE YET.** Multi-witness cutting-plane works, but the tested greedy portfolio builders do not materially beat a same-size random portfolio under stronger adversarial attack.

## Setup

- All 195 historical draws are now considered exposed; this phase is a geometry/adversarial experiment, not a fresh predictive test.
- Candidate universe: **12,000** deterministic distinct random tickets, seed `260824`.
- Portfolio size **N is free** and selected from every prefix.
- A common adversarial witness bank was grown for four rounds, adding four distinct low-payout valid 20-of-70 draws per round.
- Adversarial draws are concrete heuristic witnesses, not proofs of the exact global minimum.

Reproducible experiment: `experiments/phase8_multiwitness_builder_compare.py`.
Raw results: `results/phase8_multiwitness_builder_compare.json`.

## Multi-witness bank growth

Using bottom-32 greedy to grow the shared bank:

| round | N | fitted constraint min | weakest new adversarial witness |
|---:|---:|---:|---:|
| 0 | 898 | 0.7082 | 0.1971 |
| 1 | 891 | 0.6846 | 0.1987 |
| 2 | 847 | 0.7166 | 0.1960 |
| 3 | 705 | 0.5872 | 0.1957 |

Multiple witnesses remove the spectacular 1.5x+ fake guarantees from earlier phases, but the heuristic adversarial floor stalls near ~0.20 rather than approaching the exact universal ceiling 0.59856.

## Builder comparison on the same witness bank

| builder | N | fitted min | real-195 min | adversarial min, first attack |
|---|---:|---:|---:|---:|
| worst-8 greedy | 829 | 0.9614 | 0.9626 | 0.1942 |
| bottom-24 greedy | 893 | 0.6540 | 0.6831 | 0.1937 |
| bottom-64 / CVaR-like | 863 | 0.5446 | 0.5446 | **0.2109** |
| capped-15 bottom-24 | 716 | 0.5838 | 0.5838 | 0.1774 |
| capped-30 bottom-24 | 854 | 0.6066 | 0.6066 | 0.1991 |
| random same-N control | 863 | — | 0.3581 | 0.2005 |
| cyclic control | 847 | — | 0.2739 | **0.0000** |

The worst-8 builder is another overfit warning: it looks almost break-even on its fitted bank but is attacked down to ~0.19. Broad bottom-64 looks best in the first attack. The cyclic construction has a concrete structural hole: a valid 20-number draw paying **0 AZN** across the full 847-ticket set.

## Stronger independent attack

The apparent bottom-64 advantage was challenged with **30,000 additional random valid draws**, retaining the worst seeds and locally descending each.

### bottom-64, N=863
- strongest witnessed payout: **170 AZN**;
- witnessed return: **0.19699**;
- witness: `2,5,12,17,19,21,22,23,26,30,33,38,41,42,46,47,50,54,59,60`.

### random same-N, N=863
- strongest witnessed payout: **168 AZN**;
- witnessed return: **0.19467**.

Difference: only about **0.23 percentage points** of stake. This is not a material adversarial advantage.

## Main conclusion

Current greedy/capped/CVaR-like builders mostly improve coverage of scenarios they have seen. Under stronger search for unseen weak draws, the best greedy portfolio is essentially tied with a random portfolio of the same size.

Therefore **do not spend more phases tuning bottom-k constants**. The next portfolio builder should be a materially different optimization class.

The adversarial oracle remains useful: it exposes fake robustness very quickly and will be retained as a required gate for every future fixed or conditional portfolio component.

## Next action — Phase 9

1. Formulate a fractional maximin / linear-programming relaxation over a finite candidate-ticket pool and the growing adversarial witness bank.
2. Optimize ticket weights directly instead of greedy prefix order.
3. Round/sparsify the fractional solution into distinct-ticket portfolios while keeping N free.
4. Attack the rounded portfolio with the same strong adversarial finder and add new witnesses in a cutting-plane loop.
5. Compare LP-rounded portfolios against random and bottom-64 at matched N.
6. In parallel begin Track B rolling walk-forward dynamic selection, because universal fixed profit is mathematically impossible and Track A is a robustness component rather than the final profit mechanism.
