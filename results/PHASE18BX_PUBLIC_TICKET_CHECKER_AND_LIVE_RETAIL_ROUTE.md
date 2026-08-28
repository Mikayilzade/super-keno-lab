# Phase 18BX — public ticket-checker + live retail route

Snapshot: 2026-08-29

## Goal

Follow `STATUS.md` NEXT ACTION without re-running bounded APK mirror/hostname work: look for a genuinely new authenticated/runtime/rendered or retail/POS surface that could expose an absolute denominator for current `1001 Sevinc` draws, especially `10066 Silver` / `10072 S25`.

## New evidence

### 1. Public first-party ticket-check surface is live

Fresh search/opening exposes a first-party `Biletini Yoxla` surface at:

- `https://www.azerlotereya.com/biletini-yoxla`
- product-routed alias `https://www.azerlotereya.com/keno/biletini-yoxla`

The rendered public surface accepts a `Bilet nömrəsi` and exposes a `Yoxla` action. This is materially different from the previously bounded `1001 Sevinc` client-shell product detail pages because it is an unauthenticated validator surface intended to resolve ticket identifiers.

No indexed response payload/schema or known-valid `1001 Sevinc` ticket number was recovered in this batch, so it is **not yet** usable to infer issuance count or draw denominator.

### 2. Current official 1001 Sevinc page reconfirms the finite-draw mechanism

Fresh first-party page snapshot shows 11 current draws dated `16.09.2026` and explicitly states:

- each ticket has its own chance number;
- each prize/category draw is conducted separately;
- if tickets sell out sufficiently early, the draw may be moved forward;
- post-draw winning ticket numbers are published on official web/social surfaces.

The fresh article/explainer also explicitly states that the user can see **how many tickets remain for the draw** in the `1001 Sevinc` section of Azerlotereya.com / Misli.az.

This preserves the existing denominator model: scope is `draw + prize category + draw period`, not a game-global sequence.

### 3. Live official retail distribution is broader than the account surfaces

A fresh official Azerlotereya Telegram result states that `1001 Sevinc` tickets can currently be purchased from:

- Azerlotereya sales points;
- Misli sales points;
- Azerlotereya.com;
- Misli.az;
- Trendyol.az.

This is useful because retail/POS is now a confirmed **current** distribution route for the same game, not merely an old launch promise. It keeps POS receipts / seller-screen / terminal-card artifacts as a distinct denominator path even while web detail pages remain client-shell only.

## What did not resolve

- No absolute `total`, `remaining`, `soldCount`, `issuance`, `maxTickets`, or equivalent was exposed in the public ticket-checker snapshot.
- No public valid current ticket number tied to `10066` or `10072` was recovered, so no zero-cost checker probe was possible.
- Generic APK/mirror/`endir`/`yukle` routes were **not** reopened.
- No paid probe was executed.

## Research implication

The denominator search now has one additional live surface worth targeted work:

`public ticket identifier -> Biletini Yoxla resolver -> response schema / draw metadata`

This should be pursued only with a legitimate already-public ticket number or a directly discoverable runtime/API schema. Do not brute-force ticket identifiers.

In parallel, current physical Azerlotereya/Misli POS receipts or seller-terminal screenshots for `10066 Silver` / `10072 S25` remain high-value because the retail channel is confirmed live today.

## Status

**Not yet success.** No executable positive-EV modifier or absolute finite-pool denominator recovered.

`N` remains a free integer optimization variable.

## Next action

1. Inspect genuinely new runtime/static evidence around the first-party `Biletini Yoxla` validator to identify its request/response schema or API route, without brute-force ticket-number probing.
2. Search for a legitimate public winning-ticket artifact that can be safely passed through the checker and observe whether the response leaks draw/category/sequence metadata.
3. Continue current retail/POS artifact search for `10066 Silver` / `10072 S25`; if `cap` or `remaining` appears, compute buffered ROI immediately under 60/70/80/100% usable-value assumptions.
4. Keep exact APK build `v=1361` acquisition as priority only when a genuinely new file-reference/cache/CDN/build artifact appears.
