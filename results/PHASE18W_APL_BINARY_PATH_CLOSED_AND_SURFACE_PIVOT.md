# Phase 18W — APL binary path closure and surface pivot

Date: 2026-08-26

Status: **NO SUPER KENO EDGE VERIFIED; CI/BINARY PATH CLOSED AS A TECHNICAL SURFACE, NOT A NEGATIVE DATA RESULT.**

## Why this batch

Phase 18V prepared a workflow to inspect the public APL Fantasy Android package for backend/API strings without committing proprietary binaries. The previous batch had not observed any workflow execution.

This batch explicitly re-triggered the workflow and checked workflow runs by the exact trigger commit SHA.

## CI execution result

A new trigger commit was created for `.github/workflows/phase18v_apl_binary_endpoint_audit.yml`.

Exact trigger commit:
- `9835b04b508b85c02114546bbe4fb63989dcfb22`

The GitHub workflow-run query for that exact SHA returned **zero runs**.

The expected report still does not exist:
- `results/phase18v_apl_binary_endpoint_audit.txt` -> not found.

Decision: **do not spend more research cycles waiting for this workflow.** This is a CI/execution-surface failure, not evidence that no backend endpoint exists.

## Public app-artifact evidence refreshed

Fresh public distribution/search surfaces confirm:
- official Android package: `az.affa.fantasy`;
- developer: Fantaking / Fantaking Interactive;
- Google Play continues to expose the official APL Fantasy application;
- APKPure exposes direct XAPK download routes for the same package and published package signature/hash metadata;
- iOS/App Store tracking shows version `1.0.4`, updated **2026-08-24**;
- public app metadata exposes developer support/privacy surfaces but no indexed standings API endpoint.

Useful public sources:
- https://play.google.com/store/apps/details?id=az.affa.fantasy
- https://apkpure.net/ru/apl-fantasy/az.affa.fantasy/download/0.0.1
- https://foxdata.com/en/app-marketing-analytics/6759035296/as/US/apl-fantasy/

The APKPure download redirect exposes a public XAPK endpoint, but the current research runtime could not safely retrieve/decompress the binary. No binary was stored in the repository.

## APL denominator evidence remains unchanged

Fresh public APL/Misli material still confirms:
- Misli private league code `188533-FJA0T`;
- weekly prizes 30 / 20 / 10 AZN bonus;
- no paid Misli gambling spend is stated as qualification;
- winners are determined from public APL Fantasy private-league results;
- global APL registrations exceeded 14,000 by the first round, but this is **not** the Misli private-league denominator.

No exact Misli private-league row count was recovered in this batch.

## Fresh EV-overlay scan

No new current zero-cost offer with explicit `Lotereya` / Super Keno eligibility was found in the fresh official/public scan.

The Azerlotereya 10->10 page still contains terms through 31 August and explicit `Lotereya` eligibility, but the same official surface remains internally contradictory (`keçmiş kampaniya` title / stale FAQ dates). This is not materially new operational evidence, so its classification is unchanged and it is not promoted.

## Decision

Close the Phase-18V GitHub-Actions binary extraction path.

Do not interpret this as closing the APL lead itself. The APL lead remains live because the qualification cost is zero and the weekly bonus repeats.

## Next action

1. Pivot to **public app metadata / cached screenshots / winner-result artifacts / client-visible league pages**, not another CI retry.
2. Search for screenshots or result cards that expose ranking page counts, total rows, league-member counts, or bonus-wallet labels.
3. Use public developer/privacy/help surfaces only if they expose a concrete API/base-domain clue; do not guess endpoints.
4. Continue fresh scans for zero-cost offers with direct `Lotereya` eligibility.
5. If any live free bonus is proven Super-Keno eligible, immediately build an N-free variance-aware conversion portfolio.
