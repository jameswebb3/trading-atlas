# QSTrader — How does a target portfolio account for cash, fees and indivisible units

**Decision question:** How does a target portfolio account for cash, fees and indivisible units?

| Field | Review |
| --- | --- |
| Upstream | [QSTrader](https://github.com/mhallsmoore/qstrader) |
| Primary area | Portfolio & Risk |
| Source commit | [4c59e1584e83fcc2be644b820f827c0dd1b45c02](https://github.com/mhallsmoore/qstrader/commit/4c59e1584e83fcc2be644b820f827c0dd1b45c02) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes the path from portfolio weights to affordable order quantities inspectable: buffer, fees, ask price and rounding. This sizer's long-only, integral-unit assumptions require adaptation for derivatives. |

## Project overview

A modular, schedule-driven backtesting framework originally aimed at systematic long-short equities and ETF strategies. [Project documentation](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/README.md#L10-L16).

## Mechanism worth inspecting

The inspected dollar-weighted order sizer reserves a cash buffer, normalizes nonnegative weights, estimates broker costs and floors the resulting quantity using the latest ask price. It rejects NaN prices. [Weight contract](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/order_sizer/dollar_weighted.py#L82-L113); [sizing path](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/order_sizer/dollar_weighted.py#L132-L179).

## Important limit

This particular sizer is long-only and assumes integral units; its estimated quantity is a TODO placeholder when computing fees. Those assumptions do not directly describe leveraged perpetual contracts. [Fee estimate and quantity calculation](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/order_sizer/dollar_weighted.py#L151-L174).

## Questions to take into your own design

- After rounding and estimated fees, does the target still satisfy its budget?
- Are price validity and contract quantity rules checked before sizing?

## Why this score for a trading system

3/5: relevant portfolio-to-order mechanics, constrained by this implementation's equity and fee-estimation assumptions.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
