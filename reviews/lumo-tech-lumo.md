# lumo — A run directory needs an identity

**Decision question:** Can a saved experiment be tied to the specific code snapshot?

| Field | Review |
| --- | --- |
| Upstream | [lumo](https://github.com/lumo-tech/lumo) |
| Primary area | Research & Reproducibility |
| Source commit | [eb80990590fed96fc59efc37754f74d8cf9be70f](https://github.com/lumo-tech/lumo/commit/eb80990590fed96fc59efc37754f74d8cf9be70f) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The Experiment object creates an identity and filesystem layout and provides snapshot/trigger hooks. A unique directory does not by itself prove dataset hash, code state or decision rule; file naming can be mistaken for reproducibility. |

## What this project does

A local experiment management library with run paths, metrics, snapshots and rerun support. [README](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/README.md).

## Mechanism inspected

The Experiment object creates an identity and filesystem layout and provides snapshot/trigger hooks. [Implementation](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/src/lumo/exp/experiment.py#L96-L160).

## Limitation that matters

A unique directory does not by itself prove dataset hash, code state or decision rule; file naming can be mistaken for reproducibility. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Require dataset hash, source commit and evaluation rule in every trial manifest.

## Why this score

Transferable engineering pattern: The Experiment object creates an identity and filesystem layout and provides snapshot/trigger hooks. A unique directory does not by itself prove dataset hash, code state or decision rule; file naming can be mistaken for reproducibility.

## Source trail

[README](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/README.md) · [Documentation](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/docs/source/lumo.rst) · [Implementation](https://github.com/lumo-tech/lumo/blob/eb80990590fed96fc59efc37754f74d8cf9be70f/src/lumo/exp/experiment.py#L96-L160).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
