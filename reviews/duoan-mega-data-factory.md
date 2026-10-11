# mega-data-factory — Stage totals should use pipeline boundaries, not a sum

**Decision question:** How should a multi-stage data pipeline report input and output N?

| Field | Review |
| --- | --- |
| Upstream | [duoan/mega-data-factory](https://github.com/duoan/mega-data-factory) |
| Primary area | Data Quality & Lineage |
| Source commit | [017864532f2be55b1cdfb7fe1b8579455b701d33](https://github.com/duoan/mega-data-factory/commit/017864532f2be55b1cdfb7fe1b8579455b701d33) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | track_run takes input count from the first stage and output count from the last, sums errors and records stage metrics in a finally block. Its overall pass rate still collapses all causes of attrition into one ratio; the inspected block does not encode causal available_at. |

## What this project does

Distributed multimodal data processing pipeline with per-run and per-stage metrics. [README](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/README.md).

## Mechanism inspected

track_run takes input count from the first stage and output count from the last, sums errors and records stage metrics in a finally block. [Implementation](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/mega_data_factory/framework/metrics/collector.py#L53-L104).

## Limitation that matters

Its overall pass rate still collapses all causes of attrition into one ratio; the inspected block does not encode causal available_at. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Show per-stage drops, explicit failure reasons and first-input/last-output reconciliation for research datasets.

## Why this score

track_run takes input count from the first stage and output count from the last, sums errors and records stage metrics in a finally block. Its overall pass rate still collapses all causes of attrition into one ratio; the inspected block does not encode causal available_at.

## Source trail

[README](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/README.md) · [Implementation](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/mega_data_factory/framework/metrics/collector.py#L53-L104) · [License](https://github.com/duoan/mega-data-factory/blob/017864532f2be55b1cdfb7fe1b8579455b701d33/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
