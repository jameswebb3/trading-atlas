# Eiten — Added returns are not compounded wealth

**Decision question:** What does the plotted cumulative return represent?

| Field | Review |
| --- | --- |
| Upstream | [Eiten](https://github.com/tradytics/eiten) |
| Primary area | Backtesting & Simulation |
| Source commit | [44536c58887833b7b9bbcb30f2a270db2c712ea6](https://github.com/tradytics/eiten/commit/44536c58887833b7b9bbcb30f2a270db2c712ea6) |
| Reviewed | 2026-09-27 |
| Declared license | [GPL-3.0](https://github.com/tradytics/eiten/blob/44536c58887833b7b9bbcb30f2a270db2c712ea6/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The backtester computes percentage changes, multiplies them by portfolio weights and plots their cumulative sum. The inspected cumulative series is additive, not compounded portfolio wealth. |

## Project overview

Portfolio examples using eigen portfolios, minimum variance, Sharpe optimization and stock-price histories. [Documentation](https://github.com/tradytics/eiten/blob/44536c58887833b7b9bbcb30f2a270db2c712ea6/README.md).

## Mechanism worth inspecting

The backtester computes percentage changes, multiplies them by portfolio weights and plots their cumulative sum. [Source](https://github.com/tradytics/eiten/blob/44536c58887833b7b9bbcb30f2a270db2c712ea6/backtester.py#L24-L65).

## Important limit

The inspected cumulative series is additive, not compounded portfolio wealth. In the long-only path, clipped weights also need their own normalization policy before the curve can represent an investable portfolio. [Evidence 1](https://github.com/tradytics/eiten/blob/44536c58887833b7b9bbcb30f2a270db2c712ea6/backtester.py#L24-L65). [Evidence 2](https://github.com/tradytics/eiten/blob/44536c58887833b7b9bbcb30f2a270db2c712ea6/backtester.py#L95-L115).

## Questions to take into your own design

- Is the curve additive P&L, percentage-point sum or compounded wealth?
- Do transformed portfolio weights still satisfy the intended exposure budget?

## Why this score for a trading system

A readable example of accounting assumptions worth challenging; the inspected curve is not sufficient portfolio performance evidence.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
