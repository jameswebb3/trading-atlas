# fastquant: distinguish walk-forward context from scored test rows

**Decision question:** Can a walk-forward helper include training observations inside its test indices?

| Field | Review |
| --- | --- |
| Upstream | [fastquant](https://github.com/enzoampil/fastquant) |
| Primary area | Backtesting & Simulation |
| Source commit | [805c4440bf96ba04cfd43aaf4926e4b45f3c3f33](https://github.com/enzoampil/fastquant/commit/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/enzoampil/fastquant/blob/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides convenient backtests and a small sliding or expanding walk-forward splitter. Its explicit training-overlap option shows why a chronological split still needs a separate definition of which rows are eligible for scoring. |

## Project overview

A Python wrapper makes market-data retrieval, strategy backtesting, and parameter sweeps accessible. [Project documentation](https://github.com/enzoampil/fastquant/blob/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33/README.md#L6-L19).

## Mechanism worth inspecting

The [walk-forward documentation](https://github.com/enzoampil/fastquant/blob/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33/docs/docusaurus/docs/walk_forward_data_split.md#L64-L100) illustrates fixed window sizes. The [implementation](https://github.com/enzoampil/fastquant/blob/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33/python/fastquant/utils/data_split.py#L100-L112) shifts the test start backward by training_overlap_size for both sliding and expanding modes.

## Important limit

The [parameter documentation](https://github.com/enzoampil/fastquant/blob/805c4440bf96ba04cfd43aaf4926e4b45f3c3f33/python/fastquant/utils/data_split.py#L39-L43) itself flags overlap leakage. A context overlap can be useful for indicator warm-up, but those rows should not be scored as unseen tests; the inspected splitter does not distinguish the two or purge overlapping label intervals.

## Questions to take into your own design

- Are context rows explicitly excluded from out-of-sample scoring?
- Does the split purge training labels whose outcome extends into the test period?

## Why this score for a trading system

2/5: a compact inspectable splitter, with overlap and horizon constraints that require additional safeguards for trading research.

**Scope of this review:** README, walk-forward documentation, full splitter source.
