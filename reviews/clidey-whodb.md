# WhoDB: When can an agent-generated SQL query run without write approval?

**Decision question:** When can an agent-generated SQL query run without write approval?

| Field | Review |
| --- | --- |
| Upstream | [clidey/whodb](https://github.com/clidey/whodb) |
| Primary area | Data Quality & Lineage |
| Source commit | [011fc99d9af2f3f40255c6d0102cf06be5ddf9d5](https://github.com/clidey/whodb/commit/011fc99d9af2f3f40255c6d0102cf06be5ddf9d5) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/clidey/whodb/blob/011fc99d9af2f3f40255c6d0102cf06be5ddf9d5/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The classifier marks SQL outside a supported read grammar as mutating, including unknown syntax. Its lexer rejects ambiguous comments, escapes, and constructs rather than guessing server behavior. The source itself says the classifier must be combined with connector enforcement and trusted database schema objects. The read grammar cannot prove every engine-specific function is side-effect-free. |

## What this project does

Uses a bounded SQL read grammar: unsupported or ambiguous statements require approval. A useful reference for read-only data agents, with the explicit warning that classification is not a database security boundary.

## Mechanism inspected

The classifier marks SQL outside a supported read grammar as mutating, including unknown syntax. Its lexer rejects ambiguous comments, escapes, and constructs rather than guessing server behavior.

## Limitation that matters

The source itself says the classifier must be combined with connector enforcement and trusted database schema objects. The read grammar cannot prove every engine-specific function is side-effect-free.

## Practical check for a trading system

For any research agent with database access, require a narrow SQL grammar, true database read-only credentials, and explicit approval for uncertain queries. Check dialect edge cases before use.

## Why this score

3/5 transferable: a fail-closed SQL gate is directly useful for data exploration agents, but execution safety still depends on database permissions and connector enforcement.

## Source trail

[docs/read-only-execution.md](https://github.com/clidey/whodb/blob/011fc99d9af2f3f40255c6d0102cf06be5ddf9d5/docs/read-only-execution.md#L1); [core/src/sqlguard/classify.go](https://github.com/clidey/whodb/blob/011fc99d9af2f3f40255c6d0102cf06be5ddf9d5/core/src/sqlguard/classify.go#L117); [core/src/sqlguard/read.go](https://github.com/clidey/whodb/blob/011fc99d9af2f3f40255c6d0102cf06be5ddf9d5/core/src/sqlguard/read.go#L13)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
