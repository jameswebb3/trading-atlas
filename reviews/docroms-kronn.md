# Kronn — Treat an attempted external action with no receipt as ambiguous

**Decision question:** After a crash, is it safe to submit the same paid action again?

| Field | Review |
| --- | --- |
| Upstream | [DocRoms/Kronn](https://github.com/DocRoms/Kronn) |
| Primary area | Execution & Exchange Integration |
| Source commit | [b241b233b2b2cbf4c367b866314942e283f591e4](https://github.com/DocRoms/Kronn/commit/b241b233b2b2cbf4c367b866314942e283f591e4) |
| Reviewed | 2026-10-09 |
| Declared license | AGPL ([source](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The worker records submission before the external call; if a provider handle exists it polls, while an attempted submission with no handle refuses automatic resubmission. A media provider differs from an exchange: orders may be recoverable by client ID and fills/account state. Refusal means unresolved, not proof the external action failed. |

## What this project does

Agent media-job runner with explicit submit, poll and unsafe-resume states. [README](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/README.md).

## Mechanism inspected

The worker records submission before the external call; if a provider handle exists it polls, while an attempted submission with no handle refuses automatic resubmission. [Implementation](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/backend/src/agents/media_worker.rs#L23-L44).

## Limitation that matters

A media provider differs from an exchange: orders may be recoverable by client ID and fills/account state. Refusal means unresolved, not proof the external action failed. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For order and agent side effects, persist intent before send; on restart reconcile by external identity and authoritative events before a retry, and surface an unresolved state when evidence is incomplete.

## Why this score

The worker records submission before the external call; if a provider handle exists it polls, while an attempted submission with no handle refuses automatic resubmission. A media provider differs from an exchange: orders may be recoverable by client ID and fills/account state. Refusal means unresolved, not proof the external action failed.

## Source trail

[README](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/README.md) · [Implementation](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/backend/src/agents/media_worker.rs#L23-L44) · [License](https://github.com/DocRoms/Kronn/blob/b241b233b2b2cbf4c367b866314942e283f591e4/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
