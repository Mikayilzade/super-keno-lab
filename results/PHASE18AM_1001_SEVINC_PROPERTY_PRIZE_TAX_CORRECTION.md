# Phase 18AM — `1001 Sevinc` property-prize tax correction

Date: 2026-08-27

Status: **IMPORTANT MODEL CORRECTION; NO +EV CLAIM**

## New tax evidence

The Azerbaijan State Tax Service states that lottery winnings paid in **property / non-cash form** are treated as non-business income. After deducting the participation cash outlay, the remaining amount is taxed at **14%** under the cited rules. The separate 500-AZN exemption discussed for lottery winnings applies to **cash-form** winnings.

Sources checked 2026-08-27:
- https://taxes.gov.az/az/page/suallar-ve-cavablar?page=27
- https://taxes.gov.az/az/page/suallar-ve-cavablar?page=45

This materially changes the finite-pool EV model for physical prizes such as phones/consoles and likely any non-cash gift coupon unless the operator documents a different tax treatment for that coupon.

## Corrected prize-value model

For a property prize with assessed value `V` and one winning ticket costing `p`, approximate after-tax value before resale/usage haircut is:

`V_after_tax = V - 0.14 * (V - p)`

For resale/usage haircut `h`, a conservative economic-value model is:

`V_economic = h * V - 0.14 * (V - p)`

This is deliberately stricter than applying 14% only after the haircut, because the tax base may follow assessed prize value while resale/use value can be lower.

If sold fraction is `s` and total predetermined cap is `C`, sold tickets are approximately `M = s*C`, and break-even cap is:

`C_break_even = V_economic / (p*s)`

## Recalculated live cap ceilings

Using the latest current-cycle sold fractions already captured in STATUS.md:

### 1000-AZN gift coupon — ticket 0.5 AZN — sold 17%

Assuming the coupon is treated as a non-cash/property prize for tax purposes:

| usable-value fraction | economic value after 14% tax on assessed 1000 AZN | break-even cap |
|---:|---:|---:|
| 60% | 460.07 AZN | **5,413** |
| 70% | 560.07 AZN | **6,589** |
| 80% | 660.07 AZN | **7,766** |
| 100% | 860.07 AZN | **10,118** |

Previous untaxed ceilings `7,059 / 8,235 / 9,412 / 11,765` were too optimistic for a property-prize tax regime and must not be used for execution.

### iPhone 17 Pro 256 GB Cosmic Orange — ticket 1 AZN — sold 43%

Using current 3,289-AZN retail benchmark and no resale haircut yet:

- after-tax value ≈ **2,828.68 AZN**;
- break-even cap ≈ **6,578 tickets** at full-value use.

Any resale/usage haircut lowers this ceiling further. Previous full-retail untaxed ceiling ~7,649 was too optimistic.

### PlayStation 5 Slim 1 TB — ticket 0.5 AZN — sold 55%

Using current ~1,449.99-AZN retail benchmark and no resale haircut yet:

- after-tax value ≈ **1,247.06 AZN**;
- break-even cap ≈ **4,535 tickets** at full-value use.

Previous full-retail untaxed ceiling ~5,273 was too optimistic.

## Important uncertainty — gift coupon classification

The `1000 AZN-lik hədiyyə kuponu` may be legally/tax-operationally treated as property, voucher, or cash-equivalent by the operator. Until first-party terms or a tax receipt from this exact prize type establish otherwise, use the **14% property-prize model as the conservative default**.

## Decision

The `1001 Sevinc` finite-pool route remains open, but all live ROI calculations must now include prize-form-specific tax before declaring +EV.

The 1000-AZN coupon remains the highest-information denominator target, but its conservative cap tolerance is lower than previously recorded. No purchase should be justified from sold percentage alone.

## Next action

1. Recover exact `cap / remaining / sold count` for the current 1000-AZN coupon first, Cosmic Orange second.
2. Seek first-party evidence on whether the gift coupon is taxed/settled as property or cash-equivalent.
3. For physical prizes, use the 14% property-prize tax model before resale haircuts.
4. If denominator is recovered, compute live ROI under multiple assessed-value and resale-friction scenarios before any execution claim.
