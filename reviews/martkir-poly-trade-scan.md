# poly-trade-scan - Does a streamed Polygon block produce a complete trade tape?

**Decision question:** Does a streamed Polygon block produce a complete trade tape?

| Field | Review |
| --- | --- |
| Upstream | [martkir/poly-trade-scan](https://github.com/martkir/poly-trade-scan) |
| Primary area | Market Data & Ingestion |
| Source commit | [232f5fafc1b99c62ec2c0511db35a185f34bdcd6](https://github.com/martkir/poly-trade-scan/commit/232f5fafc1b99c62ec2c0511db35a185f34bdcd6) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Streams candidate Polymarket transactions from Polygon blocks. A transaction with multiple fills may produce only one TradeData row. |

## What this project does

A Polymarket trade monitor that subscribes to Polygon blocks, fetches transactions and receipts, and emits decoded wallet trades.

## Mechanism inspected

For each block it builds a receipt lookup, decodes matching transaction input, and emits a TradeData event; the monitor dispatches results asynchronously to callbacks.

## Limitation that matters

The inspected transaction path returns at most one matched trade for a transaction. A multi-fill transaction can therefore be undercounted, and callback tasks do not establish durable processing or restart backfill. No root license was verified.

## Practical check for a trading system

Count emitted fills against chain event logs and retain a block cursor before claiming a complete wallet tape.

## Why this score

2/5. Useful as a block-streaming sketch, but the one-event-per-transaction shape limits data completeness.

## Source trail

[README](https://github.com/martkir/poly-trade-scan/blob/232f5fafc1b99c62ec2c0511db35a185f34bdcd6/README.md#L1); [src/core/block_processor.py](https://github.com/martkir/poly-trade-scan/blob/232f5fafc1b99c62ec2c0511db35a185f34bdcd6/src/core/block_processor.py#L35); [src/core/block_processor.py](https://github.com/martkir/poly-trade-scan/blob/232f5fafc1b99c62ec2c0511db35a185f34bdcd6/src/core/block_processor.py#L76); [src/monitor.py](https://github.com/martkir/poly-trade-scan/blob/232f5fafc1b99c62ec2c0511db35a185f34bdcd6/src/monitor.py#L58).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
