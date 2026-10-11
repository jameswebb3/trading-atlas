# BTrace Circular Buffer - Can a bounded event buffer overwrite evidence without a loss receipt?

**Decision question:** Can a bounded event buffer overwrite evidence without a loss receipt?

| Field | Review |
| --- | --- |
| Upstream | [btraceio/btrace](https://github.com/btraceio/btrace) |
| Primary area | Operations & Observability |
| Source commit | [7fb5c31d3ca0c41dbfceef05c05a268b8000e940](https://github.com/btraceio/btrace/commit/7fb5c31d3ca0c41dbfceef05c05a268b8000e940) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Adding an element writes by modulo index, advances the read cursor when occupied and caps stored length. The overwritten entry is not counted or reported in this class, so a consumer cannot infer complete capture from buffer contents. |

## What this project does

A JVM tracing toolkit with a circular buffer.

## Mechanism inspected

Adding an element writes by modulo index, advances the read cursor when occupied and caps stored length.

## Limitation that matters

The overwritten entry is not counted or reported in this class, so a consumer cannot infer complete capture from buffer contents.

## Practical check for a trading system

Count evictions and treat any drop as an explicit capture gap.

## Why this score

2/5. The overwrite path is directly instructive for trading event collectors.

## Source trail

[README](https://github.com/btraceio/btrace/blob/7fb5c31d3ca0c41dbfceef05c05a268b8000e940/README.md#L1); [btrace-core/src/main/java/org/openjdk/btrace/core/CircularBuffer.java](https://github.com/btraceio/btrace/blob/7fb5c31d3ca0c41dbfceef05c05a268b8000e940/btrace-core/src/main/java/org/openjdk/btrace/core/CircularBuffer.java#L16); [btrace-core/src/main/java/org/openjdk/btrace/core/CircularBuffer.java](https://github.com/btraceio/btrace/blob/7fb5c31d3ca0c41dbfceef05c05a268b8000e940/btrace-core/src/main/java/org/openjdk/btrace/core/CircularBuffer.java#L25).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
