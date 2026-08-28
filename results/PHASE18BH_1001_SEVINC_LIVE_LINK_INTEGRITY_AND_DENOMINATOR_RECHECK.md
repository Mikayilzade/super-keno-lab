# Phase 18BH — live draw-link integrity + denominator recheck

Date: 2026-08-28

## Status

Not yet success. No absolute `cap / remaining / sold-count` was recovered for current `1001 Sevinc` draws in this batch.

## Meaningful new result

A same-day fresh first-party crawl of the current `1001 Sevinc` parent page was used as a rendered-link integrity check rather than another generic API/search attempt.

The live page still exposes 11 cards for 16.09.2026 in the established order: 3 cards at 1 AZN followed by 8 cards at 0.5 AZN. Clicking the third 1-AZN card resolves directly to:

`https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10066`

Clicking the first 0.5-AZN card resolves directly to:

`https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10072`

This independently reconfirms that the currently rendered card positions themselves still point to `10066` and `10072`; the earlier recovered link order has not drifted in the live 16.09.2026 cycle.

Sources checked on 2026-08-28:
- https://www.azerlotereya.com/lotereya/1001-sevinc
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10066
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10072

## Denominator result

Both detail links still render only the client shell (`Tirajlar / Biletlərim / Tiraj nəticələri`) to the public crawler. No `cap`, absolute sold count, or `remaining` value is present in the rendered HTML. Therefore no live ROI decision can be promoted in this batch.

This is not treated as reopening the exhausted generic client/API branch: the purpose was a current-cycle link-integrity check on the two highest-priority bound targets. Repeating the same direct detail-page crawl is now unnecessary until the rendered surface materially changes.

## Execution state

- `10066 Silver` remains target #1 because it is fully bound and the last complete first-party sold input remains 33%.
- `10072 S25 Ultra Black` remains target #2; the draw-link is live and stable, but fresh complete sold% is still unresolved.
- No autonomous purchase/probe was executed.
- Super Keno portfolio size `N` remains a free integer.

## Next action

1. Do not repeat direct public detail-page crawls for `10066/10072` unless the rendered surface changes materially.
2. Seek a genuinely new account/rendered artifact exposing `remaining`, `cap`, or absolute sold tickets for either draw.
3. Reacquire S25 sold% only from a newly dated/current complete card or other bound artifact.
4. If any sequential sold-% observations around known ticket additions become available, run `scripts/phase18bg_percent_transition_cap_solver.py` immediately.
5. Continue only genuinely new zero-cost Super-Keno modifier scans with explicit `Lotereya` scope.
