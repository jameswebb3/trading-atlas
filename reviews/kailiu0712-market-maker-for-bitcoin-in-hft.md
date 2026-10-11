# Bitcoin HFT Market Maker - How much trade volume reaches a maker order after the queue ahead?

**Decision question:** How much trade volume reaches a maker order after the queue ahead?

| Field | Review |
| --- | --- |
| Upstream | [kailiu0712/Market-Maker-for-Bitcoin-in-HFT](https://github.com/kailiu0712/Market-Maker-for-Bitcoin-in-HFT) |
| Primary area | Backtesting & Simulation |
| Source commit | [9a319cd6ee8ad70b57e08871c5db56bfd7f07c03](https://github.com/kailiu0712/Market-Maker-for-Bitcoin-in-HFT/commit/9a319cd6ee8ad70b57e08871c5db56bfd7f07c03) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The simulator subtracts queue-ahead quantity from an observed trade and caps the residual fill by the resting order size. Queue position is inferred from level depth and a configurable touch-fill fraction; market-by-price data cannot prove actual order priority. |

## What this project does

An event-driven Bitcoin market-making research stack.

## Mechanism inspected

The simulator subtracts queue-ahead quantity from an observed trade and caps the residual fill by the resting order size.

## Limitation that matters

Queue position is inferred from level depth and a configurable touch-fill fraction; market-by-price data cannot prove actual order priority.

## Practical check for a trading system

Report maker outcomes as a range across queue assumptions and distinguish inferred fills from account fills.

## Why this score

3/5. The fill rule is concrete, but its queue state is an assumption rather than an exchange observation.

## Source trail

[README](https://github.com/kailiu0712/Market-Maker-for-Bitcoin-in-HFT/blob/9a319cd6ee8ad70b57e08871c5db56bfd7f07c03/README.md#L1); [execution_simulator.py](https://github.com/kailiu0712/Market-Maker-for-Bitcoin-in-HFT/blob/9a319cd6ee8ad70b57e08871c5db56bfd7f07c03/execution_simulator.py#L233).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
