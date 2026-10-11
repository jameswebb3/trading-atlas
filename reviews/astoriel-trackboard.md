# trackboard — Review contract changes by breakage

**Decision question:** Which schema changes actually break downstream consumers?

| Field | Review |
| --- | --- |
| Upstream | [Astoriel/trackboard](https://github.com/Astoriel/trackboard) |
| Primary area | Data Quality & Lineage |
| Source commit | [db20f15572804849c5ad3496c22e0b932523d8ff](https://github.com/Astoriel/trackboard/commit/db20f15572804849c5ad3496c22e0b932523d8ff) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its diff classifies event or property removals and newly required properties as breaking, while optional additions are safe and descriptive changes informational. The rules are structural and generic; semantic timing changes or exchange meaning changes need domain checks. No root license was found. |

## What this project does

Event-contract workspace with a structural diff service for snapshots. [README](https://github.com/Astoriel/trackboard/blob/db20f15572804849c5ad3496c22e0b932523d8ff/README.md).

## Mechanism inspected

Its diff classifies event or property removals and newly required properties as breaking, while optional additions are safe and descriptive changes informational. [Implementation](https://github.com/Astoriel/trackboard/blob/db20f15572804849c5ad3496c22e0b932523d8ff/apps/api/app/services/contract_diff.py#L12-L105).

## Limitation that matters

The rules are structural and generic; semantic timing changes or exchange meaning changes need domain checks. No root license was found. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Classify feed contract changes as breaking/safe/informational before a collector deploy, with examples for field availability and nullability.

## Why this score

Its diff classifies event or property removals and newly required properties as breaking, while optional additions are safe and descriptive changes informational. The rules are structural and generic; semantic timing changes or exchange meaning changes need domain checks. No root license was found.

## Source trail

[README](https://github.com/Astoriel/trackboard/blob/db20f15572804849c5ad3496c22e0b932523d8ff/README.md) · [Implementation](https://github.com/Astoriel/trackboard/blob/db20f15572804849c5ad3496c22e0b932523d8ff/apps/api/app/services/contract_diff.py#L12-L105).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
