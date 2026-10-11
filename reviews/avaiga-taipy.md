# Taipy - Should data readiness and freshness be the same state?

**Decision question:** Should data readiness and freshness be the same state?

| Field | Review |
| --- | --- |
| Upstream | [Avaiga/taipy](https://github.com/Avaiga/taipy) |
| Primary area | Research & Reproducibility |
| Source commit | [5bcb5749521f9ddcc725c009aca00a88ff724e87](https://github.com/Avaiga/taipy/commit/5bcb5749521f9ddcc725c009aca00a88ff724e87) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The data node exposes readiness separately from validity: a node can be unwritten or currently edited, and validity has its own time rule. Neither readiness nor age proves that an upstream feed is complete or causally available. |

## What this project does

A data application framework with managed data nodes.

## Mechanism inspected

The data node exposes readiness separately from validity: a node can be unwritten or currently edited, and validity has its own time rule.

## Limitation that matters

Neither readiness nor age proves that an upstream feed is complete or causally available.

## Practical check for a trading system

Maintain separate ready, fresh and coverage states on research inputs.

## Why this score

2/5. The separate state transitions are useful, with additional market-data evidence still required.

## Source trail

[README](https://github.com/Avaiga/taipy/blob/5bcb5749521f9ddcc725c009aca00a88ff724e87/README.md#L1); [taipy/core/data/data_node.py](https://github.com/Avaiga/taipy/blob/5bcb5749521f9ddcc725c009aca00a88ff724e87/taipy/core/data/data_node.py#L334); [taipy/core/data/data_node.py](https://github.com/Avaiga/taipy/blob/5bcb5749521f9ddcc725c009aca00a88ff724e87/taipy/core/data/data_node.py#L366).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
