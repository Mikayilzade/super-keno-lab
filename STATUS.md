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
- current parent page on 2026-08-27 exposes **3 draws at 1 AZN and 8 draws at 0.5 AZN**;
- recovered current IDs: 1 AZN `10065, 10064, 10066`; 0.5 AZN `10072, 10073, 10067, 10071, 10068, 10069, 10070, 10074`;
- historical raw winning chance IDs use an offset/namespace, so `max(chance ID)` must **not** be used as sold count;
- direct per-draw pages remain client shells to the crawler;
- Trendyol public surfaces have not exposed current cap/sold/remaining.

For any denominator observation, bind:
`(drawId, prize, ticket price, draw date, sold%, source surface, crawl timestamp)`.

If exact sold tickets `M` are recovered:
`ROI = V_net / (p * M)`.
If cap `C` and remaining `R` are recovered, use `M = C - R`.

### Current execution target — drawId 10065

The current first 1-AZN card has been mapped to:

- **drawId=10065**
- **iPhone 17 Pro 256 GB Cosmic Orange**
- **1 AZN**
- draw date **16.09.2026**

As of the freshest reproducible Azerlotereya surface on 2026-08-27, this card is **43% sold**.

A first-party Misli search surface for the same prize/date/price currently exposes **35% sold**, but its crawl timestamp is about three days older. This is treated as asynchronous cache/staleness, not as a live rollback or a separate denominator. See `results/PHASE18AT_1001_SEVINC_CROSS_SURFACE_CACHE_DIVERGENCE.md`.

Execution rule: never average or merge sell-through across surfaces. Use the freshest reproducible first-party observation for the fully bound draw record and retain the source + crawl timestamp.

At retail benchmark `V=3,289 AZN`, 1-AZN ticket price and conservative 14% non-cash-prize tax model, current 43%-sold break-even cap ceilings are approximately:
- 60% usable value: **3,519 tickets**;
- 70% usable value: **4,284**;
- 80% usable value: **5,049**;
- 100% usable value: **6,578**.

A previously bound older snapshot for the same Cosmic Orange draw showed 34% sold; it is diagnostic only. Do not extrapolate crawl-to-crawl percentage movement linearly as a guaranteed transaction rate.

Fresh 2026-08-27 indexing also exposes iPhone 17 Pro 256 GB Silver at **33% sold**, up from the previously recovered 32% snapshot, confirming sell-through is continuing.

Previously recovered indexed observations also included Deep Blue 35%, PS5 Slim 55%, Galaxy S25 Ultra Black 42%, 1000-AZN gift coupon 17%, and iPad Air 26%; however only observations freshly bound to the current draw instance may be used for execution.

### Public client/API endpoint audit — exhausted for now

See `results/PHASE18AV_1001_SEVINC_PUBLIC_CLIENT_ENDPOINT_SURFACE_EXHAUSTION.md`.

Targeted searches for `drawId`, `ticketCount`, `remainingTickets`, `soldCount`, exact `10065 + qalan bilet`, and exact current-prize remaining-count surfaces did **not** recover a public indexed first-party endpoint, JSON payload, static bundle field or absolute denominator. The detail page remains a client shell to the available crawler.

A direct public-script inspection attempt was blocked by the execution environment's lack of external DNS and therefore provides no operator-side evidence. Do not treat that technical limitation as a game conclusion.

Decision: do **not** repeat generic `10065 + remaining/cap/API-field` searches unless a materially new rendered/account/client surface appears.

### Registration/client-surface audit

The official game page identifies State Tax Service registration **№316 / 12.05.2025**, but targeted exact registration/name/domain searches did **not** recover a public indexed registration/rules document containing per-prize ticket quantities. Ordinary registry-number search is closed unless a new registry surface appears.

Important consistency warning: the official parent page currently renders live cards as **3 × 1 AZN + 8 × 0.5 AZN**, while static explanatory copy has lagged live configuration in prior crawls. Execution price/category data must come only from a bound current card/draw observation.

The official explainer confirms the client surface shows how many tickets remain until the draw, so the required absolute denominator exists operationally even though crawler-accessible pages have not exposed it.

### Coupon observation status

The old **1000-AZN gift coupon 17%** observation is **not execution-valid current data**. It could not be freshly reproduced as one bound current record with prize + price + sold% + 16.09.2026 date. Do not combine the old 17% snapshot with any current price or cap.

### Property-prize tax model

Azerbaijan State Tax Service guidance indicates property/non-cash lottery prizes are treated as non-business income; after deducting participation cash outlay, the remainder is taxed at **14%**. Until coupon-specific classification is proven otherwise, use:

`V_economic = h*V - 0.14*(V-p)`

where `h` is usable/resale value fraction.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** rebuild the full current **11-prize table** for the 16.09.2026 cycle with fresh bound observations `(drawId where proven, prize, price, sold%, timestamp)` and rank candidates by break-even-cap tolerance under conservative net-value assumptions. Do not assume Cosmic Orange remains the best finite-pool target.
2. Use the ranking to choose the best low-sold/high-value candidate for any next materially different denominator search. Avoid repeating exhausted generic `10065 + remaining/cap/API-field`, registration-number, or Trendyol searches.
3. Re-snapshot Azerlotereya Cosmic Orange with timestamp. If sold% changes, expire 43% and recompute cap ceilings immediately. Do not interpret stale lower values from other surfaces as rollback.
4. If cap/remaining is recovered for any current draw, compute live ROI immediately under 60/70/80/100% value haircuts, 14% property-prize tax and an execution buffer for sell-through between observation and purchase.
5. Re-acquire the current 1000-AZN gift coupon only if it appears as one fresh bound record: prize + draw date + ticket price + sold% + timestamp. Do not reuse the expired 17% input otherwise.
6. Seek first-party evidence for coupon tax/settlement classification; default to 14% property-prize treatment until proven otherwise.
7. Continue fresh Super-Keno modifier scans only for genuinely new zero-cost/free-entry offers explicitly naming `Lotereya` or exposing a product-category label for credited balance.
8. After APL round 3 completes, inspect the next newly dated result artifact once for materially new wallet/category/standings evidence.
9. Revisit RadioArena or 10→10 only on materially new operational evidence.
10. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when Super-Keno modifier classifications actually change.
11. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
12. Do not reopen rejected draw-history prediction branches without materially new information.
