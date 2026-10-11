# convo — Controlled names can flag schema drift but not timing errors

**Decision question:** Can naming rules catch undocumented feature columns?

| Field | Review |
| --- | --- |
| Upstream | [emilyriederer/convo](https://github.com/emilyriederer/convo) |
| Primary area | Data Quality & Lineage |
| Source commit | [0b641a7c52987779c6eb5667769b1f8f326e6255](https://github.com/emilyriederer/convo/commit/0b641a7c52987779c6eb5667769b1f8f326e6255) |
| Reviewed | 2026-10-09 |
| Declared license | Unverified root license text ([source](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/LICENSE.md)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | Its evaluator constructs regex checks from vocabulary prefixes and reports invalid columns by level. Prefix regex matching does not establish units, semantics or available_at; the root license file has placeholder fields, so reuse rights are unclear. |

## What this project does

R package for controlled vocabulary and naming validation in tabular data. [README](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/README.md).

## Mechanism inspected

Its evaluator constructs regex checks from vocabulary prefixes and reports invalid columns by level. [Implementation](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/R/evaluate.R#L14-L65).

## Limitation that matters

Prefix regex matching does not establish units, semantics or available_at; the root license file has placeholder fields, so reuse rights are unclear. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Use explicit field IDs and metadata contracts for market features; treat name checks only as a first-pass signal.

## Why this score

Its evaluator constructs regex checks from vocabulary prefixes and reports invalid columns by level. Prefix regex matching does not establish units, semantics or available_at; the root license file has placeholder fields, so reuse rights are unclear.

## Source trail

[README](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/README.md) · [Implementation](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/R/evaluate.R#L14-L65) · [License](https://github.com/emilyriederer/convo/blob/0b641a7c52987779c6eb5667769b1f8f326e6255/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
