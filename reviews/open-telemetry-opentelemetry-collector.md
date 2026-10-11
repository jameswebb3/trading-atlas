# opentelemetry-collector — Retry policy distinguishes permanent failure and deadline

**Decision question:** Which failed exports should never be retried?

| Field | Review |
| --- | --- |
| Upstream | [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) |
| Primary area | Operations & Observability |
| Source commit | [ba1d4a2fb468760915c50fe4dad497c7bc3d1148](https://github.com/open-telemetry/opentelemetry-collector/commit/ba1d4a2fb468760915c50fe4dad497c7bc3d1148) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its sender immediately returns permanent errors, applies backoff to transient ones, honors throttle delays and stops when the next retry exceeds an elapsed-time or context deadline. These are telemetry semantics; order submission needs idempotency and reconciliation before any retry after an uncertain response. |

## What this project does

Telemetry collector that receives, processes and exports traces, metrics and logs. [README](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/README.md).

## Mechanism inspected

Its sender immediately returns permanent errors, applies backoff to transient ones, honors throttle delays and stops when the next retry exceeds an elapsed-time or context deadline. [Implementation](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/exporter/exporterhelper/internal/retry_sender.go#L91-L125).

## Limitation that matters

These are telemetry semantics; order submission needs idempotency and reconciliation before any retry after an uncertain response. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep explicit retry classes and deadlines for collectors; for trading writes, require client identity and exchange-state reconciliation.

## Why this score

Its sender immediately returns permanent errors, applies backoff to transient ones, honors throttle delays and stops when the next retry exceeds an elapsed-time or context deadline. These are telemetry semantics; order submission needs idempotency and reconciliation before any retry after an uncertain response.

## Source trail

[README](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/README.md) · [Implementation](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/exporter/exporterhelper/internal/retry_sender.go#L91-L125) · [License](https://github.com/open-telemetry/opentelemetry-collector/blob/ba1d4a2fb468760915c50fe4dad497c7bc3d1148/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
