# sloth — Alert on fast and slow consumption of a reliability budget

**Decision question:** Does one alert threshold catch both sudden outages and gradual degradation?

| Field | Review |
| --- | --- |
| Upstream | [slok/sloth](https://github.com/slok/sloth) |
| Primary area | Operations & Observability |
| Source commit | [8a3be4fab79defa4448d09d91b48422615980b05](https://github.com/slok/sloth/commit/8a3be4fab79defa4448d09d91b48422615980b05) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The generator derives an error budget from a declared objective and creates quick/slow page and ticket alerts using paired short and long windows. The policy assumes a meaningful total/bad-event denominator. Feed freshness and missing fills need carefully defined events; do not import web-service thresholds without calibration. |

## What this project does

SLO alert generator with multi-window, multi-burn-rate policies. [README](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/README.md).

## Mechanism inspected

The generator derives an error budget from a declared objective and creates quick/slow page and ticket alerts using paired short and long windows. [Implementation](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/internal/alert/alert.go#L28-L77).

## Limitation that matters

The policy assumes a meaningful total/bad-event denominator. Feed freshness and missing fills need carefully defined events; do not import web-service thresholds without calibration. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For a critical data/operation SLI, define the denominator and violation rule first, then consider separate fast and slow burn alerts instead of one static threshold.

## Why this score

The generator derives an error budget from a declared objective and creates quick/slow page and ticket alerts using paired short and long windows. The policy assumes a meaningful total/bad-event denominator. Feed freshness and missing fills need carefully defined events; do not import web-service thresholds without calibration.

## Source trail

[README](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/README.md) · [Implementation](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/internal/alert/alert.go#L28-L77) · [License](https://github.com/slok/sloth/blob/8a3be4fab79defa4448d09d91b48422615980b05/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
