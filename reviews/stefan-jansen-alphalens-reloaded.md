# Alphalens Reloaded — track what cleaning removes from the result

**Decision question:** Which observations and future outcomes survive a factor report?

| Field | Review |
| --- | --- |
| Upstream | [Alphalens Reloaded](https://github.com/stefan-jansen/alphalens-reloaded) |
| Primary area | Research & Reproducibility |
| Source commit | [f0a07c22d554e4b4036983cc80320b432714fe7e](https://github.com/stefan-jansen/alphalens-reloaded/commit/f0a07c22d554e4b4036983cc80320b432714fe7e) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A valuable factor-reporting reference with two concrete checks: account for sample loss at each cleaning stage and inspect future-return filtering. The convenience defaults differ from the lower-level API and can change the evaluated population. |

## Project overview

Alphalens Reloaded produces factor-performance reports, including returns, information coefficients, turnover and grouped analysis. [Project documentation](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/README.md#L17-L26).

## Mechanism worth inspecting

Factor cleaning tracks the input population, removes missing forward returns, bins factors and reports losses separately for forward-return computation and binning. It raises when total loss exceeds `max_loss`. [Cleaning stages](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/src/alphalens/utils.py#L645-L678).

## Important limit

The convenience function defaults to `max_loss=0.35` and `filter_zscore=20`. The latter filters forward returns using their full-sample mean and standard deviation; the documentation explicitly warns of lookahead bias. The lower-level forward-return function defaults this filter to None. [Convenience defaults](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/src/alphalens/utils.py#L682-L694); [filter calculation](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/src/alphalens/utils.py#L312-L318); [warning](https://github.com/stefan-jansen/alphalens-reloaded/blob/f0a07c22d554e4b4036983cc80320b432714fe7e/src/alphalens/utils.py#L785-L788).

## Questions to take into your own design

- Does each report retain the original universe and exclusions by stage, date and instrument?
- Are outcome-based filters explicitly disabled or reported as retrospective diagnostics?

## Why this score for a trading system

4/5: a highly relevant factor-research reference with both auditable sample-loss accounting and an explicit outcome-filtering trap; it still does not validate alpha or execution.

**Scope of this review:** Forward-return filtering and factor-cleaning population accounting; no factor returns were replicated.
