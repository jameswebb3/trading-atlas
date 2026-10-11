# aya - Treat dropped observations as first-class events

**Decision question:** Does a full event buffer expose how many records it lost?

| Field | Review |
| --- | --- |
| Upstream | [aya-rs/aya](https://github.com/aya-rs/aya) |
| Primary area | Market Data & Ingestion |
| Source commit | [8617e205065b91ba896511eead9be0835c86010a](https://github.com/aya-rs/aya/commit/8617e205065b91ba896511eead9be0835c86010a) |
| Reviewed | 2026-10-10 |
| Declared license | MIT OR Apache-2.0 ([MIT](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/LICENSE-MIT), [Apache](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/LICENSE-APACHE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The perf buffer yields either Sample or Lost with a count decoded from PERF_RECORD_LOST; a fixture verifies the count is delivered to the caller. It only detects losses reported by that kernel buffer. An upstream producer that never emitted an event remains invisible to this path. |

## What this project does

Aya supplies Rust APIs for eBPF programs and perf-event buffers. [README](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/README.md).

## Mechanism inspected

The perf buffer yields either Sample or Lost with a count decoded from PERF_RECORD_LOST; a fixture verifies the count is delivered to the caller. [Implementation](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/aya/src/maps/perf/perf_buffer.rs#L79-L90). [Related path](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/aya/src/maps/perf/perf_buffer.rs#L293-L305).

## Limitation that matters

It only detects losses reported by that kernel buffer. An upstream producer that never emitted an event remains invisible to this path. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Carry a loss count and its source through ingestion health; combine it with sequence and source-heartbeat checks.

## Why this score

A typed loss event is a precise completeness control, while the Linux-specific transport and unobserved upstream gaps limit direct transfer.

## Source trail

[README](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/README.md) - [Implementation](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/aya/src/maps/perf/perf_buffer.rs#L79-L90) - [Related path](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/aya/src/maps/perf/perf_buffer.rs#L293-L305) - [MIT](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/LICENSE-MIT) - [Apache](https://github.com/aya-rs/aya/blob/8617e205065b91ba896511eead9be0835c86010a/LICENSE-APACHE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
