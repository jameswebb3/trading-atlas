# Synpath - Which venue facts should override a restarted execution journal?

**Decision question:** Which venue facts should override a restarted execution journal?

| Field | Review |
| --- | --- |
| Upstream | [Synpath-ai/synpath](https://github.com/Synpath-ai/synpath) |
| Primary area | Execution & Exchange Integration |
| Source commit | [53af00c49b184d8ae5c3a4e0755fc98b26c25694](https://github.com/Synpath-ai/synpath/commit/53af00c49b184d8ae5c3a4e0755fc98b26c25694) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Compares orders, fills, positions and cash with a venue and reports named differences. A failed final-order lookup can turn an unknown ghost into a local cancellation. |

## What this project does

A multi-prediction-market API and execution engine with an explicit reconciliation pass.

## Mechanism inspected

The reconciler compares venue open orders, fills, positions and cash against its journal. It names orphans, ghosts, order drift, new fills and unexplained balance movement; orphan policy defaults to reporting rather than cancellation.

## Limitation that matters

For a journal-open order absent from open orders, a failed fetch_order falls back to marking it canceled. That can misclassify a filled order until fill recovery runs; the fill cursor also advances by timestamp, so pagination and equal-timestamp cases need separate proof.

## Practical check for a trading system

Use a typed discrepancy report and venue truth, but keep a missing terminal query as UNKNOWN until fills and final order status are reconciled.

## Why this score

3/5. Broad reconciliation is directly useful, while its ghost fallback prevents treating the module as a ready-made safety oracle.

## Source trail

[README](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/README.md#L8); [synpath/engine/reconcile.py](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/synpath/engine/reconcile.py#L1); [synpath/engine/reconcile.py](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/synpath/engine/reconcile.py#L128); [synpath/engine/reconcile.py](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/synpath/engine/reconcile.py#L166); [synpath/engine/reconcile.py](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/synpath/engine/reconcile.py#L185); [License text](https://github.com/Synpath-ai/synpath/blob/53af00c49b184d8ae5c3a4e0755fc98b26c25694/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
