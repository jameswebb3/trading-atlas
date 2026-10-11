# hyperliquid-exporter - Can malformed source logs be distinguished from quiet validators?

**Decision question:** Can malformed source logs be distinguished from quiet validators?

| Field | Review |
| --- | --- |
| Upstream | [validaoxyz/hyperliquid-exporter](https://github.com/validaoxyz/hyperliquid-exporter) |
| Primary area | Operations & Observability |
| Source commit | [1fbcd7573f642b6ccba3751e11810d8131ac78f3](https://github.com/validaoxyz/hyperliquid-exporter/commit/1fbcd7573f642b6ccba3751e11810d8131ac78f3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | Its parser checks envelope shape, source timestamp and direction before publishing valid-observation metrics. Consensus-log health does not certify perps order or fill completeness. |

## What this project does

A Hyperliquid node metrics exporter.

## Mechanism inspected

Its parser checks envelope shape, source timestamp and direction before publishing valid-observation metrics.

## Limitation that matters

Consensus-log health does not certify perps order or fill completeness.

## Practical check for a trading system

Expose parser failures and last valid source publication separately from process liveness.

## Why this score

2/5. Good monitoring separation, peripheral to trading decisions.

## Source trail

[README](https://github.com/validaoxyz/hyperliquid-exporter/blob/1fbcd7573f642b6ccba3751e11810d8131ac78f3/README.md#L1); [docs/metrics.md](https://github.com/validaoxyz/hyperliquid-exporter/blob/1fbcd7573f642b6ccba3751e11810d8131ac78f3/docs/metrics.md#L1); [internal/monitors/consensus_monitor.go](https://github.com/validaoxyz/hyperliquid-exporter/blob/1fbcd7573f642b6ccba3751e11810d8131ac78f3/internal/monitors/consensus_monitor.go#L391); [Root license](https://github.com/validaoxyz/hyperliquid-exporter/blob/1fbcd7573f642b6ccba3751e11810d8131ac78f3/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
