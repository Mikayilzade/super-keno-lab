# Phase 18AR — 1001 Sevinc registration + client-surface denominator audit

Date: 2026-08-27

Status: **NO ABSOLUTE DENOMINATOR YET; PUBLIC REGISTRATION ROUTE EXHAUSTED; CURRENT LIVE CARD REMAINS COSMIC ORANGE 43%.**

## Objective

Continue from Phase 18AQ without repeating generic search. Highest-priority target remains the current `iPhone 17 Pro 256 GB Cosmic Orange — 1 AZN — 16.09.2026` draw. The missing execution variable is the predetermined ticket cap / absolute remaining / sold count.

## Fresh current observation

A fresh first-party Azerlotereya crawl on 2026-08-27 still returns:

- prize: `iPhone 17 Pro 256 GB Cosmic Orange`;
- ticket price: `1 AZN`;
- draw date: `16.09.2026`;
- sold: **43%**.

Source: https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

No absolute remaining/cap is exposed in the crawler-visible parent-card text.

## Registration-document route

The official parent page identifies `1001 Sevinc` as registered with the Azerbaijan State Tax Service:

- registration number: **316**;
- registration date: **12.05.2025**.

A targeted search for the registration record/rules using the exact number/date/name, including State Tax Service domains, did **not** recover a public indexed registration PDF or rule document containing per-prize ticket quantities.

Decision: do not repeat ordinary indexed search for `316 / 12.05.2025` unless a new registry surface appears. The registration reference is useful provenance but currently not an accessible denominator source.

## Important current-page consistency warning

The same official parent page currently renders eleven live cards for `16.09.2026` with **3 x 1 AZN + 8 x 0.5 AZN**, while its static `Necə oynanılır?` explainer still says ticket categories are `1, 2, 5 AZN`.

Interpretation: static explanatory copy can lag the live card configuration. Therefore **price/category data used for execution must come from a bound current draw/card observation, not generic game instructions or old press releases.** This is the same anti-stale rule already applied to sold percentages.

## Client-surface attempt

A direct container/network fetch was attempted to inspect public JS/client bundles for endpoint names/fields. The execution environment had no DNS/network resolution, so this route could not be completed from the container in this run. This is a tooling/network blocker, not evidence that no public client endpoint exists.

The web crawler still sees the draw listing as a rendered/indexed surface but does not expose client-side `remaining/cap` payloads.

## Current economics unchanged

Using current 43% sold, 1 AZN price, retail benchmark 3,289 AZN and conservative 14% property-prize tax model, break-even total-cap ceilings remain approximately:

- 60% usable value: **3,519 tickets**;
- 70% usable value: **4,284**;
- 80% usable value: **5,049**;
- 100% usable value: **6,578**.

Without actual cap/remaining, this is **not** an executable positive-EV claim.

## Decision / next action

1. Keep Cosmic Orange as highest-priority finite-pool target while the bound live card remains reproducible.
2. Do not use registration-number search or static game-price copy as execution data unless a new first-party registry document appears.
3. On a materially different surface, seek absolute remaining/cap or exact prize→drawId mapping for the three current 1-AZN IDs `10065/10064/10066`.
4. Re-snapshot Cosmic Orange sold% on later runs; if it changes, recompute cap ceilings immediately.
5. If the card becomes stale/disappears before denominator recovery, expire the observation instead of carrying 43% forward.
6. Super Keno modifier branch remains parallel and unchanged; no new explicit `Lotereya`-eligible zero-cost bonus was verified in this batch.
