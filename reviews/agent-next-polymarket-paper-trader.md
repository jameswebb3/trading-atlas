# Polymarket Paper Trader — Are probability scores based on settled outcomes

**Decision question:** Are probability scores based on settled outcomes?

| Field | Review |
| --- | --- |
| Upstream | [Polymarket Paper Trader](https://github.com/agent-next/polymarket-paper-trader) |
| Primary area | Agents & Decision Systems |
| Source commit | [bc41379780268433141aefc8ae822d49610a2fe8](https://github.com/agent-next/polymarket-paper-trader/commit/bc41379780268433141aefc8ae822d49610a2fe8) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/agent-next/polymarket-paper-trader/blob/bc41379780268433141aefc8ae822d49610a2fe8/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Useful for inspecting probability-score definitions. Separate settled outcomes from price proxies before interpreting benchmark accuracy or claims of beating the market. |

## Project overview

A prediction-market paper trader with probability and trading benchmarks. [Project documentation](https://github.com/agent-next/polymarket-paper-trader/blob/bc41379780268433141aefc8ae822d49610a2fe8/benchmark/README.md).

## Mechanism worth inspecting

The benchmark distinguishes probability scoring from trading results. Its [Brier calculation](https://github.com/agent-next/polymarket-paper-trader/blob/bc41379780268433141aefc8ae822d49610a2fe8/benchmark/pm_benchmark/scoring.py#L75-L91) accepts outcome proxies, while the [relative score](https://github.com/agent-next/polymarket-paper-trader/blob/bc41379780268433141aefc8ae822d49610a2fe8/benchmark/pm_benchmark/scoring.py#L126-L142) compares model and market mean squared errors.

## Important limit

For unresolved markets, the [benchmark documentation](https://github.com/agent-next/polymarket-paper-trader/blob/bc41379780268433141aefc8ae822d49610a2fe8/benchmark/README.md#L85-L88) uses prices as outcome proxies. Agreement with a market price is different from predicting the eventual outcome.

## Questions to take into your own design

- Are probability scores based on settled outcomes?
- Are unresolved price proxies excluded from accuracy against final outcomes?

## Why this score for a trading system

2/5: a relevant scoring lesson, but the unresolved-market proxy cannot establish forecasting accuracy against final outcomes.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
