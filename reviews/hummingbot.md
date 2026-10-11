# Hummingbot: fill IDs, lost orders, and incomplete completion

**Decision question:** How does an exchange connector track lost orders and deduplicate fills?

| Field | Review |
| --- | --- |
| Upstream | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [9af100d6822da7d2d0291a906c730ef172284ee2](https://github.com/hummingbot/hummingbot/commit/9af100d6822da7d2d0291a906c730ef172284ee2) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Hummingbot keeps in-flight and lost-order states, deduplicates fills by trade ID, and waits briefly for fill details before completing an order. On timeout it proceeds with incomplete information, so fill reporting still needs a completeness check. |

## Mechanism worth inspecting

The [project overview](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/README.md#L9-L11) positions Hummingbot as a multi-exchange trading framework. The [in-flight order model](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/core/data_type/in_flight_order.py#L21-L54) separates pending creation, open, partial fill, pending cancel, and terminal states. Its [trade updater](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/core/data_type/in_flight_order.py#L351-L369) keys fills by trade ID and rejects a repeated ID before adding quantity or fee-bearing trade details.

The [client tracker restores](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/connector/client_order_tracker.py#L153-L164) open orders and separately retains orders previously marked lost. After repeated not-found responses it [marks an order failed but keeps it in a lost-order map](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/connector/client_order_tracker.py#L221-L249). The Hyperliquid connector translates a venue update into that model using [client and exchange order IDs](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/connector/exchange/hyperliquid/hyperliquid_exchange.py#L634-L655).

## Important limit

When a FILLED status arrives before complete trade details, the tracker [waits for fill updates](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/connector/client_order_tracker.py#L267-L293). After timeout it logs that completion will proceed with incomplete information. The Hyperliquid connector also states that its order-status endpoint does not return trade IDs, so it [polls fills separately](https://github.com/hummingbot/hummingbot/blob/9af100d6822da7d2d0291a906c730ef172284ee2/hummingbot/connector/exchange/hyperliquid/hyperliquid_exchange.py#L901-L930). A terminal status is therefore not a substitute for a complete fill ledger.

## Why this score for a trading system

Lost-order tracking and fill-ID deduplication address direct execution risks; the fill-wait timeout remains an explicit blind spot.

**Scope of this review:** We read the pinned README, order model, tracker, and Hyperliquid connector paths. We did not run Hummingbot or inspect every venue connector.
