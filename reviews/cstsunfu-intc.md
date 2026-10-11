# Intc - Can unresolved configuration dependencies silently enter a run?

**Decision question:** Can unresolved configuration dependencies silently enter a run?

| Field | Review |
| --- | --- |
| Upstream | [cstsunfu/intc](https://github.com/cstsunfu/intc) |
| Primary area | Data Quality & Lineage |
| Source commit | [334c5a918d694b4c8bfcb4dd62a0910ee3fd2942](https://github.com/cstsunfu/intc/commit/334c5a918d694b4c8bfcb4dd62a0910ee3fd2942) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The loader stashes dependent configs, resolves them when bases appear and raises on anything still unresolved. Resolving references does not pin the bytes of the resolved config or prove research inputs were available at decision time. |

## What this project does

A hierarchical configuration loader with deferred dependency resolution.

## Mechanism inspected

The loader stashes dependent configs, resolves them when bases appear and raises on anything still unresolved.

## Limitation that matters

Resolving references does not pin the bytes of the resolved config or prove research inputs were available at decision time.

## Practical check for a trading system

Reject unresolved dependencies and hash the resolved configuration in the run manifest.

## Why this score

2/5. Failing closed on unresolved config is useful; causal data proof is separate.

## Source trail

[README](https://github.com/cstsunfu/intc/blob/334c5a918d694b4c8bfcb4dd62a0910ee3fd2942/README.md#L1); [intc/intc/loader.py](https://github.com/cstsunfu/intc/blob/334c5a918d694b4c8bfcb4dd62a0910ee3fd2942/intc/intc/loader.py#L48); [intc/intc/loader.py](https://github.com/cstsunfu/intc/blob/334c5a918d694b4c8bfcb4dd62a0910ee3fd2942/intc/intc/loader.py#L64); [Root license](https://github.com/cstsunfu/intc/blob/334c5a918d694b4c8bfcb4dd62a0910ee3fd2942/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
