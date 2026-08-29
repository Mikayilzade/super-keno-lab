# Super Keno Lab — status

Last updated: 2026-08-29

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / finite-pool execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- History-based predictive branches remain closed as primary edge sources after strict walk-forward/seed testing.
- Fixed-list universal guarantee is mathematically impossible for the base game.
- Exact after-tax 1x Super Keno expected cash-return ratio: **0.5918070335**.
- Break-even modifier thresholds: direct cash-equivalent subsidy **40.82%**; one-wager bonus **68.97%**.

## Current conclusion

No **fully verified executable repeatable positive-EV Super Keno modifier** is known at the 2026-08-29 snapshot.

### Modifier state

- `10→10`: `official_status_conflict_conditional_positive`; conditional ROI **1.183614067** if operational/eligible. Main campaign terms say valid through **31 Aug 23:59**, FAQ still says **31 Jul 23:59**. Do not stake without materially new account/support/current-UI confirmation.
- `1001 Sevinc` purchases count immediately toward the 10 AZN qualifying wager; bonus balance is described as having no turnover requirement, but current Super-Keno eligibility is not proven strongly enough for an executable call.
- RadioArena promo: revisit only on materially new product-scope/account evidence.
- Misli APL Fantasy: repeatable free-entry bonus, but `Lotereya` eligibility/wagering/expiry/withdrawal and exact denominator remain unresolved.
- **Oley Oley:** `historical_lottery_eligible_overlay_denominator_unresolved`; no longer treat as a live executable modifier. Official launch copy on **2026-06-09** explicitly gave **2 promo chances per 5 AZN** for `Virtual İdman, ePoz-Qazan, Lotereya`. Third-week inventory and a **2026-07-17** campaign update are consistent with a six-week June–July run; by 17 July the first Changan had been awarded and the second/final car was scheduled for the following week's draw. No current/renewal artifact was recovered for the 2026-08-29 snapshot. Historical economics remain useful: Super Keno needs **1.02048241625 AZN EV per Oley-Oley chance** to break even; bonus-only 10,000 AZN weekly pool would suffice only below roughly **9,799 eligible chances** before bonus haircuts. `T_week` remains unknown.

## Closed primary routes

Do not reopen without materially new information: fixed-list geometry alone; hot/cold/pair/context/mean-reversion; supervised per-number ranking; ticket-payoff regression; continuous structure forecasting; discrete regime/Markov forecasting.

## Secondary finite-pool route — `1001 Sevinc`

This remains the strongest materially different operator-side finite-denominator mechanism currently known.

