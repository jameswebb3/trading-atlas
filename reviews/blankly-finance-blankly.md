# blankly - Does a multi-exchange book prove feed continuity?

**Decision question:** Does a multi-exchange book prove feed continuity?

| Field | Review |
| --- | --- |
| Upstream | [blankly-finance/blankly](https://github.com/blankly-finance/blankly) |
| Primary area | Market Data & Ingestion |
| Source commit | [daeea3dcc168af597e9ca904712db14957d8199f](https://github.com/blankly-finance/blankly/commit/daeea3dcc168af597e9ca904712db14957d8199f) |
| Reviewed | 2026-10-11 |
| Declared license | LGPL |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The orderbook manager dispatches venue snapshots and updates into a common price-level representation. This manager includes legacy venue handlers and the inspected path does not establish a durable sequence-gap certificate. |

## What this project does

A multi-asset trading and backtesting framework with exchange-specific WebSocket book handlers.

## Mechanism inspected

The orderbook manager dispatches venue snapshots and updates into a common price-level representation.

## Limitation that matters

This manager includes legacy venue handlers and the inspected path does not establish a durable sequence-gap certificate.

## Practical check for a trading system

Compare each venue snapshot and delta stream against source sequence rules before allowing a book into research or execution.

## Why this score

2/5. A normalization layer exists, but continuity evidence is weaker than a source-verified book.

## Source trail

[README](https://github.com/blankly-finance/blankly/blob/daeea3dcc168af597e9ca904712db14957d8199f/README.md#L1); [blankly/exchanges/managers/orderbook_manager.py](https://github.com/blankly-finance/blankly/blob/daeea3dcc168af597e9ca904712db14957d8199f/blankly/exchanges/managers/orderbook_manager.py#L99); [Root license](https://github.com/blankly-finance/blankly/blob/daeea3dcc168af597e9ca904712db14957d8199f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
