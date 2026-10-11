# datahub-repair-agent - Validate generated SQL before proposing a repair

**Decision question:** Can an agent open a repair with invented table or column names?

| Field | Review |
| --- | --- |
| Upstream | [yadneshSalvi/datahub-repair-agent](https://github.com/yadneshSalvi/datahub-repair-agent) |
| Primary area | Data Quality & Lineage |
| Source commit | [b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02](https://github.com/yadneshSalvi/datahub-repair-agent/commit/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It parses candidate SQL, checks references against live or projected upstream schemas, and blocks the repair pipeline if any generated patch fails validation. Schema YAML and dbt test patches are accepted by this reference check without inspection. A live catalog lookup is not a time-pinned market-data contract. |

## What this project does

datahub-repair-agent proposes fixes for schema drift and checks generated SQL against DataHub metadata. [README](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/README.md).

## Mechanism inspected

It parses candidate SQL, checks references against live or projected upstream schemas, and blocks the repair pipeline if any generated patch fails validation. [Implementation](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/src/repair_agent/validate/validator.py#L30-L117). [Related path](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/src/repair_agent/pipeline.py#L175-L211).

## Limitation that matters

Schema YAML and dbt test patches are accepted by this reference check without inspection. A live catalog lookup is not a time-pinned market-data contract. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Require a static reference check after agent-generated data changes and retain the schema snapshot used for that check.

## Why this score

A concrete post-generation gate, useful as a pattern while its unvalidated patch kinds and timing limits remain explicit.

## Source trail

[README](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/README.md) - [Implementation](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/src/repair_agent/validate/validator.py#L30-L117) - [Related path](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/src/repair_agent/pipeline.py#L175-L211) - [License](https://github.com/yadneshSalvi/datahub-repair-agent/blob/b993020ee0f78a36de58f5c6f3e46bb0c1ee6a02/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
