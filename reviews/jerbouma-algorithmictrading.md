# AlgorithmicTrading Cointegration - Does an in-sample cointegration test establish a tradable pair?

**Decision question:** Does an in-sample cointegration test establish a tradable pair?

| Field | Review |
| --- | --- |
| Upstream | [JerBouma/AlgorithmicTrading](https://github.com/JerBouma/AlgorithmicTrading) |
| Primary area | Signals & Models |
| Source commit | [87886cc8bf32f9ec9871c289cb5076371d5c1fb0](https://github.com/JerBouma/AlgorithmicTrading/commit/87886cc8bf32f9ec9871c289cb5076371d5c1fb0) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The code estimates the long-run OLS relationship and runs an ADF test on its residuals. Its own note says the reported ADF p-value assumes residuals were not estimated first; the file shows no out-of-sample selection gate. |

## What this project does

An educational equity statistical-arbitrage example.

## Mechanism inspected

The code estimates the long-run OLS relationship and runs an ADF test on its residuals.

## Limitation that matters

Its own note says the reported ADF p-value assumes residuals were not estimated first; the file shows no out-of-sample selection gate.

## Practical check for a trading system

Use a properly calibrated residual test and reserve untouched periods before promoting a pair.

## Why this score

2/5. The explicit caveat helps prevent false statistical confidence, but it is not a validated perpetual strategy.

## Source trail

[README](https://github.com/JerBouma/AlgorithmicTrading/blob/87886cc8bf32f9ec9871c289cb5076371d5c1fb0/README.md#L1); [Statistical Arbitrage/cointegration_analysis.py](https://github.com/JerBouma/AlgorithmicTrading/blob/87886cc8bf32f9ec9871c289cb5076371d5c1fb0/Statistical%20Arbitrage/cointegration_analysis.py#L51); [Statistical Arbitrage/cointegration_analysis.py](https://github.com/JerBouma/AlgorithmicTrading/blob/87886cc8bf32f9ec9871c289cb5076371d5c1fb0/Statistical%20Arbitrage/cointegration_analysis.py#L110); [Root license](https://github.com/JerBouma/AlgorithmicTrading/blob/87886cc8bf32f9ec9871c289cb5076371d5c1fb0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
