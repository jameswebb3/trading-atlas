# Hyperliquid Agent Skill - Is a one-shot book snapshot a historical order-flow feed?

**Decision question:** Is a one-shot book snapshot a historical order-flow feed?

| Field | Review |
| --- | --- |
| Upstream | [marcuppe/hyperliquid](https://github.com/marcuppe/hyperliquid) |
| Primary area | Market Data & Ingestion |
| Source commit | [82712c94e2b4003a6e5c29bcd0600f69a60f9d5d](https://github.com/marcuppe/hyperliquid/commit/82712c94e2b4003a6e5c29bcd0600f69a60f9d5d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The order-book script makes one l2Book info request and prints or serializes its returned levels. It records neither a receive timestamp nor an append-only event stream; a snapshot cannot reconstruct gaps or maker queue. |

## What this project does

A Hyperliquid agent skill with reference docs and small API scripts.

## Mechanism inspected

The order-book script makes one l2Book info request and prints or serializes its returned levels.

## Limitation that matters

It records neither a receive timestamp nor an append-only event stream; a snapshot cannot reconstruct gaps or maker queue.

## Practical check for a trading system

Treat this as an inspection utility and use a separate timestamped recorder for research evidence.

## Why this score

2/5. Useful for checking the current book shape, with limited research and replay value.

## Source trail

[README](https://github.com/marcuppe/hyperliquid/blob/82712c94e2b4003a6e5c29bcd0600f69a60f9d5d/README.md#L1); [references/websocket.md](https://github.com/marcuppe/hyperliquid/blob/82712c94e2b4003a6e5c29bcd0600f69a60f9d5d/references/websocket.md#L1); [scripts/market_data/order_book.py](https://github.com/marcuppe/hyperliquid/blob/82712c94e2b4003a6e5c29bcd0600f69a60f9d5d/scripts/market_data/order_book.py#L54); [Root license](https://github.com/marcuppe/hyperliquid/blob/82712c94e2b4003a6e5c29bcd0600f69a60f9d5d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
