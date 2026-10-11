# hypothesis-csv — A CSV generator has a zero-row edge case

**Decision question:** Does a generated table include empty-file cases?

| Field | Review |
| --- | --- |
| Upstream | [chobeat/hypothesis-csv](https://github.com/chobeat/hypothesis-csv) |
| Primary area | Testing & Verification |
| Source commit | [8e337fbe454a8555ef90ebea90f2dd928ba152c1](https://github.com/chobeat/hypothesis-csv/commit/8e337fbe454a8555ef90ebea90f2dd928ba152c1) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The csv strategy draws rows and infers a placeholder header width from rows[0] before writing records. With zero rows and no explicit header, indexing rows[0] is a likely failure path; this is a source inference, not an executed repro. |

## What this project does

Hypothesis strategies for typed CSV rows, headers and dialects. [README](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/README.rst).

## Mechanism inspected

The csv strategy draws rows and infers a placeholder header width from rows[0] before writing records. [Implementation](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/src/hypothesis_csv/_csv.py#L82-L108). [Test source](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/tests/test_strategies.py#L18-L22).

## Limitation that matters

With zero rows and no explicit header, indexing rows[0] is a likely failure path; this is a source inference, not an executed repro. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Generate empty and duplicate market-data batches deliberately, then assert parser status and row counts; do not assume a generator spans them.

## Why this score

The csv strategy draws rows and infers a placeholder header width from rows[0] before writing records. With zero rows and no explicit header, indexing rows[0] is a likely failure path; this is a source inference, not an executed repro.

## Source trail

[README](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/README.rst) · [Implementation](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/src/hypothesis_csv/_csv.py#L82-L108) · [Test source](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/tests/test_strategies.py#L18-L22) · [License](https://github.com/chobeat/hypothesis-csv/blob/8e337fbe454a8555ef90ebea90f2dd928ba152c1/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
