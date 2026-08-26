# Phase 18S — APL Fantasy bonus-type evidence checkpoint

Date: 2026-08-26

Status: **CURRENT ZERO-COST LEAD CONFIRMED RECURRING; SUPER KENO PRODUCT SCOPE STILL UNRESOLVED.**

## What was tested

This pass followed the Phase 18R next action: determine whether the 10/20/30 AZN APL Fantasy prizes are a bonus type that can be used in `Lotereya` / Super Keno, and obtain any public evidence on wagering, expiry, withdrawal or private-league size.

## Fresh/current evidence

Misli's current public Telegram surface now contains the **second-week APL Fantasy winner post**. It repeats the same mechanics as week 1:

- register at `aplfantasy.az`;
- create a 15-player team;
- join the Misli.az private league with code `188533-FJA0T`;
- winners are determined from the public APL Fantasy league results;
- weekly prizes remain 30 / 20 / 10 AZN `bonus`;
- winner must send the Misli.az member number to receive the bonus;
- no paid Misli wager or deposit is stated as an entry requirement.

Source snapshot:
- https://t.me/s/misliaz
- indexed current mirror: https://tlmtr.io/ar/channels/1555852363-misliaz

This materially strengthens the **repeatability** classification: the reward is not a one-off announcement; the same free-entry Misli bonus mechanism has now been observed in two consecutive APL Fantasy weeks.

## Bonus-type evidence from prior Misli fantasy campaigns

The same wording pattern — `Qalibsənsə, Misli.az üzv nömrəni bizə yaz və bonusla ürəyincə əylən!` — was used by Misli for the earlier DÇ-2026 Fantasy league, where top finishers received 50/40/30/20/10 AZN bonus amounts.

Source:
- https://t.me/s/misliaz?before=4837
- direct indexed post example: https://t.me/s/misliaz/4844

Interpretation: APL Fantasy very likely uses the same general **internal Misli account-bonus credit pattern** rather than a physical prize or external voucher. This is useful evidence about the credit mechanism, but it is **not enough to infer product scope**.

No public first-party text located in this pass states that these Fantasy bonuses may be used in `Lotereya`, nor does it state:

- one-wager vs multi-wager requirement;
- sports-only / cross-product restriction;
- expiry;
- withdrawal treatment of resulting winnings.

Therefore the project deliberately does **not** upgrade the opportunity to a Super-Keno modifier yet.

## Competition denominator

The public APL Fantasy platform is live, but the public landing page does not expose the Misli private-league team count in the crawlable surface.

AFFA publicly reported more than 10,000 platform registrations by 14 Aug 2026; later project evidence recorded >14,000 platform users. These are global platform counts, not the private Misli league denominator. Launch coverage also allows up to two teams per user. Hence neither platform registrations nor a naive 2x conversion is a valid denominator for the Misli weekly contest.

Sources:
- https://www.affa.az/index.php/news/apl-fantasy-platformasnda-qeydiyyatdan-kenlrin-say-10-000-i-tb/81283
- https://aplfantasy.az/

## Conditional Super Keno conversion value

Base exact after-tax 1x Super Keno expected return remains:

`e = 0.5918070335 cash per 1 AZN bonus stake`

If future direct evidence proves that an APL Fantasy bonus can be wagered once on 1x Super Keno and resulting winnings are withdrawable:

| bonus face value | conditional expected cash |
|---:|---:|
| 10 AZN | 5.918070335 AZN |
| 20 AZN | 11.836140670 AZN |
| 30 AZN | 17.754211005 AZN |

Because qualifying gambling spend is 0 AZN, the entry mechanic itself does not need to overcome the base-game 40.82%/68.97% subsidy thresholds. The remaining economic question is contest probability/time cost, not paid-stake EV.

## Decision

Classification remains:

`current_repeatable_free_entry_bonus_product_scope_unresolved`

But confidence in the **current + recurring + zero-paid-spend** portions is increased: two consecutive APL Fantasy weeks now show the same weekly bonus award structure.

The unresolved field is narrower than before: **bonus product scope / wagering / withdrawal**, plus private-league denominator for contest-efficiency estimation.

## Next action

1. Search only materially new first-party/app/account evidence for the credited bonus wallet/type, especially winner screenshots or terms showing where the 10/20/30 AZN appears.
2. Search exact winner-result artifacts and comments for screenshots of credited balances or messages from Misli support.
3. Attempt to recover the Misli private-league team count from APL Fantasy result/league pages or APIs if publicly exposed.
4. In parallel, continue fresh scans for other zero-cost/free-entry bonuses with **explicit** `Lotereya` eligibility; such a lead would outrank APL Fantasy immediately.
5. Do not infer Super Keno eligibility merely from the generic word `bonus` or from the fact that Misli also offers Lottery products.
