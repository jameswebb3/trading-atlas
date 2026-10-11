# MLE Agent — A generated plan is not an evaluated experiment

**Decision question:** What does an AI research planner actually verify?

| Field | Review |
| --- | --- |
| Upstream | [MLSysOps/MLE-agent](https://github.com/MLSysOps/MLE-agent) |
| Primary area | Research & Reproducibility |
| Source commit | [a29287e8152456b8d6a09121934522fd2b4e0aa8](https://github.com/MLSysOps/MLE-agent/commit/a29287e8152456b8d6a09121934522fd2b4e0aa8) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The planner stores conversation state and asks a model for task descriptions based on user requirements. The inspected planning path is prompt-driven; it does not by itself enforce data splits, execution realism, or independent evaluation. |

## What this project does

An agent workflow that drafts machine-learning project tasks and passes them to other roles. [Project README](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/README.md#L1).

## Mechanism inspected

The planner stores conversation state and asks a model for task descriptions based on user requirements. [Implementation](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/mle/agents/planner.py#L18-L49).

## Limitation that matters

The inspected planning path is prompt-driven; it does not by itself enforce data splits, execution realism, or independent evaluation. This is a source review, not a runtime or security test.

## Practical check for a trading system

Treat generated research tasks as proposals until a deterministic study contract and held-out evaluation exist.

## Why this score

The role separation is understandable, but the visible planner gives little evidence for trustworthy trading research.

## Source trail

[README](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/README.md#L1); [Implementation](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/mle/agents/planner.py#L18-L49) - [License](https://github.com/MLSysOps/MLE-agent/blob/a29287e8152456b8d6a09121934522fd2b4e0aa8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
