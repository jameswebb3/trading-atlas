# DataKitchen Observability Installer - Does a process heartbeat prove that new data arrived?

**Decision question:** Does a process heartbeat prove that new data arrived?

| Field | Review |
| --- | --- |
| Upstream | [DataKitchen/data-observability-installer](https://github.com/DataKitchen/data-observability-installer) |
| Primary area | Data Quality & Lineage |
| Source commit | [7ee0ca701c4c588e364a57699451e10e17ebb888](https://github.com/DataKitchen/data-observability-installer/commit/7ee0ca701c4c588e364a57699451e10e17ebb888) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The demo emits component heartbeats on a 25-second timer. The heartbeat says the demo loop is alive; it does not prove source freshness, row counts or data usability. |

## What this project does

An installer and demo for a hosted data observability product.

## Mechanism inspected

The demo emits component heartbeats on a 25-second timer.

## Limitation that matters

The heartbeat says the demo loop is alive; it does not prove source freshness, row counts or data usability.

## Practical check for a trading system

Pair service liveness with feed coverage and latest-valid-event checks.

## Why this score

1/5. The code is a clear negative control for equating uptime with data quality.

## Source trail

[README](https://github.com/DataKitchen/data-observability-installer/blob/7ee0ca701c4c588e364a57699451e10e17ebb888/README.md#L1); [demo/demo/heartbeat_demo.py](https://github.com/DataKitchen/data-observability-installer/blob/7ee0ca701c4c588e364a57699451e10e17ebb888/demo/demo/heartbeat_demo.py#L28); [Root license](https://github.com/DataKitchen/data-observability-installer/blob/7ee0ca701c4c588e364a57699451e10e17ebb888/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
