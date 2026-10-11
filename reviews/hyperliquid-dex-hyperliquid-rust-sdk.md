# Hyperliquid Rust SDK — nonce scope and market-order caps are explicit

**Decision question:** What does the SDK coordinate locally, and what must the trading application coordinate?

| Field | Review |
| --- | --- |
| Upstream | [Hyperliquid Rust SDK](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [aac75585daf12d0a3761126cc7da7a5e035b5853](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/commit/aac75585daf12d0a3761126cc7da7a5e035b5853) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/blob/aac75585daf12d0a3761126cc7da7a5e035b5853/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes two useful adapter boundaries: process-local nonce generation and market orders built as capped IOC limits. A trading application must define signer coordination, explicit caps and residual-fill handling. |

## Project overview

The Hyperliquid Rust SDK wraps the exchange API; the inspected source exposes request signing inputs and market-order construction. [Project documentation](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/blob/aac75585daf12d0a3761126cc7da7a5e035b5853/src/exchange/exchange_client.rs#L143-L160).

## Mechanism worth inspecting

A process-local atomic counter supplies nonces, with a wall-time resynchronization branch for a counter more than 300 seconds behind. The market-open helper constructs a rounded IOC limit order and defaults slippage to 5%. [Nonce generation](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/blob/aac75585daf12d0a3761126cc7da7a5e035b5853/src/helpers.rs#L10-L27); [process initialization](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/blob/aac75585daf12d0a3761126cc7da7a5e035b5853/src/helpers.rs#L90-L92); [market order](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk/blob/aac75585daf12d0a3761126cc7da7a5e035b5853/src/exchange/exchange_client.rs#L313-L334).

## Important limit

The local counter is not a persistent, cross-process per-signer coordination service. The stale-counter branch also deserves concurrency testing during resynchronization. The default slippage cap is a request construction choice, not a statement about expected execution cost or completion.

## Questions to take into your own design

- Are signer nonce ownership, restart and simultaneous processes explicitly coordinated?
- Are IOC price cap, rounding and residual quantity recorded rather than inferred from a market-order label?

## Why this score for a trading system

3/5: concrete native-adapter boundaries, with signer coordination and actual execution evidence requiring application-level design.

**Scope of this review:** Nonce helper and market-open construction; signing internals and complete response reconciliation were not audited.
