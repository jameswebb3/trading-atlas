# Saul - Does validation preserve a transformed value or an error reason?

**Decision question:** Does validation preserve a transformed value or an error reason?

| Field | Review |
| --- | --- |
| Upstream | [whatyouhide/saul](https://github.com/whatyouhide/saul) |
| Primary area | Data Quality & Lineage |
| Source commit | [aefe72ac8eb8e83c658e497dc1b850533ddf6153](https://github.com/whatyouhide/saul/commit/aefe72ac8eb8e83c658e497dc1b850533ddf6153) |
| Reviewed | 2026-10-11 |
| Declared license | Root license text inspected; identifier not resolved |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its validator protocol normalizes successful transformations and typed mismatch results. The project is generic and archived; no feed sequence or publication-time rule is present in the inspected module. |

## What this project does

An Elixir validation and conformation library.

## Mechanism inspected

Its validator protocol normalizes successful transformations and typed mismatch results.

## Limitation that matters

The project is generic and archived; no feed sequence or publication-time rule is present in the inspected module.

## Practical check for a trading system

Keep parse, transform and reject reasons distinct in data ingestion.

## Why this score

1/5. The result shape transfers, while the implementation stack and maintenance do not.

## Source trail

[README](https://github.com/whatyouhide/saul/blob/aefe72ac8eb8e83c658e497dc1b850533ddf6153/README.md#L1); [lib/saul.ex](https://github.com/whatyouhide/saul/blob/aefe72ac8eb8e83c658e497dc1b850533ddf6153/lib/saul.ex#L103); [Root license](https://github.com/whatyouhide/saul/blob/aefe72ac8eb8e83c658e497dc1b850533ddf6153/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
