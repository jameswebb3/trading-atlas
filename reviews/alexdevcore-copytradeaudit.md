# CopyTradeAudit - Does copied-trader skill add edge beyond the market price?

**Decision question:** Does copied-trader skill add edge beyond the market price?

| Field | Review |
| --- | --- |
| Upstream | [AlexDevCore/CopyTradeAudit](https://github.com/AlexDevCore/CopyTradeAudit) |
| Primary area | Signals & Models |
| Source commit | [cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8](https://github.com/AlexDevCore/CopyTradeAudit/commit/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Checks trader selection against price-only controls and models depth-limited, fee-bearing paper fills. A captured ask book is not an order-arrival fill, and unknown outcomes reduce the scored sample. |

## What this project does

A Polymarket research audit that compares public-trader copying with simple price-conditioned controls and models executable buy costs.

## Mechanism inspected

Trader skill aggregates resolved decisions and realized ROI rather than win rate alone. The paper execution path consumes ask depth, permits partial fills and charges fees on filled notional.

## Limitation that matters

The README's negative performance result and event counts were not independently replicated. Its paper fill consumes a captured snapshot immediately; latency, queue changes and settlement alignment require separate evidence. Markets with unknown outcomes are skipped in the skill calculation.

## Practical check for a trading system

Compare a copied signal with a price-only control, and require as-of resolved outcomes plus depth, fees and detection delay before declaring incremental value.

## Why this score

3/5 because The comparator and execution-cost mechanics are directly useful, while reported statistical and live conclusions remain unverified.

## Source trail

[README](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/README.md#L15); [README](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/README.md#L31); [src/scoring/skill.py](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/src/scoring/skill.py#L65); [src/paper/execution.py](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/src/paper/execution.py#L41); [src/paper/execution.py](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/src/paper/execution.py#L62); [License text](https://github.com/AlexDevCore/CopyTradeAudit/blob/cc5b5248dd5c4a2a77671fba32a922f9f0eb64f8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
