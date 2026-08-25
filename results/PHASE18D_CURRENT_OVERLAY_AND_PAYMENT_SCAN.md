# Phase 18D — current overlay + payment-channel scan

Date: 2026-08-26

Status: **NO CURRENT PUBLIC POSITIVE-EV SUPER-KENO MODIFIER VERIFIED. PAYMENT-REWARD STACKING NARROWED FURTHER.**

## Scope

This batch continued the external-EV route only. It did not reopen any draw-history prediction branch.

Sources screened:
- current Azerlotereya campaign listing and August 2026 campaign/news pages;
- recent cross-game/digital tournaments;
- current/recent Azerbaijani bank cashback/reward/lottery mechanics where gambling/lottery MCC treatment is published.

## Current official campaign state

Official current-campaign page snapshot on 2026-08-26 still states:

`Cari kampaniya mövcud deyil`

Source: https://www.azerlotereya.com/kampaniyalar

The archived `10 oyna, 10 qazan` page remains contradictory internally, but the dedicated page is categorized as past and its FAQ gives 14 Apr–31 Jul. It remains historical/inactive for decision purposes.

## Recent Azerlotereya promotions screened

### `Sürətlə Qazan`

Source: https://www.azerlotereya.com/kampaniyalar/suretli-qazan

- ran 7 Aug 2026 16:00 through 14 Aug 2026 14:00;
- only 52 games carrying the tournament tag qualified;
- 1 AZN wager = 10 leaderboard points;
- leaderboard display maximum 500 players;
- not a Super-Keno qualifying modifier from the published scope;
- already expired at this snapshot.

Classification: `historical_recent_ineligible_for_super_keno`.

### `Şans Karvanı 2`

Source: https://www.azerlotereya.com/xeberler/sans-karvani-2-mohtasam-aylanca-geri-qayidir-1910

The public announcement describes regional event games, smartphones, gift cards and other prizes, but does not publish a ticket-linked qualification cost/probability table from which a defensible Super-Keno overlay EV can be calculated.

Classification remains `event_marketing / not_quantifiable`.

## Payment-channel stacking audit

### Unibank

Already recorded: published cashback rules exclude gambling/betting/lottery transactions.

Classification: `current_excluded`.

### ABB / TamKart

Current personalized cashback page states that gambling and lottery operations are excluded. It explicitly lists MCC 7995 among excluded MCCs.

Source: https://abb-bank.az/ozel-kampaniya-2

ABB's recent `Qollar qazandırır` reward campaign is even more explicit: merchant names containing `Loto`, `Casino`, `Gambling` are excluded, together with MCC 7800 (government lotteries), 7801, 7802, 7995 and 9754.

Source: https://abb-bank.az/kampaniyalar/qollar-qazandirir-kampaniyasi

Classification: `current_excluded` for ordinary Super-Keno payment stacking.

### Birbank / Kapital Bank

Birbank's published lottery rules explicitly exclude MCC 7800, 7801, 7802 and 7995 from earning campaign tickets.

Source: https://birbank.az/landings/150-illiyimize-ozel-mohtesem-lotereya

Classification: `current_excluded` for lottery-reward stacking.

## Interpretation

The payment-overlay route is not merely missing an attractive cashback rate: several major public reward systems explicitly blacklist the relevant lottery/gambling merchant categories. Therefore ordinary card-reward stacking should be considered a low-priority route unless a future campaign **explicitly includes** lottery transactions or uses a different eligible transaction path under published rules.

No current public Azerlotereya campaign or bank/payment modifier exceeding the established Super-Keno break-even thresholds was verified in this batch.

## Next action

1. Prioritize non-bank external overlays: merchant/retail partner promotions, promo codes, free-ticket bundles, stimulating lotteries and cross-game qualification where lottery spend is explicitly eligible.
2. Search for participant/code denominators or defensible bounds in stimulating lotteries; without a denominator, prize-pool headlines are not EV evidence.
3. Screen account-independent current Misli/Azerlotereya announcements and terms for any offer launched after this snapshot.
4. Treat standard ABB/Birbank/Unibank cashback/reward stacking as closed for now unless materially new rules explicitly include lottery MCCs.
5. If a positive-EV modifier appears, keep N free and only then design variance-aware distinct-ticket execution.
