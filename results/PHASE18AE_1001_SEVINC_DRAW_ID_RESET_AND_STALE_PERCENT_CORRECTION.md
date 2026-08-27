# Phase 18AE — 1001 Sevinc draw-ID reset and stale sold-% correction

Date: 2026-08-27

Status: **MEANINGFUL DATA-INTEGRITY CORRECTION; ABSOLUTE DENOMINATOR STILL UNRESOLVED.**

## Why this checkpoint matters

Phase 18AC/AD identified `1001 Sevinc` as a finite-inventory route and noted a search-indexed iPhone 17 Pro card at roughly 33% sold. Fresh 27-Aug-2026 evidence shows that this percentage must **not** be carried into the current live draw set.

Official Azerlotereya social results now report that the previous cycle containing:
- 1000 AZN gift coupons,
- Xiaomi scooter,
- microwave,
- Samsung Galaxy TAB S10+,
- iPhone 17 Pro 256 GB

has already drawn winners.

Meanwhile the official `1001 Sevinc` game page now exposes a **new 16.09.2026 draw set**. Therefore sold percentages are draw-instance-specific state and must be keyed by `drawId`, not merely by prize name.

## Current draw-ID inventory recovered from first-party links

The official current game page exposes 11 clickable draw cards for 16.09.2026. Following those links yields the current draw IDs and ticket prices:

| display order | drawId | ticket price AZN | draw date |
|---:|---:|---:|---|
| 1 | 10065 | 1.0 | 2026-09-16 |
| 2 | 10064 | 1.0 | 2026-09-16 |
| 3 | 10066 | 1.0 | 2026-09-16 |
| 4 | 10072 | 0.5 | 2026-09-16 |
| 5 | 10073 | 0.5 | 2026-09-16 |
| 6 | 10067 | 0.5 | 2026-09-16 |
| 7 | 10071 | 0.5 | 2026-09-16 |
| 8 | 10068 | 0.5 | 2026-09-16 |
| 9 | 10069 | 0.5 | 2026-09-16 |
| 10 | 10070 | 0.5 | 2026-09-16 |
| 11 | 10074 | 0.5 | 2026-09-16 |

Current first-party page:
- https://www.azerlotereya.com/lotereya/1001-sevinc

Current draw URLs follow:
- `https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=<ID>`

## Fresh prize-name evidence

The official Azerlotereya Telegram feed currently advertises at least the following `1001 Sevinc` prizes in the live/next cycle:
- 1000 AZN gift coupon — 1 AZN ticket;
- iPhone 17 Pro 256 GB Deep Blue — 1 AZN;
- Samsung Galaxy TAB S10+ — 0.5 AZN;
- Samsung microwave — 0.5 AZN;
- Xiaomi scooter — 0.5 AZN.

However the public HTML returned by the draw-detail routes is a client shell and does not expose a reliable prize-name-to-drawId mapping, sold percentage, cap or remaining count. Therefore the table above intentionally does **not** guess which drawId corresponds to which prize.

## Data rule added to the research methodology

For `1001 Sevinc`, a sold percentage / remaining count / cap is valid only when all of these are tied together:

`(drawId, prize, ticket price, draw date, observed timestamp)`.

Never transfer a sold percentage across:
- a new draw date;
- a new drawId;
- a repeated prize name;
- an archived search snippet.

This prevents a false +EV signal caused by combining a stale low sold percentage with a fresh prize draw.

## Consequence for the old ~33% iPhone lead

The historical/search-indexed ~33% iPhone sold figure is now treated as **expired observational evidence**, not a current denominator input. The iPhone prize from that cycle has already been reported as won, while the game page has rolled to 16.09.2026 draw IDs.

Thus no current live ROI can be computed from that 33% value.

## What is still missing

For at least one of current draw IDs 10064..10074 we still need one of:
1. exact cap `C`;
2. exact sold count `M`;
3. exact remaining count `R` together with cap;
4. a client/API payload containing any of the above;
5. a first-party screenshot/card where the absolute remaining count is visible.

Once available:

`ROI = V_net / (p * M)`

with `M = C - R` when cap and remaining are known.

## Decision

The finite-pool route remains promising but is **not promoted to +EV**. The useful result of this batch is the exact current draw-ID inventory plus a stale-data safeguard that prevents false positive ROI calculations.

Next action: target the new 16.09.2026 draw IDs directly for client-visible cap / remaining-count payloads; do not reuse the old iPhone 33% observation.
