# Polaris — Remote run uncertainty needs a durable handle

**Decision question:** Can a long experiment resume observation of the same remote command?

| Field | Review |
| --- | --- |
| Upstream | [Polaris](https://github.com/ZJU-REAL/Polaris) |
| Primary area | Agents & Decision Systems |
| Source commit | [57612367eb9d6052e34e44d9ff613a4dc3c8c774](https://github.com/ZJU-REAL/Polaris/commit/57612367eb9d6052e34e44d9ff613a4dc3c8c774) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its experiment action serializes operation and attempt IDs, process identifiers, timeout policy and repair scope, and can restore the handle for later observation. The LLM advisor's diagnosis is not independent evidence and its large remote stack is outside current needs; a restored handle still needs source and artifact checks. |

## What this project does

A research-agent platform with persistent experiments and managed remote commands. [README](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/README.md).

## Mechanism inspected

Its experiment action serializes operation and attempt IDs, process identifiers, timeout policy and repair scope, and can restore the handle for later observation. [Implementation](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/src/backend/app/agents/voyage/actions_experiment.py#L123-L192).

## Limitation that matters

The LLM advisor's diagnosis is not independent evidence and its large remote stack is outside current needs; a restored handle still needs source and artifact checks. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Persist an operation handle and evidence snapshot for long research jobs, without allowing an LLM to declare an experiment valid.

## Why this score

Transferable engineering pattern: Its experiment action serializes operation and attempt IDs, process identifiers, timeout policy and repair scope, and can restore the handle for later observation. The LLM advisor's diagnosis is not independent evidence and its large remote stack is outside current needs; a restored handle still needs source and artifact checks.

## Source trail

[README](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/README.md) · [Documentation](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/docs/concepts.md) · [Implementation](https://github.com/ZJU-REAL/Polaris/blob/57612367eb9d6052e34e44d9ff613a4dc3c8c774/src/backend/app/agents/voyage/actions_experiment.py#L123-L192).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
