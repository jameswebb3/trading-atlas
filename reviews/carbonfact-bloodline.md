# bloodline — Carry provenance with transformed rows

**Decision question:** Can a derived row still identify how a field was produced?

| Field | Review |
| --- | --- |
| Upstream | [bloodline](https://github.com/carbonfact/bloodline) |
| Primary area | Data Quality & Lineage |
| Source commit | [22a1e9c6fb143c006e48ea37a1895608f1348782](https://github.com/carbonfact/bloodline/commit/22a1e9c6fb143c006e48ea37a1895608f1348782) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and a relevant test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The decorator wraps a transform and attaches source metadata to returned tables; tests check unknown and heuristic source labels. A propagated label is not proof of causal availability, and pandas row metadata may be too costly for large tick tables. |

## What this project does

A compact pandas row-lineage library implemented as a decorator. [README](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/README.md).

## Mechanism inspected

The decorator wraps a transform and attaches source metadata to returned tables; tests check unknown and heuristic source labels. [Implementation](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/bloodline/lineage.py#L49-L196).

## Limitation that matters

A propagated label is not proof of causal availability, and pandas row metadata may be too costly for large tick tables. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Prototype provenance on sampled feature rows or receipts, preserving UNKNOWN as a first-class source.

## Why this score

Transferable engineering pattern: The decorator wraps a transform and attaches source metadata to returned tables; tests check unknown and heuristic source labels. A propagated label is not proof of causal availability, and pandas row metadata may be too costly for large tick tables.

## Source trail

[README](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/README.md) · [Implementation](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/bloodline/lineage.py#L49-L196) · [Relevant test](https://github.com/carbonfact/bloodline/blob/22a1e9c6fb143c006e48ea37a1895608f1348782/tests/unit/test_lineage.py).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
