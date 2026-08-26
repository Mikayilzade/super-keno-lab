# Phase 18F — distributor channels + current promo-code scan

Date: 2026-08-26

Status: **NO VERIFIED CURRENT SUPER-KENO +EV MODIFIER YET; ONE LIVE PROMOCODE LEAD REQUIRES ELIGIBILITY RESOLUTION.**

## Azərpoçt / kiosk / distributor audit

Fresh official/public evidence confirms that Super Keno tickets are sold through multiple physical channels including **Azərpoçt branches**, Azərlotereya sales points, Misli points and OBA; Azerlotereya's sales-point selector also exposes postal points as a channel for Super Keno.

Sources:
- https://www.azerlotereya.com/xeberler/super-keno-lotereyaasinda-100-000-manat-uduldu-1905
- https://www.azerlotereya.com/satis-menteqeleri

No current public Azərpoçt-specific cashback, receipt-lottery, free-ticket or Super-Keno rebate was found in this scan.

Important separation: historical `Sürətli Şans` did **not** create a physical Azərpoçt stacking route. Its published terms say chance codes were generated from play on `Azerlotereya.com` and `Misli.az` (with ePoz-Qazan receiving 2 chances); physical Azərpoçt ticket purchases were not named as a qualifying source.

Source:
- https://www.azerlotereya.com/suretli-sans

Therefore physical distributor availability is an execution channel, not currently an EV modifier.

## Current live lead — Misli 10 AZN radio promo codes

Official Misli Telegram currently advertises a weekday promotion tied to 106.3 FM / RadioArena: listeners can win **10 AZN promo codes**.

Source:
- https://t.me/s/misliaz?q=%23RadioArena

This is materially different from archived Azerlotereya campaigns because the public promotional message is current and recurring on weekdays.

### What is verified

- issuer: Misli official social channel;
- value advertised: **10 AZN promo code**;
- cadence: weekdays at 20:00 via 106.3 FM;
- current public availability: yes in the fresh social snapshot.

### What is NOT yet verified

The public post does not state:
- whether promo balance can be used on lottery products or only sports betting;
- whether Super Keno is specifically eligible;
- wagering requirements / minimum odds if sportsbook-only;
- withdrawal rules for resulting winnings;
- number of codes awarded per broadcast / probability of receiving one.

Because those conditions determine whether the code is a Super-Keno EV overlay, **no positive-EV classification is allowed yet**.

### Conditional Super Keno value

If a 10 AZN promo code were genuinely usable as one-time stake on 1x Super Keno with resulting winnings withdrawable and no personal deposit/stake requirement, the exact expected after-tax cash generated would be:

`10 * 0.5918070335 = 5.918070335 AZN`

per successfully acquired free promo code, before any withdrawal friction.

If obtaining the code requires no monetary expenditure, the relevant optimization is no longer base-game ROI on personal stake; the code has positive expected cash value by construction. If winning/claiming the code requires paid qualifying activity, that cost must be included before promotion.

## Promocode infrastructure signal

Azerlotereya's current logged-in menu publicly exposes a `Promokod` section. This proves promo-code infrastructure exists on the lottery platform, but it does **not** prove that Misli RadioArena codes are cross-platform or lottery-eligible.

Source:
- https://azerlotereya.com/

Third-party pages claiming specific current promo codes or lottery free-ticket codes are excluded from the actionable ledger unless confirmed by official terms.

## Sürətli Şans denominator attempt

The official 8th-week winner list exposes 9-digit winning chance numbers around `105xxxxxx`–`106xxxxxx`, and the FAQ explains that users may receive sequential ranges of chance numbers by SMS. This suggests high code volume, but the published materials do not establish the global starting number or prove that every integer in the observed range was issued. Therefore these identifiers are **not used as a defensible denominator** and the prior overlay remains indeterminate.

Sources:
- https://www.azerlotereya.com/suretli-sans
- https://www.azerlotereya.com/faq/suretli-sans

## Decision

1. Azərpoçt / kiosk distribution remains **neutral execution infrastructure**, not a verified subsidy.
2. Historical `Sürətli Şans` physical stacking via Azərpoçt is rejected: published qualification was online-account based.
3. The **current Misli RadioArena 10 AZN promo code** is the best fresh lead and is promoted to `current_terms_unresolved` in the ledger.
4. Do not assign it positive Super-Keno EV until official eligibility/wagering/withdrawal terms are found.

## Next action

1. Resolve Misli RadioArena promo-code terms from official Misli FAQ/support/campaign pages or current social announcements; specifically test lottery/Super-Keno eligibility and wagering/withdrawal conditions.
2. Search for other current official promo-code distributions and free-ticket mechanics; ignore SEO/affiliate claims unless independently confirmed.
3. Continue distributor/retailer monitoring only for explicit subsidies, receipt-lottery qualification or discounts; plain ticket availability is not an edge.
4. Keep searching stimulating-lottery denominators, but do not infer counts from winner-number ranges without proof of numbering scheme.
5. If a free/current promo code is confirmed usable on Super Keno, immediately design the variance-aware free-stake execution with N free and calculate expected cash/downside.