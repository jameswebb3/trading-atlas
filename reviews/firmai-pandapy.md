# PandaPy - What happens when date inference hides a parsing failure?

**Decision question:** What happens when date inference hides a parsing failure?

| Field | Review |
| --- | --- |
| Upstream | [firmai/pandapy](https://github.com/firmai/pandapy) |
| Primary area | Data Quality & Lineage |
| Source commit | [120d36c5f8802a7c5c2d58179b7908d0bc823a44](https://github.com/firmai/pandapy/commit/120d36c5f8802a7c5c2d58179b7908d0bc823a44) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The date detector samples the first value of each ten-character text column and catches any exception as not-a-date. A single sampled row and bare exception handler can mask mixed date formats or a broken parser. |

## What this project does

A structured-array data helper with automatic date-column inference.

## Mechanism inspected

The date detector samples the first value of each ten-character text column and catches any exception as not-a-date.

## Limitation that matters

A single sampled row and bare exception handler can mask mixed date formats or a broken parser.

## Practical check for a trading system

Validate the full column and surface parse failures with row counts.

## Why this score

1/5. This is a small ingestion anti-pattern; stronger market-data contracts are needed.

## Source trail

[README](https://github.com/firmai/pandapy/blob/120d36c5f8802a7c5c2d58179b7908d0bc823a44/README.md#L1); [pandapy/__init__.py](https://github.com/firmai/pandapy/blob/120d36c5f8802a7c5c2d58179b7908d0bc823a44/pandapy/__init__.py#L34); [pandapy/__init__.py](https://github.com/firmai/pandapy/blob/120d36c5f8802a7c5c2d58179b7908d0bc823a44/pandapy/__init__.py#L51).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
