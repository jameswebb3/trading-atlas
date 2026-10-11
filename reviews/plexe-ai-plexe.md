# Plexe — A local checkpoint is not a durable experiment

**Decision question:** What survives when an agent workflow crashes between phases?

| Field | Review |
| --- | --- |
| Upstream | [plexe-ai/plexe](https://github.com/plexe-ai/plexe) |
| Primary area | Research & Reproducibility |
| Source commit | [a1e05f6dc4c0875e0075f3b6f020fbecef57a699](https://github.com/plexe-ai/plexe/commit/a1e05f6dc4c0875e0075f3b6f020fbecef57a699) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The checkpoint writer records experiment ID, phase, timestamp, context, feedback, and optional search artifacts to local disk. The source explicitly leaves remote persistence to another layer; a local file alone is not a durable result or proof of reproducibility. |

## What this project does

An AI model-building system with phase checkpoints and search journals. [Project README](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/README.md#L1).

## Mechanism inspected

The checkpoint writer records experiment ID, phase, timestamp, context, feedback, and optional search artifacts to local disk. [Implementation](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/plexe/checkpointing.py#L70).

## Limitation that matters

The source explicitly leaves remote persistence to another layer; a local file alone is not a durable result or proof of reproducibility. This is a source review, not a runtime or security test.

## Practical check for a trading system

Checkpoint phase state with input hashes and journal identity, then verify recovery from an interrupted write.

## Why this score

Useful checkpoint fields, with durability and exact data identity still outside the inspected path.

## Source trail

[README](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/README.md#L1); [Implementation](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/plexe/checkpointing.py#L70) - [License](https://github.com/plexe-ai/plexe/blob/a1e05f6dc4c0875e0075f3b6f020fbecef57a699/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
