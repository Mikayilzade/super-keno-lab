# Phase 18BY — public winning chance numbers + checker input boundary

Snapshot: 2026-08-29

## Goal

Continue from Phase 18BX without reopening bounded APK/mirror/hostname branches. Highest-priority target for this batch: find a legitimate already-public `1001 Sevinc` identifier that can be used to reason about the first-party `Biletini Yoxla` resolver without brute force.

## Materially new evidence

A publicly indexed result image from the first `1001 Sevinc` draw (published 2025-07-08 by news outlets reproducing the operator result graphic) exposes five explicit winning identifiers for `iPhone 16 Pro Max (256 GB) Black Titanium` under the heading **`Qalib şans nömrələri`**:

- `103932`
- `107185`
- `112723`
- `116364`
- `121104`

The associated reporting states that the first draw awarded five identical iPhone 16 Pro Max prizes at 1 AZN each and that winners were selected in the official live draw.

Source artifact discovered in image search:
- Oxu.az / operator-result graphic, 2025-07-08
- duplicate/republication on FED.az shows the same five identifiers.

## Why this matters

This is the first recovered set in the current branch of **legitimate already-public `1001 Sevinc` numeric identifiers** suitable for non-bruteforce resolver work.

However, the artifact labels them **chance numbers** (`şans nömrələri`), while the public checker UI asks for a **ticket number** (`Bilet nömrəsi`). Current first-party `1001 Sevinc` copy also mixes terminology by saying post-draw winning *ticket numbers* are published while gameplay copy says each ticket has its own *chance number*.

Therefore these values must **not yet be assumed to be valid checker inputs**. They are safe public test candidates only if a future request/response schema, UI artifact, or explicit operator wording proves that the checker accepts the chance-number field for `1001 Sevinc`.

## Denominator implication

No denominator is established from these numbers.

In particular, do **not** interpret `121104` (or any maximum observed chance number) as sold count, cap, issuance count, or remaining-ticket count. Existing evidence already shows chance identifiers can live in an offset/namespace and this batch does not overturn that conclusion.

The five values are useful as schema-resolution anchors only.

## Current checker boundary

The first-party `Biletini Yoxla` page remains publicly reachable and asks for `Bilet nömrəsi`, but no indexed API route/request schema/response payload was recovered in this batch. Direct generic API-string searching also returned no actionable endpoint. No form submission or brute-force probing was performed.

## Status

**Not yet success.** No executable positive-EV modifier and no absolute finite-pool denominator recovered.

`N` remains a free integer optimization variable.

## Next action

1. Keep the five public identifiers as a vetted zero-cost fixture set for future resolver/schema work.
2. Identify the `Biletini Yoxla` request/response schema from genuinely new static/runtime evidence; only after field semantics are established should any of the five public chance numbers be submitted.
3. Search new result-card/social/POS artifacts for a case that exposes **both** a full ticket/serial number and its `1001 Sevinc` chance number; that would directly bridge the checker-input ambiguity.
4. Continue denominator search for current `10066 Silver` / `10072 S25` through account/rendered/POS surfaces; if `total/cap/remaining` appears, compute buffered ROI immediately.
5. Do not reopen generic APK mirror / `endir` / `yukle` hostname variants without materially new evidence.
