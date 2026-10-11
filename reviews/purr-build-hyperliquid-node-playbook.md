# Hyperliquid Node Playbook — Pruning is a data-contract decision

**Decision question:** When can old node data be deleted safely?

| Field | Review |
| --- | --- |
| Upstream | [purr-build/hyperliquid-node-playbook](https://github.com/purr-build/hyperliquid-node-playbook) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fecb2413fbd0172860149f29613204ff6a708271](https://github.com/purr-build/hyperliquid-node-playbook/commit/fecb2413fbd0172860149f29613204ff6a708271) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The roles separate monitoring and pruning and expose a dry-run path for operational changes. A deletion switch can remove history needed for later reconciliation or replay; the playbook does not define the research-retention contract. |

## What this project does

An Ansible playbook for a Hyperliquid node with sync, monitoring, and pruning tasks. [Project README](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/README.md#L24).

## Mechanism inspected

The roles separate monitoring and pruning and expose a dry-run path for operational changes. [Implementation](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/roles/monitoring/tasks/main.yaml#L1). [Related source 1](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/README.md#L38). [Related source 2](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/roles/pruner/tasks/main.yml#L1).

## Limitation that matters

A deletion switch can remove history needed for later reconciliation or replay; the playbook does not define the research-retention contract. This is a source review, not a runtime or security test.

## Practical check for a trading system

Specify the oldest required backfill and audit horizon before enabling any prune policy.

## Why this score

Operationally relevant, but the roles and dependencies are heavier than a single retention rule.

## Source trail

[README](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/README.md#L24); [Implementation](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/roles/monitoring/tasks/main.yaml#L1); [Related source 1](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/README.md#L38); [Related source 2](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/roles/pruner/tasks/main.yml#L1) - [License](https://github.com/purr-build/hyperliquid-node-playbook/blob/fecb2413fbd0172860149f29613204ff6a708271/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
