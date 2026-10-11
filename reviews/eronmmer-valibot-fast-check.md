# valibot-fast-check — Generate contract-shaped arrays, then reject unsupported constraints

**Decision question:** Can a data contract drive adversarial fixture generation?

| Field | Review |
| --- | --- |
| Upstream | [Eronmmer/valibot-fast-check](https://github.com/Eronmmer/valibot-fast-check) |
| Primary area | Testing & Verification |
| Source commit | [8cdc293960a049641c34a0af76595e4108632483](https://github.com/Eronmmer/valibot-fast-check/commit/8cdc293960a049641c34a0af76595e4108632483) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The array builder reads min/max/size validations into generator bounds; for unsupported validation pipes, it filters generated values through the schema. Post-generation filtering may exhaust attempts for tight constraints, and unsupported semantics are not guaranteed to produce boundary cases; TypeScript schema details do not transfer directly. |

## What this project does

Bridge from Valibot schemas to fast-check arbitraries. [README](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/README.md).

## Mechanism inspected

The array builder reads min/max/size validations into generator bounds; for unsupported validation pipes, it filters generated values through the schema. [Implementation](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/src/builder/array.ts#L6-L55).

## Limitation that matters

Post-generation filtering may exhaust attempts for tight constraints, and unsupported semantics are not guaranteed to produce boundary cases; TypeScript schema details do not transfer directly. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Derive fixtures from the existing feed contract, but add explicit malformed, boundary and unequal-array cases where automatic generators undersample them.

## Why this score

The array builder reads min/max/size validations into generator bounds; for unsupported validation pipes, it filters generated values through the schema. Post-generation filtering may exhaust attempts for tight constraints, and unsupported semantics are not guaranteed to produce boundary cases; TypeScript schema details do not transfer directly.

## Source trail

[README](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/README.md) · [Implementation](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/src/builder/array.ts#L6-L55) · [License](https://github.com/Eronmmer/valibot-fast-check/blob/8cdc293960a049641c34a0af76595e4108632483/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
