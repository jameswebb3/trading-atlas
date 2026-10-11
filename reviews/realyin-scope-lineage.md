# scope-lineage — Preserve ambiguous column provenance

**Decision question:** What should lineage say when more than one input can supply a column?

| Field | Review |
| --- | --- |
| Upstream | [realyin/scope-lineage](https://github.com/realyin/scope-lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [12bdc08d91da73c852e6a4789e48e403f58c7719](https://github.com/realyin/scope-lineage/commit/12bdc08d91da73c852e6a4789e48e403f58c7719) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its resolver retains candidate source scopes for an ambiguous unqualified column instead of choosing one table, and returns UNKNOWN with a diagnostic when no source can be established. This relies on SQL parsing and supplied schema metadata; it does not resolve non-SQL transformations or make absent source metadata trustworthy. |

## What this project does

SQL lineage analyzer that resolves columns through query scopes and records diagnostics. [README](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/README.md).

## Mechanism inspected

Its resolver retains candidate source scopes for an ambiguous unqualified column instead of choosing one table, and returns UNKNOWN with a diagnostic when no source can be established. [Implementation](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/scope_lineage/scope/column_ref_resolver.py#L737-L776).

## Limitation that matters

This relies on SQL parsing and supplied schema metadata; it does not resolve non-SQL transformations or make absent source metadata trustworthy. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

When lineage is uncertain, store candidate parents and an explicit unresolved state; do not report a single proven source in the trial manifest.

## Why this score

Its resolver retains candidate source scopes for an ambiguous unqualified column instead of choosing one table, and returns UNKNOWN with a diagnostic when no source can be established. This relies on SQL parsing and supplied schema metadata; it does not resolve non-SQL transformations or make absent source metadata trustworthy.

## Source trail

[README](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/README.md) · [Implementation](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/scope_lineage/scope/column_ref_resolver.py#L737-L776) · [License](https://github.com/realyin/scope-lineage/blob/12bdc08d91da73c852e6a4789e48e403f58c7719/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
