# Go Hyperliquid — Never turn missing mark into a valid price

**Decision question:** What happens when a market-order price cap cannot be computed?

| Field | Review |
| --- | --- |
| Upstream | [Logarithm-Labs/go-hyperliquid](https://github.com/Logarithm-Labs/go-hyperliquid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [93ef7a5af63234ad354d0c6726c441e73199af4f](https://github.com/Logarithm-Labs/go-hyperliquid/commit/93ef7a5af63234ad354d0c6726c441e73199af4f) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The exchange interface makes exchange OID and client OID explicit; its slippage-price helper returns zero when fetching the market price fails. A zero price is indistinguishable from a numeric result to an unchecked caller, so downstream order construction must reject it. |

## What this project does

A Go SDK with order, cancel-by-ID, cancel-by-client-ID, and signing interfaces for Hyperliquid. [Project README](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/README.md#L1).

## Mechanism inspected

The exchange interface makes exchange OID and client OID explicit; its slippage-price helper returns zero when fetching the market price fails. [Implementation](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_service.go#L10). [Related source 1](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_service.go#L78). [Related source 2](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_signing.go#L36).

## Limitation that matters

A zero price is indistinguishable from a numeric result to an unchecked caller, so downstream order construction must reject it. This is a source review, not a runtime or security test.

## Practical check for a trading system

Make missing mark an error and assert that no order reaches signing or submission with an invalid cap.

## Why this score

Its exchange-specific surface is relevant, but the failure-to-zero helper is a safety counterexample, not code to copy.

## Source trail

[README](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/README.md#L1); [Implementation](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_service.go#L10); [Related source 1](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_service.go#L78); [Related source 2](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/hyperliquid/exchange_signing.go#L36) - [License](https://github.com/Logarithm-Labs/go-hyperliquid/blob/93ef7a5af63234ad354d0c6726c441e73199af4f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
