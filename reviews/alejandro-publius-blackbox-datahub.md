# BlackBox DataHub: Can a data incident agent distinguish source evidence from transport fallback?

**Decision question:** Can a data incident agent distinguish source evidence from transport fallback?

| Field | Review |
| --- | --- |
| Upstream | [alejandro-publius/blackbox-datahub](https://github.com/alejandro-publius/blackbox-datahub) |
| Primary area | Data Quality & Lineage |
| Source commit | [b72a32c64e11404b1de98b517bde7e487ca35963](https://github.com/alejandro-publius/blackbox-datahub/commit/b72a32c64e11404b1de98b517bde7e487ca35963) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/alejandro-publius/blackbox-datahub/blob/b72a32c64e11404b1de98b517bde7e487ca35963/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | An embedded context adapter falls back when unavailable and records the transport that produced an item. The investigation runner separates investigation from a later repair phase and records failed terminal states. MCP, embedded kit, and GraphQL all read the same DataHub instance, so their agreement is not independent corroboration. The repository is a demonstration of an incident workflow, not a verified production trading control. |

## What this project does

Tags the transport that delivered DataHub evidence and makes repair a separate, evidence-gated phase. Useful for incident investigation, but its demo and DataHub-specific paths are not proof that an autonomous repair is safe in trading.

## Mechanism inspected

An embedded context adapter falls back when unavailable and records the transport that produced an item. The investigation runner separates investigation from a later repair phase and records failed terminal states.

## Limitation that matters

MCP, embedded kit, and GraphQL all read the same DataHub instance, so their agreement is not independent corroboration. The repository is a demonstration of an incident workflow, not a verified production trading control.

## Practical check for a trading system

When an incident agent cites a dataset or lineage path, record the actual source and transport; do not count fallback paths as multiple witnesses. Gate repairs on explicit evidence and authority.

## Why this score

3/5 transferable: the provenance distinction and repair gate fit a data-driven trading stack, but DataHub and the agent workflow are broader than the local system and were not run here.

## Source trail

[docs/ARCHITECTURE.md](https://github.com/alejandro-publius/blackbox-datahub/blob/b72a32c64e11404b1de98b517bde7e487ca35963/docs/ARCHITECTURE.md#L1); [backend/blackbox/datahub/context_kit.py](https://github.com/alejandro-publius/blackbox-datahub/blob/b72a32c64e11404b1de98b517bde7e487ca35963/backend/blackbox/datahub/context_kit.py#L10); [backend/blackbox/agent/investigator.py](https://github.com/alejandro-publius/blackbox-datahub/blob/b72a32c64e11404b1de98b517bde7e487ca35963/backend/blackbox/agent/investigator.py#L28); [tests/test_context_kit.py](https://github.com/alejandro-publius/blackbox-datahub/blob/b72a32c64e11404b1de98b517bde7e487ca35963/tests/test_context_kit.py#L59)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
