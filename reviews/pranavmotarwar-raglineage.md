# RAGLineage - Does a freshness check actually enforce its age limit?

**Decision question:** Does a freshness check actually enforce its age limit?

| Field | Review |
| --- | --- |
| Upstream | [PranavMotarwar/raglineage](https://github.com/PranavMotarwar/raglineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [1f26fc6619635ee8f26fd4c64eba11198880cabe](https://github.com/PranavMotarwar/raglineage/commit/1f26fc6619635ee8f26fd4c64eba11198880cabe) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The check compares answer dataset versions against the current version and can warn or fail on numeric version gaps. The max_age_days parameter is documented but unused in this function; an old same-version answer passes. |

## What this project does

A RAG answer-lineage auditing library.

## Mechanism inspected

The check compares answer dataset versions against the current version and can warn or fail on numeric version gaps.

## Limitation that matters

The max_age_days parameter is documented but unused in this function; an old same-version answer passes.

## Practical check for a trading system

Test freshness against a real timestamp and fail required checks that ignore configured limits.

## Why this score

2/5. The mismatch between declared age gate and implementation is a useful contract audit.

## Source trail

[README](https://github.com/PranavMotarwar/raglineage/blob/1f26fc6619635ee8f26fd4c64eba11198880cabe/README.md#L1); [raglineage/audit/checks.py](https://github.com/PranavMotarwar/raglineage/blob/1f26fc6619635ee8f26fd4c64eba11198880cabe/raglineage/audit/checks.py#L34); [raglineage/audit/checks.py](https://github.com/PranavMotarwar/raglineage/blob/1f26fc6619635ee8f26fd4c64eba11198880cabe/raglineage/audit/checks.py#L70); [Root license](https://github.com/PranavMotarwar/raglineage/blob/1f26fc6619635ee8f26fd4c64eba11198880cabe/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
