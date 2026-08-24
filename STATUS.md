# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 10 — rolling walk-forward / adaptive conditional portfolio search`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N is a free integer optimization variable**; round-number grids are controls only.
- Physical/video investigation is deprioritized. Working assumption: lototron unchanged.
- All 195 historical rows are now exposed. Future draws after a frozen method are the only fresh validation source.

## Exact universal fixed-portfolio result — CLOSED

For any fixed 10-number ticket, exact gross mean payout across all possible 20-of-70 draws is **0.5985557942634199 AZN per 1 AZN stake**.

Therefore every fixed N-ticket portfolio satisfies:

`min_draw_return_ratio <= 0.5985557942634199`.

No fixed ticket list at any N can guarantee break-even/profit against every mathematically possible draw. Persistent real-world profit, if it exists, requires predictive/non-uniform information or an adaptive/conditional process.

## Phase 6 — historical always-plus anti-example

Free-N fit on first 160 exposed real draws selected **N=662** and was profitable 160/160 with minimum return **1.64048**, then failed 0/35 on the next frozen block; minimum return **0.37613**, average **0.505999**.

Verdict: extreme finite-history overfit.

## Phase 7 — adversarial finder

The N=662 historical portfolio was attacked down to reproducible valid draws returning only about **14–15%** of stake. Cutting-plane rebuilds still admitted 14–17% holes.

Verdict: historical rows alone miss large weak regions in fitted portfolio geometry.

## Phase 8 — multi-witness greedy/CVaR comparison

See `results/PHASE8_MULTIWITNESS_AND_BUILDERS.md`.

Best broad-tail greedy initially reached ~21% adversarial return, but a stronger independent attack reduced it to **0.19699**, while same-N random returned **0.19467**.

Verdict: greedy/capped/CVaR-like fixed geometry does not materially beat random under fresh adversarial search.

## Phase 9 — LP/fractional maximin

See:
- `src/lp_maximin.py`
- `experiments/phase9_lp_maximin.py`
- `results/phase9_lp_maximin.json`
- `results/PHASE9_LP_MAXIMIN.md`
- `results/phase9_lp_portfolio_1106.csv`

Method:
- 12,000 deterministic candidate tickets, seed `260824`;
- finite bank = all 195 real draws + adversarial witnesses;
- LP variables optimize ticket weights and minimum scenario return;
- per-ticket LP weight capped at `1/N`, matching a relaxation of N distinct uniformly purchased tickets;
- fractional solutions rounded into actual distinct-ticket portfolios;
- N searched/adapted rather than fixed to round values;
- each rounded portfolio attacked by fresh adversarial search and new witnesses added.

Final canonical GitHub run:
- **N = 1106** distinct tickets;
- fractional finite-bank floor **0.957675**;
- fractional support **1219** candidates;
- rounded finite-bank / real-195 minimum **0.432188**;
- strong adversarial witnessed return **0.225136**.

Controls:
- bottom-64 free-N control: N=1120, adversarial **0.219643**;
- random N=1106 seed 99117: **0.221519**;
- random N=1106 seed 99173: **0.223327**.

Verdict: **NO MATERIAL ADVERSARIAL ADVANTAGE OVER RANDOM.** LP greatly improves the finite-bank relaxation, but the actual rounded distinct-ticket portfolio is only ~0.18–0.55 percentage points above tested random controls under strong fresh attack. This is too small to justify further fixed-geometry optimization as the main route.

The exact 1106-ticket LP portfolio is preserved as a robust-component candidate, not as a profit strategy.

## Strategic decision

Track A fixed-portfolio geometry has now been tested with:
1. historical greedy maximin;
2. robust/capped/CVaR greedy;
3. multi-witness cutting-plane;
4. fractional LP + rounding.

All converge toward adversarial performance close to random once unseen weak draws are actively searched.

Therefore **Track A is demoted to a robustness/component role**. The adversarial oracle remains mandatory for testing any portfolio component, but no more phases should be spent merely tuning fixed-list geometry unless a new mathematical formulation provides a qualitatively different mechanism.

## Main objective — Track B

Find a process that selects or rebuilds a portfolio **before each draw** using only information that existed at that time, with the practical target of persistent positive net P/L on real future draws.

The process may:
- choose among several prebuilt complementary portfolios;
- change N freely per draw;
- use rolling statistics/signals only from prior draws;
- combine weak signals rather than relying on one hot/cold heuristic;
- abstain / buy zero tickets when the model has insufficient confidence;
- use adversarially robust portfolio components as the execution layer after a predictive decision is made.

## NEXT ACTION — Phase 10

1. Build a strict rolling walk-forward harness across the 195 draws. At every target row, training data must end before that row.
2. Use expanding and rolling windows; begin scoring only after enough history exists.
3. Compare materially different dynamic families:
   - contextual pair/triple scores;
   - rolling hot/cold with shrinkage;
   - previous-draw/group mean reversion;
   - ensemble ranking of multiple weak signals;
   - conditional selection among several prebuilt robust portfolio components;
   - abstention/confidence thresholds;
   - adaptive free N linked to signal strength.
4. Optimize for actual P/L, worst P/L, profitable-draw share, losing streak and drawdown — not hit-count alone.
5. Use nested walk-forward: thresholds/parameters are chosen only from earlier internal windows, then frozen for the next block.
6. Compare every adaptive strategy against same-cost random and no-play baselines.
7. Retain only methods showing repeated forward improvement across multiple chronological blocks, not one lucky period.
8. Use the adversarial oracle on any fixed portfolio component before allowing it into the adaptive system.
9. Save every failed family and exact seeds/results to avoid rediscovery.
10. Future draws after a frozen Phase-10+ method become the only true fresh validation set.

No autonomous recurring task is enabled for this repository.
