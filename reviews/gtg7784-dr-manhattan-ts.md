# dr-manhattan-ts - Does a resubscribed order book restart from a verified snapshot?

**Decision question:** Does a resubscribed order book restart from a verified snapshot?

| Field | Review |
| --- | --- |
| Upstream | [gtg7784/dr-manhattan-ts](https://github.com/gtg7784/dr-manhattan-ts) |
| Primary area | Market Data & Ingestion |
| Source commit | [f250ab05043172672921ec5983c1bcc930a30380](https://github.com/gtg7784/dr-manhattan-ts/commit/f250ab05043172672921ec5983c1bcc930a30380) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | On reconnect it reauthenticates and resubscribes stored market IDs, then parses incoming messages for callbacks. The inspected core WebSocket layer records last-message time but has no sequence continuity or snapshot-recovery contract. |

## What this project does

A TypeScript WebSocket client for prediction-market order books.

## Mechanism inspected

On reconnect it reauthenticates and resubscribes stored market IDs, then parses incoming messages for callbacks.

## Limitation that matters

The inspected core WebSocket layer records last-message time but has no sequence continuity or snapshot-recovery contract.

## Practical check for a trading system

Invalidate the book on disconnect and restore it only after a source-verified snapshot plus contiguous updates.

## Why this score

2/5. Resubscription is helpful operationally but cannot alone certify book completeness.

## Source trail

[README](https://github.com/gtg7784/dr-manhattan-ts/blob/f250ab05043172672921ec5983c1bcc930a30380/README.md#L1); [src/core/websocket.ts](https://github.com/gtg7784/dr-manhattan-ts/blob/f250ab05043172672921ec5983c1bcc930a30380/src/core/websocket.ts#L88); [Root license](https://github.com/gtg7784/dr-manhattan-ts/blob/f250ab05043172672921ec5983c1bcc930a30380/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
