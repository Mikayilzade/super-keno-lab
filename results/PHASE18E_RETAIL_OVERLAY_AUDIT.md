# Phase 18E — retail / merchant overlay audit

Date: 2026-08-26

Status: **NO CURRENT POSITIVE-EV RETAIL OVERLAY VERIFIED; RETAIL-RECEIPT LOTTERY CLASS REMAINS CONDITIONALLY INTERESTING.**

## OBA

OBA's published lottery terms repeatedly exclude chance-game purchases from qualification. For example, the March 2026 `Qonşuda 2 qat bayram` rules explicitly list alcohol, tobacco and **şans oyunlarının alışı** as excluded. The published `Evini OBA ilə doldur` terms likewise exclude chance games from the qualifying spend.

Sources:
- https://oba.az/lotereyalarimiz/qonsuda-2-qat-bayram-lotereyasi/
- https://www.oba.az/lotereyalarimiz/evini-oba-ile-doldur/

Decision: **OBA receipt-lottery stacking is closed under current/published mechanics unless a future campaign explicitly removes this exclusion.**

## Araz standard cashback

Araz sells Azerlotereya Poz-Qazan tickets in 360+ stores, establishing that lottery products are present in the retail channel.

Source:
- https://www.arazmarket.az/az/news/poz-qazan-oyunlari-arazda-611

However, Araz mobile-app rules explicitly state that cashback is not earned on `uduşlu oyunlar` (winning/chance games), alongside several other excluded categories.

Source:
- https://www.arazmarket.az/az/araz-app

Decision: **ordinary Araz cashback cannot be counted as a lottery subsidy.**

## Araz receipt-lottery campaigns — a distinct mechanic

Araz has also run separate receipt-lottery campaigns in which qualification is based on total receipt spend. A recent example was `Uçuşa hazır ol`, active 4 July–4 August 2026:
- every 20 AZN receipt spend = 1 chance;
- 10 winners;
- each winner received a 5,000 AZN travel voucher;
- total published prize face value = 50,000 AZN;
- the published exclusions mention tobacco and alcohol, but **do not explicitly mention lottery/chance-game purchases**.

Source:
- https://arazmarket.az/az/campaigns/arazda-ucusa-hazir-ol-lotereyasi-21

This campaign is already inactive on the 2026-08-26 snapshot, and public terms do not establish that Super Keno itself can be bought through the Araz retail checkout. Therefore it is **not an actionable Super-Keno modifier**.

Still, the campaign reveals a materially different future search class: a retailer may exclude lottery tickets from ordinary cashback while failing to exclude them from a separate receipt-lottery qualification rule. This must be checked campaign-by-campaign from exact receipt terms.

### Hypothetical break-even diagnostic

If a future Araz-style campaign:
1. explicitly allowed 20 AZN of Super Keno spend to generate one receipt-lottery chance; and
2. had the same 50,000 AZN prize face value;

then 20 AZN of 1x Super Keno has expected after-tax cash return:

`20 * 0.5918070335 = 11.83614067 AZN`

so the missing EV to break even is:

`20 - 11.83614067 = 8.16385933 AZN` per qualifying chance.

With a 50,000 AZN equal-entry prize pool, break-even would require approximately:

`total qualifying entries <= 50,000 / 8.16385933 = 6,124.55`

or at most about **6,124 total equal-weight entries** before considering prize-voucher discounting, taxes, non-cash utility or participant concentration.

This is only a diagnostic; the historical campaign is inactive and Super-Keno receipt eligibility is unverified.

## Current result

- OBA: chance-game purchases explicitly excluded from receipt-lottery qualification.
- Araz standard cashback: chance/winning games explicitly excluded.
- Araz receipt lotteries: historically published exclusions can be narrower than cashback exclusions, so **future campaign-specific stackability remains worth checking**.
- No current retail partner promotion with verified Super-Keno eligibility and positive EV was found in this batch.

## Next action

1. Search Azərpoçt / kiosk / distributor and retailer-specific promotions for exact lottery-spend qualification language.
2. Monitor future Araz receipt-lottery terms specifically for whether `uduşlu oyunlar` / `şans oyunları` are excluded from the qualifying receipt.
3. Search for promotions where prize-pool size and total entry count (or a defensible upper bound) are both published.
4. Keep retail cashback and receipt-lottery mechanics separate in the ledger; exclusion from one does not automatically prove exclusion from the other.
5. If a current campaign explicitly admits Super Keno spend, immediately compute combined EV and only then move to variance-aware ticket execution with N free.
