# go-hyperliquid: distinguish resting, filled, and error responses

**Decision question:** How can a Hyperliquid client represent per-order response outcomes?

| Field | Review |
| --- | --- |
| Upstream | [sonirico/go-hyperliquid](https://github.com/sonirico/go-hyperliquid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [91481a8c9a5a428e64b7c20c11b47707c0b891de](https://github.com/sonirico/go-hyperliquid/commit/91481a8c9a5a428e64b7c20c11b47707c0b891de) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/sonirico/go-hyperliquid/blob/91481a8c9a5a428e64b7c20c11b47707c0b891de/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | go-hyperliquid models resting, filled, and error outcomes separately and validates order fields before wire conversion. It is a useful response-shape reference, not evidence of complete order-lifecycle reconciliation. |

## Mechanism worth inspecting

The [README](https://github.com/sonirico/go-hyperliquid/blob/91481a8c9a5a428e64b7c20c11b47707c0b891de/README.md#L10-L24) presents an unofficial Go client for Hyperliquid. Its [`OrderStatus` model](https://github.com/sonirico/go-hyperliquid/blob/91481a8c9a5a428e64b7c20c11b47707c0b891de/exchange_orders.go#L24-L49) has distinct fields for a resting order, a filled order, and an error. In [`newCreateOrderAction`](https://github.com/sonirico/go-hyperliquid/blob/91481a8c9a5a428e64b7c20c11b47707c0b891de/exchange_orders.go#L79-L117), price and size conversion can fail separately; asset lookup and client order ID normalization are also checked before the wire action is built.

These details make a useful reference for a typed boundary between local order intent, valid wire request, and per-order response. A transport-level success is not itself a resting or filled outcome.

## Boundary and practical use

A response model captures what one API call reported. The inspected code does not establish how an application handles a lost response, repeated fill, or reconciliation after restart. The official Python SDK and CCXT provide adjacent request-construction references; this client's distinctive contribution in this review is its explicit result shape.

## Why this score for a trading system

Typed venue replies are useful for a Hyperliquid order adapter, but they stop short of durable order-state reconciliation.

**Scope of this review:** We read the pinned README, contributor documentation, and order-request code. We did not run the client or verify its claims of feature parity.
