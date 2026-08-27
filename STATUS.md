# Super Keno Lab — status

Last updated: 2026-08-27

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / finite-pool execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- All history-based predictive branches are closed as primary edge sources after strict walk-forward/seed testing.
- Fixed-list universal guarantee is mathematically impossible for the base game.
- Exact after-tax 1x Super Keno expected cash-return ratio: **0.5918070335**.
- Break-even modifier thresholds: direct cash-equivalent subsidy **40.82%**; one-wager bonus **68.97%**.

## Closed primary routes

Do not reopen without materially new information: fixed-list geometry alone; hot/cold/pair/context/mean-reversion; supervised per-number ranking; ticket-payoff regression; continuous structure forecasting; discrete regime/Markov forecasting.

## Current Super-Keno modifier state

No **fully verified executable repeatable positive-EV Super Keno modifier** is known at the 2026-08-27 snapshot.

- `10→10`: `official_status_conflict_conditional_positive`; ROI **1.183614067** if operational/eligible, but do not stake without new operational confirmation.
- RadioArena promo: `current_terms_unresolved_sports_context`; revisit only on materially new product-scope/account evidence.
- Misli APL Fantasy: `current_repeatable_free_entry_bonus_product_scope_unresolved`; 30/20/10 AZN weekly bonus, zero paid gambling spend stated for qualification, but `Lotereya` eligibility/wagering/expiry/withdrawal and exact Misli private-league denominator remain unresolved.
- Do not search for APL round-3 winner artifacts before round 3 is complete (28–31 Aug 2026).

Historical official 10→10 terms prove that promotional balance can be explicitly scoped to `Lotereya` and produce withdrawable winnings. Generic `bonus` wording alone is not evidence that another promotion has this scope.

## Secondary finite-pool route — `1001 Sevinc`

This is not a Super Keno modifier, but is the strongest materially different operator-side finite-denominator mechanism.

Established facts:
- each prize category has a finite predetermined ticket quantity and draw date;
- sales can close at the scheduled cutoff even if not sold out, so under-sold draws are intended;
- each purchased ticket has a chance number;
- current parent page shows **11 draws dated 16.09.2026**;
- recovered current IDs: 1 AZN `10065, 10064, 10066`; 0.5 AZN `10072, 10073, 10067, 10071, 10068, 10069, 10070, 10074`;
- historical raw winning chance IDs use an offset/namespace, so `max(chance ID)` must **not** be used as sold count;
- direct per-draw pages remain client shells to the crawler;
- Trendyol public surfaces have not exposed current cap/sold/remaining.

For any denominator observation, bind:
`(drawId, prize, ticket price, draw date, sold%, observed timestamp)`.

If exact sold tickets `M` are recovered:
`ROI = V_net / (p * M)`.
If cap `C` and remaining `R` are recovered, use `M = C - R`.

### Live sell-through snapshot — 27 Aug 2026

First-party indexed observations previously recovered:
- iPhone 17 Pro Cosmic Orange **43%**;
- Deep Blue **35%**;
- Silver **32%**;
- PlayStation 5 Slim 1 TB **55%**;
- Samsung Galaxy S25 Ultra Black **42%**;
- 1000-AZN gift coupon **17%**;
- iPad Air 13-inch (M2) Starlight 128GB **26%**.

Sell-through is directionally rising by roughly 1–2 percentage points over several days for some prizes. Percent alone cannot prove EV.

### Property-prize tax model

Azerbaijan State Tax Service guidance indicates property/non-cash lottery prizes are treated as non-business income; after deducting participation cash outlay, the remainder is taxed at **14%**. Until coupon-specific classification is proven otherwise, use this conservative model:

`V_economic = h*V - 0.14*(V-p)`

where `h` is usable/resale value fraction.

### Phase 18AN — coupon price conflict / execution guard

See `results/PHASE18AN_1001_SEVINC_COUPON_PRICE_CONFLICT.md`.

A fresh official Azerlotereya social/search surface exposes a **1000-AZN gift coupon at 1 AZN**, conflicting with the prior project assumption that the current 17%-sold coupon was **0.5 AZN**. Until price and sold% are tied to the same current drawId/date, the Phase 18AM coupon cap ceilings are **not execution-safe**.

If the same current coupon is proven to be **1 AZN** and still **17% sold**, conservative property-tax break-even cap ceilings become:
- 60% usable value: **~2,707**;
- 70%: **~3,295**;
- 80%: **~3,883**;
- 100% face value: **~5,060**.

These are approximately half the prior 0.5-AZN ceilings. No +EV claim is made until exact current price + sold% + cap/remaining are bound to one draw.

The official 1001 Sevinc explainer confirms the client surface shows how many tickets remain until the draw, so the required absolute denominator exists operationally even though crawler-accessible pages have not exposed it.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** bind the current 1000-AZN gift coupon to an exact drawId with explicit current **ticket price + sold% + draw date**; do not mix observations from different cycles.
2. Recover predetermined **cap / absolute remaining / sold count** for that exact coupon draw. Second priority: Cosmic Orange.
3. If price=1 AZN and sold%=17% belong to the same current coupon, use the stricter Phase 18AN ceilings; if a distinct 0.5-AZN coupon is proven, recompute only for that exact draw.
4. Seek first-party evidence for coupon tax/settlement classification; default to 14% property-prize treatment until proven otherwise.
5. Re-snapshot sold percentages later to estimate velocity; always store observation date.
6. If cap/remaining is recovered, compute conservative live ROI immediately with multiple value haircuts and friction.
7. Continue fresh Super-Keno modifier scans only for genuinely new zero-cost/free-entry offers explicitly naming `Lotereya` or exposing a product-category label for credited balance.
8. After APL round 3 completes, inspect the next newly dated result artifact once for materially new wallet/category/standings evidence.
9. Revisit RadioArena or 10→10 only on materially new operational evidence.
10. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when Super-Keno modifier classifications actually change.
11. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
12. Do not reopen rejected draw-history prediction branches without materially new information.
