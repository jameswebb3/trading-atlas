# Spec - Can a conformer return a structured mismatch instead of a Boolean?

**Decision question:** Can a conformer return a structured mismatch instead of a Boolean?

| Field | Review |
| --- | --- |
| Upstream | [vic/spec](https://github.com/vic/spec) |
| Primary area | Testing & Verification |
| Source commit | [bc767e8e27d9b333fd69710ffdaf3b0ab02ba7f8](https://github.com/vic/spec/commit/bc767e8e27d9b333fd69710ffdaf3b0ab02ba7f8) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The conformer protocol returns either a conformed value or a mismatch with a reason. Shape conformation does not express event-time publication, missing feed coverage or venue identity. |

## What this project does

An Elixir data-specification library.

## Mechanism inspected

The conformer protocol returns either a conformed value or a mismatch with a reason.

## Limitation that matters

Shape conformation does not express event-time publication, missing feed coverage or venue identity.

## Practical check for a trading system

Use typed mismatch receipts as a component of richer market-data contracts.

## Why this score

1/5. The result vocabulary is useful, while the implementation is generic and distant.

## Source trail

[README](https://github.com/vic/spec/blob/bc767e8e27d9b333fd69710ffdaf3b0ab02ba7f8/README.md#L1); [lib/spec/core/conformer.ex](https://github.com/vic/spec/blob/bc767e8e27d9b333fd69710ffdaf3b0ab02ba7f8/lib/spec/core/conformer.ex#L27).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
