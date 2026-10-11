# HyperSDK — A market order is still a bounded limit

**Decision question:** What does the venue actually submit when a client says market?

| Field | Review |
| --- | --- |
| Upstream | [infinitefield/hypersdk](https://github.com/infinitefield/hypersdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2c8d9a8487fa972eb1b975eea294a38b7cb69582](https://github.com/infinitefield/hypersdk/commit/2c8d9a8487fa972eb1b975eea294a38b7cb69582) |
| Reviewed | 2026-10-10 |
| Declared license | MPL-2.0 ([source](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The CLI resolves the asset, builds a client order ID, and encodes a market order with an explicit slippage-bounded limit price. The helper cannot guarantee a fill; the response still needs status inspection and later fill reconciliation. |

## What this project does

A Rust SDK and CLI for HyperCore and HyperEVM with order submission helpers. [Project README](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/README.md#L284).

## Mechanism inspected

The CLI resolves the asset, builds a client order ID, and encodes a market order with an explicit slippage-bounded limit price. [Implementation](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/hypecli/src/orders.rs#L201). [Related source 1](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/hypecli/src/orders.rs#L310).

## Limitation that matters

The helper cannot guarantee a fill; the response still needs status inspection and later fill reconciliation. This broad SDK is a larger dependency than a single order contract. This is a source review, not a runtime or security test.

## Practical check for a trading system

Store the submitted cap, TIF, client ID, rejection status, and confirmed fill separately.

## Why this score

A direct Hyperliquid order-construction reference, bounded by its response and recovery semantics.

## Source trail

[README](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/README.md#L284); [Implementation](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/hypecli/src/orders.rs#L201); [Related source 1](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/hypecli/src/orders.rs#L310) - [License](https://github.com/infinitefield/hypersdk/blob/2c8d9a8487fa972eb1b975eea294a38b7cb69582/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
