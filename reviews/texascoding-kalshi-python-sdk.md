# Kalshi Python SDK - Can a slow consumer lose order-book deltas yet see a clean stream shutdown?

**Decision question:** Can a slow consumer lose order-book deltas yet see a clean stream shutdown?

| Field | Review |
| --- | --- |
| Upstream | [TexasCoding/kalshi-python-sdk](https://github.com/TexasCoding/kalshi-python-sdk) |
| Primary area | Market Data & Ingestion |
| Source commit | [a7ec5c9d38f297403690e2b1490c0e80d1e890bf](https://github.com/TexasCoding/kalshi-python-sdk/commit/a7ec5c9d38f297403690e2b1490c0e80d1e890bf) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its sequence tracker drops duplicates and gap/reset frames; the queue raises a labelled backpressure error for stateful channels and delivers it after already buffered messages. The caller must still clear book state and resubscribe on the gap callback; a complete fill ledger is outside this path. |

## What this project does

A typed Kalshi SDK with sequence tracking and bounded WebSocket queues.

## Mechanism inspected

Its sequence tracker drops duplicates and gap/reset frames; the queue raises a labelled backpressure error for stateful channels and delivers it after already buffered messages.

## Limitation that matters

The caller must still clear book state and resubscribe on the gap callback; a complete fill ledger is outside this path.

## Practical check for a trading system

Use channel-specific overflow policy and propagate terminal errors to consumers without discarding prior evidence.

## Why this score

4/5. The source addresses two failure modes that commonly create silent book corruption.

## Source trail

[README](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/README.md#L1); [kalshi/ws/sequence.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/ws/sequence.py#L49); [kalshi/ws/sequence.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/ws/sequence.py#L100); [kalshi/ws/backpressure.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/ws/backpressure.py#L34); [kalshi/ws/backpressure.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/ws/backpressure.py#L82); [kalshi/ws/backpressure.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/ws/backpressure.py#L114); [kalshi/perps/ws/client.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/perps/ws/client.py#L614); [kalshi/perps/ws/client.py](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/kalshi/perps/ws/client.py#L630); [Root license](https://github.com/TexasCoding/kalshi-python-sdk/blob/a7ec5c9d38f297403690e2b1490c0e80d1e890bf/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
