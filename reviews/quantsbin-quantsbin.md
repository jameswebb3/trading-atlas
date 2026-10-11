# Quantsbin — Finite-difference bumps have units

**Decision question:** What does a numerical Greek's bump actually mean?

| Field | Review |
| --- | --- |
| Upstream | [Quantsbin](https://github.com/quantsbin/Quantsbin) |
| Primary area | Portfolio & Risk |
| Source commit | [362522653b4b8ebcf14461e3f44fe22dea465adc](https://github.com/quantsbin/Quantsbin/commit/362522653b4b8ebcf14461e3f44fe22dea465adc) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/quantsbin/Quantsbin/blob/362522653b4b8ebcf14461e3f44fe22dea465adc/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The numerical Greek calculator deep-copies the pricing engine into base, upward and downward variants. The inspected derivative division requires a nonzero change and, for relative bumps, a nonzero base. |

## Project overview

Python library for vanilla-option prices, numerical and analytic Greeks, and payoff analysis. [Documentation](https://github.com/quantsbin/Quantsbin/blob/362522653b4b8ebcf14461e3f44fe22dea465adc/README.md).

## Mechanism worth inspecting

The numerical Greek calculator deep-copies the pricing engine into base, upward and downward variants. It treats date shifts as days and first-derivative price bumps as a proportion of the base factor. [Source](https://github.com/quantsbin/Quantsbin/blob/362522653b4b8ebcf14461e3f44fe22dea465adc/quantsbin/derivativepricing/numericalgreeks.py#L1-L102).

## Important limit

The inspected derivative division requires a nonzero change and, for relative bumps, a nonzero base. Comparing Greeks without matching bump units can compare different quantities. [Evidence 1](https://github.com/quantsbin/Quantsbin/blob/362522653b4b8ebcf14461e3f44fe22dea465adc/quantsbin/derivativepricing/numericalgreeks.py#L1-L102).

## Questions to take into your own design

- Are bump size, units and derivative normalization recorded together?
- How are zero base values and zero bump requests rejected?

## Why this score for a trading system

Useful numerical boundary documentation for options-derived data, with a narrow implementation scope and no demonstrated forecasting value.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
