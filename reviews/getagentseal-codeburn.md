# Codeburn - Can forked agent sessions cause resource accounting to double-count?

**Decision question:** Can forked agent sessions cause resource accounting to double-count?

| Field | Review |
| --- | --- |
| Upstream | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) |
| Primary area | Operations & Observability |
| Source commit | [26c99ed8603bca8caeacef6cfab9366ec965fc77](https://github.com/getagentseal/codeburn/commit/26c99ed8603bca8caeacef6cfab9366ec965fc77) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The replay code identifies timestamped fork bursts and reads parent token-use records to adjust accounting. The detection depends on timing heuristics and may miss or misclassify unusual fork paths. |

## What this project does

An agent-session analysis tool with fork replay.

## Mechanism inspected

The replay code identifies timestamped fork bursts and reads parent token-use records to adjust accounting.

## Limitation that matters

The detection depends on timing heuristics and may miss or misclassify unusual fork paths.

## Practical check for a trading system

Carry explicit parent-session identifiers in agent research traces and reconcile token costs once.

## Why this score

2/5. The fork-accounting problem is real, but identity fields are stronger than inferred time gaps.

## Source trail

[README](https://github.com/getagentseal/codeburn/blob/26c99ed8603bca8caeacef6cfab9366ec965fc77/README.md#L1); [src/codex-fork-replay.ts](https://github.com/getagentseal/codeburn/blob/26c99ed8603bca8caeacef6cfab9366ec965fc77/src/codex-fork-replay.ts#L16); [src/codex-fork-replay.ts](https://github.com/getagentseal/codeburn/blob/26c99ed8603bca8caeacef6cfab9366ec965fc77/src/codex-fork-replay.ts#L125).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
