# copytrading-agent — Refresh actual position before target-delta orders

**Decision question:** Does a Hyperliquid follower calculate deltas from fresh account state?

| Field | Review |
| --- | --- |
| Upstream | [Gajesh2007/copytrading-agent](https://github.com/Gajesh2007/copytrading-agent) |
| Primary area | Execution & Exchange Integration |
| Source commit | [5422835ea77acdd8ef2867814b38f6c921ec2c40](https://github.com/Gajesh2007/copytrading-agent/commit/5422835ea77acdd8ef2867814b38f6c921ec2c40) |
| Reviewed | 2026-10-09 |
| Declared license | No root license file found |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Before each sync it fetches follower `clearinghouseState`, computes target deltas, filters dust and submits IOC orders with per-order status classification. Submission errors are logged and the inspected function does not immediately reconcile uncertain outcomes; mark-price fallback to entry price can be stale. |

## What this project does

Hyperliquid copy-trading agent that mirrors a leader's positions into a follower account. [README](https://github.com/Gajesh2007/copytrading-agent/blob/5422835ea77acdd8ef2867814b38f6c921ec2c40/README.md).

## Mechanism inspected

Before each sync it fetches follower `clearinghouseState`, computes target deltas, filters dust and submits IOC orders with per-order status classification. [Implementation](https://github.com/Gajesh2007/copytrading-agent/blob/5422835ea77acdd8ef2867814b38f6c921ec2c40/src/services/tradeExecutor.ts#L103-L223).

## Limitation that matters

Submission errors are logged and the inspected function does not immediately reconcile uncertain outcomes; mark-price fallback to entry price can be stale. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Reconcile submitted client IDs and fresh fills before the next target-delta cycle, including mixed batch results.

## Why this score

Before each sync it fetches follower `clearinghouseState`, computes target deltas, filters dust and submits IOC orders with per-order status classification. Submission errors are logged and the inspected function does not immediately reconcile uncertain outcomes; mark-price fallback to entry price can be stale.

## Source trail

[README](https://github.com/Gajesh2007/copytrading-agent/blob/5422835ea77acdd8ef2867814b38f6c921ec2c40/README.md) · [Implementation](https://github.com/Gajesh2007/copytrading-agent/blob/5422835ea77acdd8ef2867814b38f6c921ec2c40/src/services/tradeExecutor.ts#L103-L223).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
