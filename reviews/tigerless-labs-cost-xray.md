# Cost Xray: Which agent inputs consume the budget, and how reliable is that attribution?

**Decision question:** Which agent inputs consume the budget, and how reliable is that attribution?

| Field | Review |
| --- | --- |
| Upstream | [tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray) |
| Primary area | Agents & Decision Systems |
| Source commit | [069733fabdc1416f2535148c0652cdfbb5bb7bee](https://github.com/tigerless-labs/cost-xray/commit/069733fabdc1416f2535148c0652cdfbb5bb7bee) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | A local proxy writes redacted request/response deltas to an append-only store; a separate materializer derives events. reconcile_turn scales approximate event tokens to wire usage and partitions cached, rewritten, fresh and output cost. Provider tokenization and pricing may be approximate or change. Header and selected body-key redaction cannot guarantee that secrets in arbitrary text are removed. Proxying agent traffic is invasive and untested here. |

## What this project does

Captures agent API requests, stores redacted deltas, and allocates billed usage across prompt sections and tools, including cached input. Attribution is estimated; intercepting full prompts creates a privacy boundary.

## Mechanism inspected

A local proxy writes redacted request/response deltas to an append-only store; a separate materializer derives events. reconcile_turn scales approximate event tokens to wire usage and partitions cached, rewritten, fresh and output cost.

## Limitation that matters

Provider tokenization and pricing may be approximate or change. Header and selected body-key redaction cannot guarantee that secrets in arbitrary text are removed. Proxying agent traffic is invasive and untested here.

## Practical check for a trading system

Link run ID, model, tool and billed usage; reconcile allocations to provider totals while minimizing stored content and controlling retention.

## Why this score

3/5 transferable: per-source cost breakdown can discipline agent research budgets, but privacy and proxy maintenance favor borrowing only the accounting pattern.

## Source trail

[README.md](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/README.md#L9); [README.md](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/README.md#L133); [docs/architecture.md](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/docs/architecture.md#L7); [cost_xray/addon.py](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/cost_xray/addon.py#L36); [cost_xray/events.py](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/cost_xray/events.py#L96); [cost_xray/classify.py](https://github.com/tigerless-labs/cost-xray/blob/069733fabdc1416f2535148c0652cdfbb5bb7bee/cost_xray/classify.py#L65)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
