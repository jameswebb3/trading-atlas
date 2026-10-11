# FinanceToolkit — Drawdown depends on the initial wealth

**Decision question:** Can the first loss disappear from a drawdown series?

| Field | Review |
| --- | --- |
| Upstream | [FinanceToolkit](https://github.com/JerBouma/FinanceToolkit) |
| Primary area | Portfolio & Risk |
| Source commit | [9fa19f9e97fee229dad4d65cf9c1448597af5df5](https://github.com/JerBouma/FinanceToolkit/commit/9fa19f9e97fee229dad4d65cf9c1448597af5df5) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/JerBouma/FinanceToolkit/blob/9fa19f9e97fee229dad4d65cf9c1448597af5df5/LICENSE.txt) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The return-based drawdown method fills missing returns with zero, compounds them and divides by the running maximum of that computed wealth series. The inspected branch does not prepend initial wealth of one. |

## Project overview

Python toolkit with inspectable formulas for financial ratios, performance and risk measures. [Documentation](https://github.com/JerBouma/FinanceToolkit/blob/9fa19f9e97fee229dad4d65cf9c1448597af5df5/README.md).

## Mechanism worth inspecting

The return-based drawdown method fills missing returns with zero, compounds them and divides by the running maximum of that computed wealth series. [Source](https://github.com/JerBouma/FinanceToolkit/blob/9fa19f9e97fee229dad4d65cf9c1448597af5df5/financetoolkit/risk/risk_model.py#L17-L72).

## Important limit

The inspected branch does not prepend initial wealth of one. A loss in the first return can therefore become the initial peak; filling missing returns with zero also chooses an economic assumption. [Evidence 1](https://github.com/JerBouma/FinanceToolkit/blob/9fa19f9e97fee229dad4d65cf9c1448597af5df5/financetoolkit/risk/risk_model.py#L17-L72).

## Questions to take into your own design

- Does a one-period loss produce drawdown relative to initial capital?
- Are missing returns unknown, or explicitly proven to represent no change?

## Why this score for a trading system

Directly relevant metric semantics, with two visible boundary choices to test; this review does not assess the toolkit's other formulas.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
