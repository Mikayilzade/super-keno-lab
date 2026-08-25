# Super Keno Lab — status

Last updated: 2026-08-25

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / variance-aware execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- All 195 historical rows are exposed; future draws after a frozen method are the only fresh validation source.
- Working assumption: lototron unchanged; physical/video branch remains deprioritized.
- Mandatory rule: stochastic strategy construction must be evaluated across strategy/universe seeds, never one favorable seed.

## Exact fixed-list result — CLOSED

For a fixed 10-number ticket, exact gross return over all possible 20-of-70 draws is **0.5985557942634199 per 1 AZN stake**. Hence no fixed ticket list at any N can guarantee break-even/profit against every mathematically possible draw.

Fixed geometry has been tested via historical maximin, adversarial cutting-plane, broad-tail/CVaR greedy and LP + rounding. All converge close to random geometry under fresh adversarial attack.

## History-based predictive routes — CLOSED AS PRIMARY SOURCE

Rejected after strict walk-forward / seed robustness:
1. hot/cold, contextual pairs, group mean reversion and their ensembles;
2. supervised per-number probability ranking;
3. direct ticket-payoff regression/ranking;
4. continuous draw-structure prediction;
5. discrete regime classification using past structure transitions.

Do not reopen these routes by tuning nearby windows/K/beta values without a materially new information source.

## Phase 15 — oracle structural value

Perfect knowledge of coarse `mean/location + quadrants + balance` was economically valuable as a diagnostic and approximately break-even across multiple fixed ticket universes, but valid pre-target forecasting had no stable skill. This motivated the final discrete-state attempt.

## Phase 16 — discrete coarse regimes — CLOSED, NO GATE

See:
- `experiments/phase16_discrete_regimes.py`
- `results/phase16_discrete_regimes.json`
- `results/PHASE16_DISCRETE_REGIMES.md`

Method:
- past-only deterministic K-means regimes on the seven high-value dimensions: 4 quadrants + odd share + <=35 share + mean/location;
- K = 4 / 6 / 8 fixed in advance;
- valid predictors: class prior, Markov-1, Markov-2, nearest-context class distribution, shrinkage mixture;
- fixed 5,000-ticket universe seed `424242`;
- N free **19..400**, selected only from earlier capped-payout curves;
- 20 matched-N random replicas.

Best valid overall result was `K=8 / Markov-2`:
- ROI **0.58939**;
- matched-random mean **0.55599**;
- P/L **-5,395 AZN**;
- blocks above random **1/3**;
- positive-P/L blocks **0/3**;
- class accuracy **16.0%**.

Other valid configurations had ROI ~0.48..0.587 and all had **0/3 positive blocks**. No configuration passed the promotion gate.

Oracle class-state diagnostics were also weak: ROI **0.6079 / 0.6883 / 0.6539** for K=4/6/8, showing that coarse clustering itself discards much of the valuable exact structural information.

Decision: **close `past draw history -> next draw structure/regime` as a primary edge source.**

## Phase 17 — external purchase-economics / EV modifiers

See:
- `results/PHASE17_EXTERNAL_EV_MODIFIERS.md`
- `src/ev_modifiers.py`
- `tests/test_ev_modifiers.py`

CI: Phase-17 EV tests pass after import-path fix.

### Current exact after-tax base EV

Using the current published payout table and ticketwise tax formula:

| multiplier | expected cash / stake |
|---:|---:|
| 1x | **0.591807** |
| 2x | 0.591266 |
| 5x | 0.589036 |
| 10x | 0.586982 |

Therefore 1x is the best multiplier on expected after-tax cash. Multipliers do not create edge.

### Promotion thresholds

For 1x Super Keno:
- directly cashable rebate needed for break-even: **~40.82% of paid stake**;
- bonus balance that must itself be wagered once before withdrawing winnings: **~68.97% of paid stake**;
- a genuine 100% one-wager match would imply expected personal-capital cash ROI about **1.1836**, i.e. roughly **+18.36% expected profit** before extra account/withdrawal friction.

### Public promotion snapshot — 2026-08-25

- Official Azerlotereya `Cari kampaniyalar` page says **no current campaign**.
- A publicly indexed `10 oyna, 10 qazan` 10-AZN-for-10-AZN welcome offer is classified as a **past campaign**; it is retained only as proof that a sufficiently large external subsidy can mathematically cross break-even.
- Current Unibank cashback terms explicitly exclude gambling/betting and lottery payments, so ordinary Unibank cashback cannot be counted as a subsidy.
- No current repeatable public Super-Keno-specific promo meeting the calculated threshold is verified at this snapshot.

## Strategic decision

The project now distinguishes two fundamentally different objectives:

1. **Base-game fixed/adaptive ticket selection:** extensive history-based methods have not found a persistent edge.
2. **External EV overlays:** promotions, rebates, free tickets, stimulating-lottery codes, channel-specific rewards or other legal subsidies can mathematically make personal-capital EV positive even when the underlying ticket remains negative-EV.

The second route is now the main research direction because it changes the economics rather than trying to predict a fair draw.

## NEXT ACTION — Phase 18

1. Build a structured EV-modifier ledger: source/date, active/inactive, eligibility, eligible games, paid stake, bonus/rebate, wagering requirement, withdrawal rules, max size and expiry.
2. Search current Azerlotereya/Misli/public partner campaigns and account-independent promo-code mechanics; separate current offers from historical examples.
3. Audit stimulating-lottery / extra-chance overlays where ordinary lottery spending grants an additional prize draw; estimate overlay EV only when prize pool and participant/code counts permit defensible bounds.
4. Audit payment-channel rewards/cashback only where lottery transactions are explicitly eligible; do not assume ordinary card cashback applies.
5. For every modifier, compute effective personal-capital EV using `src/ev_modifiers.py` and classify: below threshold / near threshold / positive EV.
6. For any positive-EV modifier, design a variance-aware distinct-ticket portfolio with N free; the objective becomes preserving the subsidy-driven positive expectation while controlling worst draw/downside.
7. Examine whether multiple independent modifiers may legally stack; never assume stackability without terms.
8. Retain multipliers/multi-draw purchase only as controls unless a price discount/reward changes effective stake.
9. Keep promotions finite and capacity-limited in the economic model; a one-time +EV welcome offer is not a perpetual strategy.
10. Save exact terms, calculations, failure reasons and expiry dates so stale promotions are never mistaken for current opportunities.

No autonomous recurring task is enabled for this repository.
