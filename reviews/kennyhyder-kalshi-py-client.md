# Kalshi Py Client - Can malformed WebSocket frames disappear without a gap signal?

**Decision question:** Can malformed WebSocket frames disappear without a gap signal?

| Field | Review |
| --- | --- |
| Upstream | [kennyhyder/kalshi-py-client](https://github.com/kennyhyder/kalshi-py-client) |
| Primary area | Market Data & Ingestion |
| Source commit | [7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af](https://github.com/kennyhyder/kalshi-py-client/commit/7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | The message iterator decodes each inbound frame as JSON and yields parsed messages. It catches JSONDecodeError and continues without a count, raw-frame record or invalidation signal; downstream consumers can see an apparently continuous stream. |

## What this project does

A minimal Kalshi REST and WebSocket client.

## Mechanism inspected

The message iterator decodes each inbound frame as JSON and yields parsed messages.

## Limitation that matters

It catches JSONDecodeError and continues without a count, raw-frame record or invalidation signal; downstream consumers can see an apparently continuous stream.

## Practical check for a trading system

Record the raw malformed frame and force resynchronization for stateful feeds.

## Why this score

1/5. A direct negative example for market-data capture.

## Source trail

[README](https://github.com/kennyhyder/kalshi-py-client/blob/7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af/README.md#L1); [kalshi/ws/client.py](https://github.com/kennyhyder/kalshi-py-client/blob/7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af/kalshi/ws/client.py#L87); [kalshi/ws/client.py](https://github.com/kennyhyder/kalshi-py-client/blob/7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af/kalshi/ws/client.py#L102); [Root license](https://github.com/kennyhyder/kalshi-py-client/blob/7cf3782a6e8a5ad53f2232b7f8d74a2e548f61af/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
