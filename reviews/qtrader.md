# Sharing strategy code does not mean sharing execution behavior

**Decision question:** What does a backtest gateway assume when it fills an order?

| Field | Review |
| --- | --- |
| Upstream | [QTrader](https://github.com/josephchenhk/qtrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [209f96b8122e7a7fc18de611c821ef4d7f64ba56](https://github.com/josephchenhk/qtrader/commit/209f96b8122e7a7fc18de611c821ef4d7f64ba56) |
| Reviewed | 2026-09-26 |
| Declared license | [Unclear: README badge says JXW; no root license file](https://github.com/josephchenhk/qtrader/blob/209f96b8122e7a7fc18de611c821ef4d7f64ba56/README.md#L8) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The backtest gateway marks orders fully filled immediately; limit orders receive their requested price without a crossing check in this method. Market orders can fall back to cached bars. This is a useful counterexample to treating a shared live/backtest API as proof of realistic execution. |

## Mechanism worth inspecting

The [README](https://github.com/josephchenhk/qtrader/blob/209f96b8122e7a7fc18de611c821ef4d7f64ba56/README.md#L19-L28) promises the same strategy code across modes; the [test setup guide](https://github.com/josephchenhk/qtrader/blob/209f96b8122e7a7fc18de611c821ef4d7f64ba56/tests/README.md#L1-L5) documents gateway configuration. The [placement method](https://github.com/josephchenhk/qtrader/blob/209f96b8122e7a7fc18de611c821ef4d7f64ba56/qtrader/gateways/backtest/backtest_gateway.py#L410-L445) assigns full quantity, uses the limit price directly, and selects recent or cached closes for market prices.

## Important limit

This is the inspected gateway's explicit simulation model, not proof of how a separate live connector behaves. Core engine files are compiled artifacts in this tree, so the engine's full control flow was not inspected. License rights remain unclear.

## Questions to take into your own design

- Can an unmarketable limit order remain open in the simulation?
- Is every market-fill price qualified as available at the order's decision time?

## Why this score for a trading system

2/5: The gateway provides a precise caution about optimistic fill models, but compiled core components and unclear licensing prevent a stronger engineering recommendation.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
