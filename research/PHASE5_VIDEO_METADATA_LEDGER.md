# Phase 5 — public video and equipment metadata ledger

Date: 2026-08-24

Purpose: record externally documented operational metadata before any further statistical interpretation. Unknown fields remain UNKNOWN rather than being inferred from draw outcomes.

## Equipment baseline

Public evidence supports the use of physical draw equipment and balls for televised draw lotteries including Super Keno. A 2022 studio report describes pre-draw equipment tests, ball weighing, protective gloves, French Akanis Technologies equipment, and backup equipment. Azərlotereya management also stated that Akanis lototrons were purchased for draw lotteries.

Akanis states that its machines use air-mix technology and that RFID ball recognition is optional. The exact Azerbaijan Super Keno machine model, ball-set inventory, set-rotation policy, RFID configuration, and dates of backup-machine substitutions remain UNKNOWN.

References:
- https://metbuat.az/news/1441403/azerlotereya-da-1-milyon-manatliq-udus.html
- https://publika.az/news/sosial/404529.html
- https://fed.az/az/biznes/azerlotereyanin-sedri-lotereya-satisindan-yigilan-pullarin-63-68-uduslara-yoneldilir-musahibe-136621
- https://www.akanis.tech/

## Official video archive — June 2026

Official Telegram archive:
https://t.me/s/Azerlotereya?before=2472

The official archive contains draw-media entries across the Phase-4 weak change-point neighborhood:

| Date | Draw code | Archive evidence | Visual equipment annotation |
|---|---:|---|---|
| 2026-06-01 | 26231 | `01 Iyun 2026 Tiraj 26231.mp4`, 758.2 MB | UNKNOWN; frames not inspected in this pass |
| 2026-06-02 | 26232 | official draw media, ~17:24 shown in index | UNKNOWN |
| 2026-06-03 | 26233 | official draw media, ~17:51 | UNKNOWN |
| 2026-06-04 | 26234 | official draw media, ~17:31 | UNKNOWN |
| 2026-06-05 | 26235 | official draw entry present | UNKNOWN |
| 2026-06-06 | 26236 | official draw media, ~16:36 | UNKNOWN |
| 2026-06-07 | 26237 | official draw media, ~16:50 | UNKNOWN |
| 2026-06-08 | 26241 | official draw media, ~17:38 | UNKNOWN |

Conclusion: an official continuous media trail exists around 2026-06-01..08. A possible operational change can therefore be checked against independent video metadata rather than defined from the number data itself.

## Official YouTube archive — January 2025

- 2025-01-05, draw 25017: https://www.youtube.com/watch?v=7WuXyD0seho
- 2025-01-10, draw 25025: https://www.youtube.com/watch?v=PBc9H0Tt5hs
- 2025-01-11, draw 25026: https://www.youtube.com/watch?v=AuuHAB0rDpg

The 2025-01-05 description lists Meqa 5/36, Super Keno and 4+4. The 2025-01-11 description lists Beşdə 5 and Super Keno.

Official notice says 2025-01-06 was the final 5/36 draw and Beşdə 5 replaced it the next day. The 2025-01-15 announcement documents a wider draw-lottery branding/site refresh.

References:
- https://www.azerlotereya.com/xeberler/bu-gun-5-36-lotereyasinda-son-tiraj-oynanilacaq-66
- https://www.azerlotereya.com/xeberler/tirajli-lotereyalar-yenilandi-1820

Decision: 2025-01-07 is an externally documented program-lineup boundary, but no Super Keno machine or ball-set replacement is established by this evidence alone.

## Schedule context

- 2022 studio report described a 20:30 draw broadcast.
- Official 2023 material says Super Keno was daily at 19:45 and 4+4 ran Mon/Wed/Fri/Sat.
- Current official TV schedule says Super Keno and Beşdə 5 are daily at 19:45; 4+4 runs Tue/Fri.

References:
- https://metbuat.az/news/1441403/azerlotereya-da-1-milyon-manatliq-udus.html
- https://www.azerlotereya.com/xeberler/tirajli-lotereya-biletlari-satis-noqtalarinda-48
- https://www.azerlotereya.com/tv-yayimlari

These are program/schedule regimes, not automatically machine regimes.

## Draw-code audit

For the first 160 already-exposed rows, all 107 available official draw IDs match the deterministic calendar code `YYWWD`: 2-digit ISO week-year + 2-digit ISO week + ISO weekday (Mon=1..Sun=7).

Examples:
- 2025-01-10 -> ISO 2025-W02 Friday -> 25025.
- 2026-06-01 -> ISO 2026-W23 Monday -> 26231.

Therefore draw-number jumps are calendar-coded and should not be interpreted as sequential missing/cancelled draws without independent evidence.

Reproducible audit: `experiments/phase5_operational_regime_audit.py`.

## Weekday/shared-program sanity check

Using only the first 160 already-exposed rows, number 4 is low on several weekdays rather than confined to one day. For the documented current-schedule period anchored from 2025-11-26, the Tue/Fri-vs-other-days 70-number frequency-difference vector has design-to-diagnostic correlation -0.0027. Individual weekday profile correlations are also near zero or negative.

Conclusion: no stable weekday/shared-program frequency fingerprint is supported by the exposed sample. This does not rule out undocumented equipment or ball-set rotation.

Raw output: `results/phase5_operational_regime_audit.json`.

## Next metadata targets

1. Annotate machine/chamber/ball appearance in 2026-06-01 vs 2026-06-02 and surrounding dates.
2. Compare 2025-01-05 against 2025-01-10/11 around the documented program transition.
3. Search older 2022/2023 footage for the first stable appearance of the current studio/equipment setup.
4. Search for explicit public records of maintenance, replacement, backup-machine use, or ball-set rotation.
5. Keep the final 35-row holdout uninspected for strategy selection.
