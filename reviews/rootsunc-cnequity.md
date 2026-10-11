# CNEquity — Reconstructed history must not pass as point-in-time data

**Decision question:** Will a historical query reject a value collected only after the decision date?

| Field | Review |
| --- | --- |
| Upstream | [rootSunc/CNEquity](https://github.com/rootSunc/CNEquity) |
| Primary area | Data Quality & Lineage |
| Source commit | [c118038ea82b5bb78783c0c17a1d9251b36de71d](https://github.com/rootSunc/CNEquity/commit/c118038ea82b5bb78783c0c17a1d9251b36de71d) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/LICENSE)) |
| Review depth | 3/3: README and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Its strict point-in-time filter checks announcement, availability, source publication and local observation against as_of, and rejects reconstructed/backfill sources; best-effort keeps them with pit_is_exact=false. A test contrasts both modes. The reconstruction flag is partly inferred from source-name text and the inspected filter works at date granularity; intraday HL decisions need timestamp-level receipt and stronger provenance. |

## What this project does

Local Parquet market-data lake with incremental collection, quality audits, versioned facts and point-in-time query modes. [README](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/README.md).

## Mechanism inspected

Its strict point-in-time filter checks announcement, availability, source publication and local observation against as_of, and rejects reconstructed/backfill sources; best-effort keeps them with pit_is_exact=false. A test contrasts both modes. [Implementation](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/src/cnequity/domain/pit.py#L225-L317). [Test source](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/tests/unit/test_pit_vintages.py#L112-L148).

## Limitation that matters

The reconstruction flag is partly inferred from source-name text and the inspected filter works at date granularity; intraday HL decisions need timestamp-level receipt and stronger provenance. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Separate exact contemporaneous observations from reconstructed backfills in every historical feature join, and fail a decision-grade trial when only best-effort history exists.

## Why this score

Its strict point-in-time filter checks announcement, availability, source publication and local observation against as_of, and rejects reconstructed/backfill sources; best-effort keeps them with pit_is_exact=false. A test contrasts both modes. The reconstruction flag is partly inferred from source-name text and the inspected filter works at date granularity; intraday HL decisions need timestamp-level receipt and stronger provenance.

## Source trail

[README](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/README.md) · [Implementation](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/src/cnequity/domain/pit.py#L225-L317) · [Test source](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/tests/unit/test_pit_vintages.py#L112-L148) · [License](https://github.com/rootSunc/CNEquity/blob/c118038ea82b5bb78783c0c17a1d9251b36de71d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
