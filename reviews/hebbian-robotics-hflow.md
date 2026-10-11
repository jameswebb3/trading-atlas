# hflow - Record failed inputs even when no data row exists

**Decision question:** How do you count sources that never made it into the catalog?

| Field | Review |
| --- | --- |
| Upstream | [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) |
| Primary area | Data Quality & Lineage |
| Source commit | [bf87451d0a8cf68a49489a55d7534d913afbb96e](https://github.com/Hebbian-Robotics/hflow/commit/bf87451d0a8cf68a49489a55d7534d913afbb96e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | record_ingest_failure classifies the error, retains original type/message, fingerprints stable source/stage/version fields, and stores one failure record only if absent. Classification is heuristic and the fingerprint deliberately collapses repeated attempts; attempt frequency needs a separate counter or event stream. |

## What this project does

A robotics data pipeline catalogs canonical episodes and keeps a separate ingest-failure ledger for sources that never became episodes. [README](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/README.md).

## Mechanism inspected

record_ingest_failure classifies the error, retains original type/message, fingerprints stable source/stage/version fields, and stores one failure record only if absent. [Implementation](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/src/hflow/ingest_ledger.py#L149-L211).

## Limitation that matters

Classification is heuristic and the fingerprint deliberately collapses repeated attempts; attempt frequency needs a separate counter or event stream. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Reconcile expected market-data partitions against both successful manifests and explicit failure records; do not infer completeness from successful rows alone.

## Why this score

record_ingest_failure classifies the error, retains original type/message, fingerprints stable source/stage/version fields, and stores one failure record only if absent. Classification is heuristic and the fingerprint deliberately collapses repeated attempts; attempt frequency needs a separate counter or event stream.

## Source trail

[README](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/README.md) - [Implementation](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/src/hflow/ingest_ledger.py#L149-L211) - [License](https://github.com/Hebbian-Robotics/hflow/blob/bf87451d0a8cf68a49489a55d7534d913afbb96e/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
