# Backtrader: partial fills are explicit only when a filler is supplied

**Decision question:** Does a bar-based broker model preserve a partly filled order?

| Field | Review |
| --- | --- |
| Upstream | [Backtrader](https://github.com/mementum/backtrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [b853d7c90b6721476eb5a5ea3135224e33db1f14](https://github.com/mementum/backtrader/commit/b853d7c90b6721476eb5a5ea3135224e33db1f14) |
| Reviewed | 2026-09-25 |
| Declared license | [GPL-3.0](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/LICENSE#L1-L4) |
| Review depth | 2/3: README, broker, and order implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its broker can use a volume filler to size each bar execution and carries the remaining quantity into a Partial or Completed order state. With no filler, the broker takes the entire remaining size on an eligible execution. This is a useful explicit modeling boundary, not evidence of exchange-level fill realism. |

## Mechanism worth inspecting

The [README](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/README.rst#L80-L99) lists replay, order types, slippage, volume filling, and future-like cash adjustment. The [broker filler contract](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L98-L119) receives the order, execution price, and bar index. The [execution branch](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L687-L700) uses the remaining size when no filler is installed, otherwise the filler result. The [order record](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/order.py#L35-L59) captures execution pieces; [status transitions](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/order.py#L566-L580) distinguish remaining quantity from completion.

## Important limit

A filler's behavior is user-supplied, and OHLCV bars do not prove queue position, exchange acceptance, or true partial-fill probability. The broker also offers [cheat-on-open and cheat-on-close modes](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/README.rst#L92-L99), so timing configuration matters. The repository has GPL-3.0 terms and had not been pushed since 2024 at review time.

## Questions to take into your own design

- Which fill-size rule is active for each reported backtest?
- Does any default silently turn a plausible partial fill into full execution?
- Are simulated order states compared with venue event traces?

## Why this score for a trading system

Its configurable partial-fill path and remaining-size state are directly relevant to execution simulation, while bar volume and user-supplied filler logic limit venue fidelity.

**Scope of this review:** We read the pinned README and selected broker and order code. We did not run the broker, inspect every filler, or validate Hyperliquid behavior.
