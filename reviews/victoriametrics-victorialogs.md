# VictoriaLogs - How can a log batch retain stream and timestamp alignment?

**Decision question:** How can a log batch retain stream and timestamp alignment?

| Field | Review |
| --- | --- |
| Upstream | [VictoriaMetrics/VictoriaLogs](https://github.com/VictoriaMetrics/VictoriaLogs) |
| Primary area | Operations & Observability |
| Source commit | [243c18b91cd0478638a9bb243ac04e8f16356dc5](https://github.com/VictoriaMetrics/VictoriaLogs/commit/243c18b91cd0478638a9bb243ac04e8f16356dc5) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | logRows appends stream ID, timestamp and fields in parallel indexed slices and canonicalizes field names. The aligned row structure alone does not certify that every expected producer event arrived. |

## What this project does

A log storage engine that batches rows by stream and timestamp.

## Mechanism inspected

logRows appends stream ID, timestamp and fields in parallel indexed slices and canonicalizes field names.

## Limitation that matters

The aligned row structure alone does not certify that every expected producer event arrived.

## Practical check for a trading system

Pair indexed log rows with expected sequence counts and gap records.

## Why this score

2/5. The storage mechanism is useful as a reference for coherent event rows, with no completeness certificate.

## Source trail

[README](https://github.com/VictoriaMetrics/VictoriaLogs/blob/243c18b91cd0478638a9bb243ac04e8f16356dc5/README.md#L1); [lib/logstorage/log_rows.go](https://github.com/VictoriaMetrics/VictoriaLogs/blob/243c18b91cd0478638a9bb243ac04e8f16356dc5/lib/logstorage/log_rows.go#L107); [lib/logstorage/log_rows.go](https://github.com/VictoriaMetrics/VictoriaLogs/blob/243c18b91cd0478638a9bb243ac04e8f16356dc5/lib/logstorage/log_rows.go#L140).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
