# bio-benchmark - Evaluate answers with and without the option to abstain

**Decision question:** Does an agent know the answer, or does a forced-choice format hide uncertainty?

| Field | Review |
| --- | --- |
| Upstream | [bio-xyz/bio-benchmark](https://github.com/bio-xyz/bio-benchmark) |
| Primary area | Agents & Decision Systems |
| Source commit | [c954769d8367b6f8c914dcde755cc0c19faf8d31](https://github.com/bio-xyz/bio-benchmark/commit/c954769d8367b6f8c914dcde755cc0c19faf8d31) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It grades a free answer, then the same answer mapped into randomized multiple-choice options with and without a refusal option; the result row saves both option lists, grades, model names and errors. Both mapping and grading call LLMs, so the three scores are not independent ground truth. The choice order is saved but its RNG state is not exposed for an exact replay. |

## What this project does

bio-benchmark runs question sets against a biology research agent and stores judge outputs per task and repeat. [README](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/README.md).

## Mechanism inspected

It grades a free answer, then the same answer mapped into randomized multiple-choice options with and without a refusal option; the result row saves both option lists, grades, model names and errors. [Implementation](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/src/bio_benchmark/judge.py#L312-L468). [Related path](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/src/bio_benchmark/runner.py#L141-L198).

## Limitation that matters

Both mapping and grading call LLMs, so the three scores are not independent ground truth. The choice order is saved but its RNG state is not exposed for an exact replay. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For research agents, compare free-form, abstention-allowed and forced-choice judgments on the same frozen cases, and report judge failures separately.

## Why this score

It grades a free answer, then the same answer mapped into randomized multiple-choice options with and without a refusal option; the result row saves both option lists, grades, model names and errors. Both mapping and grading call LLMs, so the three scores are not independent ground truth. The choice order is saved but its RNG state is not exposed for an exact replay.

## Source trail

[README](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/README.md) - [Implementation](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/src/bio_benchmark/judge.py#L312-L468) - [Related path](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/src/bio_benchmark/runner.py#L141-L198) - [License](https://github.com/bio-xyz/bio-benchmark/blob/c954769d8367b6f8c914dcde755cc0c19faf8d31/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
