# groundwork — Estimate whether a proposed experiment can resolve its own question

**Decision question:** Would even an oracle beat the strongest simple baseline by a detectable amount?

| Field | Review |
| --- | --- |
| Upstream | [GuoCheng24/groundwork](https://github.com/GuoCheng24/groundwork) |
| Primary area | Research & Reproducibility |
| Source commit | [15424a677b7b5b5e907a3701f7fccf7f7a538e93](https://github.com/GuoCheng24/groundwork/commit/15424a677b7b5b5e907a3701f7fccf7f7a538e93) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Given a tuned baseline, oracle, standard error and optional random/positive controls, the gate stops work if there is no headroom, detectable effect, or functioning positive control. Its normal-approximation power arithmetic and oracle definition are simplistic for serially dependent PnL and adaptive selection. They cannot replace the house gauntlet, DSR or block-resampled uncertainty. |

## What this project does

Pre-study feasibility gate for autonomous scientific projects. [README](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/README.md).

## Mechanism inspected

Given a tuned baseline, oracle, standard error and optional random/positive controls, the gate stops work if there is no headroom, detectable effect, or functioning positive control. [Implementation](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/groundwork/gate.py#L40-L115).

## Limitation that matters

Its normal-approximation power arithmetic and oracle definition are simplistic for serially dependent PnL and adaptive selection. They cannot replace the house gauntlet, DSR or block-resampled uncertainty. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Before expensive alpha work, document simple-baseline headroom, a defensible upper bound, detectable effect under the planned split, and a positive control that proves the pipeline can detect anything.

## Why this score

Given a tuned baseline, oracle, standard error and optional random/positive controls, the gate stops work if there is no headroom, detectable effect, or functioning positive control. Its normal-approximation power arithmetic and oracle definition are simplistic for serially dependent PnL and adaptive selection. They cannot replace the house gauntlet, DSR or block-resampled uncertainty.

## Source trail

[README](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/README.md) · [Implementation](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/groundwork/gate.py#L40-L115) · [License](https://github.com/GuoCheng24/groundwork/blob/15424a677b7b5b5e907a3701f7fccf7f7a538e93/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
