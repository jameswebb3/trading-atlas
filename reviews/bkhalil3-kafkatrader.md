# KafkaTrader - Can a Kafka book consumer know it has every Kalshi delta?

**Decision question:** Can a Kafka book consumer know it has every Kalshi delta?

| Field | Review |
| --- | --- |
| Upstream | [bkhalil3/KafkaTrader](https://github.com/bkhalil3/KafkaTrader) |
| Primary area | Market Data & Ingestion |
| Source commit | [b78b1fdcb66ae523fa69af3e0bc6bf849233e02c](https://github.com/bkhalil3/KafkaTrader/commit/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Applies Kalshi price-level deltas and republishes book state through Kafka. Neither delta sequence nor fresh-snapshot readiness is established in the inspected path. |

## What this project does

A Kalshi market-data and order-management scaffold that republishes local book state to Kafka.

## Mechanism inspected

OrderBook applies price-level size deltas, rejects negative resulting quantities, updates best prices and emits the reconstructed book to a Kafka topic. A consumer can start from the latest topic offset.

## Limitation that matters

The inspected update path does not check exchange sequence numbers or request a fresh snapshot after a gap. A latest-offset consumer can begin after prior messages with no guarantee it has a complete initial book. The order-management risk check is mostly placeholder code. No root license text was verified.

## Practical check for a trading system

Require snapshot plus contiguous sequence and explicit invalid-state handling before distributing a book as current.

## Why this score

2/5. Useful as a concrete negative-quantity guard, but insufficient as a continuous feed contract.

## Source trail

[README](https://github.com/bkhalil3/KafkaTrader/blob/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c/README.md#L8); [OrderBook.py](https://github.com/bkhalil3/KafkaTrader/blob/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c/OrderBook.py#L113); [OrderBook.py](https://github.com/bkhalil3/KafkaTrader/blob/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c/OrderBook.py#L131); [OrderBook.py](https://github.com/bkhalil3/KafkaTrader/blob/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c/OrderBook.py#L183); [OrderManagementSystem.py](https://github.com/bkhalil3/KafkaTrader/blob/b78b1fdcb66ae523fa69af3e0bc6bf849233e02c/OrderManagementSystem.py#L76).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
