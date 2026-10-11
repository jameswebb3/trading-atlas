# tslearn — per-series scaling uses the supplied series

**Decision question:** Does normalization use observations after the decision being evaluated?

| Field | Review |
| --- | --- |
| Upstream | [tslearn](https://github.com/tslearn-team/tslearn) |
| Primary area | Signals & Models |
| Source commit | [09654f55d6dab2b3d5a9b5a759ce0965e1312c3b](https://github.com/tslearn-team/tslearn/commit/09654f55d6dab2b3d5a9b5a759ce0965e1312c3b) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/tslearn-team/tslearn/blob/09654f55d6dab2b3d5a9b5a759ce0965e1312c3b/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its scaler clearly separates per-series normalization from fitted moments. For trading features, the supplied series and fitting cutoff determine causality; stateless preprocessing alone does not establish it. |

## Project overview

tslearn supports time-series classification, clustering and preprocessing, including per-series and fitted mean/variance scaling. [Project documentation](https://github.com/tslearn-team/tslearn/blob/09654f55d6dab2b3d5a9b5a759ce0965e1312c3b/README.md#L73-L87).

## Mechanism worth inspecting

The mean/variance scaler is stateless for `per_timeseries=True`: transform computes moments from the series supplied to that call. With it disabled, transform uses stored fitted moments. These are different temporal contracts. [Transform](https://github.com/tslearn-team/tslearn/blob/09654f55d6dab2b3d5a9b5a759ce0965e1312c3b/tslearn/preprocessing/preprocessing.py#L449-L475); [fitting](https://github.com/tslearn-team/tslearn/blob/09654f55d6dab2b3d5a9b5a759ce0965e1312c3b/tslearn/preprocessing/preprocessing.py#L405-L430).

## Important limit

Per-series scaling is valid for a fully available trailing window, but applying it to a full historical path and then reading an early normalized point incorporates later values. Fitted scaling is only causal when its fit population predates the decision.

## Questions to take into your own design

- Is the normalization input exactly the window available at prediction time?
- Can perturbing data after a decision leave its normalized features unchanged?

## Why this score for a trading system

2/5: a useful preprocessing boundary, with modest added trading value beyond a well-specified window and fit-cutoff contract.

**Scope of this review:** Mean/variance scaler temporal semantics; clustering and distance methods were not evaluated.
