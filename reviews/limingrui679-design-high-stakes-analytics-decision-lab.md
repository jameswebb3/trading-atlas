# high-stakes-analytics-decision-lab — A report should not outgrow its evidence

**Decision question:** Can a decision report quietly promote illustrative or changed input data?

| Field | Review |
| --- | --- |
| Upstream | [limingrui679-design/high-stakes-analytics-decision-lab](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab) |
| Primary area | Research & Reproducibility |
| Source commit | [af98eecf347f0d15182fc68a2349d0dabaec1de4](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/commit/af98eecf347f0d15182fc68a2349d0dabaec1de4) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/LICENSE.txt)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The profiler hashes its source before and after reading and aborts if it changed; the decision validator rejects operational use when the declared evidence type says synthetic, hypothetical or illustrative. The operational gate trusts the case author's evidence-type text; it does not independently establish that a source is real or that its time stamps are causal for trading. |

## What this project does

Evidence-gated analytics workbench that profiles input data, records a case contract and produces a decision brief only after validation. [README](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/README.md).

## Mechanism inspected

The profiler hashes its source before and after reading and aborts if it changed; the decision validator rejects operational use when the declared evidence type says synthetic, hypothetical or illustrative. [Implementation](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/scripts/data_quality.py#L1548-L1565). [Related implementation](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/scripts/decision_engine.py#L308-L346).

## Limitation that matters

The operational gate trusts the case author's evidence-type text; it does not independently establish that a source is real or that its time stamps are causal for trading. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Bind every weight-moving research report to an input content hash and explicit evidence class; reject source changes and illustrative evidence labeled for operational use.

## Why this score

The profiler hashes its source before and after reading and aborts if it changed; the decision validator rejects operational use when the declared evidence type says synthetic, hypothetical or illustrative. The operational gate trusts the case author's evidence-type text; it does not independently establish that a source is real or that its time stamps are causal for trading.

## Source trail

[README](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/README.md) · [Implementation](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/scripts/data_quality.py#L1548-L1565) · [Related implementation](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/scripts/decision_engine.py#L308-L346) · [License](https://github.com/limingrui679-design/high-stakes-analytics-decision-lab/blob/af98eecf347f0d15182fc68a2349d0dabaec1de4/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
