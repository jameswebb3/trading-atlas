# Kaji: Is an agent approval still valid after the reviewed code changes?

**Decision question:** Is an agent approval still valid after the reviewed code changes?

| Field | Review |
| --- | --- |
| Upstream | [apokamo/kaji](https://github.com/apokamo/kaji) |
| Primary area | Agents & Decision Systems |
| Source commit | [0cbefb17e444c6183d651ab66b881c357d6fafc4](https://github.com/apokamo/kaji/commit/0cbefb17e444c6183d651ab66b881c357d6fafc4) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The review-poll evidence model stores PR identity, a full reviewed-head SHA, reaction and review signals, and the head observed at three checkpoints. Its validator enforces the invariant set before a downstream close step consumes the evidence; recovery models distinguish cause from synthetic failures. The approval mechanism trusts specific GitHub review and reaction semantics and serves a software PR loop. It does not establish human risk approval, data validity or causal support for a strategy. |

## What this project does

Carries structured PR approval evidence with the reviewed head SHA and checks that it remains the head at decision time. A precise evidence-gating pattern for agent work; it governs code review, not trade authorization.

## Mechanism inspected

The review-poll evidence model stores PR identity, a full reviewed-head SHA, reaction and review signals, and the head observed at three checkpoints. Its validator enforces the invariant set before a downstream close step consumes the evidence; recovery models distinguish cause from synthetic failures.

## Limitation that matters

The approval mechanism trusts specific GitHub review and reaction semantics and serves a software PR loop. It does not establish human risk approval, data validity or causal support for a strategy.

## Practical check for a trading system

For any agent research or release gate, capture artifact digest, reviewer event and decision time. Recheck the digest immediately before action; keep a changed-head result as a new review obligation.

## Why this score

3/5 transferable: a concrete time- and commit-bound approval contract reduces stale agent decisions, but it needs adaptation and an independent trading authorization policy.

## Source trail

[README.md](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/README.md#L16); [docs/ARCHITECTURE.md](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/docs/ARCHITECTURE.md#L1); [kaji_harness/review_poll_evidence.py](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/kaji_harness/review_poll_evidence.py#L187); [kaji_harness/review_poll_evidence.py](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/kaji_harness/review_poll_evidence.py#L205); [kaji_harness/recovery/models.py](https://github.com/apokamo/kaji/blob/0cbefb17e444c6183d651ab66b881c357d6fafc4/kaji_harness/recovery/models.py#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
