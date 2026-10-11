# Label Studio — Claim the import before processing it

**Decision question:** How can an asynchronous import avoid duplicate work after a retry?

| Field | Review |
| --- | --- |
| Upstream | [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) |
| Primary area | Research & Reproducibility |
| Source commit | [b03f43c6a634d8a54646c82785533e05a408b428](https://github.com/HumanSignal/label-studio/commit/b03f43c6a634d8a54646c82785533e05a408b428) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The importer claims a created job inside a database transaction before loading tasks; another worker that cannot claim it stops. The claim prevents a common duplicate-start path, but import completion, recovery, and prediction validity are separate states. |

## What this project does

A data-labeling platform with background import and prediction validation. [Project README](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/README.md#L1).

## Mechanism inspected

The importer claims a created job inside a database transaction before loading tasks; another worker that cannot claim it stops. [Implementation](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/label_studio/data_import/functions.py#L37).

## Limitation that matters

The claim prevents a common duplicate-start path, but import completion, recovery, and prediction validity are separate states. The platform is far larger than a trading ingestion worker. This is a source review, not a runtime or security test.

## Practical check for a trading system

Make source-batch claims atomic and store attempt, validation, and publish outcomes independently.

## Why this score

A concrete asynchronous ingestion state machine with transferable retry semantics.

## Source trail

[README](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/README.md#L1); [Implementation](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/label_studio/data_import/functions.py#L37) - [License](https://github.com/HumanSignal/label-studio/blob/b03f43c6a634d8a54646c82785533e05a408b428/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
