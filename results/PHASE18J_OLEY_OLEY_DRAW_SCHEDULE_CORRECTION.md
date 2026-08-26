# Phase 18J — Oley Oley draw-schedule correction and next-draw EV window

Date: 2026-08-26

Status: **DENOMINATOR STILL UNRESOLVED; IMPORTANT SCHEDULE CORRECTION; NEXT DRAW IS THE SECOND/FINAL CAR DRAW.**

## New evidence

Freshly indexed Misli Telegram history shows the campaign launch inventory as:
- 2 x Changan UNI-Z;
- 18 x iPhone 17 Pro;
- 30 x PlayStation 5;
- total 60,000 AZN bonus.

The first draw post lists:
- 3 x iPhone 17 Pro;
- 5 x PlayStation 5;
- 50 x 200 AZN bonus = 10,000 AZN;
- **no car**.

The third draw post lists the same electronics/bonus ladder plus **1 Changan UNI-Z**.

After the third draw, Misli advertised remaining campaign inventory:
- 1 x Changan UNI-Z;
- 9 x iPhone 17 Pro;
- 15 x PlayStation 5;
- total 30,000 AZN bonus.

That is exactly three more base weekly ladders of 3 iPhones + 5 PS5 + 10,000 AZN bonus, but only one remaining car.

Separately, a post reproducing the Misli campaign message after the first car winner states explicitly that the **second car owner will be determined in the next week's draw**.

Sources:
- https://t.me/s/misliaz?before=4825
- https://t.me/s/misliaz?q=%23Kampaniya
- https://t.me/s/fightingaz?q=%23OleyOley
- https://www.sportinfo.az/idman_xeberleri/sportinfo_tv/254962.html

## Corrected campaign structure

The evidence supports **six draws total** because 18 iPhones / 3 per draw = 6, 30 PS5 / 5 per draw = 6, and 60,000 AZN bonus / 10,000 per draw = 6.

The two cars are not weekly prizes. The first three observed draw ladders imply:
- draw 1: base ladder, no car;
- draw 2: base ladder, no car (campaign inventory/posts remain consistent with this);
- draw 3: base ladder + first car;
- draw 4: **base ladder + second/final car** (explicitly announced as next week);
- draws 5-6: base ladder only.

Therefore the Phase18I phrase `published weekly draw ladder: 1 car + ...` was too broad. Its 39.6k–64.1k break-even thresholds describe a **car draw**, not every campaign week.

## Corrected per-draw prize-value bounds

Base-game requirement is unchanged.

For 5 AZN 1x Super Keno:
- expected base cash = 2.9590351675 AZN;
- shortfall = 2.0409648325 AZN;
- 2 Oley Oley entries earned;
- required overlay EV = **1.02048241625 AZN per entry**.

Using the exact Phase18I valuation assumptions:

| scenario | non-car draw effective prize value | non-car max entries for combined EV >=1 | car draw effective prize value | car-draw max entries for combined EV >=1 |
|---|---:|---:|---:|---:|
| conservative | 11,222.45 AZN | **~10,997** | 40,397.45 AZN | **~39,587** |
| central | 19,623.00 AZN | **~19,229** | 54,633.00 AZN | **~53,536** |
| optimistic | 26,549.92 AZN | **~26,017** | 65,449.92 AZN | **~64,136** |

Interpretation: without a car, the required denominator is much smaller. The current highest-value opportunity is specifically the upcoming **draw 4**, because it is publicly identified as the second/final automobile draw.

## What remains unresolved

No defensible official weekly total-entry count, participant count, issued-number count, or explicit numbering-domain statement was found in this run.

Public sources still do not resolve:
- whether chance entries reset each draw or remain in subsequent draws;
- exact 200-AZN bonus turnover/withdrawal/product-scope rules;
- exact campaign legal start/end timestamps.

The six-draw inventory structure proves the prize schedule but **does not prove chance reset/accumulation mechanics**.

Winner-number magnitudes remain excluded as denominator evidence without a numbering rule.

## Decision

Classification remains:

`current_super_keno_eligible_denominator_unresolved`

Do not promote to +EV yet.

However, denominator research should now focus on the upcoming **second-car draw**. For that draw, a defensible pool below ~39,587 entries would be enough to pass even the conservative value gate.

## Next action

1. Prioritize draw-4 official live/video/result material for any spoken or displayed total number of chances/participants.
2. Search for exact legal campaign text or app screenshots resolving chance reset versus accumulation.
3. Resolve 200-AZN bonus conversion terms.
4. Treat later non-car draws separately with the much stricter ~11.0k / ~19.2k / ~26.0k denominator thresholds.
5. If draw-4 denominator is proven below ~39,587, immediately promote to positive-EV candidate and build variance-aware Super Keno execution with N free.
