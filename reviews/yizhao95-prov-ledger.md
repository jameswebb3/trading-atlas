# prov_ledger — Hash-chain the evidence ledger under a write lock

**Decision question:** Can a provenance row be altered or reordered without detection?

| Field | Review |
| --- | --- |
| Upstream | [yizhao95/prov_ledger](https://github.com/yizhao95/prov_ledger) |
| Primary area | Research & Reproducibility |
| Source commit | [4d9cc6038163939dac75423bed55a19cbbd111ae](https://github.com/yizhao95/prov_ledger/commit/4d9cc6038163939dac75423bed55a19cbbd111ae) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Rows hash canonical content plus the previous hash; a BEGIN IMMEDIATE write lock protects head selection before inserting the next row. A hash chain detects alteration in the stored ledger but does not prove the upstream source or timestamp was true; off-site anchoring is separate. |

## What this project does

Local provenance ledger for claims and source references. [README](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/README.md).

## Mechanism inspected

Rows hash canonical content plus the previous hash; a BEGIN IMMEDIATE write lock protects head selection before inserting the next row. [Implementation](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/orchestrator-backend/orchestrator/provenance.py#L40-L83).

## Limitation that matters

A hash chain detects alteration in the stored ledger but does not prove the upstream source or timestamp was true; off-site anchoring is separate. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Consider an append-only integrity chain for weight-moving evidence records only if the existing ledger lacks comparable tamper detection.

## Why this score

Rows hash canonical content plus the previous hash; a BEGIN IMMEDIATE write lock protects head selection before inserting the next row. A hash chain detects alteration in the stored ledger but does not prove the upstream source or timestamp was true; off-site anchoring is separate.

## Source trail

[README](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/README.md) · [Implementation](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/orchestrator-backend/orchestrator/provenance.py#L40-L83) · [License](https://github.com/yizhao95/prov_ledger/blob/4d9cc6038163939dac75423bed55a19cbbd111ae/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
