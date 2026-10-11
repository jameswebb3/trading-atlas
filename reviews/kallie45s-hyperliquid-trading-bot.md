# Hyperliquid Trading Bot - Can an order fill and still be reported as a failed send?

**Decision question:** Can an order fill and still be reported as a failed send?

| Field | Review |
| --- | --- |
| Upstream | [kallie45s/hyperliquid-trading-bot](https://github.com/kallie45s/hyperliquid-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [34825c5c56073752cc9e398d1ba8f431df43355a](https://github.com/kallie45s/hyperliquid-trading-bot/commit/34825c5c56073752cc9e398d1ba8f431df43355a) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Its adapter creates a market-like IOC limit order and inspects the returned status for resting. The inspected success check can reject a filled IOC status, while the engine stop cancels orders without proving position closure. |

## What this project does

A Hyperliquid bot with an exchange adapter and trading engine.

## Mechanism inspected

Its adapter creates a market-like IOC limit order and inspects the returned status for resting.

## Limitation that matters

The inspected success check can reject a filled IOC status, while the engine stop cancels orders without proving position closure.

## Practical check for a trading system

Treat filled, resting and rejected exchange responses distinctly and reconcile positions on shutdown.

## Why this score

1/5. This is a direct negative reference for order-result handling, not a component to adopt.

## Source trail

[README](https://github.com/kallie45s/hyperliquid-trading-bot/blob/34825c5c56073752cc9e398d1ba8f431df43355a/README.md#L1); [src/exchanges/hyperliquid/adapter.py](https://github.com/kallie45s/hyperliquid-trading-bot/blob/34825c5c56073752cc9e398d1ba8f431df43355a/src/exchanges/hyperliquid/adapter.py#L149); [src/exchanges/hyperliquid/adapter.py](https://github.com/kallie45s/hyperliquid-trading-bot/blob/34825c5c56073752cc9e398d1ba8f431df43355a/src/exchanges/hyperliquid/adapter.py#L218); [src/core/engine.py](https://github.com/kallie45s/hyperliquid-trading-bot/blob/34825c5c56073752cc9e398d1ba8f431df43355a/src/core/engine.py#L205); [src/core/engine.py](https://github.com/kallie45s/hyperliquid-trading-bot/blob/34825c5c56073752cc9e398d1ba8f431df43355a/src/core/engine.py#L211).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
