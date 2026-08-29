# Phase 18CA — 1001 Sevinc repeated sellout evidence and execution risk

Date: 2026-08-29

## Objective

Continue the finite-pool denominator route without reopening bounded APK-mirror, checker-input, Trendyol-public-search, or rejected history-prediction branches. Look specifically for materially new first-party evidence that clarifies whether category-level ticket pools actually exhaust in practice and how quickly a near-sellout state can transition to closure.

## New evidence

Two official operator Telegram surfaces establish repeated real sellouts for `1001 Sevinc` iPhone pools:

1. Misli's official channel states that the **first 1001 Sevinc draw** was held early because tickets sold out quickly; that draw awarded five iPhone 16 Pro Max (256 GB) prizes at 1 AZN per ticket.
2. Azerlotereya's official channel later posted that, with **3 days remaining**, a three-iPhone pool had **very few tickets left** (`Biletlər çox az qaldı`). A later post on the same official channel states that tickets again sold out quickly and the draw was held early; three winners each received an iPhone 16 Pro Max from 1-AZN tickets.

Direct Telegram post identifiers recovered for the later sequence:
- near-sellout post: `Azerlotereya/2108`
- completed early-sellout post: `Azerlotereya/2122`

Sources:
- https://t.me/s/misliaz?before=4222
- https://t.me/s/Azerlotereya?before=2125
- https://t.me/Azerlotereya/2108
- https://t.me/Azerlotereya/2122

## Interpretation

This is materially stronger than a rules-only statement that a draw *may* close when sold out. It shows that category/draw pools have actually reached exhaustion more than once, and that the operator publicly transitions from a qualitative near-sellout state to an early closed draw.

This supports the finite-pool mechanism as operationally real. It also raises execution-risk importance: an attractive high-sold% pool can disappear before the nominal draw date. Any future positive-EV call therefore needs not only denominator/cap evidence but a sell-through buffer and explicit availability check close to execution.

The evidence does **not** reveal an absolute cap, remaining count, or sold-ticket count. `Biletlər çox az qaldı` is qualitative and cannot be converted into a numeric denominator. Historical six-digit chance numbers remain namespace/offset values and must not be interpreted as sold counts.

## Consequences for current candidates

No classification change for `10066 Silver` or `10072 S25 Ultra Black`: denominator remains unresolved.

For a future recovered `(cap, remaining)` observation, preserve the existing buffered ROI framework and add a separate `execution_closure_risk` flag. A high sold percentage near the threshold should be treated as a rapidly expiring opportunity, not as a stable state.

`N` remains a free integer optimization variable.

## Result

**Not yet success.** Repeated real category-level sellouts are now verified from first-party operator channels, but the absolute denominator needed for executable ROI is still missing.

## Next action

1. Continue highest-priority search for a genuinely new retrievable APK/file/CDN/runtime artifact for exact Misli build `v=1361`.
2. In parallel, search only genuinely new rendered/account/retail/POS artifacts for `10066` / `10072` that expose absolute `remaining`, `total`, cap, issuance, or stock.
3. Treat historical operator social posts as useful only when they contain a numeric sold/remaining quantity or a directly interpretable product screenshot; do not spend cycles on more qualitative `few tickets left` posts.
4. If a numeric cap/remaining appears, compute buffered ROI immediately and include execution-closure risk separately.
