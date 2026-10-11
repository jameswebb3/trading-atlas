# SpreadZero - Can a YES/NO book preserve native sides?

**Decision question:** Can a YES/NO book preserve native sides?

| Field | Review |
| --- | --- |
| Upstream | [easwar16/SpreadZero](https://github.com/easwar16/SpreadZero) |
| Primary area | Market Data & Ingestion |
| Source commit | [b46a9d08c6905e1cfb009b072fe08554a175ab0f](https://github.com/easwar16/SpreadZero/commit/b46a9d08c6905e1cfb009b072fe08554a175ab0f) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It keeps Kalshi YES and NO bids separate, applies native deltas and derives YES asks from NO bids. The normalizer uses floats and does not certify snapshot/delta continuity. |

## What this project does

A cross-venue prediction-market spread scanner.

## Mechanism inspected

It keeps Kalshi YES and NO bids separate, applies native deltas and derives YES asks from NO bids.

## Limitation that matters

The normalizer uses floats and does not certify snapshot/delta continuity.

## Practical check for a trading system

Preserve native side and update order before computing a spread.

## Why this score

3/5. Explicit transformation; source integrity still separate.

## Source trail

[README](https://github.com/easwar16/SpreadZero/blob/b46a9d08c6905e1cfb009b072fe08554a175ab0f/README.md#L1); [apps/backend/src/normalizer.ts](https://github.com/easwar16/SpreadZero/blob/b46a9d08c6905e1cfb009b072fe08554a175ab0f/apps/backend/src/normalizer.ts#L181).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
