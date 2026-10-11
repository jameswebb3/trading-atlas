# NexusTrader: an ACK timeout is an unknown order, not a failed order

**Decision question:** What should happen when a Hyperliquid WebSocket order gets no ACK?

| Field | Review |
| --- | --- |
| Upstream | [NexusTrader](https://github.com/Quantweb3-com/NexusTrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [b5ed599cfbb62b443a55fa37241cd2fab499a28a](https://github.com/Quantweb3-com/NexusTrader/commit/b5ed599cfbb62b443a55fa37241cd2fab499a28a) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/LICENSE) |
| Review depth | 3/3: documentation, relevant source, and focused tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | After a Hyperliquid WebSocket ACK timeout, it queries order status by client ID through REST with cache bypass before declaring failure. A confirmed order returns a distinct timeout-confirmed result; an unconfirmed request raises. This narrows one duplicate-order race but does not prove complete fill reconciliation. |

## Mechanism worth inspecting

The [reliability guide](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/docs/source/quickstart/reliable_orders.rst#L1-L34) describes idempotent order creation and WebSocket fallback. The [base confirmation path](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/nexustrader/base/oms.py#L223-L241) fetches order status with force_refresh and updates cached state only if REST finds it. The [Hyperliquid create path](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/nexustrader/exchange/hyperliquid/oms.py#L747-L759) waits five seconds for ACK, then invokes that confirmation before choosing a distinct confirmed-timeout result or raising an unknown-state error. The [venue fetch](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/nexustrader/exchange/hyperliquid/oms.py#L1118-L1129) queries status by client ID when forced, and [tests](https://github.com/Quantweb3-com/NexusTrader/blob/b5ed599cfbb62b443a55fa37241cd2fab499a28a/test/test_ws_ack.py#L804-L873) cover confirmed and unconfirmed timeout branches.

## Important limit

REST can fail or return no order while the exchange later accepts it; that remains unknown state, not proof of rejection. This review did not run the connector against Hyperliquid or establish restart recovery, complete partial fills, and account-history reconciliation.

## Questions to take into your own design

- Is every timeout resolved through an exchange-authoritative lookup before any retry?
- How is an unresolved order quarantined until account history closes the ambiguity?

## Why this score for a trading system

Its Hyperliquid-specific ACK-to-REST confirmation path directly addresses ambiguous live order state, with remaining exchange-history and restart questions.

**Scope of this review:** We read the pinned README, reliability guide, base and Hyperliquid OMS paths, and focused tests. We did not place an order.
