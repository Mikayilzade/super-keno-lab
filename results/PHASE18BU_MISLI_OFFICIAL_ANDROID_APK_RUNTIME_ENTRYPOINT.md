# Phase 18BU — Misli official Android APK runtime entrypoint

Date: 2026-08-28

## Status

**Not yet success** — no absolute denominator (`remaining`, `total`, issuance, stock, maxTickets) for `10066 Silver` / `10072 S25` recovered in this batch.

## Materially new evidence

The current first-party Misli mobile download page at `https://yukle.misli.az/` exposes a direct Android download action. Following that first-party Android link resolves to:

`https://yukle.misli.az/misliaz_android.apk?v=1361`

The response is an Android package (`application/vnd.android.package-archive`). This is materially different from Phase 18BT's public screenshots/search-index surface: it identifies the operator's current downloadable Android binary and a concrete current query-version/build token (`v=1361`).

First-party download page also states that the Misli mobile application includes `Lotereya`, and the already-established App Store history independently places `1001 Sevinc` inside the app from December 2025 onward.

## Why this matters

The strongest remaining denominator route is now concrete rather than generic:

1. acquire the exact first-party APK corresponding to `v=1361`;
2. unpack `AndroidManifest.xml`, resources/assets and DEX/native strings;
3. enumerate hostnames, API base URLs, GraphQL/REST route fragments and feature/module identifiers around `lotereya`, `1001`, `sevinc`;
4. search schemas/field names for `remaining`, `remainingTickets`, `total`, `totalTickets`, `sold`, `soldCount`, `stock`, `inventory`, `issuance`, `maxTickets`, plus Azerbaijani equivalents (`qalan`, `bilet`, `say`);
5. bind any product endpoint to current draw IDs `10066` and `10072` before using a denominator.

This avoids reopening the rejected generic Misli web/image branch.

## Tooling boundary encountered

The web renderer successfully resolved the APK URL and MIME type, but the current binary-download path could not persist the APK in the analysis environment: the web fetch rejects APK MIME as unsupported for textual rendering, while the separate container downloader could not retrieve the host. Therefore no APK decompilation claim is made in this phase.

This is a tooling/access boundary, not evidence that the APK lacks the required fields.

## Decision

- Promote the exact first-party APK (`misliaz_android.apk?v=1361`) to the highest-priority runtime artifact.
- Do **not** return to generic Misli web/image permutations.
- Next batch should first look for a retrievable mirror/cache/hash/package metadata for this exact APK/build, or another route that allows the binary to be acquired; once available, run static endpoint/schema extraction immediately.
- `N` remains a free integer optimization variable.
- No paid probe is authorized or required.

## Candidate impact

No classification or ROI change yet. `10066 Silver` remains denominator target #1 and `10072 S25 Ultra Black` target #2.
