# Mechanist — Terminal job states need explicit error classes

**Decision question:** When should an agent stop polling a completed failure?

| Field | Review |
| --- | --- |
| Upstream | [zjunlp/Mechanist](https://github.com/zjunlp/Mechanist) |
| Primary area | Agents & Decision Systems |
| Source commit | [40537589e8fda9583d4d299f4a65dcdc1ddf74f7](https://github.com/zjunlp/Mechanist/commit/40537589e8fda9583d4d299f4a65dcdc1ddf74f7) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its client distinguishes completed jobs from failed, canceled, and stopped jobs so a killed job is reported as terminal instead of poll-timeout noise. Status mapping is local to this service; a trading research agent also needs evidence for incomplete outputs and timed-out external calls. |

## What this project does

A research-agent system with a remote mechanics job service. [Project README](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/README.md#L1).

## Mechanism inspected

Its client distinguishes completed jobs from failed, canceled, and stopped jobs so a killed job is reported as terminal instead of poll-timeout noise. [Implementation](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/mcp-servers/mechanic-db/server.py#L54).

## Limitation that matters

Status mapping is local to this service; a trading research agent also needs evidence for incomplete outputs and timed-out external calls. This is a source review, not a runtime or security test.

## Practical check for a trading system

Record queued, running, completed, canceled, stopped, and failed with separate reasons and output validity.

## Why this score

A practical asynchronous job-state distinction, though the domain and service are not trading-specific.

## Source trail

[README](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/README.md#L1); [Implementation](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/mcp-servers/mechanic-db/server.py#L54) - [License](https://github.com/zjunlp/Mechanist/blob/40537589e8fda9583d4d299f4a65dcdc1ddf74f7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
