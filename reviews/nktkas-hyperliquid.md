# nktkas/hyperliquid: serialize signed orders and inspect batch errors

**Decision question:** How are signed Hyperliquid orders serialized and nested batch errors surfaced?

| Field | Review |
| --- | --- |
| Upstream | [nktkas/hyperliquid](https://github.com/nktkas/hyperliquid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [db80d598f6e4672edc090fe69994ecec97ebc980](https://github.com/nktkas/hyperliquid/commit/db80d598f6e4672edc090fe69994ecec97ebc980) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/LICENSE) |
| Review depth | 3/3: documentation, implementation, and relevant test code read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Serializes exchange requests per wallet and network before signing, then checks top-level and per-order error responses. The nonce and lock are process-local; an error can coexist with successful sibling orders, and later fills still need reconciliation. |

## Mechanism worth inspecting

The [README](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/README.md#L9-L19) identifies a community TypeScript SDK for Hyperliquid. The [error guide](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/docs/error-handling.md#L5-L31) separates validation, API, and transport failures. The exchange [execution shell](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/_base/_shell.ts#L39-L60) takes a per-wallet-and-network lock, gets a nonce, signs, sends, then validates the response. Its [nonce manager](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/_base/_nonce.ts#L15-L41) advances the millisecond nonce in memory. The [error checker](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/_base/errors.ts#L14-L53) recognizes top-level errors and errors inside a batch of statuses; [assertSuccessResponse](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/_base/errors.ts#L80-L90) throws an API error containing the raw response. The [order response type](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/order.ts#L121-L174) distinguishes resting, filled, error, and waiting states. [Test code](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/tests/api/exchange/order.test.ts#L32-L69) covers request shapes including client order IDs and IOC; we did not run it.

The lesson is that an HTTP-level success and a successful batch are different events. A caller must preserve the raw response if one sibling order fails while another succeeds.

## Important limits

The [lock registry](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/src/api/exchange/_methods/_base/_semaphore.ts#L61-L79) and nonce map are in process memory. They do not coordinate two workers or persist through restart. The shell validates the immediate response; it does not prove later fills, cancellations, or durable recovery. The [market-order guide](https://github.com/nktkas/hyperliquid/blob/db80d598f6e4672edc090fe69994ecec97ebc980/docs/guides/market-orders.md#L1-L15) shows IOC as an aggressive limit order whose price buffer remains a caller choice.

## Questions to take into your own design

- Can two workers sign orders for the same wallet concurrently?
- When one batch item fails, do successful siblings retain their order IDs?
- Where are fills and cancels reconciled after the request returns?

## Why this score for a trading system

The inspected wallet lock, nonce path, and nested-error handling address direct Hyperliquid execution hazards, while process-local coordination and post-response order state remain outside the SDK guarantee.

**Scope of this review:** We read the pinned README, guides, implementation, and relevant test. We did not install or run the SDK or validate later venue behavior.
