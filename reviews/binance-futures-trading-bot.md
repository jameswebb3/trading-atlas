# Binance Futures Trading Bot: audit cancel-all before installing protection

**Decision question:** Can a bot's protective-order setup cancel another strategy's orders?

| Field | Review |
| --- | --- |
| Upstream | [Binance Futures Trading Bot](https://github.com/conor19w/Binance-Futures-Trading-Bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7](https://github.com/conor19w/Binance-Futures-Trading-Bot/commit/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7) |
| Reviewed | 2026-09-26 |
| Declared license | [No license file identified](https://github.com/conor19w/Binance-Futures-Trading-Bot/blob/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7/README.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | Provides Binance futures strategy and execution examples. Its protective-order setup performs symbol-wide cancellation and suppresses cancellation errors before reading position size, a concrete order-ownership risk rather than a production execution pattern to adopt. |

## Project overview

A technical-indicator bot submits futures entries and protective orders. [Project documentation](https://github.com/conor19w/Binance-Futures-Trading-Bot/blob/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7/README.md#L2-L15).

## Mechanism worth inspecting

The [protective-order path](https://github.com/conor19w/Binance-Futures-Trading-Bot/blob/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7/TradeManager.py#L131-L147) cancels all open orders for a symbol, suppresses errors, reads the current position quantity, and then creates stop-loss and take-profit orders. [Configuration documentation](https://github.com/conor19w/Binance-Futures-Trading-Bot/blob/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7/LiveTradingConfig.py#L14-L27) exposes leverage, multiple positions, and candle completion.

## Important limit

Cancellation scope can include orders owned by another process. The cancel call and [subsequent position query](https://github.com/conor19w/Binance-Futures-Trading-Bot/blob/c7e7f1fa34d5ccf8ef0b686eeb6c01241cdaa4e7/TradeManager.py#L134-L140) also use different futures API families, which needs venue-specific verification. A cancellation failure is not surfaced as a blocking state in this function, and no license file was identified.

## Questions to take into your own design

- Does cancellation target only orders owned by this strategy and account mode?
- Is failed cancellation reconciled before replacement protection is submitted?

## Why this score for a trading system

1/5: instructive cancellation failure modes, with broad ownership scope, silent exceptions, and unclear reuse permission.

**Scope of this review:** README execution/configuration guidance, annotated live configuration, protective-order source; no live requests.
