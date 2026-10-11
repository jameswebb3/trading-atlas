# BigQuery Data Lineage — Empty lineage may mean parsing failed

**Decision question:** When a SQL lineage extractor fails, should the column graph be empty?

| Field | Review |
| --- | --- |
| Upstream | [GoogleCloudPlatform/bigquery-data-lineage](https://github.com/GoogleCloudPlatform/bigquery-data-lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [2c61f343b3c7761b1ff45962efb6fff3e170e95a](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/commit/2c61f343b3c7761b1ff45962efb6fff3e170e95a) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The extractor records source tables and attempts ZetaSQL column lineage; if SQL parsing throws, it logs a warning and returns an empty column set. An empty set is ambiguous between a query with no traceable columns and a parser failure. |

## What this project does

A BigQuery job-event extractor that records table and column lineage from query metadata. [Project README](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/README.md#L1).

## Mechanism inspected

The extractor records source tables and attempts ZetaSQL column lineage; if SQL parsing throws, it logs a warning and returns an empty column set. [Implementation](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/src/main/java/com/google/cloud/solutions/datalineage/extractor/QueryJobExtractor.java#L93).

## Limitation that matters

An empty set is ambiguous between a query with no traceable columns and a parser failure. Trading feature provenance must preserve that difference. This is a source review, not a runtime or security test.

## Practical check for a trading system

Give each lineage edge a parsed, unsupported, or failed state, and block availability claims when the graph is incomplete.

## Why this score

A concrete provenance false-negative path with direct relevance to feature timing and auditability.

## Source trail

[README](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/README.md#L1); [Implementation](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/src/main/java/com/google/cloud/solutions/datalineage/extractor/QueryJobExtractor.java#L93) - [License](https://github.com/GoogleCloudPlatform/bigquery-data-lineage/blob/2c61f343b3c7761b1ff45962efb6fff3e170e95a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
