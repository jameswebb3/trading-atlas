# Typical - How can runtime types become a reusable validation schema?

**Decision question:** How can runtime types become a reusable validation schema?

| Field | Review |
| --- | --- |
| Upstream | [seandstewart/typical](https://github.com/seandstewart/typical) |
| Primary area | Data Quality & Lineage |
| Source commit | [25873c57a2ae05c825b57fface21d05305480d85](https://github.com/seandstewart/typical/commit/25873c57a2ae05c825b57fface21d05305480d85) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | SchemaBuilder derives JSON Schema definitions from wrapped Python types and caches definitions during construction. The project README marks it archived, and generated schemas still need semantic checks for time, units and market-specific constraints. |

## What this project does

An archived Python typing and schema library.

## Mechanism inspected

SchemaBuilder derives JSON Schema definitions from wrapped Python types and caches definitions during construction.

## Limitation that matters

The project README marks it archived, and generated schemas still need semantic checks for time, units and market-specific constraints.

## Practical check for a trading system

Use generated structural schemas as a first gate, then add temporal and financial invariants.

## Why this score

2/5. The mechanism is concrete but archived and generic.

## Source trail

[README](https://github.com/seandstewart/typical/blob/25873c57a2ae05c825b57fface21d05305480d85/README.md#L1); [typic/ext/schema/schema.py](https://github.com/seandstewart/typical/blob/25873c57a2ae05c825b57fface21d05305480d85/typic/ext/schema/schema.py#L61); [typic/ext/schema/schema.py](https://github.com/seandstewart/typical/blob/25873c57a2ae05c825b57fface21d05305480d85/typic/ext/schema/schema.py#L273); [typic/ext/schema/schema.py](https://github.com/seandstewart/typical/blob/25873c57a2ae05c825b57fface21d05305480d85/typic/ext/schema/schema.py#L400).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
