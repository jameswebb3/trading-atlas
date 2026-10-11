# llm-engineering-platform — Hash experiment inputs separately from run results

**Decision question:** Can two trials be recognized as the same design despite different execution IDs?

| Field | Review |
| --- | --- |
| Upstream | [200lz/llm-engineering-platform](https://github.com/200lz/llm-engineering-platform) |
| Primary area | Research & Reproducibility |
| Source commit | [2e4da662d950fe41e927e248a3eef3543852a650](https://github.com/200lz/llm-engineering-platform/commit/2e4da662d950fe41e927e248a3eef3543852a650) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It hashes a sorted, finite JSON record of dataset digest, model/config, evaluator, gates, prompt content, source commit and deployment, while excluding execution/result fields; run IDs add time and nonce. A hash only covers fields included in the identity contract; missing data revisions or temporal cutoff would make different trading trials look equivalent. |

## What this project does

LLM experiment pipeline with canonical input identity and a separate run ID. [README](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/README.md).

## Mechanism inspected

It hashes a sorted, finite JSON record of dataset digest, model/config, evaluator, gates, prompt content, source commit and deployment, while excluding execution/result fields; run IDs add time and nonce. [Implementation](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/src/llm_platform/experiments/identity.py#L24-L100).

## Limitation that matters

A hash only covers fields included in the identity contract; missing data revisions or temporal cutoff would make different trading trials look equivalent. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Define a frozen identity for research hypotheses that includes data revision, availability rule, code commit, market universe, costs and predeclared gates; keep each execution ID separate.

## Why this score

It hashes a sorted, finite JSON record of dataset digest, model/config, evaluator, gates, prompt content, source commit and deployment, while excluding execution/result fields; run IDs add time and nonce. A hash only covers fields included in the identity contract; missing data revisions or temporal cutoff would make different trading trials look equivalent.

## Source trail

[README](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/README.md) · [Implementation](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/src/llm_platform/experiments/identity.py#L24-L100) · [License](https://github.com/200lz/llm-engineering-platform/blob/2e4da662d950fe41e927e248a3eef3543852a650/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
