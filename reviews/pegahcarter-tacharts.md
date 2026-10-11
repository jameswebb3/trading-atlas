# TAcharts — A plotted lagging line is future data as a feature

**Decision question:** Does an Ichimoku chart shift a later close onto an earlier index?

| Field | Review |
| --- | --- |
| Upstream | [pegahcarter/TAcharts](https://github.com/pegahcarter/TAcharts) |
| Primary area | Signals & Models |
| Source commit | [68bd58fbea41a0f3201a302c53b4f57eccacee8d](https://github.com/pegahcarter/TAcharts/commit/68bd58fbea41a0f3201a302c53b4f57eccacee8d) |
| Reviewed | 2026-10-09 |
| Declared license | GPL-3.0 ([source](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The Chikou series is assigned close.shift(-displacement), while the Senkou spans shift forward; this is chart alignment, not an observation that existed at the earlier timestamp. Consuming the plotted Chikou column as a model feature at its displayed index would leak a future close. The inspected code is a chart builder; no trading edge is established. |

## What this project does

OHLCV technical-indicator and charting library with an Ichimoku implementation. [README](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/README.md).

## Mechanism inspected

The Chikou series is assigned close.shift(-displacement), while the Senkou spans shift forward; this is chart alignment, not an observation that existed at the earlier timestamp. [Implementation](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/TAcharts/indicators/ichimoku.py#L63-L79).

## Limitation that matters

Consuming the plotted Chikou column as a model feature at its displayed index would leak a future close. The inspected code is a chart builder; no trading edge is established. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Store indicator value time and chart display time separately, and assert that model features are available at the decision timestamp.

## Why this score

The Chikou series is assigned close.shift(-displacement), while the Senkou spans shift forward; this is chart alignment, not an observation that existed at the earlier timestamp. Consuming the plotted Chikou column as a model feature at its displayed index would leak a future close. The inspected code is a chart builder; no trading edge is established.

## Source trail

[README](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/README.md) · [Implementation](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/TAcharts/indicators/ichimoku.py#L63-L79) · [License](https://github.com/pegahcarter/TAcharts/blob/68bd58fbea41a0f3201a302c53b4f57eccacee8d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
