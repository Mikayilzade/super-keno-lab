# Phase 18CE — official Telegram archive numeric denominator probe

Date: 2026-08-29

## Objective

Continue the highest-priority `1001 Sevinc` denominator recovery route without reopening bounded generic exact-ID/APK branches. Target fresh or archived social/POS-style evidence containing numeric `remaining`, `total`, `soldCount`, stock, or an explicit numerator/denominator for current high-priority draws, especially `10066 Silver` and `10072 S25 Ultra Black`.

Portfolio size **N remains a free integer optimization variable**.

## New surface recovered

A third-party archive/analytics index for the official `Azerlotereya` Telegram channel was recovered at Telemetr (`@azerlotereya`, channel id `1466500879`). Search indexing exposes historical official-channel post text, including `1001 Sevinc` posts. This is materially different from the already-bounded generic web exact-ID route because it provides a searchable archive of operator social posts that may otherwise have weak web discoverability.

Examples visible in the indexed archive include official posts around the first `1001 Sevinc` draws (e.g. five iPhone winners; a later draw advertising 20 winners). These validate that the archive is actually ingesting `1001 Sevinc` operator content rather than merely channel metadata.

Source surface:
- https://telemetr.io/en/channels/1466500879-azerlotereya/posts

Supporting first-party current parent page remains:
- https://www.azerlotereya.com/lotereya/1001-sevinc

## Targeted probe

Queries/searches were run against the archive/index for:

- `Silver`
- `S25`
- `33%`
- `qalıb`
- `satılıb`
- variants of `1001 Sevinc` + ticket remaining/sold wording

No indexed text hit was recovered that exposes an absolute ticket count, cap, stock, numerator/denominator, or a denominator-bearing current artifact for `10066` or `10072`.

Opening the Telemetr archive page directly from the current web runtime failed, and targeted in-page `find` calls returned no matches for the denominator keywords above. Therefore the archive is useful as a **new discovery surface**, but it does not yet yield executable denominator evidence in this batch.

## Important boundary

Do **not** infer denominator from qualitative operator copy such as `20 winners`, `hundreds of gifts`, or from chance-number magnitudes. These describe prize counts / marketing inventory / namespace identifiers, not tickets issued in a prize-category pool.

The official current page still states that players may buy as many tickets as desired and that category draws can be brought forward when tickets sell earlier than scheduled; this continues to support a finite category-specific pool but does not reveal its size.

## Classification

`telegram_archive_denominator_route = NEW_SURFACE_NO_NUMERIC_HIT_YET`

This is not success and does not change the executable EV classification.

## Next action

1. Reuse this newly recovered official-channel archive only when search indexing exposes a post image/text associated with current prize names or numeric progress wording; do not spend repeated cycles on the same empty keyword set.
2. Highest priority remains a rendered product card, network/API payload, account screenshot, POS terminal/receipt, or social screenshot exposing **absolute** `remaining`, `total`, `soldCount`, stock, or a progress numerator/denominator for `10066 Silver` / `10072 S25`.
3. If a social-image artifact appears, bind it to `(drawId, prize, ticket price, draw date, sold%, source surface, crawl timestamp)` before using it in EV calculations.
4. APK acquisition remains bounded unless a genuinely new file/cache/CDN/runtime artifact appears.
5. Preserve free integer **N**.