Established facts:
- current parent page shows **11 draws dated 16.09.2026**: 3 at 1 AZN and 8 at 0.5 AZN;
- current link order recovered as `10065,10064,10066,10072,10073,10067,10071,10068,10069,10070,10074`;
- `10066` and `10072` live-link integrity reconfirmed; direct detail pages remain client-shell only;
- fresh public search index (2026-08-29) exposes the current 11-draw parent collection but no denominator-bearing indexed detail result for exact `drawId=10066` / `drawId=10072`; historical `drawId` detail routes are indexable, so generic exact-ID search is now bounded until a new cached/detail/rendered artifact appears;
- historical chance IDs are offset/namespace values, so `max(chance ID)` must not be used as sold count;
- official explainer states account/client surface can show how many tickets remain until the draw;
- **Phase 18CF tightens that semantic:** first-party wording says the surface shows how many tickets remain **for the draw to take place**, while sales stop when the **specified ticket count** is reached. Therefore a draw-bound exact remaining count `R` is operationally `C-M`, where `C` is the specified ticket target/cap and `M` sold. When paired with the already preserved integer sold%, `R` can recover or sharply narrow `C` even if the percentage is rounded/truncated. Solver: `scripts/phase18cf_remaining_plus_percent_cap_solver.py`;
- retail/POS artifacts remain a distinct denominator lead; lone six-digit chance numbers are insufficient;
- `operational_integrity_status` remains required after an official March-2026 incident where some purchased tickets failed to enter scheduled draws;
- `1001 Sevinc` is first-party identified as registration **316 / 12.05.2025**;
- first-party conditions-document namespace is known, but no indexed registration-316 DOCX has been recovered;
- Trendyol Azerbaijan is an official `1001 Sevinc` sub-distributor with an account ticket surface, but public searching exposed no denominator field;
- Misli mobile app has a live `Lotereya -> 1001 Sevinc` surface;
- exact first-party Android binary entrypoint remains `https://yukle.misli.az/misliaz_android.apk?v=1361`; browser fetch reaches APK MIME but cannot persist bytes; generic mirror/package and `endir.misli.az` branches are bounded absent new evidence;
- public `Biletini Yoxla` is live, but first-party semantics favor `Bilet nömrəsi`/serial being distinct from `şans nömrəsi`; do not submit guessed/public chance numbers;
- five legitimate public winning chance numbers from the first draw are preserved only as schema fixtures: `103932, 107185, 112723, 116364, 121104`;
- repeated real category-level sellouts are verified from first-party operator channels; `execution_closure_risk` is mandatory for future live opportunities;
- Telemetr indexes historical posts from the official `@azerlotereya` Telegram channel and exposes real `1001 Sevinc` operator copy. A targeted numeric-denominator probe (`Silver`, `S25`, `33%`, `qalıb`, `satılıb`) yielded no absolute count/cap, so classify as `NEW_SURFACE_NO_NUMERIC_HIT_YET` and do not repeat the same empty keyword set unless a new indexed artifact appears;
- **Phase 18CG adds the direct official Telegram web viewer as a distinct live first-party surface.** It exposes current message-level context and demonstrates that `1001 Sevinc` prize names + ticket prices can appear in plaintext, but the inspected live window contained no exact `R`, `M`, `C`, stock, issuance, maxTickets or numerator/denominator for `10066 Silver` / `10072 S25`. Classification: `NEW_FIRST_PARTY_SOCIAL_SURFACE_NO_DENOMINATOR_HIT`. Do not mechanically rescan the same plaintext window; reopen only on a new prize-specific/numeric post or directly inspectable media artifact.
- **Phase 18CH adds a new product-design artifact route.** A public LinkedIn post by Zulfiyya Shikhaliyeva states that she and Hasan Aliyev designed the `1001 Sevinc` UX/UI and names Azərlotereya Digital/QA contributors. Her public Behance profile lists `Middle UX/UI Designer — Azərlotereya`; the indexed first portfolio page does not expose a `1001 Sevinc` case study, while later pages/redirect destinations remain unresolved. Classification: `NEW_PRODUCT_DESIGN_ARTIFACT_ROUTE_NO_DENOMINATOR_YET`. This route is now preferred over repeating generic keyword searches because real UI mockups/screenshots could reveal exact progress/remaining field labels or values.

For any denominator observation bind `(drawId, prize, ticket price, draw date, sold%, source surface, crawl timestamp)`.
If exact sold tickets `M` are recovered: `ROI = V_net / (p*M)`. If cap `C` and remaining `R` are recovered, use `M=C-R`. If only exact `R` plus a contemporaneous integer sold% are recovered, enumerate integer `C` under plausible display rounding rules with the Phase 18CF solver.

### Current candidate hierarchy

1. **`10066 Silver`** — 1 AZN; fresh first-party sold **33%**; denominator target #1. An exact draw-bound **remaining-ticket count alone** is now sufficient to invert/narrow the cap when contemporaneous with 33%.
2. **`10072 S25 Ultra Black`** — 0.5 AZN; drawId-bound; fresh sold% unresolved.
3. `10065 Cosmic Orange` — 1 AZN; last complete first-party sold input **43%**.
4. `10064 Deep Blue` — 1 AZN; fresh sold% unresolved.
5. `1000-AZN gift coupon` — current price 0.5 AZN; drawId and fresh sold% unresolved.

### Silver execution buffer

Using ~3,150 AZN market reference and the standing 14% property-prize tax model, approximate break-even total-cap ceilings are:

