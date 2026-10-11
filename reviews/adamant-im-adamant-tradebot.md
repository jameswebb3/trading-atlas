# ADAMANT Tradebot — Market-making activity is not evidence of edge

**Decision question:** Does a market-making bot separate fills from generated volume?

| Field | Review |
| --- | --- |
| Upstream | [ADAMANT Tradebot](https://github.com/Adamant-im/adamant-tradebot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [9f81feaab1404961a764ddbecc6cc225c94e0b10](https://github.com/Adamant-im/adamant-tradebot/commit/9f81feaab1404961a764ddbecc6cc225c94e0b10) |
| Reviewed | 2026-10-06 |
| Declared license | No root license file found |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The inspected trading path keeps separate filled-amount and quote counters and records order metadata during its activity loop. The README and source center on creating volume, including two-account behavior; this is not a trading edge and no root license file was found. |

## What this project does

A self-hosted CEX market-making toolkit aimed at token issuers. [README](https://github.com/Adamant-im/adamant-tradebot/blob/9f81feaab1404961a764ddbecc6cc225c94e0b10/README.md).

## Mechanism inspected

The inspected trading path keeps separate filled-amount and quote counters and records order metadata during its activity loop. [Implementation](https://github.com/Adamant-im/adamant-tradebot/blob/9f81feaab1404961a764ddbecc6cc225c94e0b10/trade/mm_trader.js#L60-L80).

## Limitation that matters

The README and source center on creating volume, including two-account behavior; this is not a trading edge and no root license file was found. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not port its volume policy; only use separate fill counters as a reminder to reconcile quantities from venue evidence.

## Why this score

Indirect relevance only: The inspected trading path keeps separate filled-amount and quote counters and records order metadata during its activity loop. The README and source center on creating volume, including two-account behavior; this is not a trading edge and no root license file was found.

## Source trail

[README](https://github.com/Adamant-im/adamant-tradebot/blob/9f81feaab1404961a764ddbecc6cc225c94e0b10/README.md) · [Implementation](https://github.com/Adamant-im/adamant-tradebot/blob/9f81feaab1404961a764ddbecc6cc225c94e0b10/trade/mm_trader.js#L60-L80).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
