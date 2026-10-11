# ordersim — Compare the full execution trace, not only final P&L

**Decision question:** Does a faster execution engine reproduce the same order and fill path as its reference engine?

| Field | Review |
| --- | --- |
| Upstream | [tradingexpert/ordersim](https://github.com/tradingexpert/ordersim) |
| Primary area | Backtesting & Simulation |
| Source commit | [0cd832a0842e46b74959e29f2a1e5a6154212044](https://github.com/tradingexpert/ordersim/commit/0cd832a0842e46b74959e29f2a1e5a6154212044) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its equivalence helper replays the same canonical events through reference and candidate engines, then compares fills, positions, resting orders, summaries, equity and order events. The built-in equivalence suite contains only a market-order and a queue-ahead case; reconstructed virtual MBO remains modeled evidence even when two engines agree. |

## What this project does

ordersim is an execution replay framework with a canonical MBO event boundary, optional Python/C++ engines and explicit observed-versus-reconstructed order-level input paths. [Project README](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/README.md#L1).

## Mechanism inspected

The helper normalizes one input stream, runs it through reference and candidate engines, and compares six outcome families. Its replay boundary stops at the first passive fill or slice end so scalar and compiled paths can be tested against the same event boundary. [Equivalence helper](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/src/ordersim/testing/equivalence.py#L18).

## Limitation that matters

Equivalence can prove only consistency between the two implementations on the chosen fixtures, not that their shared market model is faithful. The README explicitly distinguishes observed MBO from virtual MBO inferred from L2 and trades. This is a source review, not a runtime or security test.

## Practical check for a trading system

For any replay optimization, retain a simple reference path and compare event order, ACK/fill/cancel traces, fees, position and final state across partial fills, gaps and reconnects. Label inferred queue data separately from observed order identities.

## Why this score

4/5 because replay-engine equivalence on fills and order events addresses a direct trading-system risk, with broader venue and race coverage still needed.

## Source trail

[README](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/README.md#L22); [Equivalence helper](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/src/ordersim/testing/equivalence.py#L18); [Replay boundary](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/src/ordersim/replay/boundary.py#L25); [License](https://github.com/tradingexpert/ordersim/blob/0cd832a0842e46b74959e29f2a1e5a6154212044/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