| usable value | 33% sold | 35% sold | 38% sold | 43% sold |
|---:|---:|---:|---:|---:|
| 60% | 4,391 | 4,140 | 3,814 | 3,370 |
| 70% | 5,346 | 5,040 | 4,642 | 4,103 |
| 80% | 6,300 | 5,940 | 5,471 | 4,835 |
| 100% | 8,210 | 7,740 | 7,129 | 6,300 |

Property-prize working model: `V_economic = h*V - 0.14*(V-p)` until prize-specific tax classification is proven otherwise.

## Recent phase files

- `results/PHASE18BG_1001_SEVINC_PERCENT_TRANSITION_CAP_PROBE.md`
- `scripts/phase18bg_percent_transition_cap_solver.py`
- `results/PHASE18BK_1001_SEVINC_REGISTERED_TERMS_DENOMINATOR_ROUTE.md`
- `results/PHASE18BL_1001_SEVINC_CURRENT_RULES_AND_PUBLICATION_ROUTE.md`
- `results/PHASE18BM_1001_SEVINC_OFFICIAL_PRESALE_PUBLICATION_TRACE.md`
- `results/PHASE18BN_1001_SEVINC_FIRST_PARTY_DOCUMENT_NAMESPACE.md`
- `results/PHASE18BO_10X10_LIVE_TERMS_RECHECK_AND_1001_FAST_SETTLEMENT.md`
- `results/PHASE18BP_1001_SEVINC_OFFICIAL_DRAW_TERMS_AND_225_EXCEPTION.md`
- `results/PHASE18BQ_1001_SEVINC_PDF_INDEX_DATE_AND_LINKAGE_REASSESSMENT.md`
- `results/PHASE18BR_1001_SEVINC_TRENDYOL_ACCOUNT_SURFACE.md`
- `results/PHASE18BS_TRENDYOL_PUBLIC_ARTIFACT_FIELD_BOUNDARY.md`
- `results/PHASE18BT_MISLI_CURRENT_MOBILE_SURFACE_AND_DENOMINATOR_BOUNDARY.md`
- `results/PHASE18BU_MISLI_OFFICIAL_ANDROID_APK_RUNTIME_ENTRYPOINT.md`
- `results/PHASE18BV_MISLI_APK_1361_ACQUISITION_BOUNDARY.md`
- `results/PHASE18BW_ENDIR_REDIRECT_SURFACE_AND_ANDROID_ROUTE_BOUNDARY.md`
- `results/PHASE18BX_PUBLIC_TICKET_CHECKER_AND_LIVE_RETAIL_ROUTE.md`
- `results/PHASE18BY_PUBLIC_WINNING_CHANCE_NUMBERS_AND_CHECKER_INPUT_BOUNDARY.md`
- `results/phase18by_public_1001sevinc_identifiers.csv`
- `results/PHASE18BZ_1001_SEVINC_TICKET_VS_CHANCE_NUMBER_SEMANTICS.md`
- `results/PHASE18CA_1001_SEVINC_REPEAT_SELLOUT_AND_EXECUTION_RISK.md`
- `results/PHASE18CB_OLEY_OLEY_LOTTERY_DOUBLE_CHANCE_OVERLAY.md`
- `results/PHASE18CC_OLEY_OLEY_CAMPAIGN_TIMING_AND_LIVE_STATUS_BOUNDARY.md`
- `results/PHASE18CD_CURRENT_PARENT_INDEX_AND_DRAWID_INDEXABILITY_PROBE.md`
- `results/PHASE18CE_TELEGRAM_ARCHIVE_NUMERIC_DENOMINATOR_PROBE.md`
- `results/PHASE18CF_REMAINING_COUNT_SEMANTICS_AND_CAP_INVERSION.md`
- `scripts/phase18cf_remaining_plus_percent_cap_solver.py`
- `results/PHASE18CG_DIRECT_TELEGRAM_LIVE_CONTEXT_DENOMINATOR_PROBE.md`
- `results/PHASE18CH_INTERNAL_UX_ARTIFACT_ROUTE_AND_PUBLIC_CARD_BOUNDARY.md`

