# highlight - Delay alert windows until ingestion catches up

**Decision question:** Could an alert report missing activity simply because logs have not arrived yet?

| Field | Review |
| --- | --- |
| Upstream | [highlight/highlight](https://github.com/highlight/highlight) |
| Primary area | Operations & Observability |
| Source commit | [79c3ea3a15faad5c05e8f664d53924dca2a2907e](https://github.com/highlight/highlight/commit/79c3ea3a15faad5c05e8f664d53924dca2a2907e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The log-alert worker evaluates a window ending one minute before wall-clock now, rather than the newest possible second, and then compares its count to a threshold. The one-minute delay is fixed. A source slower than that can still look empty, and a zero count says nothing about events the service never received. |

## What this project does

Highlight runs scheduled alerts over ingested logs. [README](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/README.md).

## Mechanism inspected

The log-alert worker evaluates a window ending one minute before wall-clock now, rather than the newest possible second, and then compares its count to a threshold. [Implementation](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/backend/jobs/log-alerts/log-alerts.go#L30-L35). [Related path](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/backend/jobs/log-alerts/log-alerts.go#L104-L125).

## Limitation that matters

The one-minute delay is fixed. A source slower than that can still look empty, and a zero count says nothing about events the service never received. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Use a measured per-source watermark and explicit feed-health state before interpreting a low count as a real zero.

## Why this score

The window offset is a useful warning about ingestion lag, but the hard-coded margin is too weak for a market-data completeness claim.

## Source trail

[README](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/README.md) - [Implementation](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/backend/jobs/log-alerts/log-alerts.go#L30-L35) - [Related path](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/backend/jobs/log-alerts/log-alerts.go#L104-L125) - [License](https://github.com/highlight/highlight/blob/79c3ea3a15faad5c05e8f664d53924dca2a2907e/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
