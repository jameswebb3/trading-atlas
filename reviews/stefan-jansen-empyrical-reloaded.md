# Empyrical Reloaded — the annualization clock is a parameter

**Decision question:** Does the risk metric use the same sampling clock as the return series?

| Field | Review |
| --- | --- |
| Upstream | [Empyrical Reloaded](https://github.com/stefan-jansen/empyrical-reloaded) |
| Primary area | Portfolio & Risk |
| Source commit | [efe60664f0abd957074b0751ef82228594a659a5](https://github.com/stefan-jansen/empyrical-reloaded/commit/efe60664f0abd957074b0751ef82228594a659a5) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/stefan-jansen/empyrical-reloaded/blob/efe60664f0abd957074b0751ef82228594a659a5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A transparent metrics reference with a consequential default: daily annualization assumes business days. Continuous markets and irregular return samples need an explicit clock and consistent missing-period treatment. |

## Project overview

Empyrical Reloaded provides financial return and risk metrics, including annualized volatility and Sharpe ratios. [Project documentation](https://github.com/stefan-jansen/empyrical-reloaded/blob/efe60664f0abd957074b0751ef82228594a659a5/README.md#L17-L17).

## Mechanism worth inspecting

Sharpe uses a NaN-aware sample mean and standard deviation and scales the result with the square root of an annualization factor. The daily factor maps to approximately 252 business days by default. [Sharpe calculation](https://github.com/stefan-jansen/empyrical-reloaded/blob/efe60664f0abd957074b0751ef82228594a659a5/src/empyrical/stats.py#L645-L657); [period constants](https://github.com/stefan-jansen/empyrical-reloaded/blob/efe60664f0abd957074b0751ef82228594a659a5/src/empyrical/periods.py#L1-L20).

## Important limit

A business-day default is not automatically appropriate for continuous crypto trading, intraday bars or irregular trade-level returns. NaN omission also does not certify regular coverage. Sampling frequency, return denominator and missing-period treatment must accompany the metric.

## Questions to take into your own design

- Does every displayed Sharpe identify whether inputs are bars, days or individual trades?
- Are annualization and missing-period rules identical across reporting, research and risk thresholds?

## Why this score for a trading system

3/5: a transparent financial-metric reference, with sampling-clock and coverage definitions still necessary for a valid trading comparison.

**Scope of this review:** Sharpe annualization and missing-value handling; not a comprehensive audit of financial metrics.
