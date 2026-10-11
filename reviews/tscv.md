# TSCV: a gap does not automatically make validation causal

**Decision question:** Does a time-series gap prevent future data from entering a training fold?

| Field | Review |
| --- | --- |
| Upstream | [WenjieZ/TSCV](https://github.com/WenjieZ/TSCV) |
| Primary area | Testing & Verification |
| Source commit | [3f710476e6192f0961512fec9a321861067959e2](https://github.com/WenjieZ/TSCV/commit/3f710476e6192f0961512fec9a321861067959e2) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Offers fixed-row gaps and a forward-only splitter for time-series validation. GapKFold can still train on rows after the test fold; the default gap is zero and no label horizon is inferred. |

## Project overview

Scikit-learn extension for time-series cross-validation with configurable gaps and rolling-forward windows. Provides explicit control over the separation between training and evaluation samples.

[Project documentation](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/README.md#L9-L38).

## Mechanism worth inspecting

The [README](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/README.md#L9-L36) presents gap-aware splitters. The pinned [GapKFold example](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/tscv/_split.py#L238-L273) shows early test folds trained with later rows, even after nearby rows are excluded. Its [gap implementation](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/tscv/_split.py#L119-L138) removes a fixed number of neighboring row indices. By contrast, [GapRollForward](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/tscv/_split.py#L628-L695) and its [split loop](https://github.com/WenjieZ/TSCV/blob/3f710476e6192f0961512fec9a321861067959e2/tscv/_split.py#L760-L771) keep training before each test window.

## Important limit

A fixed row gap is not calculated from a label's event end, feature publication time, or exchange clock. Both GapKFold and GapRollForward default to zero gap. The repo's last activity was in 2023 at review time; the value here is the explicit contrast between two split policies, not a recommendation to add a dependency.

## Questions to take into your own design

- Can any training row occur after the test decision?
- Is exclusion based on row count or actual label and publication intervals?
- Are fold parameters and the full set of tried variants recorded?

## Why this score for a trading system

The code makes a direct trading-validation trap visible: a gap can remove neighbors while future training rows remain; the forward-only option is useful but still needs event-time rules.

**Scope of this review:** We read the pinned README and split implementations. We did not install or run TSCV or verify every cross-validator.
