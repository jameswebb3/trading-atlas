# Backtesting.py: optimization changes both the winner and the sample

**Decision question:** What does a parameter optimizer return after trying many backtests?

| Field | Review |
| --- | --- |
| Upstream | [Backtesting.py](https://github.com/kernc/backtesting.py) |
| Primary area | Backtesting & Simulation |
| Source commit | [ca2e2611621e472542ba90f7243a1fa06a7d7108](https://github.com/kernc/backtesting.py/commit/ca2e2611621e472542ba90f7243a1fa06a7d7108) |
| Reviewed | 2026-09-25 |
| Declared license | [AGPL-3.0](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/LICENSE.md#L1-L4) |
| Review depth | 2/3: README and strategy, run, and optimizer source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes the searched parameter grid and an optional heatmap, but by default returns the best run of that search. The run starts after the longest indicator warmup, so changing parameters can also change the evaluated period. Comparing only winning summary statistics can therefore mix search selection with unequal samples. |

## Mechanism worth inspecting

The [README](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/README.md#L99-L110) presents the optimizer. Its [strategy clock](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L185-L212) allows precomputation in init and decision steps in next. The [run loop](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1314-L1354) explicitly warns that indicator lookback changes the start bar and slices indicators before each decision. The [optimizer contract](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1386-L1445) supports grid or model-based search, a trial cap, constraints, a heatmap, and a fixed seed. Its [selection path](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1530-L1564) selects the heatmap maximum and reruns that combination.

## Important limit

A seed makes search replayable; it does not turn the selected maximum into an unbiased estimate. The review did not verify whether a specific indicator uses future data. The library's [AGPL-3.0 license](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/LICENSE.md#L1-L4) matters before any code reuse.

## Questions to take into your own design

- Are all trials, their parameters, and their sample windows preserved?
- Do candidate configurations share a fixed evaluation interval after warmup?
- Is the final score calculated on a held-out period untouched by optimization?

## Why this score for a trading system

Its optimizer and indicator warmup reveal two direct research traps: selection of the maximum trial and nonidentical evaluation windows across parameter choices.

**Scope of this review:** We read the pinned README and selected strategy, run, and optimizer implementation. We did not run an optimization or audit every order type.
