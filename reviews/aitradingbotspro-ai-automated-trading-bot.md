# AI Automated Trading Bot — HTTP success is not a fill

**Decision question:** What does a webhook-driven exchange adapter actually confirm?

| Field | Review |
| --- | --- |
| Upstream | [aitradingbotspro/ai-automated-trading-bot](https://github.com/aitradingbotspro/ai-automated-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [eeb749b681a2cae1947bed0e2912a2ad729d02a3](https://github.com/aitradingbotspro/ai-automated-trading-bot/commit/eeb749b681a2cae1947bed0e2912a2ad729d02a3) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | The Hyperliquid adapter sizes from ticker last or close and calls create_order; protective stop/target orders are sent in a separate path. The inspected path can fall back to price one, and an order object is not confirmed execution. |

## What this project does

A TradingView and optional LLM webhook bridge to several exchanges, including Hyperliquid through CCXT. [Project README](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/README.md#L56).

## Mechanism inspected

The Hyperliquid adapter sizes from ticker last or close and calls create_order; protective stop/target orders are sent in a separate path. [Implementation](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/exchanges/hyperliquid.py#L81). [Related source 1](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/exchanges/hyperliquid.py#L109).

## Limitation that matters

The inspected path can fall back to price one, and an order object is not confirmed execution. The protective-order calls do not visibly establish reduce-only semantics. This is a source review, not a runtime or security test.

## Practical check for a trading system

Require valid fresh price, exchange order identity, protection ACK, and fill evidence before reporting an entry complete.

## Why this score

Its concrete adapter exposes serious execution ambiguities, making it a cautionary example rather than a live template.

## Source trail

[README](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/README.md#L56); [Implementation](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/exchanges/hyperliquid.py#L81); [Related source 1](https://github.com/aitradingbotspro/ai-automated-trading-bot/blob/eeb749b681a2cae1947bed0e2912a2ad729d02a3/exchanges/hyperliquid.py#L109).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
