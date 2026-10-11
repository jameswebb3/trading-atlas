# leoflow - Keep the outcome attached to the correct attempt

**Decision question:** Can a restart inherit the previous task outcome?

| Field | Review |
| --- | --- |
| Upstream | [neochaotic/leoflow](https://github.com/neochaotic/leoflow) |
| Primary area | Operations & Observability |
| Source commit | [9b3d80ed2ab9503a40883db76a0ac18a3135474e](https://github.com/neochaotic/leoflow/commit/9b3d80ed2ab9503a40883db76a0ac18a3135474e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | A record distinguishes success, failure and reschedule, rejects malformed or unknown versions, and carries an optional attempt epoch for matching the outcome to the execution that wrote it. The author field is only a declaration because task and agent share a UID. Invalid messages fall back to pod phase, so the reader must preserve that uncertainty. |

## What this project does

Leoflow schedules tasks and records compact versioned outcome messages. [README](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/README.md).

## Mechanism inspected

A record distinguishes success, failure and reschedule, rejects malformed or unknown versions, and carries an optional attempt epoch for matching the outcome to the execution that wrote it. [Implementation](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/internal/taskoutcome/record.go#L20-L103). [Related path](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/internal/taskoutcome/record.go#L207-L235).

## Limitation that matters

The author field is only a declaration because task and agent share a UID. Invalid messages fall back to pod phase, so the reader must preserve that uncertainty. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Give each restart an attempt identity, reject stale terminal evidence, and keep malformed outcomes distinct from genuine failures.

## Why this score

Clear restart semantics with an explicit trust caveat, useful beyond Kubernetes when a worker can restart.

## Source trail

[README](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/README.md) - [Implementation](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/internal/taskoutcome/record.go#L20-L103) - [Related path](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/internal/taskoutcome/record.go#L207-L235) - [License](https://github.com/neochaotic/leoflow/blob/9b3d80ed2ab9503a40883db76a0ac18a3135474e/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
