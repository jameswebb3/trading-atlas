# waltz — Architecture lineage is not data provenance

**Decision question:** Can an incoming flow be discovered from explicit entity references?

| Field | Review |
| --- | --- |
| Upstream | [waltz](https://github.com/finos/waltz) |
| Primary area | Data Quality & Lineage |
| Source commit | [f0af61fe3b7ba79454983b56fd948cae4bb551b6](https://github.com/finos/waltz/commit/f0af61fe3b7ba79454983b56fd948cae4bb551b6) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0 (SPDX declaration)](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/LICENSE.spdx) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The inspected harness queries incoming logical flows for a set of entity references. This is application-flow discovery, not row-level temporal lineage; the full platform is larger than a focused trading-data catalog needs. |

## What this project does

An enterprise architecture inventory that models applications and logical flows. [README](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/README.md).

## Mechanism inspected

The inspected harness queries incoming logical flows for a set of entity references. [Implementation](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/waltz-jobs/src/main/java/org/finos/waltz/jobs/harness/FlowLineageHarness.java#L49-L103).

## Limitation that matters

This is application-flow discovery, not row-level temporal lineage; the full platform is larger than a focused trading-data catalog needs. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Use the distinction to prevent a topology map from being mistaken for proof of a dataset's available_at.

## Why this score

Indirect relevance only: The inspected harness queries incoming logical flows for a set of entity references. This is application-flow discovery, not row-level temporal lineage; the full platform is larger than a focused trading-data catalog needs.

## Source trail

[README](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/README.md) · [Documentation](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/docs/features/README.md) · [Implementation](https://github.com/finos/waltz/blob/f0af61fe3b7ba79454983b56fd948cae4bb551b6/waltz-jobs/src/main/java/org/finos/waltz/jobs/harness/FlowLineageHarness.java#L49-L103).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
