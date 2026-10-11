# Nexus Trade Bot — Persist client and venue identity together

**Decision question:** What survives when a WebSocket order update arrives after a restart?

| Field | Review |
| --- | --- |
| Upstream | [haohaoi34/nexus-trade-bot](https://github.com/haohaoi34/nexus-trade-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [e56b13a615f8377fb10264900e190274fd0080ab](https://github.com/haohaoi34/nexus-trade-bot/commit/e56b13a615f8377fb10264900e190274fd0080ab) |
| Reviewed | 2026-10-10 |
| Declared license | GPL-3.0 ([source](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The adapter maintains a client-order-ID to CLOID map and derives filled size from original minus remaining size in order updates. A local cache of identifiers is not a full recovery protocol; updates may be duplicated or missed, and the inspected JSON persistence is not an atomic journal. |

## What this project does

A multi-exchange trading bot with a Hyperliquid adapter and order-update stream. [Project README](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/README.md#L69).

## Mechanism inspected

The adapter maintains a client-order-ID to CLOID map and derives filled size from original minus remaining size in order updates. [Implementation](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/exchange/hyperliquid/adapter.go#L692). [Related source 1](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/exchange/hyperliquid/websocket.go#L44).

## Limitation that matters

A local cache of identifiers is not a full recovery protocol; updates may be duplicated or missed, and the inspected JSON persistence is not an atomic journal. This is a source review, not a runtime or security test.

## Practical check for a trading system

Rebuild identity from venue orders and fills after restart, then compare cumulative filled quantity monotonically.

## Why this score

Directly relevant to order reconciliation, with a useful identity map but incomplete crash durability.

## Source trail

[README](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/README.md#L69); [Implementation](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/exchange/hyperliquid/adapter.go#L692); [Related source 1](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/exchange/hyperliquid/websocket.go#L44) - [License](https://github.com/haohaoi34/nexus-trade-bot/blob/e56b13a615f8377fb10264900e190274fd0080ab/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
