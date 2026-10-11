# AI-Trader — Which market assumptions are hidden in a convenient backtest helper

**Decision question:** Which market assumptions are hidden in a convenient backtest helper?

| Field | Review |
| --- | --- |
| Upstream | [AI-Trader](https://github.com/whchien/ai-trader) |
| Primary area | Backtesting & Simulation |
| Source commit | [7681fe331fb638beab1ae20d3552c802bbaa9174](https://github.com/whchien/ai-trader/commit/7681fe331fb638beab1ae20d3552c802bbaa9174) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/whchien/ai-trader/blob/7681fe331fb638beab1ae20d3552c802bbaa9174/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A simple reference for explicit configuration around Backtrader. Its default commission and daily feed need a deliberate execution profile before results can guide another market. |

## Project overview

A configuration-driven Backtrader project with strategies, utility functions and an MCP interface. [Project documentation](https://github.com/whchien/ai-trader/blob/7681fe331fb638beab1ae20d3552c802bbaa9174/docs/MIGRATION_GUIDE.md).

## Mechanism worth inspecting

The [broker helper](https://github.com/whchien/ai-trader/blob/7681fe331fb638beab1ae20d3552c802bbaa9174/ai_trader/utils/backtest.py#L21-L44) exposes starting cash and a commission rate whose default is documented for Taiwan equities. The [data helper](https://github.com/whchien/ai-trader/blob/7681fe331fb638beab1ae20d3552c802bbaa9174/ai_trader/utils/backtest.py#L47-L95) constructs a daily PandasData feed.

## Important limit

The inspected convenience path does not establish funding, derivatives margin, queue priority or calibrated fills. Multi-market labels do not remove the broker and feed assumptions.

## Questions to take into your own design

- Which market assumptions are hidden in a convenient backtest helper?
- Does every backtest record the actual feed timeframe and complete cost profile?

## Why this score for a trading system

2/5: relevant backtest wiring, but limited new value beyond an existing simulator and no inspected derivatives execution contract.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
