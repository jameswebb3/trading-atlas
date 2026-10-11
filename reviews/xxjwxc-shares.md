# Ashare - Can provider failover change a price series without leaving provenance?

**Decision question:** Can provider failover change a price series without leaving provenance?

| Field | Review |
| --- | --- |
| Upstream | [xxjwxc/shares](https://github.com/xxjwxc/shares) |
| Primary area | Market Data & Ingestion |
| Source commit | [21b847bb8dcdafaca7ebefe13401b5b10194a267](https://github.com/xxjwxc/shares/commit/21b847bb8dcdafaca7ebefe13401b5b10194a267) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The fetch wrapper retries another provider on any exception from the primary source. It returns the fallback data without a source flag or reason, so downstream series can mix provider semantics invisibly. |

## What this project does

An A-share price reader with primary and fallback data providers.

## Mechanism inspected

The fetch wrapper retries another provider on any exception from the primary source.

## Limitation that matters

It returns the fallback data without a source flag or reason, so downstream series can mix provider semantics invisibly.

## Practical check for a trading system

Attach provider identity and fallback reason to every ingested series.

## Why this score

2/5. The broad exception fallback is a useful warning for market-data provenance.

## Source trail

[README](https://github.com/xxjwxc/shares/blob/21b847bb8dcdafaca7ebefe13401b5b10194a267/README.md#L1); [python/Ashare.py](https://github.com/xxjwxc/shares/blob/21b847bb8dcdafaca7ebefe13401b5b10194a267/python/Ashare.py#L70); [python/Ashare.py](https://github.com/xxjwxc/shares/blob/21b847bb8dcdafaca7ebefe13401b5b10194a267/python/Ashare.py#L79); [Root license](https://github.com/xxjwxc/shares/blob/21b847bb8dcdafaca7ebefe13401b5b10194a267/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
