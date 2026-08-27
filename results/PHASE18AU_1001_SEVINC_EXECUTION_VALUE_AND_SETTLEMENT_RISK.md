# Phase 18AU — 1001 Sevinc execution-value and settlement-risk correction

Date: 2026-08-27

Status: **NO POSITIVE-EV EXECUTION GATE YET; MODEL MADE MORE CONSERVATIVE.**

## Why this batch matters

The current finite-pool target remains `drawId=10065` (iPhone 17 Pro 256 GB Cosmic Orange, 1 AZN, draw date 16.09.2026, freshest bound first-party sold-through 43%). Absolute cap / remaining / sold count is still missing.

This batch adds two execution facts that materially affect valuation and risk:

1. Azerlotereya's official 1001 Sevinc explainer states that a physical prize **cannot be exchanged for cash**. Therefore retail price is not execution-equivalent value; an actual liquidation/resale benchmark is required.
2. Azerlotereya officially disclosed a 07.03.2026 technical incident in which some purchased tickets were not included in several 1001 Sevinc draws. The operator scheduled separate additional draws for the omitted tickets. This shows a real operational/settlement-risk mode. The remedial draw appears intended to restore eligibility, but timing/processing risk is non-zero and should not be ignored when sizing a marginal +EV opportunity.

Official sources:
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23
- https://www.azerlotereya.com/xeberler/1001-sevinc-asya-lotereyasi-ila-bagli-rasmi-malumat-1896

## Current liquidation-value evidence for Cosmic Orange

Fresh/local market surfaces show materially lower prices than the 3,289 AZN major-retailer benchmark previously used as the full-value ceiling:

- local new-item listing: ~2,799 AZN;
- another new-item listing: ~3,100 AZN;
- major retailer cash price: 3,289.99 AZN.

Representative sources:
- https://qiymetleri.az/apple-iphone-17-pro-cosmic-orange-256gb-12gb-159425.html
- https://telsat.az/en/telefonlar/mobil-telefonlar/Apple-iPhone-17-Pro-256-GB-8253/
- https://kontakt.az/iphone-17-pro-256-gb-cosmic-orange

These are ask/retail observations, not guaranteed immediate buyout prices. For execution, use the lower observable market value unless a real resale quote is obtained.

## Revised cap ceilings at 43% sold

Using the existing conservative property-prize tax model:

`V_net = V_market - 0.14 * (V_market - ticket_price)`

and break-even condition:

`C_max = V_net / (ticket_price * sold_fraction)`

with `ticket_price=1` and `sold_fraction=0.43`:

| market-value assumption | after-tax economic value | break-even total cap ceiling |
|---:|---:|---:|
| 2,799 AZN | ~2,407.28 AZN | **~5,598 tickets** |
| 3,100 AZN | ~2,666.14 AZN | **~6,200 tickets** |
| 3,289 AZN | ~2,828.68 AZN | **~6,578 tickets** |

Interpretation: the previously quoted ~6,578 ceiling is a retail-price upper bound, not the preferred execution threshold. A more defensible current market-value threshold is roughly **5,600–6,200 total tickets** before adding any safety margin for further sales and execution friction.

## Execution rule added

Even if cap/remaining is recovered and raw EV exceeds 1.0, do **not** promote the draw unless it remains above 1.0 after all of:

1. freshest bound sold-through / absolute denominator;
2. 14% property-prize tax default;
3. liquidation-value benchmark rather than headline retail;
4. additional sell-through buffer between observation and purchase;
5. explicit operational-risk buffer for delayed/remedial draw handling.

The March 2026 omitted-ticket incident does not by itself prove expected monetary loss because extra draws were scheduled, so no arbitrary fixed percentage haircut is imposed yet. Instead, promotion now requires a positive margin large enough that modest settlement/timing friction cannot erase it.

## Decision

- `drawId=10065` remains the strongest reproducible finite-pool target.
- **No execution yet**: absolute `cap / remaining / sold count` remains unknown.
- Preferred current cap gate is no longer the 3,289-retail ceiling; use roughly **<5.6k–6.2k tickets** as the more realistic pre-buffer range, then tighten further for sell-through and settlement risk.

## Next action

1. Continue materially different client/rendered/account-surface attempts for exact cap/remaining on `drawId=10065`.
2. Re-snapshot the first-party sold percentage; if it rises above 43%, recompute all ceilings immediately.
3. Seek an actual quick-sale/buyout quote or stronger recent local resale evidence to replace ask-price assumptions.
4. If denominator appears, compute buffered ROI and only promote if comfortably >1 after all execution deductions.
