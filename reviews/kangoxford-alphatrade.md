# AlphaTrade - How can an orderbook simulator preserve price-time priority and action latency?

**Decision question:** How can an orderbook simulator preserve price-time priority and action latency?

| Field | Review |
| --- | --- |
| Upstream | [KangOxford/AlphaTrade](https://github.com/KangOxford/AlphaTrade) |
| Primary area | Backtesting & Simulation |
| Source commit | [2b1951fb47392db0e6d832c81a21a39a6b5eed05](https://github.com/KangOxford/AlphaTrade/commit/2b1951fb47392db0e6d832c81a21a39a6b5eed05) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Implements price-time book matching and delayed execution-agent actions. Historical queue observability and venue-specific matching remain separate questions. |

## What this project does

A JAX limit-order-book simulator and execution-learning environment using historical order messages.

## Mechanism inspected

The book chooses best price then earliest time and nanoseconds at that price, matches partial quantities, and advances agent actions with an observation-to-action delay. The execution environment can switch to a market order near its deadline.

## Limitation that matters

Its book state is limited by the recorded order-log schema and fixed array capacity; simulation of one venue does not establish Hyperliquid queue behavior or actual fill allocation. No root license text was verified.

## Practical check for a trading system

Use price-time and delay as explicit simulator contracts, then test venue-specific cancel/add semantics and bounded-state overflow separately.

## Why this score

4/5. Price-time matching and delayed agent actions are strong direct microstructure references.

## Source trail

[README](https://github.com/KangOxford/AlphaTrade/blob/2b1951fb47392db0e6d832c81a21a39a6b5eed05/README.md#L1); [gymnax_exchange/jaxob/JaxOrderBookArrays.py](https://github.com/KangOxford/AlphaTrade/blob/2b1951fb47392db0e6d832c81a21a39a6b5eed05/gymnax_exchange/jaxob/JaxOrderBookArrays.py#L88); [gymnax_exchange/jaxob/JaxOrderBookArrays.py](https://github.com/KangOxford/AlphaTrade/blob/2b1951fb47392db0e6d832c81a21a39a6b5eed05/gymnax_exchange/jaxob/JaxOrderBookArrays.py#L115); [gymnax_exchange/jaxen/exec_env.py](https://github.com/KangOxford/AlphaTrade/blob/2b1951fb47392db0e6d832c81a21a39a6b5eed05/gymnax_exchange/jaxen/exec_env.py#L302).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
