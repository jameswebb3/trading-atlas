# pydantic2zod - Generate a second-language schema, then test parity

**Decision question:** Will a Python data contract reject the same records in a TypeScript consumer?

| Field | Review |
| --- | --- |
| Upstream | [argyle-engineering/pydantic2zod](https://github.com/argyle-engineering/pydantic2zod) |
| Primary area | Data Quality & Lineage |
| Source commit | [c828effc73d2aaa2e8f81bce88d13f5cb092a700](https://github.com/argyle-engineering/pydantic2zod/commit/c828effc73d2aaa2e8f81bce88d13f5cb092a700) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The parser orders referenced models by dependency and the generator maps selected numeric field bounds into Zod constraints. The inspected generator handles a defined subset of model and field constructs. A generated schema is not evidence that custom validators or market-time rules remain equivalent. |

## What this project does

pydantic2zod parses Pydantic model declarations and generates Zod code. [README](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/README.md).

## Mechanism inspected

The parser orders referenced models by dependency and the generator maps selected numeric field bounds into Zod constraints. [Implementation](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/pydantic2zod/_parser.py#L51-L63). [Related path](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/pydantic2zod/_codegen.py#L160-L188).

## Limitation that matters

The inspected generator handles a defined subset of model and field constructs. A generated schema is not evidence that custom validators or market-time rules remain equivalent. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Build a shared corpus of accepted and rejected event payloads and run it against both validators before using generated contracts across services.

## Why this score

Cross-language parity is useful where a Python producer meets a TypeScript consumer; the inspected code does not supply a complete trading-event contract.

## Source trail

[README](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/README.md) - [Implementation](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/pydantic2zod/_parser.py#L51-L63) - [Related path](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/pydantic2zod/_codegen.py#L160-L188) - [License](https://github.com/argyle-engineering/pydantic2zod/blob/c828effc73d2aaa2e8f81bce88d13f5cb092a700/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
