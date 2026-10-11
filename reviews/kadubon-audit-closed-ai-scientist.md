# audit-closed-ai-scientist — Compare research agents under a matched discovery budget

**Decision question:** Does an autonomous scientist still win after candidate shopping is accounted for?

| Field | Review |
| --- | --- |
| Upstream | [kadubon/audit-closed-ai-scientist](https://github.com/kadubon/audit-closed-ai-scientist) |
| Primary area | Agents & Decision Systems |
| Source commit | [1e844d1bca18d7bb298aa198e1250bb07bd7ea44](https://github.com/kadubon/audit-closed-ai-scientist/commit/1e844d1bca18d7bb298aa198e1250bb07bd7ea44) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Each trial gives a naive selector and an audit-closed selector the same candidate set and sample budget; it records acceptance, independent replication and replay integrity under null and signal scenarios. The examples use generated data and a specific e-process protocol; observed benchmark differences are not evidence about trading returns or a production agent. A house implementation needs serial-dependence-aware inference. |

## What this project does

Synthetic benchmark of statistical validity in autonomous hypothesis selection. [README](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md).

## Mechanism inspected

Each trial gives a naive selector and an audit-closed selector the same candidate set and sample budget; it records acceptance, independent replication and replay integrity under null and signal scenarios. [Implementation](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/benchmarks/discovery_validity_benchmark.py#L36-L89).

## Limitation that matters

The examples use generated data and a specific e-process protocol; observed benchmark differences are not evidence about trading returns or a production agent. A house implementation needs serial-dependence-aware inference. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Evaluate research agents on the same candidate/data/compute budget, report false acceptances under null, and require evidence-log replay before trusting a selected finding.

## Why this score

Each trial gives a naive selector and an audit-closed selector the same candidate set and sample budget; it records acceptance, independent replication and replay integrity under null and signal scenarios. The examples use generated data and a specific e-process protocol; observed benchmark differences are not evidence about trading returns or a production agent. A house implementation needs serial-dependence-aware inference.

## Source trail

[README](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md) · [Implementation](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/benchmarks/discovery_validity_benchmark.py#L36-L89) · [License](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
