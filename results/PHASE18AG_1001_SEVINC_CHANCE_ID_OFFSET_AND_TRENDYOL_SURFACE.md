# Phase 18AG — 1001 Sevinc chance-ID offset correction + Trendyol client-surface pivot

Date: 2026-08-27

Status: **NO CURRENT ABSOLUTE DENOMINATOR YET; IMPORTANT FALSE-SHORTCUT CLOSED; NEW CLIENT SURFACE IDENTIFIED.**

## Why this batch

Phase 18AF established that current draw IDs `10064..10074` are real and current for the 16.09.2026 cycle, but Azerlotereya public HTML/search surfaces do not server-render `sold / remaining / cap`.

This batch deliberately avoided repeating those same draw-ID searches. It targeted two materially different evidence classes:

1. historical official/result artifacts that could reveal how chance numbers are encoded;
2. alternate official distribution clients that may expose ticket metadata differently.

## Historical chance-ID correction

The first `1001 Sevinc` draw sold out early and was moved forward. Five winners received iPhone 16 Pro Max 256 GB prizes at 1 AZN per ticket.

Published winner-artifact chance numbers were:

- `103932`
- `107185`
- `112723`
- `116364`
- `121104`

The same historical record states that this first draw sold out early.

### Critical inference

**Do not use `max(winning chance ID)` as a proxy for sold tickets.**

All five published winning IDs are already in the `100k+` range. This is strong evidence that the visible chance number contains an offset / namespace / allocated number block rather than being a simple counter starting at 1 for that draw.

Therefore:

- `121104` does **not** prove 121,104 tickets were sold;
- a highest observed chance number does not provide an absolute denominator unless the operator's mapping from chance ID to ticket ordinal is independently proven;
- future video/result-card analysis must not promote a draw to +EV merely because a winning number appears numerically small/large.

This closes a potentially dangerous false-denominator shortcut.

## New materially different surface — Trendyol

Azerlotereya and Trendyol officially began cooperation in December 2025, with Trendyol acting as an official e-commerce sub-distributor for `1001 Sevinc`.

Published integration details say Trendyol users can:

- buy `1001 Sevinc` tickets;
- see ticket status;
- see draw date;
- see lottery result information in their Trendyol account.

This is materially different from the crawler-visible Azerlotereya draw-detail shell and is therefore a valid next denominator-recovery target.

It does **not** yet prove Trendyol exposes total cap / sold / remaining. But it creates a second client implementation that may carry richer draw metadata or cached rendered artifacts.

## Current 16.09.2026 state

The operator page still exposes 11 current cards for 16.09.2026:

- 1 AZN draw IDs: `10065, 10064, 10066`;
- 0.5 AZN draw IDs: `10072, 10073, 10067, 10071, 10068, 10069, 10070, 10074`.

Current absolute `cap / sold / remaining` is still unresolved.

## Method rule added

A valid finite-pool ROI observation must now bind:

`(drawId, prize, ticket price, draw date, observation timestamp, absolute sold or cap-minus-remaining source)`

and **must not derive sold count from raw chance IDs** unless a separately verified ID-to-ordinal mapping exists.

## Decision

No +EV classification yet.

The finite-pool route remains open because official rules explicitly allow scheduled draws to proceed under-sold and the UI is documented to show how many tickets remain. The blocker is data exposure, not mechanism validity.

## Next action

1. Target Trendyol's `1001 Sevinc` rendered/account/public-cache surfaces for current draw metadata rather than repeating Azerlotereya draw-ID search.
2. Search newly indexed current social screenshots/cards specifically for a visible `qalan bilet` / remaining-ticket number tied to one of the current prizes/draw IDs.
3. Treat historical chance IDs only as identifiers, not counts.
4. If any absolute denominator is recovered, bind it to prize/price/date/timestamp and calculate conservative ROI immediately.
5. Continue the primary Super Keno external-EV scan in parallel; do not reopen history-based draw prediction.

## Public sources checked

- Azerlotereya `1001 Sevinc` current page and official rules/blog.
- Historical first-draw result image showing the five chance IDs.
- Historical official/social archive confirming the first draw sold out early.
- Trendyol/Azerlotereya cooperation announcement describing Trendyol as official sub-distributor and its ticket-status/result integration.
