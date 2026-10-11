# Hyperliquid Python SDK: explicit order-to-wire boundary

**Decision question:** Which order fields and signing boundaries does the official Hyperliquid SDK expose?

| Field | Review |
| --- | --- |
| Upstream | [hyperliquid-dex/hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2fdb18f9517675ea03695a0962bd19eece9c83f0](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/commit/2fdb18f9517675ea03695a0962bd19eece9c83f0) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/LICENSE.md) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The official SDK keeps client order IDs, reduce-only, and order types explicit before converting requests to signed wire actions. It documents request construction, but this review does not establish fill reconciliation or retry behavior. |

## Mechanism worth inspecting

The [basic order example](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/examples/basic_order.py#L8-L24) shows the public call shape. In [`Exchange.order`](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/exchange.py#L140-L161), order type, `reduce_only`, and optional `cloid` remain explicit. [`bulk_orders`](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/exchange.py#L163-L188) converts the request into wire fields, creates a timestamp, signs the action, and posts it. The same file exposes [cancellation by client order ID](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/exchange.py#L333-L350).

The SDK also computes a [slippage-adjusted aggressive price](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/2fdb18f9517675ea03695a0962bd19eece9c83f0/hyperliquid/exchange.py#L112-L132), with precision rules that differ for perps and spot. These source paths are useful when checking that another connector preserves Hyperliquid's order identity, precision, and signing boundaries.

## Boundary and practical use

This is a request-construction reference. The paths examined do not show how an application deduplicates fills, recovers an uncertain send, or reconciles open orders after restart. A correct signed request and a correct account state are separate questions.

## Why this score for a trading system

The venue request and client-ID paths are directly relevant to order placement, but lifecycle reconciliation is outside the inspected SDK path.

**Scope of this review:** We read the pinned README, order example, and exchange implementation. We did not install or run the SDK or validate responses against the live venue.
