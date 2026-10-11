# Zenflow: Can an agent message disappear when its target finishes?

**Decision question:** Can an agent message disappear when its target finishes?

| Field | Review |
| --- | --- |
| Upstream | [zendev-sh/zenflow](https://github.com/zendev-sh/zenflow) |
| Primary area | Agents & Decision Systems |
| Source commit | [91f57ed03b673a1927a0115b17fd7f064657925f](https://github.com/zendev-sh/zenflow/commit/91f57ed03b673a1927a0115b17fd7f064657925f) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The router drains unread messages with a typed drop event before closing a terminal step. The delivery engine wakes idle targets that have unread mail, using a per-step lock to avoid a read-versus-terminal race. The architecture enumerates drop causes and exposes a drop callback. Default mailbox is in memory and bounded; explicit drop reporting improves observability but does not itself recover a lost research instruction. Agent synthesis and accuracy remain independent problems. |

## What this project does

Routes inter-agent messages through per-step mailboxes and emits typed reasons when delivery fails, including full mailboxes and terminal targets. Its wake loop and in-memory mailbox still need durable evidence if message loss would affect a research decision.

## Mechanism inspected

The router drains unread messages with a typed drop event before closing a terminal step. The delivery engine wakes idle targets that have unread mail, using a per-step lock to avoid a read-versus-terminal race. The architecture enumerates drop causes and exposes a drop callback.

## Limitation that matters

Default mailbox is in memory and bounded; explicit drop reporting improves observability but does not itself recover a lost research instruction. Agent synthesis and accuracy remain independent problems.

## Practical check for a trading system

In a multi-agent research review, test target cancellation, full mailbox and shutdown while messages are pending. Require an acknowledged evidence item or a recorded drop before finalizing the verdict.

## Why this score

3/5 transferable: typed drops and terminal draining address silent agent coordination failures, but implementation is broad and does not validate trading conclusions.

## Source trail

[README.md](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/README.md#L49); [docs/architecture.md](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/docs/architecture.md#L131); [docs/architecture.md](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/docs/architecture.md#L139); [internal/router/router.go](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/internal/router/router.go#L910); [internal/router/delivery_engine.go](https://github.com/zendev-sh/zenflow/blob/91f57ed03b673a1927a0115b17fd7f064657925f/internal/router/delivery_engine.go#L304)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
