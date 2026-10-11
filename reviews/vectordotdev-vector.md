# vector — An empty bounded queue may admit one oversized event

**Decision question:** Does a byte limit always bound memory usage?

| Field | Review |
| --- | --- |
| Upstream | [vectordotdev/vector](https://github.com/vectordotdev/vector) |
| Primary area | Operations & Observability |
| Source commit | [f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8](https://github.com/vectordotdev/vector/commit/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8) |
| Reviewed | 2026-10-09 |
| Declared license | MPL-2.0 ([source](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/LICENSE-3rdparty.csv)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The channel caps permits charged for an item at the queue limit, allowing a single oversized item into an empty queue to avoid deadlock. An event larger than the configured limit can still be resident; the limit is not an absolute memory ceiling. |

## What this project does

Event pipeline with memory-buffer channels and backpressure. [README](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/README.md).

## Mechanism inspected

The channel caps permits charged for an item at the queue limit, allowing a single oversized item into an empty queue to avoid deadlock. [Implementation](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/lib/vector-buffers/src/topology/channel/limited_queue.rs#L330-L369).

## Limitation that matters

An event larger than the configured limit can still be resident; the limit is not an absolute memory ceiling. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Test pathological exchange payload sizes and define reject, spill or quarantine behavior for oversized messages.

## Why this score

The channel caps permits charged for an item at the queue limit, allowing a single oversized item into an empty queue to avoid deadlock. An event larger than the configured limit can still be resident; the limit is not an absolute memory ceiling.

## Source trail

[README](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/README.md) · [Implementation](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/lib/vector-buffers/src/topology/channel/limited_queue.rs#L330-L369) · [License](https://github.com/vectordotdev/vector/blob/f6cf6c992b5cbee85bc1bd0da822548b1fb57dc8/LICENSE-3rdparty.csv).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
