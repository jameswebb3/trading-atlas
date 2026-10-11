# Stock SDK Cache - Does a quote cache separate TTL expiry from source freshness?

**Decision question:** Does a quote cache separate TTL expiry from source freshness?

| Field | Review |
| --- | --- |
| Upstream | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) |
| Primary area | Market Data & Ingestion |
| Source commit | [c6c9a790870c5c607379e542e214a02ea05979c4](https://github.com/chengzuopeng/stock-sdk/commit/c6c9a790870c5c607379e542e214a02ea05979c4) |
| Reviewed | 2026-10-11 |
| Declared license | ISC |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It expires entries against Date.now and refreshes last-access time when a value is read. A live cache TTL does not identify the market timestamp or coverage of the quote returned. |

## What this project does

An equity quote SDK with in-memory TTL and LRU caching.

## Mechanism inspected

It expires entries against Date.now and refreshes last-access time when a value is read.

## Limitation that matters

A live cache TTL does not identify the market timestamp or coverage of the quote returned.

## Practical check for a trading system

Store source event time and receive time alongside cache age before treating a quote as fresh.

## Why this score

2/5. The cache implementation is concrete, but freshness needs source timestamps.

## Source trail

[README](https://github.com/chengzuopeng/stock-sdk/blob/c6c9a790870c5c607379e542e214a02ea05979c4/README.md#L1); [src/core/cache.ts](https://github.com/chengzuopeng/stock-sdk/blob/c6c9a790870c5c607379e542e214a02ea05979c4/src/core/cache.ts#L53); [src/core/cache.ts](https://github.com/chengzuopeng/stock-sdk/blob/c6c9a790870c5c607379e542e214a02ea05979c4/src/core/cache.ts#L80); [Root license](https://github.com/chengzuopeng/stock-sdk/blob/c6c9a790870c5c607379e542e214a02ea05979c4/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
