# flowscope — SQL lineage must be scoped to one statement

**Decision question:** Can a column occurrence be attributed to the wrong SQL statement?

| Field | Review |
| --- | --- |
| Upstream | [flowscope](https://github.com/pondpilot/flowscope) |
| Primary area | Data Quality & Lineage |
| Source commit | [dd5cbb6442c63bfc0f2a7193678ac3f129445cb3](https://github.com/pondpilot/flowscope/commit/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and a relevant test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The editor adapter filters occurrence and body spans to the selected statement; tests assert the surviving source names and spans. This tracks declared SQL dependencies, not actual data values or publication time. |

## What this project does

A client-side SQL lineage analyzer with a Rust/WASM core and editor integration. [README](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/README.md).

## Mechanism inspected

The editor adapter filters occurrence and body spans to the selected statement; tests assert the surviving source names and spans. [Implementation](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/vscode/src/statementScopedLineage.ts#L152-L291).

## Limitation that matters

This tracks declared SQL dependencies, not actual data values or publication time. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

If a local SQL lineage receipt is added, include statement identity and source span rather than only a table-level edge.

## Why this score

Transferable engineering pattern: The editor adapter filters occurrence and body spans to the selected statement; tests assert the surviving source names and spans. This tracks declared SQL dependencies, not actual data values or publication time.

## Source trail

[README](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/README.md) · [Documentation](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/docs/linter-architecture.md) · [Implementation](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/vscode/src/statementScopedLineage.ts#L152-L291) · [Relevant test](https://github.com/pondpilot/flowscope/blob/dd5cbb6442c63bfc0f2a7193678ac3f129445cb3/vscode/tests/statementScopedLineage.test.ts).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
