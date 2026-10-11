# Research Flywheel: Can a research claim be revised without losing its supporting evidence?

**Decision question:** Can a research claim be revised without losing its supporting evidence?

| Field | Review |
| --- | --- |
| Upstream | [lidapengpeng/research-flywheel](https://github.com/lidapengpeng/research-flywheel) |
| Primary area | Research & Reproducibility |
| Source commit | [0685757d556d4d6c8a42695ff4ef3e47eb2f77ed](https://github.com/lidapengpeng/research-flywheel/commit/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | SQLite claim_ledger records text, evidence, source path, confidence, status and user verdict. The report projects claim, evidence, status and tags as edges; the architecture describes feedback and claim promotion in a local-first loop. A linked path and confidence label are annotations, not source verification or statistical validation. The graph renderer is Markdown and does not establish temporal validity despite a future-facing note in its output. |

## What this project does

Stores each claim with evidence, confidence, status and user verdict, then renders a local graph of claim-to-evidence links. Useful as a knowledge-work pattern; its existence does not verify that a claim is true.

## Mechanism inspected

SQLite claim_ledger records text, evidence, source path, confidence, status and user verdict. The report projects claim, evidence, status and tags as edges; the architecture describes feedback and claim promotion in a local-first loop.

## Limitation that matters

A linked path and confidence label are annotations, not source verification or statistical validation. The graph renderer is Markdown and does not establish temporal validity despite a future-facing note in its output.

## Practical check for a trading system

For a trading research conclusion, link the precise dataset/run/protocol and the result that supports it, carry explicit superseded or rejected status, and prohibit promotion from a citation alone.

## Why this score

3/5 transferable: an explicit claim-evidence-verdict record is relevant to a long-lived research corpus, but the current house already has ledger and methodology controls and would only borrow the status-link pattern.

## Source trail

[README.md](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/README.md#L3); [docs/architecture.md](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/docs/architecture.md#L41); [docs/architecture.md](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/docs/architecture.md#L66); [rf/memory/sqlite_store.py](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/rf/memory/sqlite_store.py#L78); [rf/memory/index.py](https://github.com/lidapengpeng/research-flywheel/blob/0685757d556d4d6c8a42695ff4ef3e47eb2f77ed/rf/memory/index.py#L117)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
