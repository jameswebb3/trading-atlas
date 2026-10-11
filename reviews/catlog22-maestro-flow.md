# Maestro Flow — Resume needs a specific execution identity

**Decision question:** Which previous agent run does a resume command actually continue?

| Field | Review |
| --- | --- |
| Upstream | [catlog22/maestro-flow](https://github.com/catlog22/maestro-flow) |
| Primary area | Research & Reproducibility |
| Source commit | [f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a](https://github.com/catlog22/maestro-flow/commit/f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The runner records an execution ID and can resume a specified run or the most recent stored run. Resuming last is convenient but ambiguous when several experiments share a workspace; saved chat context is not a frozen data or evaluation state. |

## What this project does

An agent workflow runner with persisted CLI history. [Project README](https://github.com/catlog22/maestro-flow/blob/f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a/README.md#L1).

## Mechanism inspected

The runner records an execution ID and can resume a specified run or the most recent stored run. [Implementation](https://github.com/catlog22/maestro-flow/blob/f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a/src/agents/cli-agent-runner.ts#L597).

## Limitation that matters

Resuming last is convenient but ambiguous when several experiments share a workspace; saved chat context is not a frozen data or evaluation state. This is a source review, not a runtime or security test.

## Practical check for a trading system

Require an explicit run ID and manifest hash for research-agent resume.

## Why this score

A useful identity boundary, with no proof that replayed work is deterministic.

## Source trail

[README](https://github.com/catlog22/maestro-flow/blob/f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a/README.md#L1); [Implementation](https://github.com/catlog22/maestro-flow/blob/f888ceca62dd8bf8c4b5b4c5d70a2083342f9d9a/src/agents/cli-agent-runner.ts#L597).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
