# BikeDNA - Can a data check detect combinations that are invalid together?

**Decision question:** Can a data check detect combinations that are invalid together?

| Field | Review |
| --- | --- |
| Upstream | [anerv/BikeDNA](https://github.com/anerv/BikeDNA) |
| Primary area | Data Quality & Lineage |
| Source commit | [281832e9247c802663e2ea5b20d0d6986beb790f](https://github.com/anerv/BikeDNA/commit/281832e9247c802663e2ea5b20d0d6986beb790f) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its incompatible-tag checker compares declared pairs of fields and counts offending edges. The rule catches cross-field contradictions but does not establish historical availability, upstream completeness or trading-specific units. |

## What this project does

A reproducible assessment toolkit for bicycle infrastructure datasets.

## Mechanism inspected

Its incompatible-tag checker compares declared pairs of fields and counts offending edges.

## Limitation that matters

The rule catches cross-field contradictions but does not establish historical availability, upstream completeness or trading-specific units.

## Practical check for a trading system

Encode impossible combinations between venue, asset, side and timestamp fields as explicit contracts.

## Why this score

2/5. The cross-field check is useful; the source domain and time semantics remain different.

## Source trail

[README](https://github.com/anerv/BikeDNA/blob/281832e9247c802663e2ea5b20d0d6986beb790f/README.md#L1); [bikedna/evaluation_functions.py](https://github.com/anerv/BikeDNA/blob/281832e9247c802663e2ea5b20d0d6986beb790f/bikedna/evaluation_functions.py#L354); [bikedna/evaluation_functions.py](https://github.com/anerv/BikeDNA/blob/281832e9247c802663e2ea5b20d0d6986beb790f/bikedna/evaluation_functions.py#L375); [bikedna/evaluation_functions.py](https://github.com/anerv/BikeDNA/blob/281832e9247c802663e2ea5b20d0d6986beb790f/bikedna/evaluation_functions.py#L382).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
