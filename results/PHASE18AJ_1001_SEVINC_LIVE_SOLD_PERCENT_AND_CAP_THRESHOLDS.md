# Phase 18AJ — 1001 Sevinc live sold% recovered; cap thresholds derived

Date: 2026-08-27

Status: **MATERIALLY NEW LIVE EVIDENCE; ABSOLUTE DENOMINATOR STILL UNRESOLVED.**

## New first-party observation

On 2026-08-27 the official Azerlotereya `1001 Sevinc / Tirajlar` surface was newly indexed with a current prize and live sell-through:

- prize: **iPhone 17 Pro 256 GB Cosmic Orange**;
- ticket price: **1 AZN**;
- draw date: **16.09.2026**;
- displayed sell-through: **Satıldı: 43%**.

Source:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

This is the first current-cycle sold-percentage observation that can be safely attached to the 16.09.2026 cycle. Previous Deep Blue / Galaxy TAB / coupon observations were from a completed prior cycle and remain invalid for the current draw IDs.

The exact `drawId` of the Cosmic Orange prize is **not yet proven**. The three current 1-AZN draw IDs remain `10065, 10064, 10066`; direct per-draw URLs still render only the client shell to the crawler. Therefore do not bind Cosmic Orange to one of those IDs yet.

## Current retail value benchmark

A current Azerbaijan official Apple partner (iSpace Azerbaijan) lists:

- iPhone 17 Pro 256 GB Cosmic Orange: **3,289 AZN**.

Source:
- https://ispace.az/en/product/iphone-17-pro-256-gb-cosmic-orange-mg8h4zd-a

This is a retail benchmark, **not** guaranteed realizable net value. Taxes, resale haircut, transaction costs and prize-specific valuation must be accounted for before any actionable EV claim.

## What 43% sold already tells us

Let:
- `C` = predetermined ticket cap for this prize;
- `s = 0.43` = displayed sold fraction;
- `p = 1 AZN` = ticket price;
- `M = s*C` = approximate sold tickets at the snapshot;
- `V_net` = conservative net realizable value of the prize.

If the draw were held at the current sell-through, expected return per ticket is approximately:

`ROI = V_net / (p * M) = V_net / (0.43 * C)`.

Therefore break-even requires:

`C < V_net / 0.43`.

Using the 3,289-AZN retail benchmark only as a scale reference:

| assumed net realizable value | V_net | break-even cap at 43% sold |
|---:|---:|---:|
| 60% of retail | 1,973.40 AZN | **< 4,589 tickets** |
| 70% of retail | 2,302.30 AZN | **< 5,354 tickets** |
| 80% of retail | 2,631.20 AZN | **< 6,119 tickets** |
| 100% retail (non-conservative ceiling) | 3,289.00 AZN | **< 7,649 tickets** |

These are **cap thresholds, not EV estimates**. We still need the actual predetermined cap `C` or absolute remaining/sold count.

Because the UI displays an integer percentage, the underlying sold fraction may be rounded. A proper final calculation should use absolute sold/remaining counts if available rather than treating 43% as exact.

## Search result

Targeted searches on 2026-08-27 for the exact current prize plus `qalan bilet / qalıb / Satıldı` did not expose an absolute remaining count or cap. Direct URLs for `drawId=10065/10064/10066` still return only the client shell to the crawler.

## Decision

The `1001 Sevinc` finite-pool route is strengthened, not closed. We now have a live current-cycle state variable (`43% sold`) and a current prize-value benchmark, so any future recovery of `C`, `remaining`, or an absolute sold count immediately yields a live ROI calculation.

Do **not** buy based on the 43% figure alone. Without the absolute cap, positive EV is not established.

## Next action

1. Recover the predetermined cap or absolute remaining count for the **current Cosmic Orange** prize from a newly indexed/rendered first-party card, social artifact, client payload or account-facing surface.
2. Bind the prize to its exact current drawId among `10065/10064/10066` before maintaining a time series.
3. If another current prize receives a sold% before its absolute cap is known, record the same cap-threshold table rather than inferring EV.
4. Keep scanning genuinely new Super-Keno modifiers with explicit `Lotereya` eligibility; do not reopen rejected history-prediction routes.
