# Phase 18BW — `endir.misli.az` redirect surface and Android-route boundary

Date: 2026-08-29

## Objective

Follow the current `STATUS.md` / `NEXT ACTION` without repeating the already-bounded generic APK mirror/package-search branch. Investigate a materially new Android download hostname (`endir.misli.az`) that appeared in fresh indexing and determine whether it is an independent retrievable APK/CDN surface that can provide bytes or a new file/build reference for the current Misli Android app.

## Evidence

1. A fresh third-party index published in 2026 explicitly describes `endir.misli.az` as the Android APK download location for Misli.
2. Historical Azerbaijan sports-media coverage from 17 Jan 2023 also published `https://endir.misli.az/` as both the iOS and Android mobile-app download entrypoint. This establishes that the hostname is not a newly invented SEO-only string.
3. Direct current web retrieval of `https://endir.misli.az/` redirects to the first-party download page at `https://yukle.misli.az/`.
4. The redirected page's Android download control still resolves to the exact current binary URL already established in Phase 18BU/BV: `https://yukle.misli.az/misliaz_android.apk?v=1361`.
5. Browser-backed retrieval of that APK still reaches the real file and fails only because the runtime rejects the Android package MIME (`application/vnd.android.package-archive`).
6. Direct container retrieval remains DNS-blocked for `yukle.misli.az`, so no APK bytes were persisted in this run.
7. The current official iOS App Store surface shows Misli.az version 3.1.7 (23 Jul) and developer Azerlotereya ASC; this provides a fresh cross-platform release-state reference but does not disclose Android package identity or denominator fields.

## Result

`endir.misli.az` is **not an independent current APK/CDN surface**. It is a legacy/alias entrypoint that currently redirects to `yukle.misli.az`. Therefore it does not bypass the Phase 18BV acquisition boundary and should not be treated as a separate route unless future evidence shows a direct file path, cache object, alternate DNS/CDN target, or changed redirect behavior.

This is useful negative evidence because it closes a newly surfaced hostname without reopening generic mirror searching.

## Denominator impact

No absolute `remaining`, `total`, `soldCount`, `stock`, `issuance`, or `maxTickets` field for `10066 Silver` or `10072 S25` was recovered.

No ROI classification changes.

`N` remains a free integer optimization variable.

## Branch policy update

- Mark `endir.misli.az` as an alias/redirect-only route under the present state.
- Do not spend another batch probing generic `endir` vs `yukle` hostname variants unless a materially new direct-file URL, DNS target, package ID, build number, response header/cache key, or archived asset appears.
- Continue prioritizing: (a) a persistable APK/file reference for build 1361; or (b) genuinely new authenticated/rendered/POS evidence exposing the finite denominator for `10066` / `10072`.

## Next action

Search for a materially new **file-reference/cache/CDN artifact** tied to the exact first-party APK, or a new package/build identifier that enables deterministic acquisition. In parallel, prefer new account/rendered/POS evidence for the current `1001 Sevinc` draws over generic public searching.
