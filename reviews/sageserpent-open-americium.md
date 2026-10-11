# Americium - Can a property test reproduce the exact generated case without replaying a whole search?

**Decision question:** Can a property test reproduce the exact generated case without replaying a whole search?

| Field | Review |
| --- | --- |
| Upstream | [sageserpent-open/americium](https://github.com/sageserpent-open/americium) |
| Primary area | Testing & Verification |
| Source commit | [e95ea040ab9e3775b8495d71eb282678cb7d6a78](https://github.com/sageserpent-open/americium/commit/e95ea040ab9e3775b8495d71eb282678cb7d6a78) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The runner can reproduce a case from a serialized recipe and bypasses generation and shrink settings for that replay. A recipe identifies generator decisions under the same code; it does not snapshot external market inputs or venue responses. |

## What this project does

A Scala property-testing library with explicit reproduction recipes.

## Mechanism inspected

The runner can reproduce a case from a serialized recipe and bypasses generation and shrink settings for that replay.

## Limitation that matters

A recipe identifies generator decisions under the same code; it does not snapshot external market inputs or venue responses.

## Practical check for a trading system

Pair generated-case recipes with immutable market tapes and code revisions.

## Why this score

2/5. The recipe is stronger than seed alone but not a full research manifest.

## Source trail

[README](https://github.com/sageserpent-open/americium/blob/e95ea040ab9e3775b8495d71eb282678cb7d6a78/README.markdown#L1); [core-library/src/main/scala/com/sageserpent/americium/TrialsImplementation.scala](https://github.com/sageserpent-open/americium/blob/e95ea040ab9e3775b8495d71eb282678cb7d6a78/core-library/src/main/scala/com/sageserpent/americium/TrialsImplementation.scala#L259); [core-library/src/main/scala/com/sageserpent/americium/TrialsImplementation.scala](https://github.com/sageserpent-open/americium/blob/e95ea040ab9e3775b8495d71eb282678cb7d6a78/core-library/src/main/scala/com/sageserpent/americium/TrialsImplementation.scala#L291); [Root license](https://github.com/sageserpent-open/americium/blob/e95ea040ab9e3775b8495d71eb282678cb7d6a78/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
