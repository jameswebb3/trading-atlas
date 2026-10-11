# Jev Trade — Subscribe separately to fills and order state

**Decision question:** Which exchange streams are needed to reconstruct a live account?

| Field | Review |
| --- | --- |
| Upstream | [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a3f2f834a1b97dd42fab1193814179ac2e96d7cd](https://github.com/aowang-ai/jev-trade/commit/a3f2f834a1b97dd42fab1193814179ac2e96d7cd) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Its user subscription requests fills, order updates, and clearinghouse state as separate channels. The set of subscriptions does not itself prove gap recovery; suppressing an initial fill snapshot to avoid duplicates could instead omit missing fills. |

## What this project does

A Hyperliquid trading bot with market and user WebSocket feeds. [Project README](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/README.md#L25).

## Mechanism inspected

Its user subscription requests fills, order updates, and clearinghouse state as separate channels. [Implementation](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/src/feed.ts#L101). [Related source 1](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/src/feed.ts#L140).

## Limitation that matters

The set of subscriptions does not itself prove gap recovery; suppressing an initial fill snapshot to avoid duplicates could instead omit missing fills. This is a source review, not a runtime or security test.

## Practical check for a trading system

Deduplicate by trade ID and reconcile all three account views against REST after a disconnect.

## Why this score

Direct stream-shape reference, but snapshot and gap handling remain unproven.

## Source trail

[README](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/README.md#L25); [Implementation](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/src/feed.ts#L101); [Related source 1](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/src/feed.ts#L140) - [License](https://github.com/aowang-ai/jev-trade/blob/a3f2f834a1b97dd42fab1193814179ac2e96d7cd/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
