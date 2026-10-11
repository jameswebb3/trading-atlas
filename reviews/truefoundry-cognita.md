# cognita - A two-stage sync with visible failure states

**Decision question:** Can an index refresh remove old data before the replacement is safely loaded?

| Field | Review |
| --- | --- |
| Upstream | [truefoundry/cognita](https://github.com/truefoundry/cognita) |
| Primary area | Data Quality & Lineage |
| Source commit | [8bcaae790af1effd398520338d6c623ff92b98fb](https://github.com/truefoundry/cognita/commit/8bcaae790af1effd398520338d6c623ff92b98fb) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It snapshots existing item hashes, loads changed batches, records failed item IDs, and only then starts FULL-mode cleanup of old vectors. This is a document index, not a market-data collector. The inspected path does not establish an atomic switch between old and new collections, and partial batch failures still need repair. |

## What this project does

Cognita ingests source documents into a vector collection and tracks a data-ingestion run. [README](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/README.md).

## Mechanism inspected

It snapshots existing item hashes, loads changed batches, records failed item IDs, and only then starts FULL-mode cleanup of old vectors. [Implementation](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/backend/indexer/indexer.py#L63-L128). [Related path](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/backend/indexer/indexer.py#L149-L195).

## Limitation that matters

This is a document index, not a market-data collector. The inspected path does not establish an atomic switch between old and new collections, and partial batch failures still need repair. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

When refreshing a trading dataset, compare source identities and hashes, preserve the last usable version until replacement is validated, and make incomplete batches visible.

## Why this score

Useful sequencing and failure states, but the source mechanism does not solve temporal availability or atomic market-data cutover.

## Source trail

[README](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/README.md) - [Implementation](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/backend/indexer/indexer.py#L63-L128) - [Related path](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/backend/indexer/indexer.py#L149-L195) - [License](https://github.com/truefoundry/cognita/blob/8bcaae790af1effd398520338d6c623ff92b98fb/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
