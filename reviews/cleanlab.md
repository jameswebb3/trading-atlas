# A suspected label error is model evidence, not ground truth

**Decision question:** Should a trading label be deleted because a classifier disagrees with it?

| Field | Review |
| --- | --- |
| Upstream | [Cleanlab](https://github.com/cleanlab/cleanlab) |
| Primary area | Data Quality & Lineage |
| Source commit | [750625747de1b26d8530954f51f0530bd0b51d3c](https://github.com/cleanlab/cleanlab/commit/750625747de1b26d8530954f51f0530bd0b51d3c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Cleanlab flags and ranks suspected label issues using model probabilities and several filtering rules. Its documentation encourages out-of-sample probabilities; the function accepts supplied probabilities without demonstrating their time split. Trading labels need causal prediction provenance and review before automatic removal. |

## Mechanism worth inspecting

The [overview](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/README.md#L22-L40) explains model-based dataset diagnosis. The [filter documentation](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/cleanlab/filter.py#L95-L107) recommends out-of-sample probabilities. The [implementation](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/cleanlab/filter.py#L417-L450) combines issue masks, removes selected disagreements, and optionally returns a ranking.

## Important limit

Model disagreement may reflect regime change, weak features, or a poorly trained model rather than a bad label. The inspected function receives predictions; it does not establish chronology, purging of overlapping outcomes, or the validity of a trading target.

## Questions to take into your own design

- Were the probabilities generated without future data or overlapping outcome leakage?
- Will suspected labels be reviewed and retained with provenance instead of silently deleted?

## Why this score for a trading system

2/5: The issue-mask workflow can assist label review, but adapting model-based data cleaning to financial targets requires substantial causal and statistical safeguards.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
