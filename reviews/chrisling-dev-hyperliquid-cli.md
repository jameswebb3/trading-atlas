# hyperliquid-cli - What happens to pending requests when a local socket closes?

**Decision question:** What happens to pending requests when a local socket closes?

| Field | Review |
| --- | --- |
| Upstream | [chrisling-dev/hyperliquid-cli](https://github.com/chrisling-dev/hyperliquid-cli) |
| Primary area | Operations & Observability |
| Source commit | [c32a108b37cab18a281f186ef39ee817baf6b5d2](https://github.com/chrisling-dev/hyperliquid-cli/commit/c32a108b37cab18a281f186ef39ee817baf6b5d2) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | It tracks request IDs, times out requests and rejects all pending promises on socket close. A local timeout cannot prove whether an already-sent exchange order landed. |

## What this project does

A Hyperliquid CLI with a local RPC server.

## Mechanism inspected

It tracks request IDs, times out requests and rejects all pending promises on socket close.

## Limitation that matters

A local timeout cannot prove whether an already-sent exchange order landed.

## Practical check for a trading system

Reconcile by client order ID before retrying a timed-out order.

## Why this score

2/5. Sound IPC cleanup; venue outcome remains unknown.

## Source trail

[README](https://github.com/chrisling-dev/hyperliquid-cli/blob/c32a108b37cab18a281f186ef39ee817baf6b5d2/README.md#L1); [src/client/index.ts](https://github.com/chrisling-dev/hyperliquid-cli/blob/c32a108b37cab18a281f186ef39ee817baf6b5d2/src/client/index.ts#L65); [Root license](https://github.com/chrisling-dev/hyperliquid-cli/blob/c32a108b37cab18a281f186ef39ee817baf6b5d2/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
