# TradingAgents A-Stock — Can an agent use today's snapshot in a historical report

**Decision question:** Can an agent use today's snapshot in a historical report?

| Field | Review |
| --- | --- |
| Upstream | [TradingAgents A-Stock](https://github.com/simonlin1212/TradingAgents-astock) |
| Primary area | Agents & Decision Systems |
| Source commit | [b0594a4f2b8ff7c32807ebc9ec269007fffe895c](https://github.com/simonlin1212/TradingAgents-astock/commit/b0594a4f2b8ff7c32807ebc9ec269007fffe895c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/simonlin1212/TradingAgents-astock/blob/b0594a4f2b8ff7c32807ebc9ec269007fffe895c/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Makes current-versus-historical data limitations visible. For causal historical research, reject ineligible snapshots at the data boundary rather than relying on a prose warning to the agent. |

## Project overview

An A-share adaptation of TradingAgents with local market-data sources and specialist research roles. [Project documentation](https://github.com/simonlin1212/TradingAgents-astock/blob/b0594a4f2b8ff7c32807ebc9ec269007fffe895c/CHANGES_FROM_UPSTREAM.md).

## Mechanism worth inspecting

The [data adapter](https://github.com/simonlin1212/TradingAgents-astock/blob/b0594a4f2b8ff7c32807ebc9ec269007fffe895c/tradingagents/dataflows/a_stock.py#L209-L237) detects historical analysis dates and produces a snapshot warning. [Fundamental retrieval](https://github.com/simonlin1212/TradingAgents-astock/blob/b0594a4f2b8ff7c32807ebc9ec269007fffe895c/tradingagents/dataflows/a_stock.py#L982-L1017) prepends that warning but still includes current valuation fields.

## Important limit

The warning describes a timing problem; it does not remove the current values or enforce point-in-time eligibility. A model can still receive data unavailable on the historical decision date.

## Questions to take into your own design

- Can an agent use today's snapshot in a historical report?
- Are current-only endpoints refused when a historical decision date is requested?

## Why this score for a trading system

2/5: a concrete timing caution, but the inspected historical-report path still carries current valuation data.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
