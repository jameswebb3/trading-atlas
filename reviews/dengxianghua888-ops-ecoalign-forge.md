# EcoAlign Forge - Is a shortened input hash enough to identify research evidence?

**Decision question:** Is a shortened input hash enough to identify research evidence?

| Field | Review |
| --- | --- |
| Upstream | [dengxianghua888-ops/ecoalign-forge](https://github.com/dengxianghua888-ops/ecoalign-forge) |
| Primary area | Data Quality & Lineage |
| Source commit | [6397f39233b6073aa79bfecc6a0cb3b6c58d7511](https://github.com/dengxianghua888-ops/ecoalign-forge/commit/6397f39233b6073aa79bfecc6a0cb3b6c58d7511) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its lineage record includes policy version and a SHA-256 hash of guidelines content truncated to 12 hex characters. The short digest is convenient for display but weaker as a durable identity for a research input. |

## What this project does

A data-generation pipeline with lineage metadata.

## Mechanism inspected

Its lineage record includes policy version and a SHA-256 hash of guidelines content truncated to 12 hex characters.

## Limitation that matters

The short digest is convenient for display but weaker as a durable identity for a research input.

## Practical check for a trading system

Persist full input digests and keep short prefixes only for display.

## Why this score

2/5. Explicit policy lineage is useful; evidence identity should not depend on a 48-bit prefix.

## Source trail

[README](https://github.com/dengxianghua888-ops/ecoalign-forge/blob/6397f39233b6073aa79bfecc6a0cb3b6c58d7511/README.md#L1); [src/ecoalign_forge/schemas/lineage.py](https://github.com/dengxianghua888-ops/ecoalign-forge/blob/6397f39233b6073aa79bfecc6a0cb3b6c58d7511/src/ecoalign_forge/schemas/lineage.py#L17); [src/ecoalign_forge/schemas/lineage.py](https://github.com/dengxianghua888-ops/ecoalign-forge/blob/6397f39233b6073aa79bfecc6a0cb3b6c58d7511/src/ecoalign_forge/schemas/lineage.py#L56); [Root license](https://github.com/dengxianghua888-ops/ecoalign-forge/blob/6397f39233b6073aa79bfecc6a0cb3b6c58d7511/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
