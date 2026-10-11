# Aster & HL Trading Bot - How does a market maker limit duplicate orders during asynchronous placement?

**Decision question:** How does a market maker limit duplicate orders during asynchronous placement?

| Field | Review |
| --- | --- |
| Upstream | [0xagarg/perp-dex-trading-bot](https://github.com/0xagarg/perp-dex-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3609d93782ebce3757b06b516c3680de012a4c82](https://github.com/0xagarg/perp-dex-trading-bot/commit/3609d93782ebce3757b06b516c3680de012a4c82) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Serializes duplicate-order cleanup and post-only placement around a local lock. The open-order snapshot and cancel response need venue-side reconciliation. |

## What this project does

A multi-venue perpetuals workstation with a shared order coordinator and a Hyperliquid adapter.

## Mechanism inspected

The coordinator filters existing orders by type and side, cancels older duplicates, applies price and quantity step rounding, and holds an operation lock while creating a post-only limit order. The adapter retries initialization with bounded backoff.

## Limitation that matters

The duplicate scan works from the caller-provided open-order snapshot, which may already be stale. Local locks and successful cancel calls do not establish that every venue order disappeared or that no fill arrived meanwhile. No root license text was verified.

## Practical check for a trading system

Reconcile live order IDs after cancellation and creation, including late fills and adapter reconnects.

## Why this score

3/5. The order coordination is a useful direct pattern, but its safety rests on fresh venue state.

## Source trail

[README](https://github.com/0xagarg/perp-dex-trading-bot/blob/3609d93782ebce3757b06b516c3680de012a4c82/README.md#L11); [src/core/order-coordinator.ts](https://github.com/0xagarg/perp-dex-trading-bot/blob/3609d93782ebce3757b06b516c3680de012a4c82/src/core/order-coordinator.ts#L81); [src/core/order-coordinator.ts](https://github.com/0xagarg/perp-dex-trading-bot/blob/3609d93782ebce3757b06b516c3680de012a4c82/src/core/order-coordinator.ts#L117); [src/exchanges/hyperliquid-adapter.ts](https://github.com/0xagarg/perp-dex-trading-bot/blob/3609d93782ebce3757b06b516c3680de012a4c82/src/exchanges/hyperliquid-adapter.ts#L56).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
