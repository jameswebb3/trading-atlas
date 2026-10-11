# OpenAGS Auto Researcher - Does a container sandbox prevent an agent from changing the host workspace?

**Decision question:** Does a container sandbox prevent an agent from changing the host workspace?

| Field | Review |
| --- | --- |
| Upstream | [openags/auto-researcher](https://github.com/openags/auto-researcher) |
| Primary area | Agents & Decision Systems |
| Source commit | [9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f](https://github.com/openags/auto-researcher/commit/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It applies container limits but mounts a configured host workspace at /workspace with read-write access. The limits do not protect files in that bind mount; a generated experiment can mutate the host workspace. |

## What this project does

A Docker-based automated experiment engine.

## Mechanism inspected

It applies container limits but mounts a configured host workspace at /workspace with read-write access.

## Limitation that matters

The limits do not protect files in that bind mount; a generated experiment can mutate the host workspace.

## Practical check for a trading system

Mount immutable inputs read-only and isolate writable scratch space for generated research code.

## Why this score

2/5. The code shows why container limits and filesystem authority are separate controls.

## Source trail

[README](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/README.md#L1); [packages/app/src/research/experiment.ts](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/packages/app/src/research/experiment.ts#L59); [packages/app/src/research/experiment.ts](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/packages/app/src/research/experiment.ts#L80); [Root license](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
