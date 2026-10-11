# Lance — An immutable manifest is a snapshot boundary

**Decision question:** Can concurrent writers publish the same dataset version?

| Field | Review |
| --- | --- |
| Upstream | [Lance](https://github.com/lance-format/lance) |
| Primary area | Data Quality & Lineage |
| Source commit | [2468b0d8709e3e8ec425b6796f9cb48e89e8fccd](https://github.com/lance-format/lance/commit/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The commit path writes a manifest with create-only semantics and maps already-existing or failed preconditions to a conflict result. Its format and storage stack are much larger than a local trading corpus; a manifest version still needs source receipt and temporal coverage. |

## What this project does

A lakehouse file format with versioned manifests and object-store commits. [README](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/README.md).

## Mechanism inspected

The commit path writes a manifest with create-only semantics and maps already-existing or failed preconditions to a conflict result. [Implementation](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/rust/lance-table/src/io/commit.rs#L1624-L1675).

## Limitation that matters

Its format and storage stack are much larger than a local trading corpus; a manifest version still needs source receipt and temporal coverage. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Use content-addressed or exclusive-create manifests for frozen trial inputs; retain the current storage stack.

## Why this score

Transferable engineering pattern: The commit path writes a manifest with create-only semantics and maps already-existing or failed preconditions to a conflict result. Its format and storage stack are much larger than a local trading corpus; a manifest version still needs source receipt and temporal coverage.

## Source trail

[README](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/README.md) · [Documentation](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/docs/src/guide/blob.md) · [Implementation](https://github.com/lance-format/lance/blob/2468b0d8709e3e8ec425b6796f9cb48e89e8fccd/rust/lance-table/src/io/commit.rs#L1624-L1675).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
