# cherries - Capture the source state before an experiment starts

**Decision question:** Can an experiment be replayed when its checkout had uncommitted code?

| Field | Review |
| --- | --- |
| Upstream | [liblaf/cherries](https://github.com/liblaf/cherries) |
| Primary area | Research & Reproducibility |
| Source commit | [7918bbd93722db56578d10f6c7b76bfc199832ae](https://github.com/liblaf/cherries/commit/7918bbd93722db56578d10f6c7b76bfc199832ae) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | At run start it records each scoped repository’s HEAD, working-tree patch, status, submodule topology and allowed untracked source files, with hashes in a source manifest. It also captures the entrypoint and environment before calling the experiment. The allowlist excludes data and large or unlisted files; replay still requires a recoverable Git base. This source snapshot does not prove that input rows existed at the claimed decision time. |

## What this project does

Cherries is a local experiment tracker that captures run parameters, metrics, artefacts and source evidence. [README](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/README.md).

## Mechanism inspected

At run start it records each scoped repository’s HEAD, working-tree patch, status, submodule topology and allowed untracked source files, with hashes in a source manifest. It also captures the entrypoint and environment before calling the experiment. [Implementation](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/src/liblaf/cherries/_capture.py#L109-L203). [Related path](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/src/liblaf/cherries/core/_run.py#L190-L238).

## Limitation that matters

The allowlist excludes data and large or unlisted files; replay still requires a recoverable Git base. This source snapshot does not prove that input rows existed at the claimed decision time. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For a research run, make a dirty checkout explicit, retain the scoped patch and source hashes, and reject a replay claim when the base commit or required data snapshot is unavailable.

## Why this score

This handles a frequent reproducibility gap more concretely than storing a commit alone, while retaining a clear boundary around data provenance.

## Source trail

[README](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/README.md) - [Implementation](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/src/liblaf/cherries/_capture.py#L109-L203) - [Related path](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/src/liblaf/cherries/core/_run.py#L190-L238) - [License](https://github.com/liblaf/cherries/blob/7918bbd93722db56578d10f6c7b76bfc199832ae/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
