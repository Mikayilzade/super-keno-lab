# Phase 18K — Oley Oley denominator search

Date: 2026-08-26

Status: **NOT YET SUCCESS — no defensible draw-4 denominator or upper bound found.**

## Objective

Resolve the highest-priority uncertainty from Phase 18J: total entries / participant count / issued chance range for the upcoming fourth `Oley Oley` draw, which includes the second and final Changan UNI-Z.

For 5 AZN of 1x Super Keno, the conservative positive-EV gate remains approximately **39,587 total entries** for a car draw. Below that threshold the overlay would be positive EV even under the conservative prize-value scenario used in Phase 18I/J.

## Fresh public evidence checked

Current Misli public/forwarded campaign material was re-scanned on 2026-08-26 for:
- `4-cü tiraj`, `dördüncü tiraj`, `dördüncü həftə`;
- participant / chance counts;
- issued-number ranges;
- chance reset / carry-forward wording;
- 200-AZN bonus rules;
- third-week result artefacts and the linked Instagram winner post.

### Confirmed

1. Misli's official Telegram material explicitly says the third draw was held with:
   - 1 Changan UNI-Z;
   - 3 iPhone 17 Pro;
   - 5 PlayStation 5;
   - 50 × 200 AZN bonus.
2. The third-week result post tells users to click `Kampaniyaya qoşul` and continue earning chances for the **next winners**, at 1 chance per 5 AZN sports betting and 2 chances per 5 AZN in Virtual Sport / ePoz-Qazan / Lottery.
3. After the third draw, the published remaining inventory is:
   - 1 Changan UNI-Z;
   - 9 iPhone 17 Pro;
   - 15 PlayStation 5;
   - total 30,000 AZN bonus.
4. A campaign-forwarded public post states that the **second car winner will be determined in the next week's draw**, corroborating Phase 18J's conclusion that draw 4 is the final car draw.

### Still not published / not recoverable from searchable public text

- total number of chances in draw 1, 2, 3 or upcoming draw 4;
- participant count;
- maximum issued chance number;
- whether chance IDs are sequential and therefore usable as a denominator proxy;
- whether unused/chances earned in prior weeks remain eligible or reset after each draw;
- exact 200-AZN bonus wagering / withdrawal / product-scope rules.

The linked third-week Instagram result page is not text-fetchable through the available public web interface, so its image-level winning-number list could not be treated as verified denominator evidence in this run.

## Important methodological restriction

A maximum observed winning number, if recovered later, is **not automatically an upper bound on total entries**. It can only be used if official rules or platform behaviour establish that chance numbers are issued sequentially from a known origin without gaps / per-user prefixes / hashing.

Similarly, a minimum number of distinct winners only creates a trivial lower bound and cannot establish positive EV.

## Decision

Classification stays:

`current_super_keno_eligible_denominator_unresolved`

Do **not** promote `Oley Oley + Super Keno` to positive EV yet.

The current public web index is now sufficiently exhausted that repeating nearby text searches has low value. The next evidence sources should be materially different.

## NEXT ACTION

1. Inspect **draw video / live-stream frames** for any displayed total chance count, randomizer range, numbered balls/cards, or on-screen participant statistics.
2. Inspect third- and fourth-draw **winner images** for chance-number format and compare multiple weeks to infer whether numbering resets or accumulates.
3. Search app-specific / cached campaign terms for reset/carry-forward wording and the 200-AZN bonus conditions.
4. If sequential numbering is proven, use the largest issued number immediately before draw 4 as a denominator proxy; otherwise do not infer denominator from winner IDs.
5. Keep the conservative car-draw gate at **~39,587 entries** until better prize-value or bonus-value evidence changes it.
