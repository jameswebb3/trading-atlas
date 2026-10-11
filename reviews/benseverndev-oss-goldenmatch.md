# goldenmatch — Entity matching needs a bounded candidate path

**Decision question:** Can a new identifier be matched without rescanning every record?

| Field | Review |
| --- | --- |
| Upstream | [goldenmatch](https://github.com/benseverndev-oss/goldenmatch) |
| Primary area | Data Quality & Lineage |
| Source commit | [37a3d7b55f6a708ef9372504bab0330612a9ffdd](https://github.com/benseverndev-oss/goldenmatch/commit/37a3d7b55f6a708ef9372504bab0330612a9ffdd) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | Its single-record path can query ANN candidates or fall back to brute force, refusing the latter above a row-count threshold. Person/company deduplication differs from market symbol identity; probabilistic matches cannot replace exchange asset IDs or effective-date mappings. |

## What this project does

An entity-resolution project that combines candidate retrieval with pair scoring and a golden-record workflow. [README](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/README.md).

## Mechanism inspected

Its single-record path can query ANN candidates or fall back to brute force, refusing the latter above a row-count threshold. [Implementation](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/packages/python/goldenmatch/goldenmatch/core/match_one.py#L19-L143).

## Limitation that matters

Person/company deduplication differs from market symbol identity; probabilistic matches cannot replace exchange asset IDs or effective-date mappings. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not use fuzzy matching for venue symbols; a deterministic ID/effective-date table remains the requirement.

## Why this score

Indirect relevance only: Its single-record path can query ANN candidates or fall back to brute force, refusing the latter above a row-count threshold. Person/company deduplication differs from market symbol identity; probabilistic matches cannot replace exchange asset IDs or effective-date mappings.

## Source trail

[README](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/README.md) · [Documentation](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/docs/oss-llm-usage.md) · [Implementation](https://github.com/benseverndev-oss/goldenmatch/blob/37a3d7b55f6a708ef9372504bab0330612a9ffdd/packages/python/goldenmatch/goldenmatch/core/match_one.py#L19-L143).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
