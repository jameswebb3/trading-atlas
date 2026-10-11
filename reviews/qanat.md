# Qanat: report flat periods alongside held-period performance

**Decision question:** Can a backtest distinguish total elapsed periods from periods with portfolio exposure?

| Field | Review |
| --- | --- |
| Upstream | [Qanat](https://github.com/fidetolabs/qanat) |
| Primary area | Backtesting & Simulation |
| Source commit | [05799e6acb3a1e557acb71a70da0c13832f2c10f](https://github.com/fidetolabs/qanat/commit/05799e6acb3a1e557acb71a70da0c13832f2c10f) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/fidetolabs/qanat/blob/05799e6acb3a1e557acb71a70da0c13832f2c10f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Replays table-based research pipelines and reports both held and flat periods. Its totals separate compounded portfolio return from additive attribution and show held-period hit rates alongside all-period metrics, preserving the denominator behind each headline. |

## Project overview

A beta research engine transforms raw data through inspectable tables into portfolio weights. [Project documentation](https://github.com/fidetolabs/qanat/blob/05799e6acb3a1e557acb71a70da0c13832f2c10f/README.md#L28-L44).

## Mechanism worth inspecting

The [backtest documentation](https://github.com/fidetolabs/qanat/blob/05799e6acb3a1e557acb71a70da0c13832f2c10f/docs/backtest.md#L69-L80) explains exposure denominators. [totals_of](https://github.com/fidetolabs/qanat/blob/05799e6acb3a1e557acb71a70da0c13832f2c10f/src/qanat/backtest.py#L355-L399) compounds every period, separately sums attribution, and returns held/flat counts plus both hit rates.

## Important limit

A held-period subset answers a different question from the full elapsed investment return. [Zero held periods](https://github.com/fidetolabs/qanat/blob/05799e6acb3a1e557acb71a70da0c13832f2c10f/src/qanat/backtest.py#L394-L395) yield numeric zeros rather than an undefined-value marker. The broader documentation claims point-in-time views, but that enforcement was not audited in this focused accounting review.

## Questions to take into your own design

- Are flat exposure periods visible next to every held-only statistic?
- Do compounded portfolio return and additive cost attribution reconcile under their distinct definitions?

## Why this score for a trading system

3/5: directly useful accounting and denominator source; broader replay guarantees and beta readiness are not established by this review.

**Scope of this review:** README, full replay documentation, totals accounting source.
