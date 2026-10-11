# VictoriaMetrics — A bounded metrics queue can drop its oldest observations

**Decision question:** What does a full telemetry queue sacrifice?

| Field | Review |
| --- | --- |
| Upstream | [VictoriaMetrics/VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) |
| Primary area | Operations & Observability |
| Source commit | [2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | FastQueue buffers blocks in memory and spills to disk; the configured persistent size cap drops oldest data, while disabling persistence can reject writes when memory fills. This behavior is acceptable only for explicitly lossy telemetry, never an order, fill or audit journal. |

## What this project does

Time-series metrics database with memory and persistent queueing paths. [README](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/README.md).

## Mechanism inspected

FastQueue buffers blocks in memory and spills to disk; the configured persistent size cap drops oldest data, while disabling persistence can reject writes when memory fills. [Implementation](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/lib/persistentqueue/fastqueue.go#L48-L82).

## Limitation that matters

This behavior is acceptable only for explicitly lossy telemetry, never an order, fill or audit journal. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Classify every queue by loss policy and show dropped-block counters before using telemetry to explain incidents.

## Why this score

FastQueue buffers blocks in memory and spills to disk; the configured persistent size cap drops oldest data, while disabling persistence can reject writes when memory fills. This behavior is acceptable only for explicitly lossy telemetry, never an order, fill or audit journal.

## Source trail

[README](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/README.md) · [Implementation](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/lib/persistentqueue/fastqueue.go#L48-L82) · [License](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/2dcf2265734e00e0f6f4e42a3d0a6beedec0e5b6/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
