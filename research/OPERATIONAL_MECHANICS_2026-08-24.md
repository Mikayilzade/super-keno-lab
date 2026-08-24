# Super Keno operational mechanics and regime clues

Date: 2026-08-24

## Why this matters

Phase 2 showed that portfolio geometry alone behaves close to a fair/random same-size portfolio on synthetic draws. Therefore a persistent edge, if one exists, is more likely to require an empirical or operational signal in how real draws are produced, timestamped, scheduled or changed over time.

## Official observations

### Current rule registration

The official Super Keno page states registration **285 / 07.01.2025**, effective **10.01.2025 through 31.12.2027**.

Source: https://www.azerlotereya.com/game/superkeno

Dataset consequence: the copied 195-row history contains **8 rows before the current-rule effective date**: one 2022 row plus 2025-01-01 through 2025-01-07. These are now tagged conceptually as **legacy/pre-current-rule** and must not be mixed into current-regime signal fitting without an explicit reason.

### Draw mechanism wording is ambiguous

The official Super Keno game page describes the game as a **virtual numeric lottery** in which 20 of 70 numbered balls are taken from a **lototron**.

A separate official explainer says online draw lotteries can be conducted in a virtual/computer environment and lists Super Keno among popular draw games available online.

Sources:
- https://www.azerlotereya.com/game/superkeno
- https://www.azerlotereya.com/bloq/online-lotereya-tirajli-lotereya-ve-poz-qazandan-nece-ferqlenir-22

This does **not** yet establish whether Super Keno uses a physical ball machine, a software RNG feeding a virtual lototron, or another audited process. The exact generator must be established before claiming any equipment/RNG bias hypothesis.

### Live schedule vs result timestamp

The official TV schedule says Super Keno is broadcast live **every day at 19:45** on Xəzər TV / Azərlotereya TV. Multiple official news items from 2022, 2023, 2025 and April 2026 repeat 19:45.

However, the official current results page records recent Super Keno result metadata such as draw **26347 on 23.08.2026 at 18:45**.

Sources:
- https://www.azerlotereya.com/tv-yayimlari
- https://www.azerlotereya.com/xeberler/super-keno-lotereyaasinda-100-000-manat-uduldu-1905
- https://www.azerlotereya.com/lotereya-neticeleri

The one-hour difference is **not treated as evidence of a draw-time change**. Plausible alternatives include backend/server timezone handling, display normalization or a genuine schedule metadata change. It is a data-quality / regime clue that needs direct archive/video verification.

### Live broadcasts exist

The official site states Super Keno draws are broadcast on Xəzər TV and the Azərlotereya YouTube channel. This gives a possible path to inspect historical draw videos for machine/software presentation changes, draw timing, studio/equipment changes and recurring operational metadata.

### Technical interruptions

The official FAQ says that if a technical problem occurs during a draw, the draw can be cancelled or moved to another date and the information will be announced through official channels.

Source: https://www.azerlotereya.com/lotereya/fast-loto

This means draw-level exception metadata is potentially relevant and should be collected if available.

## Research implications

1. Future signal fitting should use the **current-rule regime (>= 2025-01-10)** by default.
2. Preserve legacy rows for comparison/regime-change tests, not as automatic training data.
3. Determine the actual randomization mechanism from official rules, audited documentation or historical draw footage.
4. Resolve the **19:45 vs 18:45** discrepancy before using draw time as a feature.
5. Search historical broadcasts/news for equipment, studio, software or schedule changes and for cancelled/postponed draws.
6. If a documented operational regime change is found, evaluate number/pair statistics separately on each side rather than pooling all history.

No operational edge is claimed yet.