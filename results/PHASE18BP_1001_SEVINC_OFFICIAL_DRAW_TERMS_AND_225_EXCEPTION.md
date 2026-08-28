# PHASE 18BP — 1001 Sevinc official draw-terms artifact and §2.2.5 exception reassessment

Date: 2026-08-28

## Result

Not yet success: no absolute ticket cap/remaining count was recovered for draw 10066 or 10072. However, this batch found a materially new first-party PDF in Azerlotereya's legislation/static namespace whose text describes the operating terms for property-prize draws and materially changes the registration-316 denominator strategy.

Source artifact:

`https://st.azerlotereya.com/public/Data/Files/Legislation/Documents/PG/mu/NM/SQ/9_4a76908c-c0ba-436b-89d7-c1f31937bebf.pdf`

The PDF is titled/introduced as `Tiraj açıqlamaları` and states, among other things:

- ticket price may vary by prize category;
- tickets sold through all channels participate in formation of the prize fund for the corresponding prize category;
- the lottery prize fund is formed from goods/items;
- the value of each prize is at least 50% of the total amount of tickets sold in that prize category;
- if tickets sell before the intended end of sales, the draw may be brought forward;
- tickets for each draw/prize category are printed/generated only for that category, and a ticket can participate only in that draw/category period;
- each prize corresponds to one ticket;
- property-prize tax is stated as 14% after subtracting the player's cash stake from the prize value.

## Why this matters

### 1. The §2.2.5 exception is now a serious/default interpretation, not a remote caveat

Earlier phases relied on the 2019 rule that registered lottery conditions contain ticket quantity/numbers except where the prize-fund amount depends on sold-ticket amount. This PDF says directly that sold tickets participate in formation of the category prize fund and links each prize value to the total amount of tickets sold in that category (minimum 50%).

Therefore we must no longer assume that registration package 316 is legally required to expose a fixed absolute ticket quantity/range. The registration-document hunt can continue, but its expected value as the primary denominator route is reduced.

This is a correction to the earlier working assumption that fixed physical goods likely implied the sold-dependent exception would not apply.

### 2. Finite-pool behavior still appears real

The same official terms explicitly contemplate tickets being fully sold before the planned sales-end date and moving the draw earlier. The current 1001 Sevinc page also says the draw can be brought forward when tickets are sold early. So there is still an operational finite-pool/end-of-sales mechanism even though the registered legal terms may not disclose the cap.

### 3. Denominator scope is category + draw period

The PDF states that tickets are generated/printed for the corresponding prize category and that each ticket participates only in that category and draw period. This supports binding any recovered denominator to `(drawId, prize category, draw period)`, not to the entire 1001 Sevinc game globally.

### 4. Tax model receives direct first-party support

The PDF explicitly describes property prizes as non-entrepreneurial income and gives 14% tax after subtracting ticket stake. This supports the repo's standing working tax formula, subject to prize-specific/legal changes.

## Evidence-confidence note

The PDF is first-party and highly relevant to 1001-Sevinc-like property draws. Search discovery linked it through the exact property-lottery terminology, but the rendered pages inspected in this batch did not expose a visible `registration 316` marker inside the PDF itself. Treat the linkage to registration 316 as `strongly relevant / not yet document-ID-proven`, while the mechanics stated in the PDF are usable as first-party evidence for the property-draw model.

## Branch decision

- **Downgrade** `registration 316 must contain absolute C` from high-confidence expectation to conditional/low expectation because the sold-dependent-fund exception is now materially supported.
- **Do not close** document metadata recovery completely: registration 316/amendments could still disclose issuance/count fields voluntarily or by category.
- **Promote** materially new account/rendered/POS observations of `remaining/total` and sequential sold-% transitions back to the strongest denominator routes.
- Do not repeat generic launch-media search or random UUID guessing.

## NEXT ACTION

1. Search for a direct metadata/page relation between this PDF (or sibling legislation documents) and `1001 Sevinc / 316` so the legal-document linkage can be made exact.
2. In parallel prioritize new rendered/account/POS evidence exposing remaining or total tickets for current `10066 Silver` / `10072 S25`.
3. If any `remaining`, `total`, or sequential percentage observations are found, bind them to exact draw/category/time and immediately compute cap/ROI with free integer N.
4. Keep operational-integrity status separate from mathematical ROI.
