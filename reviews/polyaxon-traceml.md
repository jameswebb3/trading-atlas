# traceml — Scalar metrics must be scalar

**Decision question:** Can a tracker accept an array as if it were one number?

| Field | Review |
| --- | --- |
| Upstream | [traceml](https://github.com/polyaxon/traceml) |
| Primary area | Research & Reproducibility |
| Source commit | [b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88](https://github.com/polyaxon/traceml/commit/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/polyaxon/traceml/blob/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its metric converter accepts native floats and zero-dimensional arrays, and asserts when a value has more dimensions. It returns UNKNOWN if NumPy is unavailable; a numeric scalar can still be statistically invalid or have zero effective sample. |

## What this project does

An ML event processing engine associated with Polyaxon. [README](https://github.com/polyaxon/traceml/blob/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88/README.md).

## Mechanism inspected

Its metric converter accepts native floats and zero-dimensional arrays, and asserts when a value has more dimensions. [Implementation](https://github.com/polyaxon/traceml/blob/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88/traceml/traceml/processors/events_processors/events_metrics_processors.py#L24-L35).

## Limitation that matters

It returns UNKNOWN if NumPy is unavailable; a numeric scalar can still be statistically invalid or have zero effective sample. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Validate metric shape and unknown status before a run can be called complete.

## Why this score

Transferable engineering pattern: Its metric converter accepts native floats and zero-dimensional arrays, and asserts when a value has more dimensions. It returns UNKNOWN if NumPy is unavailable; a numeric scalar can still be statistically invalid or have zero effective sample.

## Source trail

[README](https://github.com/polyaxon/traceml/blob/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88/README.md) · [Implementation](https://github.com/polyaxon/traceml/blob/b8c5e9dee0bfd38aeb830f7aefea8ecc7463aa88/traceml/traceml/processors/events_processors/events_metrics_processors.py#L24-L35).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
