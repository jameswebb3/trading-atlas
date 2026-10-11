# Neural - Does cancel response mean confirmed cancellation?

**Decision question:** Does cancel response mean confirmed cancellation?

| Field | Review |
| --- | --- |
| Upstream | [IntelIP/Neural](https://github.com/IntelIP/Neural) |
| Primary area | Execution & Exchange Integration |
| Source commit | [61984aa447ef7b1b5cd6b1d74f42026e1f8047ac](https://github.com/IntelIP/Neural/commit/61984aa447ef7b1b5cd6b1d74f42026e1f8047ac) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The Kalshi adapter maps create, cancel and status responses to common result objects. Any non-null cancel response becomes cancelled, without checking a terminal venue state. |

## What this project does

An SDK with normalized prediction-market exchange adapters.

## Mechanism inspected

The Kalshi adapter maps create, cancel and status responses to common result objects.

## Limitation that matters

Any non-null cancel response becomes cancelled, without checking a terminal venue state.

## Practical check for a trading system

Keep cancel acceptance and confirmed terminal cancellation separate.

## Why this score

2/5. Adapter abstraction is useful but overstates outcome certainty.

## Source trail

[README](https://github.com/IntelIP/Neural/blob/61984aa447ef7b1b5cd6b1d74f42026e1f8047ac/README.md#L1); [neural/trading/kalshi_adapter.py](https://github.com/IntelIP/Neural/blob/61984aa447ef7b1b5cd6b1d74f42026e1f8047ac/neural/trading/kalshi_adapter.py#L162); [Root license](https://github.com/IntelIP/Neural/blob/61984aa447ef7b1b5cd6b1d74f42026e1f8047ac/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
