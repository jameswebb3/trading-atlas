# open-multi-agent — Persist tool intent and approval before agent side effects

**Decision question:** Which agent tool calls will be repeated after a restart?

| Field | Review |
| --- | --- |
| Upstream | [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) |
| Primary area | Agents & Decision Systems |
| Source commit | [6ec5498643c7e431aa66751f17f47a529e7f927c](https://github.com/open-multi-agent/open-multi-agent/commit/6ec5498643c7e431aa66751f17f47a529e7f927c) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It checkpoints the assistant turn before tools run; pending approvals are persisted before notifying a human; completed tools get individual commit records so a restored round skips them. A crash after an external tool side effect but before its commit checkpoint can still repeat that call. Side-effecting tools need an idempotency key or reconciliation, and checkpoint writes themselves must be durable. |

## What this project does

Agent runner with per-tool checkpoints, durable approval suspension and event journal. [README](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/README.md).

## Mechanism inspected

It checkpoints the assistant turn before tools run; pending approvals are persisted before notifying a human; completed tools get individual commit records so a restored round skips them. [Implementation](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/packages/core/src/agent/runner.ts#L1233-L1325).

## Limitation that matters

A crash after an external tool side effect but before its commit checkpoint can still repeat that call. Side-effecting tools need an idempotency key or reconciliation, and checkpoint writes themselves must be durable. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For agent write tools, persist intent and approval, record a stable action ID, and classify crash windows before allowing automatic replay.

## Why this score

It checkpoints the assistant turn before tools run; pending approvals are persisted before notifying a human; completed tools get individual commit records so a restored round skips them. A crash after an external tool side effect but before its commit checkpoint can still repeat that call. Side-effecting tools need an idempotency key or reconciliation, and checkpoint writes themselves must be durable.

## Source trail

[README](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/README.md) · [Implementation](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/packages/core/src/agent/runner.ts#L1233-L1325) · [License](https://github.com/open-multi-agent/open-multi-agent/blob/6ec5498643c7e431aa66751f17f47a529e7f927c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
