# CCXT: where a unified order call exposes venue-specific behavior

**Decision question:** How does a unified order API translate market orders and venue errors for Hyperliquid?

| Field | Review |
| --- | --- |
| Upstream | [ccxt/ccxt](https://github.com/ccxt/ccxt) |
| Primary area | Execution & Exchange Integration |
| Source commit | [eb062f442781a7f69335cf50d2916c9f8d79d509](https://github.com/ccxt/ccxt/commit/eb062f442781a7f69335cf50d2916c9f8d79d509) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/LICENSE.txt) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | CCXT translates a Hyperliquid market order into a protected IOC limit and checks per-order errors inside a successful response. Its unified call still requires venue-specific price, slippage, and response handling. |

## Project overview

API library for 100+ cryptocurrency exchanges and prediction markets. Provides common methods for market data, orders, and account access, plus normalized data for cross-exchange analysis.

[Project documentation](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/README.md#L5-L23).

## Mechanism worth inspecting

The [manual describes](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/wiki/Manual.md#L1-L24) a unified trading API. The Hyperliquid adapter makes the venue-specific boundary visible: [`createOrderRequest`](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/ts/src/hyperliquid.ts#L2271-L2306) sets IOC as the default for a market order and computes a rounded limit price from a reference price and slippage. It then serializes [reduce-only and the client order ID](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/ts/src/hyperliquid.ts#L2306-L2341) into Hyperliquid's order payload.

The adapter's [error handler](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/ts/src/hyperliquid.ts#L5041-L5073) also looks inside the per-order `statuses` array. A top-level `status: ok` therefore does not by itself show that every order succeeded. This is a useful reference for deciding where a generic connector's contract must expose venue responses rather than hide them.

## Boundary and practical use

The [scheduled-cancel method](https://github.com/ccxt/ccxt/blob/eb062f442781a7f69335cf50d2916c9f8d79d509/ts/src/hyperliquid.ts#L2754-L2795) exposes a venue safeguard, but the code includes an example of an eligibility error; callers must inspect the actual response. The source review did not verify order recovery after a disconnect, fills, or live behavior. Treat the adapter as a map of request and response semantics, not as proof that one unified call supplies a complete order lifecycle.

## Why this score for a trading system

The inspected Hyperliquid adapter exposes real order-wire semantics and nested errors; it does not resolve later fills or cancellations.

**Scope of this review:** We read the pinned README, manual, and Hyperliquid adapter. We did not install or run CCXT or inspect every exchange implementation.
