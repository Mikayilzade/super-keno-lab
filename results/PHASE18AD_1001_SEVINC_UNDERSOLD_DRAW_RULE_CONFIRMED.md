# Phase 18AD — 1001 Sevinc under-sold draw rule confirmed

Date: 2026-08-27

Status: **MEANINGFUL MECHANISM CONFIRMED; +EV NOT YET PROVEN.**

## New first-party evidence

The official Azerlotereya 1001 Sevinc explainer states that tickets may be purchased until the predeclared draw date, and that sales stop either:

1. one day before the announced draw date, **or**
2. earlier when ticket sales reach the predetermined quantity.

The same explainer states that each item has its own predetermined draw date and winners are selected in the live lototron draw.

Official game rules additionally state that if tickets sell out early and more than seven business days remain, the draw may be brought forward after advance notice.

Sources checked 2026-08-27:
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23
- https://www.azerlotereya.com/lotereya/1001-sevinc

## Consequence

This removes the main uncertainty from Phase 18AC about unsold-ticket treatment.

The published mechanism implies that a draw is **not conditional on full sell-out**: if the predetermined cap is not reached, sales still close before the scheduled date and the draw proceeds on that date. Full sell-out is only an alternative early-stop condition and can move the draw earlier.

Therefore under-subscription is a real operator-side state and can increase per-ticket EV relative to a fully sold inventory, assuming only sold/issued chance numbers participate in the lototron draw.

The official explainer also says every purchased ticket has its own chance number and that the site shows how many tickets remain for a draw. This is strong evidence that the relevant denominator is a finite issued-ticket pool rather than an abstract unlimited probability space.

## EV model

For a single-prize draw with ticket price `p`, actual valid sold/issued tickets `M`, and conservative net realizable prize value `V_net`:

`EV per ticket = V_net / M`

`ROI on ticket cost = V_net / (p * M)`

Break-even sold-count threshold:

`M_break_even = V_net / p`

If live sold percentage `s` and predetermined cap `C` are both known, then approximately:

`M = s * C`

and the live ROI becomes:

`ROI = V_net / (p * s * C)`.

## What remains unresolved

1. Exact predetermined ticket cap `C` for each active 16.09.2026 draw.
2. Exact current sold/remaining count (search-indexed public pages expose percentages but not the absolute count).
3. Conservative `V_net` after tax, resale discount, liquidity/friction and any transfer restrictions.
4. Direct confirmation that only sold/issued chance numbers are loaded into the physical draw; the published wording strongly points this way, but exact implementation details should be confirmed before declaring +EV.

## Decision

The finite-pool branch is **strengthened, not yet promoted**. Under-sold draws are now confirmed as an intended operating state, so recovering the cap/remaining-ticket number has high information value.

Next action: target client-visible `qalan bilet` / remaining-ticket values, page/API payloads, cached draw cards, or first-party screenshots for current draw IDs. Once `C` or an absolute remaining count is recovered, compute conservative ROI bounds immediately.
