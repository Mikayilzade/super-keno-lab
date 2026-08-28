# Phase 18BK — 1001 Sevinc registered-terms denominator route

Date: 2026-08-28

## Outcome

Not yet success: no live absolute `cap / remaining / sold-count` for drawId `10066` or `10072` was recovered in this batch.

However, a materially new denominator route was established from the governing lottery rules rather than from the exhausted public client/API surfaces.

## New evidence

The Central Bank page reproducing the binding `Lotereyaların təşkili və keçirilməsi Qaydası` states in section 2.2.5 that lottery conditions must include the ticket price, ticket sample, **the number and numbers of lottery tickets** (except lotteries whose prize fund depends on sold-ticket proceeds), and acquisition rules.

The same rules state in section 2.4 that the organizer must provide the lottery conditions to a participant upon request, and in section 2.5 that the conditions must be announced through mass media after registration and before ticket sales begin.

The rules also require ticket-level fields including ticket number/series, draw date, price, registration information and draw number (3.1), and require the organizer to keep records of sold ticket counts/numbers/series (4.2.4). Electronic ticket numbers/series must be sequential and must not duplicate printed-ticket numbering (5.8).

The current first-party `1001 Sevinc` page identifies the product as registered with the State Tax Service under:

- registration number: **316**
- registration date: **12.05.2025**

This registration key provides a concrete anchor for locating or requesting the registered conditions instead of trying to infer the denominator from public sold-% cards.

## Why this matters

If the registered conditions for registration `316 / 12.05.2025` use a fixed ticket pool for the relevant prize-category/draw and retain an explicit ticket quantity or range, that document can expose `C` directly or constrain it strongly enough to make the finite-pool EV calculation executable.

This route is materially different from the already-rejected generic API/detail-page/registry-crawl paths: the target is now the **registered lottery conditions/document package** required by regulation, keyed by a known registration number.

Caution: the rules contain an exception when the prize fund is determined from sold-ticket proceeds. `1001 Sevinc` appears operationally to use predetermined non-cash prizes, but the registered conditions must be read before assuming that every current draw has a single fixed `C` in the exact form required for ROI.

## Research performed

Fresh searches were run for the current 16.09.2026 cards, retail/POS artifacts, public rules/conditions, and the exact registration key. No indexed copy of the registration-316 conditions was found in this batch.

## Decision

Open a new primary denominator route:

`registration 316 -> registered conditions -> ticket quantity/range -> bind to current draw/category -> validate against live sold% / remaining surface`

Do not treat historical chance numbers as ordinals and do not reopen the exhausted public detail-page crawl.

## NEXT ACTION

1. Search official/regulatory archives specifically for the registered `1001 Sevinc` conditions keyed by **316 / 12.05.2025**, including amendments/new editions.
2. If the document is found, extract ticket quantity/range semantics and determine whether quantities apply globally, by prize category, by draw, or by issuance batch.
3. Bind any quantity to `10066 Silver` / `10072 S25` only after matching draw/category/date semantics.
4. If exact `C` becomes available, combine with current sold fraction/remaining and immediately compute buffered ROI under 60/70/80/100% usable value and the standing tax model.
5. Preserve `N` as a free integer optimization variable.

## Sources

- Central Bank of Azerbaijan, `Lotereyaların təşkili və keçirilməsi Qaydası`, especially sections 2.2.5, 2.4, 2.5, 3.1, 4.2.4, 5.8.
- Azerlotereya first-party `1001 Sevinc` page: registration `316 / 12.05.2025`.
