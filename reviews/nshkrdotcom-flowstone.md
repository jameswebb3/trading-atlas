# FlowStone: Does an orchestrator always persist lineage and approval state before reporting success?

**Decision question:** Does an orchestrator always persist lineage and approval state before reporting success?

| Field | Review |
| --- | --- |
| Upstream | [nshkrdotcom/flowstone](https://github.com/nshkrdotcom/flowstone) |
| Primary area | Research & Reproducibility |
| Source commit | [16e6839adcaeb564b9b3993e93583c9cc58725fa](https://github.com/nshkrdotcom/flowstone/commit/16e6839adcaeb564b9b3993e93583c9cc58725fa) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/nshkrdotcom/flowstone/blob/16e6839adcaeb564b9b3993e93583c9cc58725fa/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The lineage persistence layer writes to a repository when configured, falls back to an in-memory server, and otherwise returns ok. The checkpoint module stores pending and resolved approvals in GenServer state. This is one source path, not a full deployment audit. Other materialization and audit paths may persist information; they do not make this specific lineage fallback durable. |

## What this project does

Models data assets and lineage, but its lineage recorder returns success when neither database nor in-memory server is available, while approval checkpoints live in memory. Useful as a persistence-gap test case.

## Mechanism inspected

The lineage persistence layer writes to a repository when configured, falls back to an in-memory server, and otherwise returns ok. The checkpoint module stores pending and resolved approvals in GenServer state.

## Limitation that matters

This is one source path, not a full deployment audit. Other materialization and audit paths may persist information; they do not make this specific lineage fallback durable.

## Practical check for a trading system

Crash or disable each persistence backend and verify that an accepted experiment or approval cannot be reported durable when its evidence vanished.

## Why this score

2/5 adjacent: the concrete silent-success and volatile-checkpoint paths provide useful failure cases for reproducibility tests; the Elixir framework itself is not trading-specific.

## Source trail

[README.md](https://github.com/nshkrdotcom/flowstone/blob/16e6839adcaeb564b9b3993e93583c9cc58725fa/README.md#L1); [lib/flowstone/lineage_persistence.ex](https://github.com/nshkrdotcom/flowstone/blob/16e6839adcaeb564b9b3993e93583c9cc58725fa/lib/flowstone/lineage_persistence.ex#L9); [lib/flowstone/checkpoint.ex](https://github.com/nshkrdotcom/flowstone/blob/16e6839adcaeb564b9b3993e93583c9cc58725fa/lib/flowstone/checkpoint.ex#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
