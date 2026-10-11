# Change future prices and require earlier factor values to stay unchanged

**Decision question:** Can a vectorized factor read the future without making it obvious?

| Field | Review |
| --- | --- |
| Upstream | [Spectre](https://github.com/Heerozh/spectre) |
| Primary area | Signals & Models |
| Source commit | [c0e7fd974227b376a5790cc66d49f65d58929af8](https://github.com/Heerozh/spectre/commit/c0e7fd974227b376a5790cc66d49f65d58929af8) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/Heerozh/spectre/blob/c0e7fd974227b376a5790cc66d49f65d58929af8/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Spectre computes factors over full arrays and includes a lookahead probe that replaces future OHLCV values, reruns the engine, and compares earlier outputs. This is a useful causal regression pattern for vectorized research. One cut and one perturbation do not establish all feature, universe, or publication-time semantics. |

## Project overview

PyTorch-based factor engine with GPU execution for cross-sectional trading research. Includes a future-data perturbation check to investigate lookahead in factor outputs.

[Project documentation](https://github.com/Heerozh/spectre/blob/c0e7fd974227b376a5790cc66d49f65d58929af8/README.md#L5-L9).

## Mechanism worth inspecting

The [README warning](https://github.com/Heerozh/spectre/blob/c0e7fd974227b376a5790cc66d49f65d58929af8/README.md#L238-L246) notes that custom factors receive more than historical inputs. Its [lookahead documentation](https://github.com/Heerozh/spectre/blob/c0e7fd974227b376a5790cc66d49f65d58929af8/README.md#L576-L583) describes future perturbation. The [implementation](https://github.com/Heerozh/spectre/blob/c0e7fd974227b376a5790cc66d49f65d58929af8/spectre/factors/engine.py#L314-L339) changes the second half of loaded OHLCV, clears cached columns, reruns, and asserts equality of first-half factor output.

## Important limit

A factor can pass this probe while depending on an unperturbed external series, future universe membership, revisions, or a leak outside the selected cut. The routine uses random mutations; robust regressions should record seeds and include deterministic sentinels.

## Questions to take into your own design

- Which causal inputs remain unperturbed by the test?
- Can the same regression be reproduced at several decision cutoffs?

## Why this score for a trading system

4/5: The inspected future-perturbation path directly tests a costly trading research failure, with a clear boundary around what it can detect.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
