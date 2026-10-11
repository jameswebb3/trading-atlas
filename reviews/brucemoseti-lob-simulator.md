# LOB Simulator - What does genuine FIFO matching add to a maker simulation?

**Decision question:** What does genuine FIFO matching add to a maker simulation?

| Field | Review |
| --- | --- |
| Upstream | [BruceMoseti/lob-simulator](https://github.com/BruceMoseti/lob-simulator) |
| Primary area | Backtesting & Simulation |
| Source commit | [c1f02a08236a1e48ab077d7bbf2f143ab6666a26](https://github.com/BruceMoseti/lob-simulator/commit/c1f02a08236a1e48ab077d7bbf2f143ab6666a26) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation, and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Models resting orders as FIFO objects and tests partial sweeps, cancellations and quantity conservation. Synthetic queue certainty should not be presented as observed exchange queue priority. |

## What this project does

A discrete-event order-book simulator with integer-tick prices, resting-order queues, partial fills and Poisson-generated flow.

## Mechanism inspected

Each price level stores individual orders; queue_ahead_of sums the live quantity before a particular order. The matching engine walks the queue and tests cover price priority, partial sweeps and cancellation.

## Limitation that matters

Queue position is exact only inside the synthetic book. Poisson flow and generated cancellations cannot establish a historical venue queue or adverse-selection rate.

## Practical check for a trading system

Use the book as a semantic test fixture for matching and inventory accounting; keep calibration to real trade and depth data as a separate task.

## Why this score

3/5 because A readable matching oracle and test cases are valuable, while the synthetic arrival model limits empirical trading conclusions.

## Source trail

[README](https://github.com/BruceMoseti/lob-simulator/blob/c1f02a08236a1e48ab077d7bbf2f143ab6666a26/README.md#L84); [src/lobsim/order_book.py](https://github.com/BruceMoseti/lob-simulator/blob/c1f02a08236a1e48ab077d7bbf2f143ab6666a26/src/lobsim/order_book.py#L144); [src/lobsim/matching_engine.py](https://github.com/BruceMoseti/lob-simulator/blob/c1f02a08236a1e48ab077d7bbf2f143ab6666a26/src/lobsim/matching_engine.py#L43); [tests/test_matching.py](https://github.com/BruceMoseti/lob-simulator/blob/c1f02a08236a1e48ab077d7bbf2f143ab6666a26/tests/test_matching.py#L44); [License text](https://github.com/BruceMoseti/lob-simulator/blob/c1f02a08236a1e48ab077d7bbf2f143ab6666a26/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
