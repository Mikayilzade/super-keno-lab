# Phase 18BI — retail-ticket artifact route

Date: 2026-08-28

## Outcome

**Not yet success.** No absolute `cap / remaining / sold-count` was recovered for `drawId=10066` (Silver) or `drawId=10072` (S25 Ultra Black).

This batch deliberately did **not** repeat the closed public detail-page/API/registry/Trendyol-download paths. Instead it tested whether the now-current offline/retail distribution channel creates a materially different artifact surface that could expose denominator information.

## Materially new operational evidence

A fresh official Azerlotereya Telegram result post for the current 1001 Sevinc product explicitly says that tickets for the **next draw** are available from:

- Azerlotereya retail sales points;
- Misli points;
- Azerlotereya.com;
- Misli.az;
- Trendyol.az.

This confirms that the present product is not purely account/client-side; there is a current physical-ticket / retail-receipt surface that was not part of the prior denominator crawl.

The official Azerlotereya site also currently exposes a general **`Bilet yoxla` / ticket-number checker** and the official 1001 Sevinc explainer says every purchased 1001 Sevinc ticket has its own `şans nömrəsi` used in the draw. Historical official/result imagery visibly publishes six-digit winning chance numbers.

## What this does and does not prove

It **does prove** a new artifact class exists: physical ticket / point-of-sale receipt / purchase-history image carrying a ticket or chance identifier, potentially with draw/prize metadata.

It **does not prove** that the identifier is a simple 1..C serial number. Prior work already showed historical chance IDs use an offset/namespace, so neither a large observed chance number nor `max(chance ID)` may be treated as sold count or cap.

Therefore the only useful retail artifact is one that reveals additional structured fields such as:

- draw/prize identifier or exact prize name;
- ticket/chance number plus an issuance sequence/ordinal;
- total/remaining quantity;
- range endpoints;
- batch/series code whose semantics can be independently validated.

A screenshot containing only one six-digit chance number is **not enough** to infer the denominator.

## Search result

Fresh searches for public images/posts containing `1001 Sevinc` ticket numbers, chance numbers, or personal-ticket screenshots returned historical winning-number graphics, promotional cards, and general instructions, but no current 16.09.2026 retail receipt/ticket artifact exposing an absolute quantity.

No paid purchase or manual probe was performed.

## Decision

Keep this route **open but evidence-gated** because it is materially different from the exhausted client/API paths. Do not repeatedly search generic `1001 Sevinc bilet` terms. Re-enter only when a newly dated/current physical-ticket, receipt, account purchase-history screenshot, or retailer UI artifact appears.

## Next action

1. Continue denominator hunt for `10066` / `10072` only through genuinely new rendered/account/retail artifacts.
2. Treat current physical-ticket/receipt images as high-value if they expose more than a single chance number.
3. If a structured issuance ordinal/range is found, validate its semantics across at least two tickets/draws before using it to estimate `C` or `M`.
4. Keep the Phase 18BG percentage-transition solver ready for sequential rendered observations; no autonomous paid probe.
5. Preserve free integer `N`.

## Sources checked

- Official Azerlotereya Telegram, current 1001 Sevinc post (fresh crawl 2026-08-28): next-draw purchase channels include retail points, Misli points, Azerlotereya.com, Misli.az, Trendyol.az.
- Official Azerlotereya 1001 Sevinc parent/explainer pages, fresh crawl 2026-08-28: current draw structure and one unique chance number per purchased ticket; remaining-ticket count is visible in the logged-in/client product surface.
- Official Azerlotereya general ticket-check surface, fresh crawl 2026-08-28: ticket-number checker exists.
- Historical official/result imagery: six-digit 1001 Sevinc winning chance-number examples; used only to reject the unsafe `chance number == sold count` assumption, not as current-cycle data.
