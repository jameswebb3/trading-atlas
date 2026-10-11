# NumPy Financial — Can the same cash-flow sequence have more than one internal rate of return

**Decision question:** Can the same cash-flow sequence have more than one internal rate of return?

| Field | Review |
| --- | --- |
| Upstream | [NumPy Financial](https://github.com/numpy/numpy-financial) |
| Primary area | Portfolio & Risk |
| Source commit | [22c29b4ad61a5e413d4858e46e3f26f55ebdf328](https://github.com/numpy/numpy-financial/commit/22c29b4ad61a5e413d4858e46e3f26f55ebdf328) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/numpy/numpy-financial/blob/22c29b4ad61a5e413d4858e46e3f26f55ebdf328/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Makes multiple-root IRR selection explicit rather than treating the reported rate as uniquely determined. Useful when separating investor cash-flow returns from strategy performance, with an indirect fit for trade execution. |

## Project overview

A collection of elementary financial functions replacing the former NumPy financial-function module. [Project documentation](https://github.com/numpy/numpy-financial/blob/22c29b4ad61a5e413d4858e46e3f26f55ebdf328/README.md#L3-L10).

## Mechanism worth inspecting

The IRR routine constructs real roots, excludes rates below minus one and invokes a selection function when several roots remain. The default selector applies a sign filter and then chooses the smallest magnitude. [Root handling](https://github.com/numpy/numpy-financial/blob/22c29b4ad61a5e413d4858e46e3f26f55ebdf328/numpy_financial/_financial.py#L1152-L1168); [default selection](https://github.com/numpy/numpy-financial/blob/22c29b4ad61a5e413d4858e46e3f26f55ebdf328/numpy_financial/_financial.py#L997-L1014).

## Important limit

One reported IRR can therefore contain a selection-policy decision. It is not interchangeable with time-weighted strategy return, realised trading PnL or a funding-adjusted perpetual-contract ledger.

## Questions to take into your own design

- Are external deposits and withdrawals separated from trading gains?
- Is the root-selection policy disclosed when several IRRs exist?

## Why this score for a trading system

2/5: a relevant reporting caution only when deposits and withdrawals require a cash-flow return measure.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
