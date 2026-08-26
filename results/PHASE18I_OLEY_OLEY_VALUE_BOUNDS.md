# Phase 18I — Oley Oley prize-value bounds and denominator threshold

Date: 2026-08-26

Status: **LIVE SUPER-KENO-ELIGIBLE OVERLAY; DENOMINATOR STILL UNRESOLVED; VALUE BOUNDS MATERIAL**

## Verified live mechanics

Fresh official Misli posts state that participants must join the campaign and then receive:
- 1 chance per 5 AZN of sports betting;
- 2 chances per 5 AZN in Virtual Idman, ePoz-Qazan and **Lotereya**.

Published weekly draw ladder:
- 1 x Changan UNI-Z;
- 3 x iPhone 17 Pro;
- 5 x PlayStation 5;
- 50 x 200 AZN bonus = 10,000 AZN nominal bonus.

After the third draw Misli publicly advertised remaining inventory equal to three more weekly ladders (1 car, 9 iPhones, 15 PS5, 30,000 AZN bonus), consistent with a repeated weekly ladder.

Official/current campaign page:
- https://www.misli.az/kampaniyalar/oley-oley

Official Misli Telegram snapshot:
- https://t.me/s/misliaz

No defensible public total-entry count or explicit number-domain/denominator was located. Winner-number ranges are **not** used to infer denominator because the numbering/reset scheme remains unproven.

## Current local prize reference prices

Snapshot 2026-08-26:
- Changan Azerbaijan lists Uni-Z IDD at **38,900 AZN**: https://changan.az/model/uni-z-idd/
- Baku Electronics lists iPhone 17 Pro 256GB around **3,099.99 AZN** current promotional price: https://bakuelectronics.az/mehsul/telefon-iphone-17-pro-256gb-silver-222749
- Baku Electronics lists PS5 Slim Blue-Ray 1TB at **1,449.99 AZN** current promotional price: https://bakuelectronics.az/mehsul/playstation-5-slim-blue-ray-201123

Exact campaign storage/color/configuration is not publicly established, so these are valuation references, not claims that every awarded unit is the exact same retail SKU.

## Base-game break-even requirement

Current exact after-tax 1x Super Keno expected cash return is:

`e = 0.5918070335 per 1 AZN stake`.

For 5 AZN spend:
- expected base cash = `5e = 2.9590351675 AZN`;
- shortfall to break-even = `2.0409648325 AZN`;
- Oley Oley grants 2 entries;
- required overlay EV per entry = **1.02048241625 AZN**.

Thus, if weekly campaign prize value is `V` and there are `M` equal-probability qualifying entries in the weekly pool, combined personal-capital EV is >=1 only if approximately:

`M <= V / 1.02048241625`.

## Three prize-value scenarios

These deliberately separate prize *face/retail value* from expected realizable value.

### Conservative liquidation scenario

Assumptions:
- car realizable value = 75% of 38,900;
- each iPhone = 70% of 3,099.99;
- each PS5 = 65% of 1,449.99;
- 200-AZN bonuses assigned **zero value** because wagering/withdrawal terms remain unresolved.

Weekly effective prize value: **40,397.45 AZN**.

Break-even maximum weekly entries: **~39,587**.

### Central scenario

Assumptions:
- car = 90% of reference price;
- iPhones = 85% of reference price;
- PS5 = 80% of reference price;
- 10,000-AZN nominal bonus valued as if it required one full wager at 1x Super Keno and produced withdrawable winnings: `10,000 * 0.5918070335 = 5,918.07 AZN` expected cash.

Weekly effective prize value: **54,633.00 AZN**.

Break-even maximum weekly entries: **~53,536**.

### Optimistic retail/face-value scenario

Assumptions:
- full reference retail value for car/electronics;
- full 10,000 AZN bonus counted as cash-equivalent face value.

Weekly prize value: **65,449.92 AZN**.

Break-even maximum weekly entries: **~64,136**.

## Important implication

The earlier bonus-only threshold (~9,799 weekly entries) was far too conservative for assessing the full overlay because it intentionally ignored the car and electronics. Once the non-cash prizes are included, the weekly competition pool could be roughly **40k–64k entries** and still be mathematically compatible with break-even depending on realizable prize values and bonus rules.

This makes Oley Oley materially more plausible as a positive-EV overlay than the bonus-only pilot suggested, but **no +EV claim is valid without a defensible weekly denominator or upper bound**.

## Bonus-term audit

Public search on 2026-08-26 did not locate official text resolving:
- whether the 200-AZN prize is withdrawable directly;
- required turnover/wagering multiple;
- eligible product scope for wagering the bonus;
- expiry.

Therefore the central bonus valuation is a scenario only, not a verified rule.

## Decision

Classification remains:

`current_super_keno_eligible_denominator_unresolved`

Do not stake based on this overlay yet.

## Next action

1. Search official draw videos/results/screenshots for an explicit total-entry count, ticket-number domain, or statement of weekly reset/accumulation.
2. Search campaign/legal terms through any newly indexed official source; specifically bonus conversion and campaign period.
3. If no denominator can be recovered, attempt an evidence-based **upper bound from platform/campaign participation disclosures**, but never infer it merely from observed winner numbers.
4. In parallel scan other current lottery-eligible overlays; Oley Oley remains the highest-priority candidate until its denominator is resolved or campaign ends.
5. If an official denominator/upper bound is below the conservative ~39.6k threshold, promote immediately to positive-EV candidate and design variance-aware Super Keno execution with N free.
