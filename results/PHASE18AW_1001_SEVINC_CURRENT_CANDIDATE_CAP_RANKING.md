# Phase 18AW — 1001 Sevinc current-candidate break-even cap ranking

Date: 2026-08-27

Status: **NO EXECUTABLE +EV YET; TARGET PRIORITY CHANGED.**

## Purpose

The previous denominator search focused too heavily on `drawId=10065` / iPhone 17 Pro 256 GB Cosmic Orange. This checkpoint follows the Phase-18 NEXT ACTION and compares the currently recovered 16.09.2026 prize observations on the quantity that matters when the absolute denominator is still missing: **how large the total predetermined ticket cap could be before the draw stops being break-even**.

No ticket purchase is justified by this report. Absolute `cap / remaining / sold-count` remains the missing execution variable.

## Current parent-draw structure

Fresh Azerlotereya parent page snapshot on 2026-08-27 still renders **11 draws dated 16.09.2026**: **3 × 1 AZN** and **8 × 0.5 AZN**.

Current ordered draw links recovered from the first-party page remain:

- 1 AZN: `10065, 10064, 10066`
- 0.5 AZN: `10072, 10073, 10067, 10071, 10068, 10069, 10070, 10074`

Source: https://www.azerlotereya.com/lotereya/1001-sevinc

`drawId=10065` is already bound to **iPhone 17 Pro 256 GB Cosmic Orange / 1 AZN / 16.09.2026**. The exact IDs for the other prize names below are not guessed unless independently proven.

## Evidence discipline

Only a record bound to the current 16.09.2026 cycle may be used for execution. Older Telegram/social posts are retained only as historical context. In particular, a fresh crawl of the official Telegram feed exposed a previous-cycle set (`1000 AZN gift coupon`, `iPhone 17 Pro Deep Blue`, Galaxy Tab S10+, microwave, scooter) followed by a completed-draw post; those items must **not** be blindly carried into the current cycle.

The full current 11-prize name mapping is still not recoverable from the crawler because the live cards are client-rendered. Therefore this report ranks only candidates with already recovered current-cycle sell-through observations and does not fabricate the four/five missing names.

## Valuation model

For a non-cash prize with market benchmark `V`, ticket price `p`, usable/resale haircut `h`, and current sold fraction `s`, use the conservative property-prize tax model already adopted in Phase 18:

`V_economic = h*V - 0.14*(V-p)`

If the predetermined total ticket cap is `C`, current sold tickets are approximately `s*C`; break-even at the observed sell-through requires:

`C <= V_economic / (p*s)`

This is a **cap ceiling**, not a claim that the actual cap is below it.

## Current candidate ranking

Market benchmarks used for ranking are deliberately ordinary Azerbaijan cash/retail references rather than maximum advertised prices:

- iPhone 17 Pro 256 GB: **3,149.99 AZN** current cash listing (Mobifon); Kontakt current retail reference is 3,289.99 AZN, so 3,149.99 is the more conservative ranking input.
- Galaxy S25 Ultra 256 GB: **2,399.99 AZN** current discounted retail reference (Phonex).
- PS5 Slim 1 TB: **1,399 AZN** current Baku listing (Orange Store/Wolt); a lower 1,189.99 AZN market listing exists, so denominator execution must later use a sale/liquidation benchmark rather than the optimistic number.
- iPad Air 13 M2 128 GB Wi-Fi+4G: **1,649 AZN** current iSpace listing.

Current-cycle sell-through observations already recovered by prior checkpoints:

- Cosmic Orange: **43%** (freshest bound Azerlotereya observation), 1 AZN, `drawId=10065`.
- iPhone Silver: **33%**, 1 AZN; exact current ID unresolved.
- iPhone Deep Blue: **35%**, 1 AZN; exact current ID unresolved.
- PS5 Slim: **55%**, 0.5 AZN working current-card price class; exact current ID unresolved.
- Galaxy S25 Ultra Black: **42%**, 0.5 AZN working current-card price class; exact current ID unresolved.
- iPad Air 13 M2: **26%**, 0.5 AZN working current-card price class; exact current ID unresolved.

