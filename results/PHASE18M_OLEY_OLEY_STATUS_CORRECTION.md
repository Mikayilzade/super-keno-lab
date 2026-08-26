# Phase 18M — Oley Oley live-status correction

Date: 2026-08-26

Status: **NO CURRENT EDGE; OLEY OLEY MOVED FROM CURRENT/LIVE TO HISTORICAL-INACTIVE FOR EXECUTION PURPOSES.**

## Why this checkpoint was necessary

Phase 18H-L treated `Oley Oley` as the highest-priority live overlay because public indexed material still exposed the campaign page and the first three draw announcements. A fresh 2026-08-26 scan shows that this was stale-state risk: the public web keeps old campaign URLs/search snippets after the relevant drawing window.

## Fresh evidence

1. Misli's current Telegram feed, fetched 2026-08-26, contains current football/fantasy/promotional content but no live `Oley Oley` join/draw call in the current feed window.
2. Fresh indexed Azerbaijan media/Telegram mirrors describe the second Changan UNI-Z as already awarded and use retrospective wording equivalent to "in the Oley Oley campaign that was held" (`Misli.az-da keçirilmiş “Oley Oley” kampaniyasında ...`).
3. Earlier official/Misli material explicitly said the second vehicle would be awarded in the next draw after the first car. The second car being delivered therefore proves that the car-draw window identified in Phase 18J/K is no longer upcoming.
4. No current 2026-08-26 public call-to-action for earning new Oley Oley chances was found in the fresh official feed.

Relevant public evidence:
- current Misli Telegram feed: https://t.me/s/misliaz
- earlier draw-3 official feed context: https://t.me/s/misliaz?before=4865
- media proof that first car was won and second car would be next: https://www.sportinfo.az/idman_xeberleri/sportinfo_tv/254962.html
- fresh indexed mirror describing the second car as already awarded: Telemetrio/Showline search snapshot surfaced 2026-08-26.

## Decision

`Oley Oley` is no longer classified as a current executable Super-Keno overlay.

Previous classification:

`current_super_keno_eligible_denominator_unresolved`

New classification:

`historical_lottery_eligible_overlay_denominator_unresolved`

The denominator research remains valuable for methodology and for evaluating a future repeat of the same campaign, but it is **not worth spending current execution effort on extracting old winner IDs before a new live version appears**.

## Economic interpretation retained

The Phase 18I/J threshold work remains valid as a reusable template:
- for 5 AZN 1x Super Keno, base expected cash = 2.9590351675 AZN;
- shortfall to break-even = 2.0409648325 AZN;
- 2 Oley entries per 5 AZN were granted while the campaign was live;
- required overlay EV = 1.02048241625 AZN per entry;
- conservative car-draw break-even pool threshold was ~39,587 entries;
- non-car conservative threshold was ~10,997 entries.

These thresholds should be reused instantly if the same mechanic returns with comparable prizes.

## NEXT ACTION

1. Stop treating Oley Oley denominator extraction as the highest-priority current task; retain it as archived methodology.
2. Fresh-scan Misli/Azerlotereya and partner channels for **currently active** lottery-eligible overlays only.
3. Pay particular attention to promotions with explicit `Lotereya` eligibility, direct bonus/free ticket value, cross-game chance generation, or prize-pool overlays with a defensible participant denominator.
4. Run every current candidate through the exact Phase-17 EV modifier calculator before any execution design.
5. If no live positive-EV overlay exists, keep searching new information sources rather than reopening history-based draw prediction.
