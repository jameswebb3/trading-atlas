# Allora Hyperliquid bot — Returning None can erase order uncertainty

**Decision question:** What does the caller know after an order exception?

| Field | Review |
| --- | --- |
| Upstream | [Allora Hyperliquid bot](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7b6a60a2006ee9ce1a03937f732047d5fb0b8ced](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot/commit/7b6a60a2006ee9ce1a03937f732047d5fb0b8ced) |
| Reviewed | 2026-10-06 |
| Declared license | No root license file found |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | Its order helper submits a market open and catches every exception, returning None; it also returns None when price lookup fails. None conflates no order attempted with an uncertain exchange outcome, while its prediction path is neither causal evidence nor a verified HL-perp alpha. |

## What this project does

A Hyperliquid bot combining an external prediction service and LLM trade validation. [README](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot/blob/7b6a60a2006ee9ce1a03937f732047d5fb0b8ced/README.md).

## Mechanism inspected

Its order helper submits a market open and catches every exception, returning None; it also returns None when price lookup fails. [Implementation](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot/blob/7b6a60a2006ee9ce1a03937f732047d5fb0b8ced/core/orders.py#L127-L158).

## Limitation that matters

None conflates no order attempted with an uncertain exchange outcome, while its prediction path is neither causal evidence nor a verified HL-perp alpha. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep a distinct UNKNOWN_SUBMIT state and reconcile the venue after timeout; do not use its prediction strategy.

## Why this score

Direct trading-system relevance: Its order helper submits a market open and catches every exception, returning None; it also returns None when price lookup fails. None conflates no order attempted with an uncertain exchange outcome, while its prediction path is neither causal evidence nor a verified HL-perp alpha.

## Source trail

[README](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot/blob/7b6a60a2006ee9ce1a03937f732047d5fb0b8ced/README.md) · [Implementation](https://github.com/HarbhagwanDhaliwal/Allora_HyperLiquid_AutoTradeBot/blob/7b6a60a2006ee9ce1a03937f732047d5fb0b8ced/core/orders.py#L127-L158).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