## NEXT ACTION — Phase 18 continuation

1. **Highest immediate priority remains `10066 Silver` denominator recovery.** Target genuinely new Misli/Azerlotereya authenticated/runtime/rendered or retail/POS evidence exposing the **absolute number of tickets remaining for the draw**. Because 33% sold is already draw-bound, a contemporaneous exact `R` can now be enough to infer/narrow `C`.
2. **New immediate subroute from Phase 18CH:** resolve the two public LinkedIn short links from the `1001 Sevinc` UX/UI designer post and inspect additional Behance/Dribbble/portfolio pages for Zulfiyya Shikhaliyeva and Hasan Aliyev. Prioritize actual `1001 Sevinc` mockups/screenshots with progress bars, remaining-ticket labels, percentage labels or count fields. If exact field labels are recovered, use them for narrow asset/API searches.
3. Prefer a **single rendered product-card, network/API response, screenshot/social preview, retail terminal or receipt** carrying both the 33% progress and absolute remaining count. `total`, `cap`, `soldCount`, stock or a numerator/denominator remain equally valid. Generic exact-ID search-index probing for `10066`/`10072` is bounded unless a new cached/detail/rendered artifact appears.
4. If exact `R` is recovered for `10066`, immediately run `scripts/phase18cf_remaining_plus_percent_cap_solver.py` under round/floor/ceil assumptions, compute compatible `C`, `M`, ROI, execution buffer and maximum positive-EV purchase size with **N free**. Do not combine stale percentage and remaining observations without modeling intervening sales.
5. Social-channel searching is now split into two bounded surfaces: Telemetr and direct official Telegram. Reuse either only when a newly indexed/current prize-specific post, numeric wording, or directly inspectable media artifact appears; do not repeat the Phase 18CE keyword set or the Phase 18CG recent plaintext window mechanically.
6. Obtain APK bytes for exact first-party build `misliaz_android.apk?v=1361` only through a genuinely new runtime/file reference/cache/CDN artifact. Once available, extract manifest/assets/DEX strings, API hosts/routes and `1001 Sevinc` schema fields (`remaining`, `total`, `soldCount`, `stock`, `issuance`, `maxTickets` or equivalent).
7. Do **not** repeat generic exact-string mirror/package searches for build 1361 or treat `endir.misli.az` as independent unless a materially new build number, direct-file URL, cache surface, package identifier, DNS/CDN target, response-header artifact, support artifact, or retrievable file reference appears.
8. **Oley Oley is bounded as historical unless renewed.** Reopen only on materially new current Misli Campaigns/account/support/terms evidence, a renewal/relaunch, or a denominator-bearing artifact. Do not treat June–July evidence as proof of current eligibility.
9. `Biletini Yoxla` remains bounded; reopen only with paired full ticket/serial + chance-number artifact, safe request schema, or network/API evidence. Do not submit guessed/public chance numbers.
10. Trendyol: revisit only on a materially new account screenshot, support/help artifact, app payload/network capture, or directly interpretable ticket-card surface.
11. Historical social/POS searching should prioritize **numeric** sold/remaining quantities, progress screenshots, receipt/terminal fields, or direct product-card captures; do not spend cycles on additional qualitative sold-out posts alone.
12. If sequential sold-% observations around known ticket additions become available, run the Phase 18BG solver; do not execute paid probes autonomously.
13. Treat `1001 Sevinc` denominator scope as **draw + prize category + draw period**, not global game-wide, unless an artifact explicitly proves otherwise.
14. Revisit `10→10` only on materially new evidence resolving the 31-Aug/31-Jul conflict and/or proving current Super-Keno bonus eligibility.
15. Keep `results/phase18_ev_modifier_ledger.csv` synchronized only when classifications actually change.
16. If any live zero-cost bonus is proven Super-Keno eligible, immediately design a variance-aware distinct-ticket conversion with **N free**, constrained only by bonus terms.
17. Do not reopen rejected draw-history prediction branches without materially new information.
