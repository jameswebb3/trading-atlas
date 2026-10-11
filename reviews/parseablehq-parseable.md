# parseable - Validate batches against an explicit stream schema

**Decision question:** Can a stream reject an empty or malformed batch before it enters storage?

| Field | Review |
| --- | --- |
| Upstream | [parseablehq/parseable](https://github.com/parseablehq/parseable) |
| Primary area | Market Data & Ingestion |
| Source commit | [b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf](https://github.com/parseablehq/parseable/commit/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 ([source](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The ingest path rejects an empty object, chooses a batch path or per-record path by partition settings, and converts the input against a static or evolving stream schema before processing. The recorded p_timestamp is an ingestion timestamp, not source publication time. Dynamic schema inference can accept fields a market-data contract would need to reject; upstream is AGPL. |

## What this project does

Parseable ingests structured log events with configurable stream schemas and partitions. [README](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/README.md).

## Mechanism inspected

The ingest path rejects an empty object, chooses a batch path or per-record path by partition settings, and converts the input against a static or evolving stream schema before processing. [Implementation](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/src/handlers/http/modal/utils/ingest_utils.rs#L305-L365). [Related path](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/src/handlers/http/ingest.rs#L69-L108).

## Limitation that matters

The recorded p_timestamp is an ingestion timestamp, not source publication time. Dynamic schema inference can accept fields a market-data contract would need to reject; upstream is AGPL. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Keep strict schema mode for decision inputs and store source, publication and receipt times separately; reject unknown fields or mark a schema migration.

## Why this score

The explicit schema switch and batch rejection are transferable, but generic log ingestion is not a point-in-time market-data contract.

## Source trail

[README](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/README.md) - [Implementation](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/src/handlers/http/modal/utils/ingest_utils.rs#L305-L365) - [Related path](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/src/handlers/http/ingest.rs#L69-L108) - [License](https://github.com/parseablehq/parseable/blob/b8fb6ce1f54ec3a6da4596e609b7340ba6da69cf/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
