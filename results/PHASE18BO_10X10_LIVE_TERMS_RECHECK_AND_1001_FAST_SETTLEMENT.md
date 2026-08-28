# Phase 18BO — 10→10 live terms recheck + 1001 Sevinc fast settlement

Date: 2026-08-28

## Outcome

**Not yet executable success.** A materially fresh first-party crawl recovered the live `10 oyna, 10 qazan` campaign page and a second `/game/10oyna-10qazan` surface crawled three days earlier. Both expose current-looking campaign terms, but the page remains internally inconsistent on the campaign end date.

## New evidence

First-party campaign terms currently state:

- new Azerlotereya.com users who deposit at least 10 AZN, wager at least 10 AZN, and verify their account receive 10 AZN additional balance;
- limited to the first 10,000 qualifying users and one use per user;
- the main terms state validity through **31 August 23:59**;
- users arriving through an existing Misli.az account are excluded;
- qualifying deposited balance may be wagered in `Lotereya`, `ePoz-Qazan`, and `Digital Oyunlar`;
- **1001 Sevinc tickets are counted immediately without waiting for their draw** for campaign qualification;
- from 24 July, qualifying bonuses are loaded on Monday or Thursday;
- additional balance has **no turnover requirement** and may be played as desired;
- unused deposited/additional balance withdrawn directly to a card incurs a 30% fee (minimum 5 AZN), while winnings withdrawn to card have no commission.

The same page's FAQ still says the campaign is valid from 14 April 10:00 through **31 July 23:59**. This conflicts with the main terms and prevents treating the offer as presently executable without account/support confirmation.

## Why this matters

The `1001 Sevinc` fast-settlement clause is operationally useful and was not previously captured as a strong execution detail: a qualifying user does not need to wait until the scheduled item-lottery draw for those ticket purchases to count toward the 10 AZN campaign wager requirement. This can reduce campaign timing risk materially near the deadline.

However, this does **not** resolve the two remaining blockers for a live Super-Keno-positive-EV call:

1. current campaign validity/availability must be confirmed despite the 31-August vs 31-July contradiction;
2. the credited 10 AZN additional balance must be confirmed operationally usable on Super Keno under the current account UI/product scope, not inferred solely from generic `istədiyi kimi oynaya bilər` wording.

No autonomous spend or account registration was performed.

## Classification

`10→10`: keep `official_status_conflict_conditional_positive`.

The mathematical conditional ROI remains attractive if the offer is operational and the bonus is Super-Keno eligible, but the classification is **not promoted to executable** from this batch alone.

## Source snapshot

- https://www.azerlotereya.com/kampaniya/10oyna-10qazan — crawled 2026-08-28
- https://www.azerlotereya.com/game/10oyna-10qazan — crawled within the preceding three days

## NEXT ACTION

Return to the highest-priority `1001 Sevinc` denominator route: first-party metadata/CMS/search-index/archive artifacts that can reveal the registered-conditions document for registration **316 / 12.05.2025**. Revisit `10→10` only if a materially new account/support/current UI artifact resolves the date conflict or proves Super-Keno bonus eligibility.

`N` remains a free integer optimization variable.
