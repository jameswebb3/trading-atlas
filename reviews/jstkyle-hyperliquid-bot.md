# Hyperliquid Copy Bot - How does a copy executor repair missed leader fills?

**Decision question:** How does a copy executor repair missed leader fills?

| Field | Review |
| --- | --- |
| Upstream | [jstkyle/hyperliquid_bot](https://github.com/jstkyle/hyperliquid_bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [6a96ce04460e6c9470d6d3b977646b2490fbf9cf](https://github.com/jstkyle/hyperliquid_bot/commit/6a96ce04460e6c9470d6d3b977646b2490fbf9cf) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Pairs WebSocket fill reaction with timed account-position reconciliation on Hyperliquid. Position convergence cannot recover missing fill timing or prove PnL attribution. |

## What this project does

A Hyperliquid copy-trading bot with a primary WebSocket fill copier and a periodic position-state reconciliation loop.

## Mechanism inspected

The fast path scales each observed leader fill, while a separate reconciliation loop wakes on a leader event or timer and compares desired versus follower position. This separates response speed from drift repair.

## Limitation that matters

A state diff can repair current exposure but cannot reconstruct the exact missed fill price, time or path. The README says positions open before startup are not copied; its in-memory dedup window is not a durable fill ledger.

## Practical check for a trading system

Use fill events for low-latency actions and account snapshots as an independent state check, with explicit provenance for any repair order.

## Why this score

3/5 because The two-path design is directly applicable to order-state reliability, but copy behavior and historical attribution remain limited.

## Source trail

[README](https://github.com/jstkyle/hyperliquid_bot/blob/6a96ce04460e6c9470d6d3b977646b2490fbf9cf/README.md#L60); [README](https://github.com/jstkyle/hyperliquid_bot/blob/6a96ce04460e6c9470d6d3b977646b2490fbf9cf/README.md#L165); [copybot/engine/fill_copier.py](https://github.com/jstkyle/hyperliquid_bot/blob/6a96ce04460e6c9470d6d3b977646b2490fbf9cf/copybot/engine/fill_copier.py#L71); [copybot/engine/reconciliation.py](https://github.com/jstkyle/hyperliquid_bot/blob/6a96ce04460e6c9470d6d3b977646b2490fbf9cf/copybot/engine/reconciliation.py#L82).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
