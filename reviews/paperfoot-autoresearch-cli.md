# autoresearch-cli — A best-run command needs an explicit metric direction

**Decision question:** How does an autonomous experiment runner choose its winner?

| Field | Review |
| --- | --- |
| Upstream | [paperfoot/autoresearch-cli](https://github.com/paperfoot/autoresearch-cli) |
| Primary area | Research & Reproducibility |
| Source commit | [921c735ae22fdbbb0ec383263a1c8e14d9a598de](https://github.com/paperfoot/autoresearch-cli/commit/921c735ae22fdbbb0ec383263a1c8e14d9a598de) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | best filters to kept or baseline runs with a metric and compares them using a direction read from config; absent direction defaults to lower-is-better. A missing direction can rank a return metric backwards; best-of-many selection is not out-of-sample evidence. |

## What this project does

Rust CLI for agent-driven experiments with a configured metric, retained runs and diffs. [README](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/README.md).

## Mechanism inspected

best filters to kept or baseline runs with a metric and compares them using a direction read from config; absent direction defaults to lower-is-better. [Implementation](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/src/cmd/best.rs#L5-L39).

## Limitation that matters

A missing direction can rank a return metric backwards; best-of-many selection is not out-of-sample evidence. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require metric name, direction, units, preregistered split and number of attempted runs in every best-run summary.

## Why this score

best filters to kept or baseline runs with a metric and compares them using a direction read from config; absent direction defaults to lower-is-better. A missing direction can rank a return metric backwards; best-of-many selection is not out-of-sample evidence.

## Source trail

[README](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/README.md) · [Implementation](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/src/cmd/best.rs#L5-L39) · [License](https://github.com/paperfoot/autoresearch-cli/blob/921c735ae22fdbbb0ec383263a1c8e14d9a598de/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
