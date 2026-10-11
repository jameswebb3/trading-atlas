# Finlab Crypto — Count the observations your overfit test drops

**Decision question:** Can an overfitting diagnostic silently omit the final observations?

| Field | Review |
| --- | --- |
| Upstream | [finlab-python/finlab_crypto](https://github.com/finlab-python/finlab_crypto) |
| Primary area | Signals & Models |
| Source commit | [2b3305fd6adacdf1732866d3e931e1fa061ebdf8](https://github.com/finlab-python/finlab_crypto/commit/2b3305fd6adacdf1732866d3e931e1fa061ebdf8) |
| Reviewed | 2026-10-10 |
| Declared license | GPL-3.0 ([source](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The CSCV implementation divides returns into equal bins using floor division and compares the best in-sample candidate with its out-of-sample rank. Rows after n_bins times the floored bin size are unused. |

## What this project does

Crypto research tools for Binance data, vectorized backtests, optimization, and CSCV overfitting diagnostics. [Project README](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/README.md#L7).

## Mechanism inspected

The CSCV implementation divides returns into equal bins using floor division and compares the best in-sample candidate with its out-of-sample rank. [Implementation](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/overfitting.py#L37). [Related source 1](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/overfitting.py#L55). [Related source 2](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/strategy.py#L113).

## Limitation that matters

Rows after n_bins times the floored bin size are unused. A changelog also records a prior same-bar execution-price bug. Binance spot execution does not transfer to perps. This is a source review, not a runtime or security test.

## Practical check for a trading system

Report total rows, rows actually used, candidate universe, and exact fill-price semantics with every CSCV result.

## Why this score

Concrete diagnostic code reveals both a sample-denominator hazard and an execution-timing correction; it is not independent alpha evidence.

## Source trail

[README](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/README.md#L7); [Implementation](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/overfitting.py#L37); [Related source 1](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/overfitting.py#L55); [Related source 2](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/finlab_crypto/strategy.py#L113) - [License](https://github.com/finlab-python/finlab_crypto/blob/2b3305fd6adacdf1732866d3e931e1fa061ebdf8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
