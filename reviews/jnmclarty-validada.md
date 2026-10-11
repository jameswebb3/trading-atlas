# Validada - Which DataFrame violations can be reported separately?

**Decision question:** Which DataFrame violations can be reported separately?

| Field | Review |
| --- | --- |
| Upstream | [jnmclarty/validada](https://github.com/jnmclarty/validada) |
| Primary area | Data Quality & Lineage |
| Source commit | [da806ee649d67e2ac36ad4f22493003622493ee5](https://github.com/jnmclarty/validada/commit/da806ee649d67e2ac36ad4f22493003622493ee5) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its checks expose missing values, nonunique indices and monotonicity as individual rule results. No reviewed rule establishes when a row became available for a trading decision. |

## What this project does

A composable DataFrame validation library.

## Mechanism inspected

Its checks expose missing values, nonunique indices and monotonicity as individual rule results.

## Limitation that matters

No reviewed rule establishes when a row became available for a trading decision.

## Practical check for a trading system

Add available-at and venue-specific invariants beside shape and null checks.

## Why this score

2/5. The composable checks are useful, but historical causality is outside this library.

## Source trail

[README](https://github.com/jnmclarty/validada/blob/da806ee649d67e2ac36ad4f22493003622493ee5/README.md#L1); [validada/core.py](https://github.com/jnmclarty/validada/blob/da806ee649d67e2ac36ad4f22493003622493ee5/validada/core.py#L107); [Root license](https://github.com/jnmclarty/validada/blob/da806ee649d67e2ac36ad4f22493003622493ee5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
