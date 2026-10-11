# tierkreis - Restart a failed workflow node by location

**Decision question:** Can a failed experiment step be retried without rerunning every upstream step?

| Field | Review |
| --- | --- |
| Upstream | [Quantinuum/tierkreis](https://github.com/Quantinuum/tierkreis) |
| Primary area | Research & Reproducibility |
| Source commit | [2221c632f05ecd0cbe60d277722f3870efadd1f3](https://github.com/Quantinuum/tierkreis/commit/2221c632f05ecd0cbe60d277722f3870efadd1f3) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The runtime reloads active runs with their graph and inputs, reports errors by node location, and exposes restart_task for selected failed task locations. Its quantum workflow infrastructure is a large adaptation cost; the inspected path does not establish that node restart is safe for non-idempotent trading side effects. |

## What this project does

Tierkreis runs graph-shaped workflows across executors and stores workflow and run state. [README](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/README.md).

## Mechanism inspected

The runtime reloads active runs with their graph and inputs, reports errors by node location, and exposes restart_task for selected failed task locations. [Implementation](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/tierkreis/src/runtime.rs#L478-L503). [Related path](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/tierkreis/src/runtime.rs#L733-L741).

## Limitation that matters

Its quantum workflow infrastructure is a large adaptation cost; the inspected path does not establish that node restart is safe for non-idempotent trading side effects. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For offline research jobs, persist step identity, inputs and outputs so a failed step can be rerun only after validating its upstream artifacts.

## Why this score

The runtime reloads active runs with their graph and inputs, reports errors by node location, and exposes restart_task for selected failed task locations. Its quantum workflow infrastructure is a large adaptation cost; the inspected path does not establish that node restart is safe for non-idempotent trading side effects.

## Source trail

[README](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/README.md) - [Implementation](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/tierkreis/src/runtime.rs#L478-L503) - [Related path](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/tierkreis/src/runtime.rs#L733-L741) - [License](https://github.com/Quantinuum/tierkreis/blob/2221c632f05ecd0cbe60d277722f3870efadd1f3/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
