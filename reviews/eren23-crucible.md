# Crucible - Can a research run enforce a declared experiment contract?

**Decision question:** Can a research run enforce a declared experiment contract?

| Field | Review |
| --- | --- |
| Upstream | [eren23/crucible](https://github.com/eren23/crucible) |
| Primary area | Agents & Decision Systems |
| Source commit | [2152579cc9ecee238c1c28e36931ea2ec8ca1f23](https://github.com/eren23/crucible/commit/2152579cc9ecee238c1c28e36931ea2ec8ca1f23) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The contract resolves tracker settings and metadata, then validates local and remote configurations. The reviewed remote path relies on W&B, and contract validation does not establish result correctness. |

## What this project does

An experiment framework with a validated local or remote tracking contract.

## Mechanism inspected

The contract resolves tracker settings and metadata, then validates local and remote configurations.

## Limitation that matters

The reviewed remote path relies on W&B, and contract validation does not establish result correctness.

## Practical check for a trading system

Keep a self-hosted experiment contract that validates required fields before execution.

## Why this score

2/5. The explicit contract is transferable; external tracking and result claims are not.

## Source trail

[README](https://github.com/eren23/crucible/blob/2152579cc9ecee238c1c28e36931ea2ec8ca1f23/README.md#L1); [src/crucible/core/experiment_contract.py](https://github.com/eren23/crucible/blob/2152579cc9ecee238c1c28e36931ea2ec8ca1f23/src/crucible/core/experiment_contract.py#L21); [src/crucible/core/experiment_contract.py](https://github.com/eren23/crucible/blob/2152579cc9ecee238c1c28e36931ea2ec8ca1f23/src/crucible/core/experiment_contract.py#L105).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
