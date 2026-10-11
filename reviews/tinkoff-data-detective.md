# data-detective — Normalized names can collide in a lineage key

**Decision question:** Can two source identifiers map to the same catalog URN?

| Field | Review |
| --- | --- |
| Upstream | [data-detective](https://github.com/Tinkoff/data-detective) |
| Primary area | Data Quality & Lineage |
| Source commit | [19e64d997908caa9999c9a61bcacb73c42181ea8](https://github.com/Tinkoff/data-detective/commit/19e64d997908caa9999c9a61bcacb73c42181ea8) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/Tinkoff/data-detective/blob/19e64d997908caa9999c9a61bcacb73c42181ea8/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its URN helper lowercases and replaces non-alphanumeric characters with underscores before joining location parts. That normalization is lossy, so punctuation variants may share an identifier; a URN also does not capture data version or receipt. |

## What this project does

A metadata catalog for datasets, pipelines and enterprise assets. [README](https://github.com/Tinkoff/data-detective/blob/19e64d997908caa9999c9a61bcacb73c42181ea8/README.md).

## Mechanism inspected

Its URN helper lowercases and replaces non-alphanumeric characters with underscores before joining location parts. [Implementation](https://github.com/Tinkoff/data-detective/blob/19e64d997908caa9999c9a61bcacb73c42181ea8/data-detective-etl/common/urn.py#L5-L48).

## Limitation that matters

That normalization is lossy, so punctuation variants may share an identifier; a URN also does not capture data version or receipt. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep original upstream ID and a separate collision-checked canonical key in the dataset catalog.

## Why this score

Transferable engineering pattern: Its URN helper lowercases and replaces non-alphanumeric characters with underscores before joining location parts. That normalization is lossy, so punctuation variants may share an identifier; a URN also does not capture data version or receipt.

## Source trail

[README](https://github.com/Tinkoff/data-detective/blob/19e64d997908caa9999c9a61bcacb73c42181ea8/README.md) · [Implementation](https://github.com/Tinkoff/data-detective/blob/19e64d997908caa9999c9a61bcacb73c42181ea8/data-detective-etl/common/urn.py#L5-L48).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
