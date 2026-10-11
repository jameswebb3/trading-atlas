# Impler — Keep rejected rows alongside accepted imports

**Decision question:** What should a bulk import return when some rows fail schema validation?

| Field | Review |
| --- | --- |
| Upstream | [implerhq/impler.io](https://github.com/implerhq/impler.io) |
| Primary area | Data Quality & Lineage |
| Source commit | [d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93](https://github.com/implerhq/impler.io/commit/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The AJV review service copies input, compiles a schema, and separates valid from invalid rows with recorded errors. A partitioned import can still hide coverage loss if downstream consumers see only accepted rows. |

## What this project does

A data-import platform with schema mappings and review steps. [Project README](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/README.md#L1).

## Mechanism inspected

The AJV review service copies input, compiles a schema, and separates valid from invalid rows with recorded errors. [Implementation](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/apps/api/src/app/review/service/AJV.service.ts#L50).

## Limitation that matters

A partitioned import can still hide coverage loss if downstream consumers see only accepted rows. The platform is larger than a focused market-data validator. This is a source review, not a runtime or security test.

## Practical check for a trading system

Record total, accepted, rejected, and error reasons before exposing any imported trading dataset.

## Why this score

Its valid/invalid partition is a concrete ingestion accounting pattern.

## Source trail

[README](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/README.md#L1); [Implementation](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/apps/api/src/app/review/service/AJV.service.ts#L50) - [License](https://github.com/implerhq/impler.io/blob/d67d1a336eba4be51f4dc4f8ca1ac08d1d1eae93/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