Because the exact prize→drawId binding is not yet proven for the 0.5-AZN names, these are **ranking observations, not execution records**.

| candidate | p | sold | V benchmark | cap ceiling @60% usable | @70% | @80% | @100% |
|---|---:|---:|---:|---:|---:|---:|---:|
| iPad Air 13 M2 | 0.5 | 26% | 1,649 | **5,835** | 7,104 | 8,372 | 10,909 |
| Galaxy S25 Ultra | 0.5 | 42% | 2,399.99 | **5,257** | 6,400 | 7,543 | 9,829 |
| iPhone 17 Pro Silver | 1 | 33% | 3,149.99 | **4,391** | 5,346 | 6,300 | 8,209 |
| iPhone 17 Pro Deep Blue | 1 | 35% | 3,149.99 | **4,140** | 5,040 | 5,940 | 7,740 |
| iPhone 17 Pro Cosmic Orange | 1 | 43% | 3,149.99 | **3,370** | 4,103 | 4,835 | 6,300 |
| PS5 Slim 1 TB | 0.5 | 55% | 1,399 | **2,340** | 2,849 | 3,358 | 4,375 |

## Main finding

**Cosmic Orange is no longer the best denominator-search target.**

On the conservative 60%-usable-value scenario, the current ranking is:

1. **iPad Air 13 M2 — cap tolerance ~5.84k**
2. **Galaxy S25 Ultra — ~5.26k**
3. iPhone Silver — ~4.39k
4. iPhone Deep Blue — ~4.14k
5. Cosmic Orange — ~3.37k
6. PS5 Slim — ~2.34k

The two best recovered candidates are both 0.5-AZN cards. This is economically intuitive: low ticket price offsets much of the lower prize value, while lower sell-through further increases tolerated total cap.

The iPad ranking is sensitive to exact model/storage/connectivity and current price. It must be bound to the actual current draw before execution. The same applies to Galaxy S25 Ultra storage/color.

## Incomplete full-table reconstruction

The automation goal was to rebuild all 11 current names. The first-party page exposes all 11 prices/dates and draw IDs through link order but does not render names in crawler HTML. Fresh text/social surfaces did **not** provide a trustworthy complete current 11-name list. Carrying previous-cycle names forward would create a stale-data error, so the missing names are intentionally left unresolved.

This is still a meaningful completion of the ranking objective because the best recovered target changed materially.

## Decision / next action

1. **New finite-pool target #1: iPad Air 13 M2 current 0.5-AZN card.** First bind its exact current `drawId`, exact model/storage/connectivity and fresh sold%.
2. **Target #2: Galaxy S25 Ultra current 0.5-AZN card.** Bind exact ID/model and fresh sold%.
3. Search for absolute `remaining / cap / sold-count` on these two targets through a materially different rendered/account/client surface; do not reopen exhausted generic `10065 + API/remaining` searches.
4. If either target yields an absolute denominator, immediately compute buffered live ROI under 60/70/80/100% usable value and 14% property-prize tax.
5. Re-snapshot sell-through before any execution calculation. The cap ceiling must use the freshest bound observation.
6. Continue trying to recover the complete 11-prize mapping only from a fresh current-cycle first-party/rendered artifact; do not populate unknown names from previous cycles.

## Sources used for current market benchmarks

- https://www.mobifon.az/ru/apple/telefonlar-1667687197/p/iphone-17-pro-256-gb-cosmic-orange-1764670571
- https://kontakt.az/iphone-17-pro-256-gb-cosmic-orange
- https://phonex.az/az/products/samsung-galaxy-s25-ultra-256gb-1699
- https://wolt.com/az/aze/baku/venue/orange-store/itemid-1170398d6964b18b2b9509aa
- https://ispace.az/en/category/ipad-air
