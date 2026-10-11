# Hyperliquid Copy Bot — Size from current account evidence

**Decision question:** How should a copy order react when account equity cannot be refreshed?

| Field | Review |
| --- | --- |
| Upstream | [nullelove/hyperliquid-copy-bot](https://github.com/nullelove/hyperliquid-copy-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7df903b701fed966941fd964af5d5c301c1122d2](https://github.com/nullelove/hyperliquid-copy-bot/commit/7df903b701fed966941fd964af5d5c301c1122d2) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Its fill handler fetches account equity and positions before deriving the follower order size, with retries around those reads. A copy fill may arrive late or twice, and an equity fetch retry alone does not establish cursor continuity or execution idempotency. |

## What this project does

A Hyperliquid fill-copying bot with position and equity sizing rules. [Project README](https://github.com/nullelove/hyperliquid-copy-bot/blob/7df903b701fed966941fd964af5d5c301c1122d2/README.md#L7).

## Mechanism inspected

Its fill handler fetches account equity and positions before deriving the follower order size, with retries around those reads. [Implementation](https://github.com/nullelove/hyperliquid-copy-bot/blob/7df903b701fed966941fd964af5d5c301c1122d2/src/copyTrader.ts#L75).

## Limitation that matters

A copy fill may arrive late or twice, and an equity fetch retry alone does not establish cursor continuity or execution idempotency. This is a source review, not a runtime or security test.

## Practical check for a trading system

Reject copying when account state is unknown; key each copied intent to a deduplicated source fill and reconcile after reconnect.

## Why this score

Relevant account-state sequencing, but the bot does not establish a complete recovery contract.

## Source trail

[README](https://github.com/nullelove/hyperliquid-copy-bot/blob/7df903b701fed966941fd964af5d5c301c1122d2/README.md#L7); [Implementation](https://github.com/nullelove/hyperliquid-copy-bot/blob/7df903b701fed966941fd964af5d5c301c1122d2/src/copyTrader.ts#L75).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
