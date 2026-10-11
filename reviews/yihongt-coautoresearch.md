# CoAutoResearch - Can a research agent keep generated files inside managed paths?

**Decision question:** Can a research agent keep generated files inside managed paths?

| Field | Review |
| --- | --- |
| Upstream | [YihongT/CoAutoResearch](https://github.com/YihongT/CoAutoResearch) |
| Primary area | Agents & Decision Systems |
| Source commit | [263895de7ced31a277281183a52d50ea3e527fe4](https://github.com/YihongT/CoAutoResearch/commit/263895de7ced31a277281183a52d50ea3e527fe4) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It declares managed paths and required reviewer files, then rejects symlinked or invalid template paths. Path discipline and reviewer files do not prove the content of a research claim. |

## What this project does

An automated research workflow with a managed workspace and reviewer outputs.

## Mechanism inspected

It declares managed paths and required reviewer files, then rejects symlinked or invalid template paths.

## Limitation that matters

Path discipline and reviewer files do not prove the content of a research claim.

## Practical check for a trading system

Constrain generated research artifacts and require a separate evidence reviewer.

## Why this score

2/5. The managed-path controls are concrete; evaluation quality remains external.

## Source trail

[README](https://github.com/YihongT/CoAutoResearch/blob/263895de7ced31a277281183a52d50ea3e527fe4/README.md#L1); [bin/auto-research.js](https://github.com/YihongT/CoAutoResearch/blob/263895de7ced31a277281183a52d50ea3e527fe4/bin/auto-research.js#L23); [bin/auto-research.js](https://github.com/YihongT/CoAutoResearch/blob/263895de7ced31a277281183a52d50ea3e527fe4/bin/auto-research.js#L159).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
