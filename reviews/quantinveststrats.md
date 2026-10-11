# QuantInvestStrats: keep decision dates separate from traded dates

**Decision question:** Does a target allocation become a position before it could have been acted on?

| Field | Review |
| --- | --- |
| Upstream | [QuantInvestStrats (qis)](https://github.com/ArturSepp/QuantInvestStrats) |
| Primary area | Portfolio & Risk |
| Source commit | [2a925bb9dfd3387268a169d180cf88dea6ededbf](https://github.com/ArturSepp/QuantInvestStrats/commit/2a925bb9dfd3387268a169d180cf88dea6ededbf) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/LICENSE.txt) |
| Review depth | 3/3: documentation, relevant source, and focused regression tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Maps dated allocation decisions onto executable price observations and rejects negative implementation lags or colliding trade dates. Useful for portfolio accounting; interior price gaps still require an explicit marking policy, and this is not an exchange fill simulator. |

## Project overview

Portfolio analytics and backtesting library that turns prices and target weights into holdings, costs, and performance reports. Makes allocation timing and weight drift explicit.

[Project documentation](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/README.md#L24-L37).

## Mechanism worth inspecting

The [overview](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/README.md#L24-L33) and [portfolio guide](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/docs/portfolio_backtesting.md#L16-L50) distinguish target weights from held units and drifting realised weights. The [backtester](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/src/qis/portfolio/backtester.py#L149-L174) validates the lag and warns about interior missing prices. Its [date mapping](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/src/qis/portfolio/backtester.py#L187-L215) moves targets to the first price observation on or after the decision date, adds the lag, and rejects multiple decisions mapping to the same trade date. [Focused tests](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/src/qis/portfolio/tests/backtester_negative_lag_test.py#L38-L59) exercise the negative-lag boundary.

## Important limit

Zero lag is permitted. Correct decision timestamps therefore remain the caller's responsibility. The [implementation](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/src/qis/portfolio/backtester.py#L160-L174) warns that a held leg with an interior NaN drops out of NAV on that date; it does not reject that input. The [guide](https://github.com/ArturSepp/QuantInvestStrats/blob/2a925bb9dfd3387268a169d180cf88dea6ededbf/docs/portfolio_backtesting.md#L52-L63) describes funded-holdings accounting and leaves derivative conventions to supplied inputs. Neither a mapped price nor a cost rate proves fillability.

## Questions to take into your own design

- Are signal availability, decision time, and execution time stored separately?
- Should an unpriceable held position stop valuation, use an explicitly stale mark, or be reported as unknown?

## Why this score for a trading system

4/5: directly useful accounting and causal-timing checks, supported by implementation and targeted test code. Zero-lag inputs and permissive missing-price handling prevent treating the backtester as a complete execution or data-validity gate.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
