# SAGE - Can an agent reject invalid generated code before research use?

**Decision question:** Can an agent reject invalid generated code before research use?

| Field | Review |
| --- | --- |
| Upstream | [JieMaMagic/SAGE](https://github.com/JieMaMagic/SAGE) |
| Primary area | Agents & Decision Systems |
| Source commit | [b6d96a6b02404bdb2006974be35927819966306e](https://github.com/JieMaMagic/SAGE/commit/b6d96a6b02404bdb2006974be35927819966306e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The code agent parses output with AST checks and issues targeted repairs for validation failures. Syntactic validity does not imply safe execution, causal validity or correct backtest results. |

## What this project does

A research agent pipeline with generated-code validation.

## Mechanism inspected

The code agent parses output with AST checks and issues targeted repairs for validation failures.

## Limitation that matters

Syntactic validity does not imply safe execution, causal validity or correct backtest results.

## Practical check for a trading system

Separate syntax repair from sandbox controls and research evidence checks.

## Why this score

2/5. The staged validation is useful but narrow.

## Source trail

[README](https://github.com/JieMaMagic/SAGE/blob/b6d96a6b02404bdb2006974be35927819966306e/README.md#L1); [researchclaw/pipeline/code_agent.py](https://github.com/JieMaMagic/SAGE/blob/b6d96a6b02404bdb2006974be35927819966306e/researchclaw/pipeline/code_agent.py#L790); [researchclaw/pipeline/code_agent.py](https://github.com/JieMaMagic/SAGE/blob/b6d96a6b02404bdb2006974be35927819966306e/researchclaw/pipeline/code_agent.py#L834).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
