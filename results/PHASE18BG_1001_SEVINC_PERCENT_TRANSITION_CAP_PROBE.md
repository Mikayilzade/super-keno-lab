# Phase 18BG — 1001 Sevinc percentage-transition cap inference

Date: 2026-08-28

## Status

Not yet success. No absolute `cap / remaining / sold-count` was recovered for current draws in this batch.

## New result

The official 1001 Sevinc explainer explicitly states that users can see how many tickets remain until the draw in the Azerlotereya/Misli 1001 Sevinc section. Public crawlers still expose only integer `Satıldı %` for selected cards and not the absolute remaining count.

A materially different fallback route is now formalized: infer the hidden total cap `C` from **controlled percentage transitions** rather than from API discovery.

Let:
- `C` = predetermined ticket cap,
- `M` = tickets sold before observation,
- `k` = known cumulative tickets added during a tightly controlled observation window,
- displayed percentage = integer function of `100*M/C`.

For floor display, a visible `p%` implies:

`ceil(p*C/100) <= M <= ceil((p+1)*C/100)-1`.

After a known controlled increment `k`, intersect the corresponding integer interval for `M+k`. Multiple before/after/no-change observations can sharply restrict feasible `C` values.

Example: if a card remains at 33% through cumulative +49 tickets, changes to 34% at +50, remains 34% through +99, then changes to 35% at +100, the floor model constrains `C` to a narrow band around ~5k rather than leaving it unbounded. The exact solver is committed as `scripts/phase18bg_percent_transition_cap_solver.py`.

## Important limitations

- A single 33% -> 34% transition is not enough to identify an upper cap because the initial sold count can be anywhere inside the displayed 33% bucket.
- The useful information comes from the **last no-change point plus first change point for two consecutive percentage boundaries**.
- External purchases during the probe contaminate exact inference. The observation window would need to be short, and the solver should then be treated as a bound rather than exact recovery.
- Display rounding mode is not yet proven. The solver supports both `floor` and half-up `nearest` models; execution requires consistency under both or independent proof of the UI rule.
- This route requires paid ticket additions if used actively. No purchase was made and no autonomous spend is authorized by this research batch.

## Why this matters

The main blocker is no longer purely "find an undocumented API". Even if absolute remaining stays account-only, the visible integer sold percentage contains enough information to recover/strongly bound cap if controlled transitions can be observed.

For current priority `drawId=10066 Silver`, the execution question remains whether cap is below the already-calculated break-even ceilings. A recovered cap around 5k would materially change the decision; a cap materially above ~8.2k would kill Silver even under the 100% usable-value ceiling at the current 33% snapshot.

## Current web check

Fresh public first-party surfaces on 2026-08-28 still show the current 16.09.2026 cycle as 11 draws (3 x 1 AZN and 8 x 0.5 AZN), but no new public absolute denominator appeared in this batch. A fresh Super-Keno modifier scan also found no new zero-cost offer explicitly proving current `Lotereya` eligibility.

## Next action

1. Continue waiting for a materially new account/rendered artifact that exposes absolute remaining/cap directly for `10066` or `10072`.
2. Keep the percentage-transition solver ready as a fallback denominator-recovery method; do not execute paid probes autonomously.
3. If a user-visible/account screenshot or other artifact provides sequential sold-% observations around actual purchases, feed them into the solver immediately.
4. Preserve free integer `N`; no change to Super-Keno portfolio optimization state.
