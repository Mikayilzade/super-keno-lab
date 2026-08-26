# Phase 18N — 10→10 welcome bonus: official contradiction audit

Date: 2026-08-26

Status: **EXECUTION-CRITICAL STATUS UNRESOLVED; CONDITIONAL +EV MECHANISM CONFIRMED**

## Why this was reopened

This is not a return to a rejected history-based branch. A fresh 2026-08-26 crawl of the official Azerlotereya offer page contains materially new/current-dated evidence that conflicts with the site's campaign classification.

## Official evidence observed 2026-08-26

Dedicated official offer page:
- https://www.azerlotereya.com/game/10oyna-10qazan
- https://www.azerlotereya.com/kampaniya/10oyna-10qazan

The live page body explicitly states:
- registration through **31 August**;
- new Azerlotereya.com users only;
- deposit at least 10 AZN;
- play at least 10 AZN;
- eligible sections explicitly include **Lotereya**, ePoz-Qazan and Digital Oyunlar;
- first 10,000 qualifying users;
- 10 AZN additional balance;
- additional balance can be played with **no turnover requirement**;
- unused deposited/additional balance withdrawal is subject to 30% commission with minimum 5 AZN;
- winnings withdrawal has no commission.

The same page's detailed condition #5 says the campaign is valid through **31 August 23:59** and condition #8 refers to bonus-crediting after **24 July**.

However:
- the page/search title labels it **"keçmiş kampaniya"** (past campaign);
- the embedded FAQ still says **14 April 10:00 through 31 July 23:59**;
- the public `Cari kampaniyalar` page does not currently expose it as an active campaign.

Therefore official first-party evidence is internally contradictory. The body/conditions look like a later extension to 31 August, while the classification/FAQ look stale or inconsistent. We cannot responsibly call it either definitely active or definitely inactive from public web evidence alone.

## Super Keno applicability

If the offer is operational, Super Keno fits the published product scope because it is in the `Lotereya` section. No inference from generic platform access is needed here; the offer terms explicitly name `Lotereya`.

## Exact conditional economics

Using the project's exact 1x after-tax Super Keno cash return:

`e = 0.5918070335`

If 10 AZN personal funds are played once and the resulting 10 AZN bonus is also played once:

`expected cash = e * (10 + 10) = 11.83614067 AZN`

Relative to 10 AZN personal outlay:

- expected personal-capital ROI = **1.183614067**;
- expected profit = **+1.83614067 AZN**;
- expected profit rate = **+18.3614%**.

This remains the strongest known external-EV mechanism in the project if operational eligibility is confirmed.

## Alternative: withdraw bonus unused

The published 30% withdrawal commission with minimum 5 AZN means direct withdrawal of the 10 AZN bonus is inferior to one 1x Super Keno wager under the model. The bonus-play path converts 10 AZN bonus into ~5.9181 AZN expected withdrawable winnings, while direct unused-balance withdrawal can lose at least 5 AZN to the minimum commission.

## Execution gate

Do **not** stake based solely on this page conflict. Promote to `current_positive_ev` only if at least one of the following is observed:

1. a new account UI shows live 10→10 progress/eligibility;
2. official *2080/support confirms on or after 2026-08-26 that new users still qualify through 31 August;
3. a fresh official social post/current-campaign listing explicitly states the extension is active.

If any gate passes, this should immediately become the project's first current actionable +EV candidate, subject to the user's actual new-account eligibility.

## RadioArena side result

The Misli RadioArena post is still live in current indexed Telegram material: weekdays at 20:00 on 106.3 FM, chance to win a 10 AZN promo code. Public first-party terms still do not resolve eligible product, wagering, expiry, withdrawal or number of codes. Because the post is tagged `#Futbol`, it remains secondary to the 10→10 lead until cross-product eligibility is proven.

## Next action

1. Reconcile the ledger so Oley Oley is historical, not current.
2. Treat 10→10 as `official_status_conflict_conditional_positive`, not confidently inactive.
3. Continue fresh active-overlay scans, but prioritize any first-party evidence resolving 10→10 operational status.
4. If operational status is confirmed, design a variance-aware Super Keno execution for the 20 AZN total wager path with **N free** rather than forcing round ticket counts.
