# Hyperliquid Rust Bot — Do not forget exposure before a close fills

**Decision question:** What state survives a failed closing order?

| Field | Review |
| --- | --- |
| Upstream | [0xTan1319/hyperliquid-trading-bot-rust](https://github.com/0xTan1319/hyperliquid-trading-bot-rust) |
| Primary area | Execution & Exchange Integration |
| Source commit | [5852e4c15b683329da78b099268e1309c2908c64](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/commit/5852e4c15b683329da78b099268e1309c2908c64) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Its open path sends a market order without a client ID; the close path changes local position tracking around the send. Removing a tracked position before exchange fill confirmation can hide live exposure after a rejected or delayed close. |

## What this project does

An experimental Rust bot for Hyperliquid perpetual orders. [Project README](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/README.md#L41).

## Mechanism inspected

Its open path sends a market order without a client ID; the close path changes local position tracking around the send. [Implementation](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/src/executor.rs#L81). [Related source 1](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/src/executor.rs#L235).

## Limitation that matters

Removing a tracked position before exchange fill confirmation can hide live exposure after a rejected or delayed close. This is a source review, not a runtime or security test.

## Practical check for a trading system

Retain the open position until a reconciled fill proves the remaining size is zero.

## Why this score

A concise negative execution case; the project is experimental and offers no reliable order journal.

## Source trail

[README](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/README.md#L41); [Implementation](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/src/executor.rs#L81); [Related source 1](https://github.com/0xTan1319/hyperliquid-trading-bot-rust/blob/5852e4c15b683329da78b099268e1309c2908c64/src/executor.rs#L235).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
