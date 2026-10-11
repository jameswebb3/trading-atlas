# strat-validation - Can overlapping labels and many trials inflate a strategy's score?

**Decision question:** Can overlapping labels and many trials inflate a strategy's score?

| Field | Review |
| --- | --- |
| Upstream | [sergosumy007/strat-validation](https://github.com/sergosumy007/strat-validation) |
| Primary area | Research & Reproducibility |
| Source commit | [d939bbea2cc461cebccc1452de89a449a1a31b39](https://github.com/sergosumy007/strat-validation/commit/d939bbea2cc461cebccc1452de89a449a1a31b39) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Purges overlapping outcome windows and adjusts Sharpe evidence for the number of tested variants. DSR cannot correct an unrecorded search or a feature available after decision time. |

## What this project does

A standalone research toolkit for combinatorial purged cross-validation and deflated Sharpe calculations.

## Mechanism inspected

The splitter uses both prediction and evaluation times to purge overlapping training labels, adds an embargo after test intervals, and recombines test folds into out-of-sample paths. The DSR code estimates a Sharpe hurdle from trial count.

## Limitation that matters

These methods do not repair bad available-at timestamps, missing costs or an incomplete count of attempted variants. The same repository's formulas require the researcher to supply honest trial variance and effective trial count.

## Practical check for a trading system

Bind every trial and label interval to a manifest, then compute purged paths and a selection-aware statistic only after data and execution assumptions pass.

## Why this score

3/5 because Directly relevant inferential controls are implemented, with correctness depending on truthful inputs and trial bookkeeping.

## Source trail

[README](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/README.md#L1); [cpcv.py](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/cpcv.py#L104); [cpcv.py](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/cpcv.py#L116); [deflated_sharpe.py](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/deflated_sharpe.py#L103); [deflated_sharpe.py](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/deflated_sharpe.py#L127); [License text](https://github.com/sergosumy007/strat-validation/blob/d939bbea2cc461cebccc1452de89a449a1a31b39/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
