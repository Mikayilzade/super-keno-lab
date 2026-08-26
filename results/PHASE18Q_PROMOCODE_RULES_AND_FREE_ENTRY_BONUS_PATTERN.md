# Phase 18Q — generic promo-code rules exhaustion + free-entry bonus pattern

Date: 2026-08-26

Status: **NO CURRENT EXECUTABLE +EV SUPER KENO MODIFIER CONFIRMED.**

## Objective

Follow the Phase 18P next action without re-crawling the same RadioArena post: search first-party Misli generic promo-code/help/bonus surfaces for product-scope behavior, then scan fresh/current public material for newly visible Lottery-eligible or zero-cost bonus mechanics.

## RadioArena / generic promo-code rules

The official Misli Telegram post continues to advertise a 10 AZN RadioArena promo code: weekdays at 20:00 on 106.3 FM, tagged `#Futbol #RadioArena #Promokod`.

Public first-party search still does **not** expose:
- eligible product(s);
- whether `Lotereya` / Super Keno can consume the code;
- wagering requirement;
- expiry;
- withdrawal rules for resulting winnings;
- number of codes awarded.

The Misli public help surface `/komek-webview/bonus` and current campaign page `/kampaniyalar` resolve publicly as JS/iframe shells and do not expose generic bonus/promo terms in the indexed text. First-party site searches likewise did not return a generic promo-code policy.

Decision: keep RadioArena as `current_terms_unresolved_sports_context`. The `#Futbol` tag is weak evidence for a sports context, not proof of sports-only use. Do not count the 10 AZN as Super-Keno capital without product-scope confirmation.

Conditional value remains: if a code were fully usable once on 1x Super Keno and winnings were withdrawable, expected after-tax cash value would be **5.918070335 AZN per 10-AZN code** with zero personal stake for the bonus wager itself.

## Free-entry bonus pattern discovered

Official Misli Telegram history documents a DÇ-2026 Fantasy league where participation required only:
1. register at the public FIFA Fantasy site;
2. create a 15-player team;
3. join the `Misli_az` league.

At each round, the top five received Misli bonuses:
- 1st: 50 AZN;
- 2nd: 40 AZN;
- 3rd: 30 AZN;
- 4th: 20 AZN;
- 5th: 10 AZN.

The post instructs winners to send their Misli member number and says they can enjoy the bonus, but it does not expose product-scope/wager/withdrawal terms.

This World-Cup campaign is **historical / finished**, not a current opportunity on 2026-08-26. It is retained because it proves a materially different modifier class: a Misli bonus can be awarded from a **zero-paid-spend external competition**, so future fantasy/quiz/social competitions should be screened even when they are not ticket-linked.

If a future free-entry 10/20/30/40/50 AZN bonus is explicitly usable once on 1x Super Keno, the corresponding expected after-tax cash values before any bonus-specific restrictions are approximately:
- 10 -> 5.9181 AZN;
- 20 -> 11.8361 AZN;
- 30 -> 17.7542 AZN;
- 40 -> 23.6723 AZN;
- 50 -> 29.5904 AZN.

Because personal qualifying spend can be zero, such a mechanism would not need to overcome the 40.82% paid-stake subsidy threshold; its value is limited instead by the probability/cost of winning the external contest and the bonus restrictions.

## Fresh Lottery scan

The current Misli public feed still visibly carries Super Keno / lottery content, but no newly dated public post found in this batch offered a free ticket, rebate, extra draw or directly Lottery-qualified current bonus. The current campaign page is a client-rendered shell in the public text fetch, so absence of a rendered campaign card is not used as proof that no account-targeted campaign exists.

## Decision

- No strategy promoted to executable +EV.
- RadioArena generic public rule discovery is now considered **surface-exhausted** unless a new first-party terms page/post or account UI appears; do not spend repeated cycles on the same searches.
- Add `free-entry external competition -> Misli bonus` as a new modifier class to the ledger, historical for now.

## Next action

1. Scan newly dated Misli Telegram/social/news for **free-entry competitions, quizzes, fantasy rounds, promo giveaways, free balance or free tickets**, not only stake-linked campaigns.
2. For each, separate qualification cost from bonus face value and obtain exact bonus product scope before assigning Super Keno EV.
3. Search Azerlotereya/Misli partner channels for a current explicit `Lotereya` qualifier or free lottery ticket mechanism.
4. Revisit RadioArena only on materially new terms/product evidence.
5. Revisit 10→10 only on materially new operational evidence.
6. If a live zero-cost or +EV modifier becomes confirmed, design a distinct-ticket Super Keno execution with N free and wager capped only by modifier terms.

## Public sources used

- Official Misli Telegram RadioArena promo-code post: https://t.me/s/misliaz?q=%23Promokod
- Official Misli Telegram DÇ-2026 Fantasy winner/bonus posts: https://t.me/s/misliaz/4844 and neighboring official posts
- Misli public bonus help shell: https://www.misli.az/komek-webview/bonus
- Misli public campaign shell: https://www.misli.az/kampaniyalar
