# dplyneage - Leave conflicting lineage metadata unresolved

**Decision question:** When two upstream columns disagree, should lineage invent a single type or label?

| Field | Review |
| --- | --- |
| Upstream | [tgerke/dplyneage](https://github.com/tgerke/dplyneage) |
| Primary area | Data Quality & Lineage |
| Source commit | [ef3d30d9f8a055c55065fb804256ad8b2e299da0](https://github.com/tgerke/dplyneage/commit/ef3d30d9f8a055c55065fb804256ad8b2e299da0) |
| Reviewed | 2026-10-10 |
| Declared license | OSL-3.0 ([source](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Metadata propagation runs only along identity edges. It accumulates candidate values to a fixpoint, never overwrites a target’s own value and fills a missing field only when exactly one candidate survives; conflicting inputs stay empty. The inspected algorithm deliberately propagates nothing across transformed, aggregated or indirect edges. A blank field means unresolved, not verified absence. The source uses OSL-3.0; copying code or adding the package has license cost. |

## What this project does

dplyneage extracts and displays column lineage across R and SQL transformation pipelines. [README](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/README.md).

## Mechanism inspected

Metadata propagation runs only along identity edges. It accumulates candidate values to a fixpoint, never overwrites a target’s own value and fills a missing field only when exactly one candidate survives; conflicting inputs stay empty. [Implementation](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/R/lineage_pipeline.R#L344-L400). [Related path](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/R/lineage_pipeline.R#L1-L32).

## Limitation that matters

The inspected algorithm deliberately propagates nothing across transformed, aggregated or indirect edges. A blank field means unresolved, not verified absence. The source uses OSL-3.0; copying code or adding the package has license cost. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

In a dataset-lineage map, preserve conflicting upstream classifications as unresolved and make the conflict visible before an experiment consumes the merged column.

## Why this score

It gives a concrete way to avoid false certainty in lineage, with a domain and license boundary that favors implementing the small rule locally.

## Source trail

[README](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/README.md) - [Implementation](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/R/lineage_pipeline.R#L344-L400) - [Related path](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/R/lineage_pipeline.R#L1-L32) - [License](https://github.com/tgerke/dplyneage/blob/ef3d30d9f8a055c55065fb804256ad8b2e299da0/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
