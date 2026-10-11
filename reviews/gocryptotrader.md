# GoCryptoTrader: invalidate a book on checksum failure, but mind ordering

**Decision question:** What makes an incremental order book safe to use after an update?

| Field | Review |
| --- | --- |
| Upstream | [GoCryptoTrader](https://github.com/thrasher-corp/gocryptotrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [4354537e9817d8404c9c38c0f5bdfab2dfe173b1](https://github.com/thrasher-corp/gocryptotrader/commit/4354537e9817d8404c9c38c0f5bdfab2dfe173b1) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/thrasher-corp/gocryptotrader/blob/4354537e9817d8404c9c38c0f5bdfab2dfe173b1/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Invalidates book state after empty, malformed, or checksum-failing depth updates. The inspected path explicitly allows some out-of-order updates and can silently skip older IDs, so a checksum is only one part of a reliable sequence contract. |

## Mechanism worth inspecting

The [overview](https://github.com/thrasher-corp/gocryptotrader/blob/4354537e9817d8404c9c38c0f5bdfab2dfe173b1/README.md#L50-L71) includes exchange order books and trade processing. The [depth update path](https://github.com/thrasher-corp/gocryptotrader/blob/4354537e9817d8404c9c38c0f5bdfab2dfe173b1/exchanges/orderbook/incremental_updates.go#L64-L119) invalidates state on an empty update, update error, checksum mismatch, or failed book validation. Yet [its ordering comments and switch](https://github.com/thrasher-corp/gocryptotrader/blob/4354537e9817d8404c9c38c0f5bdfab2dfe173b1/exchanges/orderbook/incremental_updates.go#L80-L85) say out-of-order updates are not an error here and can be skipped under an option. A separate [WebSocket event guide](https://github.com/thrasher-corp/gocryptotrader/blob/4354537e9817d8404c9c38c0f5bdfab2dfe173b1/docs/WS_ORDER_EVENTS.md#L14-L29) identifies cumulative executed quantity and client order ID as distinct fields.

## Important limit

Checksum algorithms and sequence semantics vary by venue; the inspected generic path does not establish Hyperliquid L2 correctness. A valid checksum can still be computed on stale but internally consistent state if the missing-update condition is not detected.

## Questions to take into your own design

- Does each venue adapter enforce its own sequence and snapshot rule?
- Does a failed checksum make the book unavailable to strategies until a verified resync?

## Why this score for a trading system

Book invalidation on checksum failure is directly useful for LOB research, but permissive update ordering needs venue-specific controls.

**Scope of this review:** We read the pinned README, order-book update code, and order-event documentation. We did not consume a live feed.
