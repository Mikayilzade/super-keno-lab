# Phase 18V — APL Fantasy binary/API surface checkpoint

Date: 2026-08-26

Status: **NO SUPER KENO EDGE VERIFIED; NEW API-RECOVERY PATH PREPARED, EXECUTION NOT YET OBSERVED.**

## Why this batch

Phase 18U established that ordinary indexed web search cannot expose the Misli private-league denominator for APL Fantasy. `aplfantasy.az` is rendered as an app shell to crawlers, while Misli explicitly says private-league results are publicly visible through the official APL Fantasy product.

The next materially different surface is therefore the public client binary/network configuration rather than another search-engine query.

## Fresh public app-distribution evidence

- Android package: `az.affa.fantasy`.
- Developer: Fantaking / Fantaking Interactive.
- APKPure currently exposes APL Fantasy Android build `1.0.2`, dated 2026-08-12, as an XAPK (~44 MB on the current download page).
- App Store tracking shows iOS build `1.0.4`, updated 2026-08-24.
- Google Play / app metadata identifies the same official APL Fantasy product and Fantaking as developer.

Sources:
- https://apkpure.net/br/apl-fantasy/az.affa.fantasy/download
- https://play.google.com/store/apps/details?id=az.affa.fantasy
- https://foxdata.com/en/app-marketing-analytics/6759035296/as/US/apl-fantasy/

## Repository work added

Added:
- `experiments/phase18v_apl_binary_endpoint_audit.sh`
- `.github/workflows/phase18v_apl_binary_endpoint_audit.yml`

The script is intentionally evidence-minimal:
1. downloads the public XAPK into a temporary runner directory;
2. extracts only printable network-looking strings from APK/dex/native/config assets;
3. retains candidate absolute URLs plus strings mentioning API/league/ranking/standing/private/Fantaking/APL;
4. writes only the extracted text report to `results/`;
5. explicitly fails if any `.apk`, `.xapk`, or `.aab` is found inside the repository tree.

The proprietary application binary is **not** intended to be stored in this repository.

## Execution state

A workflow file and a follow-up trigger commit were created, but the GitHub connector's workflow/status surfaces did not show a new run or status for the trigger commit during this batch. Therefore no endpoint is claimed yet.

This is treated as an execution/surface issue, not evidence that the app contains no discoverable backend URL.

## Fresh overlay scan in parallel

A fresh first-party/public scan did **not** surface a new zero-cost offer with explicit `Lotereya` / Super Keno eligibility. Current Misli indexed material continues to show lottery product posts and historical campaign material, while APL Fantasy remains the strongest live zero-paid-spend bonus lead whose bonus product scope is unresolved.

No classification in the EV-modifier ledger changes in this batch.

## Decision

Do **not** repeat ordinary search variants for the Misli APL league code.

The next useful actions are:
1. check whether `results/phase18v_apl_binary_endpoint_audit.txt` appears from CI;
2. if endpoint/domain strings appear, query only public unauthenticated league/ranking routes and recover total rows for `188533-FJA0T` without accessing personal data;
3. if CI remains unavailable, use another public app-artifact/static-analysis surface rather than repeating indexed search;
4. continue fresh scans for zero-cost offers with direct `Lotereya` eligibility;
5. if a bonus is proven Super-Keno eligible, immediately move to N-free variance-aware conversion.
