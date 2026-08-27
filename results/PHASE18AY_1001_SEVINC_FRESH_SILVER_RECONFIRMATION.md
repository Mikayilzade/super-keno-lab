# Phase 18AY — fresh Silver reconfirmation and execution-priority update

Date: 2026-08-28

Status: **MEANINGFUL FRESHNESS UPDATE; NO POSITIVE-EV CLAIM.**

## Fresh first-party search-cache evidence

Azerlotereya's current `1001 Sevinc` draw surface was crawled today and the search cache now reproduces a current-cycle record containing:

- `iPhone 17 Pro 256 GB Deep Blue` — **1 AZN** — draw date **16.09.2026**;
- `iPhone 17 Pro 256 GB Silver` — **1 AZN** — draw date **16.09.2026** — **Satıldı: 33%**.

Source surface:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

The parent first-party page crawled today still exposes exactly 11 current draw cards for 16.09.2026: three at 1 AZN and eight at 0.5 AZN.

This is a materially new freshness signal because Phase 18AX had demoted iPad Air 13 M2 / Galaxy S25 Ultra when their complete current-cycle records could not be reproduced. Silver now *is* freshly reproducible as `(prize, price, draw date, sold%, timestamp)`.

## Execution priority

The existing priority rule remains:

1. bound + fresh;
2. fresh but unbound;
3. unbound and not freshly reproducible.

Therefore:

- **#1 remains drawId=10065 Cosmic Orange**, because it is fully bound to exact drawId and had the last complete first-party execution record;
- **#2 becomes iPhone 17 Pro 256 GB Silver at 33% sold**, because it is freshly reproduced today but exact drawId binding is not yet proven;
- Deep Blue is also freshly reproduced for prize/price/date, but today's snippet does not expose a sold percentage;
- iPad Air 13 M2 / Galaxy S25 Ultra remain lower until a new complete current-cycle record appears.

Do **not** infer Silver's drawId merely from snippet text ordering. The three current 1-AZN draw IDs are known to be `10065, 10064, 10066`, but a safe binding requires an explicit card-order/artifact relation in the same current surface.

## Silver break-even cap tolerance

Using the standing 14% property-prize tax model and a conservative current iPhone 17 Pro 256 GB market benchmark of about **3,150 AZN**, at **33% sold** the maximum total ticket cap compatible with break-even is approximately:

| usable/resale value fraction | net economic prize value | break-even cap ceiling |
|---:|---:|---:|
| 60% | 1,449.14 AZN | **4,391 tickets** |
| 70% | 1,764.14 AZN | **5,346 tickets** |
| 80% | 2,079.14 AZN | **6,300 tickets** |
| 100% | 2,709.14 AZN | **8,210 tickets** |

These are diagnostic ceilings only. A real execution threshold must be lower because sold% can increase before purchase and because resale/settlement friction exists.

Silver therefore has materially more cap tolerance than Cosmic Orange at 43% sold, but Cosmic remains execution target #1 until Silver is bound to an exact drawId or an absolute denominator is recovered directly.

## Absolute denominator search

No current first-party/public result in this run exposed:

- predetermined ticket cap;
- absolute sold count;
- absolute remaining count.

The exact `drawId=10065` detail page still renders as a JS/client shell through the web surface.

A direct public HTML/JS-bundle download attempt from the runtime was also unavailable because the container has no external DNS/network access. This is an environment limitation, not evidence that the endpoint does not exist. Do not repeat this exact container-download path in the next run unless network/tool capability materially changes.

## Decision

No +EV claim is made.

Fresh candidate hierarchy now:

1. **Cosmic Orange / drawId 10065** — bound, last execution sold input 43%;
2. **Silver / 1 AZN / 16.09.2026 / 33% sold** — fresh but unbound, economically stronger cap tolerance;
3. Deep Blue — fresh price/date, sold% absent in today's snippet;
4. iPad/S25 — potentially attractive historically but not freshly execution-grade.

## Next action

1. Seek an explicit current artifact that binds Silver to one of `10064/10066` without relying on inferred snippet order.
2. Continue searching absolute `cap / remaining / sold-count` for bound `drawId=10065` through a genuinely new rendered/account artifact.
3. If Silver becomes bound first, promote it above Cosmic because its 33% sell-through gives substantially more cap tolerance at similar prize value.
4. Re-promote iPad/S25 immediately if a fresh complete current-cycle record appears.
5. Do not claim positive EV until an absolute denominator is recovered.
