# Backtesting Execution Simulator - Do simulated orders respect arrival delay and price-time matching?

**Decision question:** Do simulated orders respect arrival delay and price-time matching?

| Field | Review |
| --- | --- |
| Upstream | [SarthakDalmia1/backtesting_execution_simulator](https://github.com/SarthakDalmia1/backtesting_execution_simulator) |
| Primary area | Backtesting & Simulation |
| Source commit | [a0a5fcd2d0c033c5853dcef5187a717bc341bc10](https://github.com/SarthakDalmia1/backtesting_execution_simulator/commit/a0a5fcd2d0c033c5853dcef5187a717bc341bc10) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation, and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Separates order, cancel, data and fill-report delays while matching against a simulated price-time book. Internal FIFO tests do not validate historical queue position or the advertised performance target. |

## What this project does

A C++ event-driven simulator with an internal order book, configurable order and market-data latency, and maker/taker fill records.

## Mechanism inspected

Order submission, cancellation and incoming market data enter the event queue at different effective times. Matching emits one fill for each side at the resting order's price and applies partial quantities.

## Limitation that matters

The inspected matcher is an internally generated order book. Correct FIFO behavior inside that book does not establish historical queue position or fills against a live venue. The README's performance target is not a measured result in this review.

## Practical check for a trading system

Use it to test the sequencing contract, then compare modeled fill timing and queue assumptions against captured venue events before using its PnL as evidence.

## Why this score

3/5 because Concrete delay and matching paths are readable and matching tests exist, but external fill realism remains unverified.

## Source trail

[README](https://github.com/SarthakDalmia1/backtesting_execution_simulator/blob/a0a5fcd2d0c033c5853dcef5187a717bc341bc10/README.md#L95); [cpp/execution/execution_simulator.cpp](https://github.com/SarthakDalmia1/backtesting_execution_simulator/blob/a0a5fcd2d0c033c5853dcef5187a717bc341bc10/cpp/execution/execution_simulator.cpp#L25); [cpp/orderbook/matching_engine.cpp](https://github.com/SarthakDalmia1/backtesting_execution_simulator/blob/a0a5fcd2d0c033c5853dcef5187a717bc341bc10/cpp/orderbook/matching_engine.cpp#L208); [tests/test_matching_engine.cpp](https://github.com/SarthakDalmia1/backtesting_execution_simulator/blob/a0a5fcd2d0c033c5853dcef5187a717bc341bc10/tests/test_matching_engine.cpp#L83); [License text](https://github.com/SarthakDalmia1/backtesting_execution_simulator/blob/a0a5fcd2d0c033c5853dcef5187a717bc341bc10/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
