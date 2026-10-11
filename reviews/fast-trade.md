# Fast Trade: metric names do not establish metric definitions

**Decision question:** Can a report's max_drawdown field mean minimum equity rather than a drawdown percentage?

| Field | Review |
| --- | --- |
| Upstream | [Fast Trade](https://github.com/jrmeier/fast-trade) |
| Primary area | Backtesting & Simulation |
| Source commit | [e4b1ddd6c8eb140fe519dfbd4c916531b4b89634](https://github.com/jrmeier/fast-trade/commit/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Offers fast dataframe backtests with unusually explicit metric documentation. The inspected report distinguishes a conventional nested drawdown calculation from a top-level field named max_drawdown that actually stores minimum equity, making metric semantics essential before comparison. |

## Project overview

A Polars-based library runs trading backtests and stores compatible market datasets. [Project documentation](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/README.md#L8-L25).

## Mechanism worth inspecting

The [metric documentation](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/docs/METRICS.md#L6-L51) explains its nonstandard return, Sharpe, and top-level drawdown meanings. [Summary construction](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/fast_trade/build_summary.py#L48-L54) sets max_drawdown to minimum equity, while [nested drawdown metrics](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/fast_trade/summary/metrics.py#L67-L90) calculate equity relative to its running peak.

## Important limit

A named field cannot safely be compared across engines without its units and formula. Separately, [rule evaluation](https://github.com/jrmeier/fast-trade/blob/e4b1ddd6c8eb140fe519dfbd4c916531b4b89634/fast_trade/evaluate.py#L63-L76) catches errors without appending failed results; a mixed set can report all successful evaluated rules while omitting an errored rule. This review does not verify claimed performance benchmarks.

## Questions to take into your own design

- Does each exported metric include its formula, units, and annualization basis?
- Do failed evaluations remain visible in the decision denominator?

## Why this score for a trading system

2/5: useful documentation and concrete metric-audit examples, with nonstandard headline definitions and an inspected rule-evidence gap.

**Scope of this review:** README, full metric documentation, summary/drawdown code, and rule evaluator.
