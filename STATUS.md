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
`(drawId, prize, ticket price, draw date, sold%, observed timestamp)`.

If exact sold tickets `M` are recovered:
`ROI = V_net / (p * M)`.
If cap `C` and remaining `R` are recovered, use `M = C - R`.

### Live sell-through integrity — 27 Aug 2026

Current execution-quality target:
- **iPhone 17 Pro 256 GB Cosmic Orange — 1 AZN — 16.09.2026 — 43% sold**, freshly reproducible on Azerlotereya.

A cached first-party Misli snapshot for the **same prize + same 1-AZN price + same 16.09.2026 draw date**, crawled about three days earlier, showed **34% sold**. See `results/PHASE18AQ_1001_SEVINC_COSMIC_ORANGE_SELLTHROUGH_VELOCITY.md`.

This is the first bound multi-timestamp sell-through pair for a current draw. Observed index movement is **+9 percentage points over approximately three crawl-days**. Do not extrapolate it linearly as a guaranteed sales rate; crawl timestamps are observation times, not exact transaction timestamps. The important conclusion is that finite-pool EV is materially time-sensitive and must be recomputed immediately before any purchase.

At retail benchmark `V=3,289 AZN`, 1-AZN ticket price and conservative 14% non-cash-prize tax model, current 43%-sold break-even cap ceilings are approximately:
- 60% usable value: **3,519 tickets**;
- 70% usable value: **4,284**;
- 80% usable value: **5,049**;
- 100% usable value: **6,578**.

At the older 34% snapshot those ceilings were about 4,450 / 5,418 / 6,385 / 8,320 respectively. The admissible cap has therefore already tightened materially during the same draw cycle.

Previously recovered indexed observations also included Deep Blue 35%, Silver 32%, PS5 Slim 55%, Galaxy S25 Ultra Black 42%, 1000-AZN gift coupon 17%, and iPad Air 26%; however only observations freshly bound to the current draw instance may be used for execution.

### Phase 18AR — registration/client-surface audit

See `results/PHASE18AR_1001_SEVINC_REGISTRATION_AND_CLIENT_SURFACE_AUDIT.md`.

Fresh first-party crawl still reproduces Cosmic Orange at **43% sold**. The official game page identifies State Tax Service registration **№316 / 12.05.2025**, but targeted exact registration/name/domain searches did **not** recover a public indexed registration/rules document containing per-prize ticket quantities. Ordinary registry-number search is therefore closed unless a new registry surface appears.

Important consistency warning: the same official parent page currently renders live cards as **3 × 1 AZN + 8 × 0.5 AZN**, while its static `Necə oynanılır?` copy still says `1, 2, 5 AZN`. Static explanatory copy can lag live configuration; execution price/category data must come only from a bound current card/draw observation.

A materially different client-bundle fetch was attempted, but the execution container had no DNS/network access. This is a tooling blocker, not evidence that no client endpoint exists.

### Coupon observation status

The old **1000-AZN gift coupon 17%** observation is **not execution-valid current data**. Phase 18AP could not freshly reproduce one current coupon record binding prize + price + sold% + 16.09.2026 date. Current coupon price also remains unresolved. Do not combine the old 17% snapshot with any current price or cap.

### Property-prize tax model

Azerbaijan State Tax Service guidance indicates property/non-cash lottery prizes are treated as non-business income; after deducting participation cash outlay, the remainder is taxed at **14%**. Until coupon-specific classification is proven otherwise, use:

`V_economic = h*V - 0.14*(V-p)`

where `h` is usable/resale value fraction.

The official 1001 Sevinc explainer confirms the client surface shows how many tickets remain until the draw, so the required absolute denominator exists operationally even though crawler-accessible pages have not exposed it.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** keep Cosmic Orange as the freshest bound target. Recover exact drawId and predetermined **cap / absolute remaining / sold count** from a materially different rendered/account/client surface; do not repeat ordinary registration-number search.
2. Re-snapshot the same Cosmic Orange card later with timestamp. If sold% changes, recompute cap ceilings immediately; if the card disappears/stales, expire the 43% observation.
3. If cap/remaining is recovered, compute live ROI immediately under 60/70/80/100% value haircuts, 14% property-prize tax and an execution buffer for sell-through between observation and purchase.
4. Re-acquire the current 1000-AZN gift coupon only if it appears as one fresh bound record: prize + draw date + ticket price + sold% + timestamp. Do not reuse the expired 17% input otherwise.
5. Recover exact prize→drawId mapping for any newly bound coupon card before computing ROI.
6. Seek first-party evidence for coupon tax/settlement classification; default to 14% property-prize treatment until proven otherwise.
7. Continue fresh Super-Keno modifier scans only for genuinely new zero-cost/free-entry offers explicitly naming `Lotereya` or exposing a product-category label for credited balance.
8. After APL round 3 completes, inspect the next newly dated result artifact once for materially new wallet/category/standings evidence.
9. Revisit RadioArena or 10→10 only on materially new operational evidence.
10. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when Super-Keno modifier classifications actually change.
11. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
12. Do not reopen rejected draw-history prediction branches without materially new information.
