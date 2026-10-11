# arnio — Name every row a cleaning step drops

**Decision question:** Can a data-cleaning pipeline explain which observations disappeared at each step?

| Field | Review |
| --- | --- |
| Upstream | [im-anishraj/arnio](https://github.com/im-anishraj/arnio) |
| Primary area | Data Quality & Lineage |
| Source commit | [d966fd742057d422dae3ac037de3af5515410bee](https://github.com/im-anishraj/arnio/commit/d966fd742057d422dae3ac037de3af5515410bee) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It injects a stable sentinel ID, compares survivors after each operation, records dropped input indices by step and errors if a custom step removes the sentinel. The sentinel is an in-memory row position, not a durable market event identity; transformations that duplicate or merge rows need a richer mapping. |

## What this project does

DataFrame cleaning pipeline with optional per-step row lineage. [README](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/README.md).

## Mechanism inspected

It injects a stable sentinel ID, compares survivors after each operation, records dropped input indices by step and errors if a custom step removes the sentinel. [Implementation](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/arnio/pipeline.py#L238-L258). [Related implementation](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/arnio/pipeline.py#L411-L456).

## Limitation that matters

The sentinel is an in-memory row position, not a durable market event identity; transformations that duplicate or merge rows need a richer mapping. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Carry source event IDs through data preparation and write per-stage accepted, dropped and reason counts to the batch manifest.

## Why this score

It injects a stable sentinel ID, compares survivors after each operation, records dropped input indices by step and errors if a custom step removes the sentinel. The sentinel is an in-memory row position, not a durable market event identity; transformations that duplicate or merge rows need a richer mapping.

## Source trail

[README](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/README.md) · [Implementation](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/arnio/pipeline.py#L238-L258) · [Related implementation](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/arnio/pipeline.py#L411-L456) · [License](https://github.com/im-anishraj/arnio/blob/d966fd742057d422dae3ac037de3af5515410bee/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
