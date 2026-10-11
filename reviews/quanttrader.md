# QuantTrader: duplicate fills and unmatched fills need different handling

**Decision question:** What happens when a fill arrives twice or before its order?

| Field | Review |
| --- | --- |
| Upstream | [QuantTrader](https://github.com/letianzj/quanttrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [224341d57e146aeaa143516049d2f37ff102dbf0](https://github.com/letianzj/quanttrader/commit/224341d57e146aeaa143516049d2f37ff102dbf0) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/letianzj/quanttrader/blob/224341d57e146aeaa143516049d2f37ff102dbf0/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Indexes fills by fill ID, ignores a duplicate, and updates average fill price and partial status for a known order. An unmatched fill is only logged; it is not attached later by the inspected manager, which limits recovery from reordered exchange events. |

## Mechanism worth inspecting

The [overview](https://github.com/letianzj/quanttrader/blob/224341d57e146aeaa143516049d2f37ff102dbf0/README.md#L6-L12) describes one event-driven strategy path for backtest and live brokerage. The [order manager](https://github.com/letianzj/quanttrader/blob/224341d57e146aeaa143516049d2f37ff102dbf0/quanttrader/order/order_manager.py#L18-L38) keeps separate order and fill dictionaries. The [fill handler](https://github.com/letianzj/quanttrader/blob/224341d57e146aeaa143516049d2f37ff102dbf0/quanttrader/order/order_manager.py#L109-L144) rejects repeated fill IDs, updates weighted average fill price and filled quantity, and marks a known order partial or complete. The same handler only logs a fill whose order ID is unknown.

## Important limit

An exchange can deliver a fill before a delayed order acknowledgement. The inspected manager does not buffer that orphan or reconcile it later. The project's live path is Interactive Brokers oriented and does not demonstrate Hyperliquid behavior.

## Questions to take into your own design

- Are orphan fills retained until account and order history can reconcile them?
- Are fill IDs deduplicated across restarts, not only within one process?

## Why this score for a trading system

Its fill-ID deduplication is directly relevant, but missing fill-before-order recovery reduces its value as an execution reference.

**Scope of this review:** We read the pinned README, event structure, and order-manager source. We did not run a broker session.
