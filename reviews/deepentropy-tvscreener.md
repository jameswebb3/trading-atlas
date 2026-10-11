# TVScreener - What should ingestion do when upstream response columns collide?

**Decision question:** What should ingestion do when upstream response columns collide?

| Field | Review |
| --- | --- |
| Upstream | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) |
| Primary area | Market Data & Ingestion |
| Source commit | [6faf496fa8b2af205eb485784412a48222986e96](https://github.com/deepentropy/tvscreener/commit/6faf496fa8b2af205eb485784412a48222986e96) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The base parser detects duplicate column labels and renames subsequent collisions with stable suffixes. Renaming lets data load but may hide an upstream schema shift unless the collision is reported. |

## What this project does

A market screener client with response-table normalization.

## Mechanism inspected

The base parser detects duplicate column labels and renames subsequent collisions with stable suffixes.

## Limitation that matters

Renaming lets data load but may hide an upstream schema shift unless the collision is reported.

## Practical check for a trading system

Fail or warn on duplicate field labels and preserve the raw response schema.

## Why this score

2/5. This small ingestion guard prevents ambiguous field access; it is not historical data verification.

## Source trail

[README](https://github.com/deepentropy/tvscreener/blob/6faf496fa8b2af205eb485784412a48222986e96/README.md#L1); [tvscreener/core/base.py](https://github.com/deepentropy/tvscreener/blob/6faf496fa8b2af205eb485784412a48222986e96/tvscreener/core/base.py#L44); [tvscreener/core/base.py](https://github.com/deepentropy/tvscreener/blob/6faf496fa8b2af205eb485784412a48222986e96/tvscreener/core/base.py#L79).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
