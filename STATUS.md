# Super Keno Lab — status

Last updated: 2026-08-27

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / variance-aware execution`

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

- `10→10`: `official_status_conflict_conditional_positive`; mathematically ROI **1.183614067** if operational and eligible, but do not stake without new operational confirmation.
- RadioArena promo: `current_terms_unresolved_sports_context`; do not revisit without materially new product-scope terms/account evidence.
- Misli APL Fantasy: `current_repeatable_free_entry_bonus_product_scope_unresolved`; 30/20/10 AZN weekly bonus, zero paid gambling spend stated for qualification, but `Lotereya` eligibility/wagering/expiry/withdrawal and exact Misli private-league denominator remain unresolved.
- Do not search for APL round-3 winner artifacts before round 3 is complete (28–31 Aug 2026).

Historical official 10→10 terms prove that promotional additional balance can be explicitly scoped to `Lotereya` and produce withdrawable winnings. Generic `bonus` wording alone is not evidence that another promotion has this scope.

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
`(drawId, prize, ticket price, draw date, observed timestamp)`.

If exact sold tickets `M` are recovered, conservative single-prize ROI is:
`ROI = V_net / (p * M)`.
If cap `C` and remaining `R` are recovered, use `M = C - R`.

### Phase 18AJ — first live sold% recovered

See `results/PHASE18AJ_1001_SEVINC_LIVE_SOLD_PERCENT_AND_CAP_THRESHOLDS.md`.

On 27 Aug 2026, the official `1001 Sevinc / Tirajlar` search-index surface exposed:
- **iPhone 17 Pro 256 GB Cosmic Orange**;
- ticket price **1 AZN**;
- draw date **16.09.2026**;
- **Satıldı: 43%**.

Current Azerbaijan retail benchmark used for this exact iPhone: **3,289 AZN**.

### Phase 18AK — multi-prize live sell-through snapshot

See `results/PHASE18AK_1001_SEVINC_MULTI_PRIZE_LIVE_SELLTHROUGH.md`.

Current first-party search-index observations on 27 Aug 2026:
- iPhone 17 Pro Cosmic Orange **43%**;
- Deep Blue **35%**;
- Silver **32%**;
- PlayStation 5 Slim 1 TB **55%**;
- Samsung Galaxy S25 Ultra Black **42%**;
- 1000-AZN gift coupon **17%**;
- iPad Air 13-inch (M2) Starlight 128GB **26%**.

Earlier Misli index values imply sell-through is directionally rising by roughly 1–2 percentage points over several days for some prizes. Percent alone still cannot prove EV.

### Phase 18AM — property-prize tax correction

See `results/PHASE18AM_1001_SEVINC_PROPERTY_PRIZE_TAX_CORRECTION.md`.

New first-party tax evidence materially corrects prior cap ceilings. Azerbaijan State Tax Service guidance states that lottery prizes paid in **property/non-cash form** are treated as non-business income; after deducting participation cash outlay, the remaining amount is taxed at **14%**. The 500-AZN lottery exemption discussed elsewhere applies to **cash-form** winnings.

Therefore physical-prize EV must use, approximately:

`V_after_tax = V - 0.14 * (V - p)`

and a conservative resale/use model:

`V_economic = h*V - 0.14*(V-p)`

where `h` is usable/resale value fraction. This is stricter than taxing only the haircut value.

Corrected current break-even cap ceilings:

1. **1000-AZN gift coupon**, 0.5 AZN ticket, 17% sold — assuming conservative property-prize tax treatment until exact coupon classification is proven:
   - 60% usable value: **~5,413** cap;
   - 70%: **~6,589**;
   - 80%: **~7,766**;
   - 100% face value: **~10,118**.
2. **iPhone 17 Pro 256 GB Cosmic Orange**, 1 AZN, 43% sold, 3,289-AZN retail benchmark:
   - after-tax full-use value ≈ **2,828.68 AZN**;
   - break-even cap ≈ **6,578** before any resale haircut.
3. **PS5 Slim 1 TB**, 0.5 AZN, 55% sold, ~1,449.99-AZN benchmark:
   - after-tax full-use value ≈ **1,247.06 AZN**;
   - break-even cap ≈ **4,535** before resale haircut.

Previous untaxed Phase 18AL ceilings must **not** be used for execution. The coupon remains the highest-information denominator target, but its tax classification is itself an unresolved variable: gift coupon may be property/voucher/cash-equivalent operationally. Until proven otherwise, use the 14% property-prize model.

No +EV claim is made until exact cap/remaining is recovered.

## NEXT ACTION — Phase 18 continuation

1. Highest priority: recover predetermined **cap / absolute remaining / sold count** for the current **1000-AZN gift coupon** draw; second priority Cosmic Orange.
2. Seek first-party evidence for the **tax/settlement classification of the 1000-AZN gift coupon**; default conservatively to 14% property-prize treatment until proven otherwise.
3. Bind prize names to exact draw IDs only from explicit evidence, never from card ordering alone.
4. Re-snapshot current sold percentages on later dates to estimate sell-through velocity; always store crawl/observation date.
5. If cap/remaining is recovered, compute conservative live ROI immediately using property-form tax, multiple `V_net` haircuts, resale/usage friction and any exact coupon-specific treatment.
6. Expand the current-cycle prize/sold table only when first-party indexed evidence exposes additional prizes; do not mix old-cycle snippets.
7. Continue fresh Super-Keno modifier scans only for genuinely new zero-cost/free-entry offers that explicitly name `Lotereya` or expose a product-category label for credited bonus/promocode balance.
8. After APL round 3 completes, inspect the next newly dated Misli APL result artifact once for materially new wallet/category/standings evidence.
9. Revisit RadioArena or 10→10 only on materially new operational evidence.
10. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when Super-Keno modifier classifications actually change.
11. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
12. Do not reopen rejected draw-history prediction branches without materially new information.
