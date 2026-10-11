# Public Data Lens - A source snapshot should retain the original row

**Decision question:** Can a changed CSV feed be parsed without losing its source evidence?

| Field | Review |
| --- | --- |
| Upstream | [hike-lab/public-data-lens](https://github.com/hike-lab/public-data-lens) |
| Primary area | Data Quality & Lineage |
| Source commit | [3e210af3911ea7e215e59111a3b145c9322f5522](https://github.com/hike-lab/public-data-lens/commit/3e210af3911ea7e215e59111a3b145c9322f5522) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Validates snapshot encoding and required columns, then preserves the original row, line number and source identity for every parsed record. Raw-row provenance does not establish publication time or market-data semantics; downstream timing and value contracts are still required. |

## What this project does

A public-data discovery layer built from monthly Korean government catalog snapshots. The reviewed parser keeps each raw row and its line number before normalization.

## Mechanism inspected

The parser validates the complete byte stream against UTF-8 with BOM support and then CP949, rejects unsupported encodings, rejects a changed required column set, and emits each row with its original source dictionary and row number. It also rejects a missing source listing key rather than silently inventing identity.

## Limitation that matters

A preserved CSV row proves what the snapshot contained, not when a field became available to a trading decision. The parser checks required columns and key presence, but the inspected path does not validate market-data units, corrected values or a publisher clock. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep raw payload, line or message position, schema version and receipt time beside normalized market observations. Reject incompatible layouts before deriving signals and distinguish missing from unpublished values.

## Why this score

3/5 because this code gives a concrete transferable raw-to-normalized provenance boundary, with trading-specific timing and value checks still absent.

## Source trail

[README](https://github.com/hike-lab/public-data-lens/blob/3e210af3911ea7e215e59111a3b145c9322f5522/README.md#L10); [Encoding and row parser](https://github.com/hike-lab/public-data-lens/blob/3e210af3911ea7e215e59111a3b145c9322f5522/apps/server/datanav/pipeline/parse.py#L56); [License](https://github.com/hike-lab/public-data-lens/blob/3e210af3911ea7e215e59111a3b145c9322f5522/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
