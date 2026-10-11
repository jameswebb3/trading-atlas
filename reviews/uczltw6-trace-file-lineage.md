# trace-file-lineage — Declared lineage is not observed lineage

**Decision question:** Can a pipeline map distinguish planned output from an artifact actually produced?

| Field | Review |
| --- | --- |
| Upstream | [uczltw6/trace-file-lineage](https://github.com/uczltw6/trace-file-lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [0293797ea05b7bf1d373679bd4281cf26d5a7cd1](https://github.com/uczltw6/trace-file-lineage/commit/0293797ea05b7bf1d373679bd4281cf26d5a7cd1) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It emits can_generate for an output named in a declaration, upgrading to was_generated_by only when a captured execution links command, run and output. The captured-run match does not by itself prove content correctness or timestamp availability; inference quality depends on capture completeness. |

## What this project does

File-lineage analyzer that combines pipeline declarations with captured run evidence. [README](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/README.md).

## Mechanism inspected

It emits can_generate for an output named in a declaration, upgrading to was_generated_by only when a captured execution links command, run and output. [Implementation](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/skills/trace-file-lineage/scripts/lineage_core/pipeline.py#L99-L133).

## Limitation that matters

The captured-run match does not by itself prove content correctness or timestamp availability; inference quality depends on capture completeness. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Label map edges as declared, observed or verified, and require observed artifact identity before using a lineage edge as trial provenance.

## Why this score

It emits can_generate for an output named in a declaration, upgrading to was_generated_by only when a captured execution links command, run and output. The captured-run match does not by itself prove content correctness or timestamp availability; inference quality depends on capture completeness.

## Source trail

[README](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/README.md) · [Implementation](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/skills/trace-file-lineage/scripts/lineage_core/pipeline.py#L99-L133) · [License](https://github.com/uczltw6/trace-file-lineage/blob/0293797ea05b7bf1d373679bd4281cf26d5a7cd1/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
