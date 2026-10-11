# Freqtrade: what sliced backtests can reveal about lookahead

**Decision question:** Can a strategy validator expose future-data leakage without proving every possible path safe?

| Field | Review |
| --- | --- |
| Upstream | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) |
| Primary area | Testing & Verification |
| Source commit | [c0a991f5632cb900075ff2864b6671ed71a319d7](https://github.com/freqtrade/freqtrade/commit/c0a991f5632cb900075ff2864b6671ed71a319d7) |
| Reviewed | 2026-09-25 |
| Declared license | [GPL-3.0](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Freqtrade provides a concrete lookahead check by comparing baseline and sliced backtests. It only assesses exercised signals, and pair-dependent strategies can produce false positives. |

## Project overview

Python crypto trading bot combining backtesting, strategy optimization, and dry-run trading. Includes lookahead analysis for investigating whether strategy decisions depend on future data.

[Project documentation](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/README.md#L9-L24).

## Mechanism worth inspecting

Freqtrade's [lookahead analysis](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/docs/lookahead-analysis.md#L51-L59) first runs a full baseline backtest. It then reruns individual entry and exit cases on sliced data and compares results. The [implementation compares indicator dataframes](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/freqtrade/optimize/analysis/lookahead.py#L65-L95) and checks whether the corresponding entry or exit still appears in the [sliced runs](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/freqtrade/optimize/analysis/lookahead.py#L139-L201).

The key pattern is a differential test: ask whether an earlier decision changes when later data is withheld.

## Where the evidence stops

The [documentation states](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/docs/lookahead-analysis.md#L98-L112) that untriggered signals are not checked and that pair-dependent behavior or limit-order callbacks can create false positives. The [implementation also enforces a minimum number of trades](https://github.com/freqtrade/freqtrade/blob/c0a991f5632cb900075ff2864b6671ed71a319d7/freqtrade/optimize/analysis/lookahead.py#L203-L222). "No bias detected" is therefore a statement about the exercised cases, not a general proof of causal correctness.

## Questions to take into your own validator

- Does the check report how many distinct signal paths were exercised?
- Can it identify the first indicator value or decision that changed?
- Are test conditions stable between the baseline and sliced runs?
- Are insufficient coverage and no detected bias distinct outcomes?

## Why this score for a trading system

The sliced-backtest comparison targets lookahead in trading signals; coverage stops at signals actually exercised in the test.

**Scope of this review:** We inspected the pinned documentation and lookahead implementation. We did not run a strategy, inspect all backtest internals, or validate the detector's sensitivity on an independent benchmark.
