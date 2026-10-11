# HolmesGPT — Duplicate read protection does not apply to writes

**Decision question:** When is it safe for an agent to suppress a repeated tool call?

| Field | Review |
| --- | --- |
| Upstream | [HolmesGPT/holmesgpt](https://github.com/HolmesGPT/holmesgpt) |
| Primary area | Operations & Observability |
| Source commit | [46e3a728d762b774d2ec458357decb8698541ce5](https://github.com/HolmesGPT/holmesgpt/commit/46e3a728d762b774d2ec458357decb8698541ce5) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It blocks an identical prior call only on the assumption that tools are read-only; the source warns that this guard should change if tools mutate resources. A duplicate write may need idempotent replay, not suppression based on argument equality; a read may also need refresh after state changes. |

## What this project does

An operations investigation agent with tool-call safeguards. [Project README](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/README.md#L1).

## Mechanism inspected

It blocks an identical prior call only on the assumption that tools are read-only; the source warns that this guard should change if tools mutate resources. [Implementation](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/holmes/core/safeguards.py#L24).

## Limitation that matters

A duplicate write may need idempotent replay, not suppression based on argument equality; a read may also need refresh after state changes. This is a source review, not a runtime or security test.

## Practical check for a trading system

Classify tools by effect and use durable idempotency keys for any trading write.

## Why this score

A concrete agent-tool safety boundary with direct implications for order APIs.

## Source trail

[README](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/README.md#L1); [Implementation](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/holmes/core/safeguards.py#L24) - [License](https://github.com/HolmesGPT/holmesgpt/blob/46e3a728d762b774d2ec458357decb8698541ce5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
