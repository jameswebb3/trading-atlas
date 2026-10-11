# DataJoint: recheck the inputs before committing a long computation

**Decision question:** Can a computation commit a result after its parent data changed during execution?

| Field | Review |
| --- | --- |
| Upstream | [DataJoint](https://github.com/datajoint/datajoint-python) |
| Primary area | Data Quality & Lineage |
| Source commit | [f8f1fb9295bf55d30a5337c9360aadb7a665fbdd](https://github.com/datajoint/datajoint-python/commit/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Defines scientific workflows through relational dependencies. Its long-computation path fetches inputs again inside a transaction and compares their hash before insertion, preventing a result from silently committing against changed parents. |

## Project overview

A scientific data-pipeline framework expresses workflow steps as tables and dependencies as foreign keys. [Project documentation](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/README.md#L1-L8).

## Mechanism worth inspecting

The [three-part computation contract](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/src/datajoint/autopopulate.py#L289-L324) separates fetch, compute, and insert. The [population implementation](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/src/datajoint/autopopulate.py#L687-L704) hashes fetched inputs, computes outside the final transaction, fetches again inside it, and rejects a mismatch. [Error handling](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/src/datajoint/autopopulate.py#L706-L724) cancels the transaction and records or propagates the error before any successful commit.

## Important limit

The hash covers fetched_data, not the entire surrounding environment. A mutable file path or remote identifier returned as a string can remain equal while its content changes. The [job reservation path](https://github.com/datajoint/datajoint-python/blob/f8f1fb9295bf55d30a5337c9360aadb7a665fbdd/src/datajoint/autopopulate.py#L660-L676) coordinates computation, but does not establish idempotency of arbitrary external side effects.

## Questions to take into your own design

- Does the fetch result identify immutable content, or merely mutable locations?
- Can a changed input cause explicit rejection before a ledger result becomes authoritative?

## Why this score for a trading system

3/5: a precise transferable protection for long research jobs and relational provenance. It does not supply a trading-specific experiment or execution model.

**Scope of this review:** README relational model, three-part method documentation, input revalidation, reservation, and commit/rollback code.
