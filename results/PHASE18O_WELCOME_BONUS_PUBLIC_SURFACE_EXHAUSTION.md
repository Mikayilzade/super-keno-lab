# Phase 18O — 10→10 public-surface exhaustion / operational-status gate

Date: 2026-08-26

Status: **PUBLIC FIRST-PARTY WEB EVIDENCE REMAINS INTERNALLY CONTRADICTORY; DO NOT EXECUTE WITHOUT OPERATIONAL CONFIRMATION.**

## Goal

Resolve whether the `10 oyna, 10 qazan` 10-AZN welcome bonus is actually operational on 2026-08-26, without treating stale page text as live eligibility.

## Fresh first-party surfaces checked

### Dedicated campaign page

`https://www.azerlotereya.com/kampaniya/10oyna-10qazan`

Fresh crawl still exposes:
- explicit `31 avqust` registration/end date;
- first 10,000 qualifying new users;
- minimum 10 AZN deposit and 10 AZN play;
- `Lotereya`, `ePoz-Qazan`, and Digital Oyunlar explicitly eligible;
- condition #5: valid through 31 Aug 23:59;
- condition #8: bonus-crediting language from 24 July onward;
- no turnover requirement for the additional 10 AZN;
- no withdrawal commission on winnings;
- a registration CTA.

At face value this is operational-looking content.

### Current-campaign index

`https://www.azerlotereya.com/kampaniyalar`

Fresh crawl on the same date says:

`Cari kampaniya mövcud deyil`

and exposes no active campaign card.

### Campaign FAQ

`https://www.azerlotereya.com/faq/10oyna-10qazan`

Fresh crawl still says campaign dates are **14 April 10:00 through 31 July 23:59**, twice in the FAQ. The FAQ itself says campaign participation/progress should be checked through the `*2080` contact centre.

### Official Telegram history

Official `@Azerlotereya` Telegram contains a launch-era post advertising `10 oyna, 10 qazan` and instructing new users to register, load 10 AZN, play it, and receive another 10 AZN. This confirms the mechanism was genuinely promoted by the operator, but no fresh indexed 2026-08-26 social post was found that resolves the July-vs-August extension/status conflict.

## Interpretation

The public first-party web estate now presents three mutually inconsistent signals simultaneously:

1. **Dedicated page body:** operational-looking, 31-Aug expiry, Lotereya eligible.
2. **Current campaign index:** no current campaign.
3. **FAQ:** expired 31-Jul.

This cannot be resolved responsibly by further repeating ordinary public-page search. The dedicated page may be an extended campaign whose metadata/FAQ/index were not synchronized, or it may be stale body content left on a historical page. Both explanations fit the public evidence.

Therefore the correct executable classification remains:

`official_status_conflict_conditional_positive`

and the operational gate is now explicit:

**Do not stake for this promotion unless at least one operational signal confirms eligibility:**
- account UI shows 10→10 progress/eligibility;
- current `*2080` support confirms the campaign is active for a new account on/after 2026-08-26;
- a newly dated official post/current-campaign card explicitly confirms the extension.

## Conditional economics unchanged

If operational and eligible:
- 10 AZN personal paid play at 1x Super Keno expected after-tax cash: `5.918070335` AZN;
- 10 AZN bonus played once at 1x expected after-tax cash: `5.918070335` AZN;
- total expected withdrawable winnings: `11.83614067` AZN;
- personal outlay: `10 AZN`;
- expected profit: `+1.83614067 AZN`;
- expected personal-capital ROI: **1.183614067 (+18.3614%)**.

Withdrawing the unused 10-AZN bonus directly is inferior under published terms because unused deposited/additional balance withdrawal carries 30% commission with a 5-AZN minimum; a 10-AZN withdrawal would net only 5 AZN, versus 5.918070335 AZN expected cash from one 1x Super Keno wager.

## Decision

Public-web investigation of 10→10 is **exhausted as a useful next-action loop** until a materially new operational signal appears. Keep the candidate in the ledger, but do not spend more routine research cycles re-crawling the same three contradictory pages.

Next research should move to other current first-party Lottery-eligible overlays (RadioArena/promo-code mechanics/new campaigns), while passively rechecking 10→10 only when a new dated source or operational signal appears.
