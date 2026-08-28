# Super Keno Lab — status

Last updated: 2026-08-28

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

No **fully verified executable repeatable positive-EV Super Keno modifier** is known at the 2026-08-28 snapshot.

- `10→10`: `official_status_conflict_conditional_positive`; ROI **1.183614067** if operational/eligible, but do not stake without new operational confirmation.
- RadioArena promo: `current_terms_unresolved_sports_context`; revisit only on materially new product-scope/account evidence.
- Misli APL Fantasy: `current_repeatable_free_entry_bonus_product_scope_unresolved`; 30/20/10 AZN weekly bonus, zero paid gambling spend stated for qualification, but `Lotereya` eligibility/wagering/expiry/withdrawal and exact Misli private-league denominator remain unresolved.
- Do not search for APL round-3 winner artifacts before round 3 is complete (28–31 Aug 2026).
- Fresh modifier scan in Phase 18BG found no new zero-cost offer explicitly proving current `Lotereya` eligibility.

Historical official 10→10 terms prove promotional balance can be explicitly scoped to `Lotereya` and produce withdrawable winnings. Generic `bonus` wording alone is not evidence that another promotion has this scope.

## Secondary finite-pool route — `1001 Sevinc`

This remains the strongest materially different operator-side finite-denominator mechanism currently known.

Established facts:
- each prize category has a finite predetermined ticket quantity and draw date;
- sales can close at scheduled cutoff even if not sold out, so under-sold draws are intended;
- current parent page shows **11 draws dated 16.09.2026**: 3 at 1 AZN and 8 at 0.5 AZN;
- current link order recovered as: `10065,10064,10066,10072,10073,10067,10071,10068,10069,10070,10074`;
- historical raw winning chance IDs use an offset/namespace, so `max(chance ID)` must not be used as sold count;
- generic API/client-shell/registry/Trendyol/local-download/public-Telegram paths have not exposed current cap/sold/remaining and remain closed unless materially new surface appears;
- official explainer states the account/client surface can show how many tickets remain until the draw, confirming that the absolute denominator exists operationally.

For any denominator observation bind `(drawId, prize, ticket price, draw date, sold%, source surface, crawl timestamp)`.
If exact sold tickets `M` are recovered: `ROI = V_net / (p*M)`. If cap `C` and remaining `R` are recovered, use `M=C-R`.

### Current bound draw map

- `10065` — iPhone 17 Pro 256 GB Cosmic Orange — 1 AZN — 16.09.2026 — last complete first-party sold input **43%**.
- `10064` — iPhone 17 Pro 256 GB Deep Blue — 1 AZN — 16.09.2026 — fresh sold% unresolved; older Misli snapshot ~34% is monitoring only.
- `10066` — iPhone 17 Pro 256 GB Silver — 1 AZN — 16.09.2026 — fresh first-party sold **33%**; current execution target #1.
- `10072` — Samsung Galaxy S25 Ultra Black — 0.5 AZN — 16.09.2026 — drawId-bound; current sold% still requires fresh reacquisition before execution use.
- `1000-AZN gift coupon` — current ticket price resolved as **0.5 AZN**; drawId and fresh sold% unresolved; expired 17% observation must not be reused.

### Silver execution buffer

Using ~3,150 AZN market reference and the standing 14% property-prize tax model, Silver's approximate break-even total-cap ceilings are:

| usable value | 33% sold | 35% sold | 38% sold | 43% sold |
|---:|---:|---:|---:|---:|
| 60% | 4,391 | 4,140 | 3,814 | 3,370 |
| 70% | 5,346 | 5,040 | 4,642 | 4,103 |
| 80% | 6,300 | 5,940 | 5,471 | 4,835 |
| 100% | 8,210 | 7,740 | 7,129 | 6,300 |

Any future positive-EV call must use current sold fraction or a conservative forward execution buffer.

### Property-prize tax model

Azerbaijan State Tax Service guidance indicates property/non-cash lottery prizes are treated as non-business income; after deducting participation cash outlay, the remainder is taxed at **14%**. Until prize-specific classification is proven otherwise, use `V_economic = h*V - 0.14*(V-p)`, where `h` is usable/resale value fraction.

### Phase 18BG — controlled sold-% transition cap solver

See `results/PHASE18BG_1001_SEVINC_PERCENT_TRANSITION_CAP_PROBE.md` and `scripts/phase18bg_percent_transition_cap_solver.py`.

No new public absolute denominator was found. A new non-API fallback has been formalized: infer hidden ticket cap `C` from the integer `Satıldı %` display across **controlled consecutive percentage transitions**. Under a floor-display model, visible `p%` implies `ceil(p*C/100) <= M <= ceil((p+1)*C/100)-1`; known cumulative ticket additions allow these intervals to be intersected across observations. The solver supports floor and nearest-integer models.

A single percentage jump does not identify `C`. The useful pattern is the last no-change point and first-change point around **two consecutive percentage boundaries**. This can narrow a cap near ~5k to a tight band. External purchases contaminate exact inference, so any such test would need a short observation window and conservative bounds.

**No paid probe was executed and no autonomous spend is authorized.** The route is kept as a fallback if account screenshots/observations become available or if a controlled manual probe is later explicitly chosen.

## Current candidate hierarchy

1. **`10066 Silver`** — fully bound; 1 AZN; fresh 33% sold; denominator target #1.
2. **`10072 S25 Ultra Black`** — fully drawId-bound; 0.5 AZN; potentially superior economics, but fresh sold% remains unresolved.
3. `10065 Cosmic Orange` — fully bound; 1 AZN; last complete sold input 43%.
4. `10064 Deep Blue` — fully bound; 1 AZN; fresh sold% unresolved.
5. `1000-AZN gift coupon` — current price 0.5 AZN; drawId and fresh sold% unresolved.

The decisive variable remains absolute `cap / remaining / sold-count`.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** seek absolute `cap / remaining / sold-count` for `10066 Silver` and `10072 S25` only through materially new rendered/account/client artifacts. Do not reopen exhausted generic API, registry, Trendyol, local-download or stale social paths.
2. If sequential account/rendered sold-% observations around known ticket additions become available, run `scripts/phase18bg_percent_transition_cap_solver.py` immediately; do not execute paid probes autonomously.
3. Reacquire a fresh complete first-party sold percentage for `10072 / S25` only when a newly dated/current card or rendered artifact surfaces.
4. Recover a fresh sold% for `10064 Deep Blue`; never infer it from neighboring snippets.
5. Bind the 1000-AZN gift coupon to a current drawId and reacquire its sold% as one fresh record.
6. Recover other current 0.5-AZN candidates only from current-cycle artifacts; never import previous-cycle prize names.
7. If cap/remaining is recovered for any current draw, compute buffered live ROI immediately under 60/70/80/100% usable value, 14% property-prize tax and a sell-through execution buffer.
8. Continue fresh Super-Keno modifier scans only for genuinely new zero-cost/free-entry offers explicitly naming `Lotereya` or exposing a product-category label for credited balance.
9. After APL round 3 completes, inspect the next newly dated result artifact once for materially new wallet/category/standings evidence.
10. Revisit RadioArena or 10→10 only on materially new operational evidence.
11. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when Super-Keno modifier classifications actually change.
12. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
13. Do not reopen rejected draw-history prediction branches without materially new information.
