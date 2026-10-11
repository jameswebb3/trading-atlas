# JAX-LOB - Does an order-book simulator preserve the queue after a cancel-and-replace?

**Decision question:** Does an order-book simulator preserve the queue after a cancel-and-replace?

| Field | Review |
| --- | --- |
| Upstream | [KangOxford/jax-lob](https://github.com/KangOxford/jax-lob) |
| Primary area | Backtesting & Simulation |
| Source commit | [d1f596610b04a09941c7a1b609e5bab541ecfc98](https://github.com/KangOxford/jax-lob/commit/d1f596610b04a09941c7a1b609e5bab541ecfc98) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Book arrays match by best price and earliest timestamp; the environment prepends agent cancels and actions to data messages. The environment describes a naive cancel-all action that resets queue position, so this path is not a faithful proxy for every live replacement policy. |

## What this project does

A JAX limit-order-book simulator and execution environment.

## Mechanism inspected

Book arrays match by best price and earliest timestamp; the environment prepends agent cancels and actions to data messages.

## Limitation that matters

The environment describes a naive cancel-all action that resets queue position, so this path is not a faithful proxy for every live replacement policy.

## Practical check for a trading system

Track queue-priority resets explicitly when using a LOB simulator as an execution reference.

## Why this score

3/5. Price-time matching is directly relevant, with queue treatment limiting live-execution transfer.

## Source trail

[README](https://github.com/KangOxford/jax-lob/blob/d1f596610b04a09941c7a1b609e5bab541ecfc98/README.md#L1); [gymnax_exchange/jaxob/JaxOrderBookArrays.py](https://github.com/KangOxford/jax-lob/blob/d1f596610b04a09941c7a1b609e5bab541ecfc98/gymnax_exchange/jaxob/JaxOrderBookArrays.py#L89); [gymnax_exchange/jaxob/JaxOrderBookArrays.py](https://github.com/KangOxford/jax-lob/blob/d1f596610b04a09941c7a1b609e5bab541ecfc98/gymnax_exchange/jaxob/JaxOrderBookArrays.py#L106); [gymnax_exchange/jaxen/exec_env.py](https://github.com/KangOxford/jax-lob/blob/d1f596610b04a09941c7a1b609e5bab541ecfc98/gymnax_exchange/jaxen/exec_env.py#L169); [gymnax_exchange/jaxen/exec_env.py](https://github.com/KangOxford/jax-lob/blob/d1f596610b04a09941c7a1b609e5bab541ecfc98/gymnax_exchange/jaxen/exec_env.py#L171).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
