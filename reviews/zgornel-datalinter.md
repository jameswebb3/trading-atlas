# DataLinter - Preserve a visible not-available state for data checks

**Decision question:** Can a quality report tell a failed check from one it could not run?

| Field | Review |
| --- | --- |
| Upstream | [zgornel/DataLinter](https://github.com/zgornel/DataLinter) |
| Primary area | Data Quality & Lineage |
| Source commit | [97ad395cfa0b67a2eea0e296b16010159b0d77c6](https://github.com/zgornel/DataLinter/commit/97ad395cfa0b67a2eea0e296b16010159b0d77c6) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/LICENSE.md)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its check types distinguish PassedCheck, FailedCheck and NotAvailableCheck, and the row path accumulates selected results by rule and row. The inspected row path excludes NotAvailableCheck from its output. An aggregate report may therefore omit unevaluated rows unless another path records them. |

## What this project does

DataLinter runs contextual rules over code, columns, rows and datasets. [README](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/README.md).

## Mechanism inspected

Its check types distinguish PassedCheck, FailedCheck and NotAvailableCheck, and the row path accumulates selected results by rule and row. [Implementation](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/src/linter.jl#L52-L64). [Related path](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/src/linter.jl#L287-L305).

## Limitation that matters

The inspected row path excludes NotAvailableCheck from its output. An aggregate report may therefore omit unevaluated rows unless another path records them. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Require passed, failed and unavailable counts to reconcile to the expected checks for each batch; never turn unavailable into success.

## Why this score

The three-state vocabulary is useful, but the row-output omission makes this a cautionary reference rather than a ready quality gate.

## Source trail

[README](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/README.md) - [Implementation](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/src/linter.jl#L52-L64) - [Related path](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/src/linter.jl#L287-L305) - [License](https://github.com/zgornel/DataLinter/blob/97ad395cfa0b67a2eea0e296b16010159b0d77c6/LICENSE.md).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
