# coinjoin-analysis - What does a detector score mean when coinjoin labels are incomplete?

**Decision question:** What does a detector score mean when coinjoin labels are incomplete?

| Field | Review |
| --- | --- |
| Upstream | [crocs-muni/coinjoin-analysis](https://github.com/crocs-muni/coinjoin-analysis) |
| Primary area | Market Data Ingestion |
| Source commit | [b788741cdd7e508d73fba198b09082985e0f3ed8](https://github.com/crocs-muni/coinjoin-analysis/commit/b788741cdd7e508d73fba198b09082985e0f3ed8) |
| Reviewed | 2026-10-10 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Perturbs known coordinator labels at several drop rates and compares detections against the remaining labeled sample. Its own assessment code removes baseline apparent false positives because the interval lacks complete ground truth; the resulting rates are conditional sensitivity, not absolute mainnet accuracy. |

## What this project does

A collection of Bitcoin CoinJoin extraction, analysis and emulation scripts covering multiple wallet protocols. The inspected assessment probes coordinator discovery when known labels are deliberately removed.

## Mechanism inspected

The assessment repeats random, front and tail drops of known attributions, runs the detector again, and counts predicted versus known coordinator transactions. For the zero-drop baseline it stores apparent false positives and false negatives, then excludes those baseline sets from later comparisons because the complete label map is unavailable.

## Limitation that matters

The baseline correction avoids blaming every unknown transaction on the detector, but it also means reported rates measure degradation relative to a partially labeled baseline. They do not estimate absolute false-merge or false-split rates on all mainnet transactions. Wallet emulations can give fuller ownership truth, but their synthetic setting does not establish live prevalence. This is a source review, not an independent replication.

## Practical check for a trading system

For on-chain labels used in a market feature, keep unknown distinct from negative, evaluate perturbations against fixed known labels, and publish coverage and protocol strata alongside error counts before using the feature in a decision.

## Why this score

3/5 because partial-ground-truth sensitivity is a concrete transferable evaluation pattern for on-chain signals, while it does not itself supply an executable trading edge.

## Source trail

[README and label caveat](https://github.com/crocs-muni/coinjoin-analysis/blob/b788741cdd7e508d73fba198b09082985e0f3ed8/README.md#L78); [Attribution-drop experiment](https://github.com/crocs-muni/coinjoin-analysis/blob/b788741cdd7e508d73fba198b09082985e0f3ed8/src/cj_process/cj_assesment.py#L179); [Incomplete-truth baseline](https://github.com/crocs-muni/coinjoin-analysis/blob/b788741cdd7e508d73fba198b09082985e0f3ed8/src/cj_process/cj_assesment.py#L234); [Emulation scenarios](https://github.com/crocs-muni/coinjoin-analysis/blob/b788741cdd7e508d73fba198b09082985e0f3ed8/src/emulation/scenarios.py#L203).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
