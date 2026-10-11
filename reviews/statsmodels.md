# Statsmodels: correct a declared family of tests, not one winning p-value

**Decision question:** How should many statistical claims be counted together?

| Field | Review |
| --- | --- |
| Upstream | [Statsmodels](https://github.com/statsmodels/statsmodels) |
| Primary area | Signals & Models |
| Source commit | [fe7883d47b7a99e1972b1cd8628174845aa00e52](https://github.com/statsmodels/statsmodels/commit/fe7883d47b7a99e1972b1cd8628174845aa00e52) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Provides Bonferroni, Holm, Benjamini-Hochberg, and other multiple-test corrections over a supplied vector of p-values. The correction only covers tests included in that vector; hidden feature or parameter trials leave the denominator understated. |

## Project overview

Statistical modelling library for regression, time-series analysis, and inference. Includes diagnostics and multiple-testing corrections for research that compares many signals or models.

[Project documentation](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/README.md#L40-L93).

## Mechanism worth inspecting

The [statistics overview](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/README.md#L62-L89) includes time-series and hypothesis-test tooling. The [statistics guide](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/docs/source/stats.rst#L314-L360) lists multiple-comparison procedures. The [multipletests API](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/statsmodels/stats/multitest.py#L99-L160) takes the full p-value array and a named method; the [FDR branch](https://github.com/statsmodels/statsmodels/blob/fe7883d47b7a99e1972b1cd8628174845aa00e52/statsmodels/stats/multitest.py#L269-L278) delegates Benjamini-Hochberg or Benjamini-Yekutieli correction. The method is explicit, inspectable research policy.

## Important limit

No function can count hypotheses that were never supplied. Trading trials are often dependent and selected adaptively, so a corrected p-value is not a substitute for complete experiment history, an untouched evaluation set, or a return-distribution correction.

## Questions to take into your own design

- Is the family of tried variants recorded before selecting the winner?
- Are the correction assumptions appropriate for dependent trials?

## Why this score for a trading system

Multiple-test procedures are relevant to strategy selection, but they require a complete preregistered trial family and valid p-values.

**Scope of this review:** We read the pinned README, statistics guide, and multiple-testing implementation. We did not evaluate a trading signal.
