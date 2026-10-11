# DSH Lineage: Can a research conclusion prove its upstream artifacts still match the recorded bytes?

**Decision question:** Can a research conclusion prove its upstream artifacts still match the recorded bytes?

| Field | Review |
| --- | --- |
| Upstream | [dongsheng123132/dsh-lineage](https://github.com/dongsheng123132/dsh-lineage) |
| Primary area | Research & Reproducibility |
| Source commit | [f68e899abd5c894a213997ac42d2644ec8ce7d95](https://github.com/dongsheng123132/dsh-lineage/commit/f68e899abd5c894a213997ac42d2644ec8ce7d95) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/dongsheng123132/dsh-lineage/blob/f68e899abd5c894a213997ac42d2644ec8ce7d95/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Events with divergent uses of the same idempotency key are rejected. Immutable event files are atomically published and read back. Verification walks an upstream or downstream closure, rehashes referenced objects, and reports missing, stale, dangling or cyclic evidence. Hash equality proves byte identity, not factual truth or causal validity. The graph requires explicit edges and cannot discover omitted dependencies by itself. |

## What this project does

Builds an append-only evidence graph with idempotent events, content hashes, upstream closure and missing or stale artifact states. A concrete reference for reproducible research provenance, not a proof that the underlying claim is true.

## Mechanism inspected

Events with divergent uses of the same idempotency key are rejected. Immutable event files are atomically published and read back. Verification walks an upstream or downstream closure, rehashes referenced objects, and reports missing, stale, dangling or cyclic evidence.

## Limitation that matters

Hash equality proves byte identity, not factual truth or causal validity. The graph requires explicit edges and cannot discover omitted dependencies by itself.

## Practical check for a trading system

For any promoted result, create typed edges to the exact input artifacts and run a closure check that fails on missing or stale bytes; keep methodology checks separate from byte provenance.

## Why this score

3/5 transferable: the local immutable ledger and closure verification are directly relevant to experiment traceability, but they do not validate an alpha claim or establish completeness of the recorded graph.

## Source trail

[README.md](https://github.com/dongsheng123132/dsh-lineage/blob/f68e899abd5c894a213997ac42d2644ec8ce7d95/README.md#L1); [lib/lineage.mjs](https://github.com/dongsheng123132/dsh-lineage/blob/f68e899abd5c894a213997ac42d2644ec8ce7d95/lib/lineage.mjs#L324); [lib/lineage.mjs](https://github.com/dongsheng123132/dsh-lineage/blob/f68e899abd5c894a213997ac42d2644ec8ce7d95/lib/lineage.mjs#L418); [SECURITY.md](https://github.com/dongsheng123132/dsh-lineage/blob/f68e899abd5c894a213997ac42d2644ec8ce7d95/SECURITY.md#L5)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
