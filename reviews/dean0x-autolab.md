# autolab — Start competing research agents from one fixed commit

**Decision question:** Are agent experiments comparable if each starts from a different code state?

| Field | Review |
| --- | --- |
| Upstream | [dean0x/autolab](https://github.com/dean0x/autolab) |
| Primary area | Agents & Decision Systems |
| Source commit | [fabd7aaf14208ab74b978810b97b1fe9b8969d59](https://github.com/dean0x/autolab/commit/fabd7aaf14208ab74b978810b97b1fe9b8969d59) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Initialization resolves one base branch commit, creates a dedicated branch/worktree per agent from that base and records the base in the evolve configuration. The inspected setup does not freeze external data, model versions or timing; worktree isolation alone cannot make results comparable or causal. |

## What this project does

Autonomous experiment suite with separate Git worktrees for competing agents. [README](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/README.md).

## Mechanism inspected

Initialization resolves one base branch commit, creates a dedicated branch/worktree per agent from that base and records the base in the evolve configuration. [Implementation](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/auto-evolve/auto_evolve.py#L550-L635).

## Limitation that matters

The inspected setup does not freeze external data, model versions or timing; worktree isolation alone cannot make results comparable or causal. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

When comparing research agents, pin a common code/data snapshot and record each branch and result manifest before selecting a winner.

## Why this score

Initialization resolves one base branch commit, creates a dedicated branch/worktree per agent from that base and records the base in the evolve configuration. The inspected setup does not freeze external data, model versions or timing; worktree isolation alone cannot make results comparable or causal.

## Source trail

[README](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/README.md) · [Implementation](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/auto-evolve/auto_evolve.py#L550-L635) · [License](https://github.com/dean0x/autolab/blob/fabd7aaf14208ab74b978810b97b1fe9b8969d59/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
