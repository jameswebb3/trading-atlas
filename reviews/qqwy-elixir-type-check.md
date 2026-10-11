# TypeCheck — Reject extra keys at a critical boundary

**Decision question:** Can a new unrecognized payload field pass silently?

| Field | Review |
| --- | --- |
| Upstream | [TypeCheck](https://github.com/Qqwy/elixir-type_check) |
| Primary area | Data Quality & Lineage |
| Source commit | [6d0db2c96ed676c146ba11c69218b34f072d8c10](https://github.com/Qqwy/elixir-type_check/commit/6d0db2c96ed676c146ba11c69218b34f072d8c10) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/Qqwy/elixir-type_check/blob/6d0db2c96ed676c146ba11c69218b34f072d8c10/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The fixed-map checker separately detects missing, superfluous and wrong-typed keys. Strictness is useful for a versioned envelope but too brittle for optional upstream fields unless the schema explicitly allows them. |

## What this project does

An Elixir runtime type-checking library with generated checks and readable failure paths. [README](https://github.com/Qqwy/elixir-type_check/blob/6d0db2c96ed676c146ba11c69218b34f072d8c10/README.md).

## Mechanism inspected

The fixed-map checker separately detects missing, superfluous and wrong-typed keys. [Implementation](https://github.com/Qqwy/elixir-type_check/blob/6d0db2c96ed676c146ba11c69218b34f072d8c10/lib/type_check/builtin/fixed_map.ex#L39-L145).

## Limitation that matters

Strictness is useful for a versioned envelope but too brittle for optional upstream fields unless the schema explicitly allows them. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Use strict envelopes for owned trial receipts and explicit versioning for external payload evolution.

## Why this score

Transferable engineering pattern: The fixed-map checker separately detects missing, superfluous and wrong-typed keys. Strictness is useful for a versioned envelope but too brittle for optional upstream fields unless the schema explicitly allows them.

## Source trail

[README](https://github.com/Qqwy/elixir-type_check/blob/6d0db2c96ed676c146ba11c69218b34f072d8c10/README.md) · [Implementation](https://github.com/Qqwy/elixir-type_check/blob/6d0db2c96ed676c146ba11c69218b34f072d8c10/lib/type_check/builtin/fixed_map.ex#L39-L145).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
