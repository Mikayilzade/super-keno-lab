# Phase 18BZ — 1001 Sevinc ticket-vs-chance-number semantics

Date: 2026-08-29

## Objective

Continue the Phase 18BY `Biletini Yoxla` route without submitting public chance numbers and determine whether first-party evidence supports treating a `1001 Sevinc` `şans nömrəsi` as the checker input `Bilet nömrəsi`.

## New first-party evidence

1. The current Azerlotereya checker is public at both the generic and product-routed surfaces and labels its only input **`Bilet nömrəsi`**:
   - https://www.azerlotereya.com/biletini-yoxla
   - https://www.azerlotereya.com/keno/biletini-yoxla

2. Azerlotereya's current `1001 Sevinc` explainer explicitly states that **each purchased ticket has its own `şans nömrəsi`** and that winning is determined when the draw balls match that chance number. It separately states that the client surface shows **how many tickets remain until the draw**, and that sales stop when the predetermined ticket count is reached:
   - https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23

3. The public first-draw winner graphic labels the five recovered six-digit values (`103932, 107185, 112723, 116364, 121104`) specifically as **`Qalib şans nömrələri`**, not ticket numbers.

4. Separate first-party Poz-Qazan pages describe a physically printed **serial number** as a ticket-validity field: damaged tickets whose `seriya nömrəsi` is unreadable are not accepted for prize payment. This does not prove the exact 1001-Sevinc schema, but it confirms that the operator distinguishes ticket/serial identifiers from game-result numbers in other lottery products.

## Conclusion

The evidence now favors **distinct semantics**:

- `Bilet nömrəsi` / ticket or serial identifier = checker-resolution key;
- `şans nömrəsi` = draw-participation number attached to a purchased 1001-Sevinc ticket.

Therefore the five Phase-18BY chance-number fixtures must **not** be submitted to `Biletini Yoxla` merely because they are six-digit public numbers. The checker route cannot currently be used to infer the finite denominator without an artifact that binds a full ticket/serial identifier to its 1001-Sevinc chance number or exposes the checker request/response schema directly.

This also strengthens the product-card route: the official explainer independently confirms that an absolute `tickets remaining` quantity is deliberately surfaced to users and that the sale has a predetermined stopping count. That is the denominator field to recover; chance-number maxima remain invalid as sold-count proxies.

## Branch disposition

- `Biletini Yoxla` remains a valid secondary lead but is **bounded** until one of the following materially new artifacts appears: paired ticket+chance screenshot/receipt, public POS ticket, static bundle/API schema, or safe runtime/network capture.
- Do not submit guessed/public chance numbers.
- Do not infer cap from chance-number magnitude.
- Continue primary search for exact `remaining` / `total` / cap fields for draw/category-scoped `10066 Silver` and `10072 S25`.

## N constraint

No portfolio-size restriction was introduced. **N remains a free integer optimization variable.**
