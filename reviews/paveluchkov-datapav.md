# DataPav - When an upstream node disappears, do downstream fields remain visibly broken?

**Decision question:** When an upstream node disappears, do downstream fields remain visibly broken?

| Field | Review |
| --- | --- |
| Upstream | [PaveLuchkov/datapav](https://github.com/PaveLuchkov/datapav) |
| Primary area | Data Quality & Lineage |
| Source commit | [775908d0de490e9eddc519a12747c306e17c7db5](https://github.com/PaveLuchkov/datapav/commit/775908d0de490e9eddc519a12747c306e17c7db5) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Deletion marks orphaned columns and dependent inputs as broken while preserving unrelated node fields. This is editor state, not a runtime guarantee that downstream jobs refuse those broken inputs. |

## What this project does

A visual data-lineage editor.

## Mechanism inspected

Deletion marks orphaned columns and dependent inputs as broken while preserving unrelated node fields.

## Limitation that matters

This is editor state, not a runtime guarantee that downstream jobs refuse those broken inputs.

## Practical check for a trading system

Propagate broken-lineage state into the execution gate rather than filling missing fields silently.

## Why this score

2/5. The scoped invalidation pattern transfers to data pipelines, with runtime enforcement still needed.

## Source trail

[README](https://github.com/PaveLuchkov/datapav/blob/775908d0de490e9eddc519a12747c306e17c7db5/README.md#L1); [src/hooks/useLineageState.js](https://github.com/PaveLuchkov/datapav/blob/775908d0de490e9eddc519a12747c306e17c7db5/src/hooks/useLineageState.js#L280); [src/hooks/useLineageState.js](https://github.com/PaveLuchkov/datapav/blob/775908d0de490e9eddc519a12747c306e17c7db5/src/hooks/useLineageState.js#L336).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
