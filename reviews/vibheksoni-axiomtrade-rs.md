# AxiomTrade RS — Verify the advertised venue surface

**Decision question:** Does an SDK that mentions Hyperliquid implement Hyperliquid trading?

| Field | Review |
| --- | --- |
| Upstream | [vibheksoni/axiomtrade-rs](https://github.com/vibheksoni/axiomtrade-rs) |
| Primary area | Execution & Exchange Integration |
| Source commit | [713518ee935a1f0161d27b138e2c46e122fc785a](https://github.com/vibheksoni/axiomtrade-rs/commit/713518ee935a1f0161d27b138e2c46e122fc785a) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | The inspected Hyperliquid module calls public info endpoints, including open orders for a user. The trading documentation inspected centers on Solana tokens; the reviewed Hyperliquid path does not show place or cancel order implementation. |

## What this project does

A multi-chain Rust SDK advertising market reads and trading workflows. [Project README](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/README.md#L29).

## Mechanism inspected

The inspected Hyperliquid module calls public info endpoints, including open orders for a user. [Implementation](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/src/api/hyperliquid.rs#L144). [Related source 1](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/docs/src/api/trading.md#L1).

## Limitation that matters

The trading documentation inspected centers on Solana tokens; the reviewed Hyperliquid path does not show place or cancel order implementation. This is a source review, not a runtime or security test.

## Practical check for a trading system

Map each advertised capability to an actual venue-specific method before adopting an SDK.

## Why this score

Useful as a scope-check example, not a complete Hyperliquid execution integration.

## Source trail

[README](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/README.md#L29); [Implementation](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/src/api/hyperliquid.rs#L144); [Related source 1](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/docs/src/api/trading.md#L1) - [License](https://github.com/vibheksoni/axiomtrade-rs/blob/713518ee935a1f0161d27b138e2c46e122fc785a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
