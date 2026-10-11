# HyperLiquid.Net: connected is not yet synchronized

**Decision question:** When is a newly connected Hyperliquid order book ready for decisions?

| Field | Review |
| --- | --- |
| Upstream | [JKorf/HyperLiquid.Net](https://github.com/JKorf/HyperLiquid.Net) |
| Primary area | Execution & Exchange Integration |
| Source commit | [9daabc2cf7898abb492da7a48f6ecb50d24dc8a6](https://github.com/JKorf/HyperLiquid.Net/commit/9daabc2cf7898abb492da7a48f6ecb50d24dc8a6) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/JKorf/HyperLiquid.Net/blob/9daabc2cf7898abb492da7a48f6ecb50d24dc8a6/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | HyperLiquid.Net marks an order book synced only after its first snapshot arrives and waits for a new snapshot during resync. The pattern concerns market-data readiness; it does not prove that every downstream consumer rejects stale books. |

## Mechanism worth inspecting

The [client README](https://github.com/JKorf/HyperLiquid.Net/blob/9daabc2cf7898abb492da7a48f6ecb50d24dc8a6/README.md#L8-L20) lists WebSocket reconnection and a client-side order book. In [`DoStartAsync`](https://github.com/JKorf/HyperLiquid.Net/blob/9daabc2cf7898abb492da7a48f6ecb50d24dc8a6/HyperLiquid.Net/SymbolOrderBooks/HyperLiquidSymbolOrderBook.cs#L69-L87), subscription success first changes the book to `Syncing`; it waits for an initial `SetOrderBook` event before reporting `Synced`. On a timeout or error it closes the subscription instead of presenting a synchronized book. Updates retain [exchange and local event times](https://github.com/JKorf/HyperLiquid.Net/blob/9daabc2cf7898abb492da7a48f6ecb50d24dc8a6/HyperLiquid.Net/SymbolOrderBooks/HyperLiquidSymbolOrderBook.cs#L90-L93), and resync waits for another set event.

## Boundary and practical use

This review covers readiness of one market-data component inside an exchange client, not order submission. We did not trace every consuming strategy or determine the maximum acceptable age of a snapshot. The transferable rule is to expose distinct states for connected, awaiting initial data, and synchronized.

## Why this score for a trading system

Waiting for an initial book snapshot addresses a direct market-feed readiness risk, but downstream stale-book rejection was not traced.

**Scope of this review:** We read the pinned README, API map, and order-book implementation. We did not run the client or inspect all reconnection paths.
