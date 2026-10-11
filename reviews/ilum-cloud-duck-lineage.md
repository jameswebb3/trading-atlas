# duck_lineage — Lineage runs have start, complete and failure

**Decision question:** Can a dataset edge be tied to one run and its outcome?

| Field | Review |
| --- | --- |
| Upstream | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [33cb810b8025bca52e5a7ba5571a7400e53f6852](https://github.com/ilum-cloud/duck_lineage/commit/33cb810b8025bca52e5a7ba5571a7400e53f6852) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/ilum-cloud/duck_lineage/blob/33cb810b8025bca52e5a7ba5571a7400e53f6852/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The event builder creates START, COMPLETE and FAIL records, attaches a run ID and can attach a parent run. A declared edge alone does not prove the run completed or that every output row was valid; the extension is not a reason to add infrastructure. |

## What this project does

A DuckDB extension that emits OpenLineage events from SQL queries. [README](https://github.com/ilum-cloud/duck_lineage/blob/33cb810b8025bca52e5a7ba5571a7400e53f6852/README.md).

## Mechanism inspected

The event builder creates START, COMPLETE and FAIL records, attaches a run ID and can attach a parent run. [Implementation](https://github.com/ilum-cloud/duck_lineage/blob/33cb810b8025bca52e5a7ba5571a7400e53f6852/src/lineage_event_builder.cpp#L36-L83).

## Limitation that matters

A declared edge alone does not prove the run completed or that every output row was valid; the extension is not a reason to add infrastructure. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Include run outcome and parent trial in local lineage receipts, not just an edge.

## Why this score

Transferable engineering pattern: The event builder creates START, COMPLETE and FAIL records, attaches a run ID and can attach a parent run. A declared edge alone does not prove the run completed or that every output row was valid; the extension is not a reason to add infrastructure.

## Source trail

[README](https://github.com/ilum-cloud/duck_lineage/blob/33cb810b8025bca52e5a7ba5571a7400e53f6852/README.md) · [Implementation](https://github.com/ilum-cloud/duck_lineage/blob/33cb810b8025bca52e5a7ba5571a7400e53f6852/src/lineage_event_builder.cpp#L36-L83).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
