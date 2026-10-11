# pyruns — Hardware capture is scoped evidence

**Decision question:** Can a run tell assigned GPUs from GPUs merely visible on a host?

| Field | Review |
| --- | --- |
| Upstream | [pyruns](https://github.com/LthreeC/pyruns) |
| Primary area | Research & Reproducibility |
| Source commit | [9c119f64590b1f11d79bb83d8c41dda14dd65a3d](https://github.com/LthreeC/pyruns/commit/9c119f64590b1f11d79bb83d8c41dda14dd65a3d) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | Its environment capture labels GPU scope as assigned, detected or disabled and checks visible-device filters. GPU inventory is only execution context; it cannot certify the dataset, result, or statistical independence of a trading trial. |

## What this project does

A disk-first command-run manager with saved logs, environment and history. [README](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/README.md).

## Mechanism inspected

Its environment capture labels GPU scope as assigned, detected or disabled and checks visible-device filters. [Implementation](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/pyruns/core/run_environment.py#L21-L101).

## Limitation that matters

GPU inventory is only execution context; it cannot certify the dataset, result, or statistical independence of a trading trial. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not expand infrastructure for this; retain environment metadata only when it can change numeric reproducibility.

## Why this score

Indirect relevance only: Its environment capture labels GPU scope as assigned, detected or disabled and checks visible-device filters. GPU inventory is only execution context; it cannot certify the dataset, result, or statistical independence of a trading trial.

## Source trail

[README](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/README.md) · [Documentation](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/docs/ui-guide.md) · [Implementation](https://github.com/LthreeC/pyruns/blob/9c119f64590b1f11d79bb83d8c41dda14dd65a3d/pyruns/core/run_environment.py#L21-L101).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
