# Regulated Document Pipeline - How is a processed artifact tied to its source version?

**Decision question:** How is a processed artifact tied to its source version?

| Field | Review |
| --- | --- |
| Upstream | [aws-samples/document-processing-pipeline-for-regulated-industries](https://github.com/aws-samples/document-processing-pipeline-for-regulated-industries) |
| Primary area | Data Quality & Lineage |
| Source commit | [1b86d2da846a74d98b63feac1603da81aa63e0f6](https://github.com/aws-samples/document-processing-pipeline-for-regulated-industries/commit/1b86d2da846a74d98b63feac1603da81aa63e0f6) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The lineage handler carries documentId and optional versionId into a metadata update. Document-version tracking does not itself establish when a market observation became available or whether every record arrived. |

## What this project does

An AWS document-processing reference pipeline.

## Mechanism inspected

The lineage handler carries documentId and optional versionId into a metadata update.

## Limitation that matters

Document-version tracking does not itself establish when a market observation became available or whether every record arrived.

## Practical check for a trading system

Keep immutable source version and processing receipt together for each published dataset.

## Why this score

2/5. A transferable identity pattern with heavy AWS-specific plumbing.

## Source trail

[README](https://github.com/aws-samples/document-processing-pipeline-for-regulated-industries/blob/1b86d2da846a74d98b63feac1603da81aa63e0f6/README.md#L1); [code/metadata/lineage.py](https://github.com/aws-samples/document-processing-pipeline-for-regulated-industries/blob/1b86d2da846a74d98b63feac1603da81aa63e0f6/code/metadata/lineage.py#L59); [Root license](https://github.com/aws-samples/document-processing-pipeline-for-regulated-industries/blob/1b86d2da846a74d98b63feac1603da81aa63e0f6/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
