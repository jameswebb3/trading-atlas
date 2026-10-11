# Alphalens: Evaluate factor rank and turnover separately

**Decision question:** Does a factor predict future ranks, and how fast does the selected basket change?

| Field | Review |
| --- | --- |
| Upstream | [quantopian/alphalens](https://github.com/quantopian/alphalens) |
| Primary area | Signals & Models |
| Source commit | [77084f1e4c2c0be407e032d444fb19e4be4b0f37](https://github.com/quantopian/alphalens/commit/77084f1e4c2c0be407e032d444fb19e4be4b0f37) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/quantopian/alphalens/blob/77084f1e4c2c0be407e032d444fb19e4be4b0f37/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Computes cross-sectional Spearman information coefficients against forward returns and tracks quantile turnover. Forward returns are valid for evaluation only after timing and universe membership have been fixed causally. |

## Mechanism worth inspecting

The factor_information_coefficient path computes rank correlation between factor values and forward returns by period. The same module defines quantile_turnover as names entering a prior quantile. Together they separate apparent predictive rank from trading churn.

**Source trail:** [project overview](https://github.com/quantopian/alphalens/blob/77084f1e4c2c0be407e032d444fb19e4be4b0f37/README.rst) · [documentation](https://github.com/quantopian/alphalens/blob/77084f1e4c2c0be407e032d444fb19e4be4b0f37/README.rst#L28-L45) · [implementation](https://github.com/quantopian/alphalens/blob/77084f1e4c2c0be407e032d444fb19e4be4b0f37/alphalens/performance.py#L28-L42) · [additional source](https://github.com/quantopian/alphalens/blob/77084f1e4c2c0be407e032d444fb19e4be4b0f37/alphalens/performance.py#L568-L585).

## Important limit

These metrics do not prove that factor values existed at signal time, that instruments were tradable, or that turnover survives fees and fills. The archived Quantopian project is best read as a statistical reference.

## Questions to take into your own design

- Are factor timestamps and return horizons locked before scoring?
- Does reported IC survive turnover and cost assumptions?

## Why this score for a trading system

Factor IC and turnover are relevant diagnostics, yet the equity-oriented, older code does not establish causal availability or trading costs.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
