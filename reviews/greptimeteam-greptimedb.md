# greptimedb - Timestamp units are part of the data contract

**Decision question:** Can seconds and milliseconds be silently confused at ingestion?

| Field | Review |
| --- | --- |
| Upstream | [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) |
| Primary area | Market Data & Ingestion |
| Source commit | [6e1a1374111887fa31df1b9573e27d37a2b06329](https://github.com/GreptimeTeam/greptimedb/commit/6e1a1374111887fa31df1b9573e27d37a2b06329) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Resolution accepts specific second/milli/micro/nano spellings and rejects unknown resolution or out-of-range epoch conversion. The parser defaults to milliseconds if no resolution is supplied; a trading ingestion contract should require an explicit unit instead. |

## What this project does

A time-series database pipeline parses numeric epoch fields with a configured time resolution. [README](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/README.md).

## Mechanism inspected

Resolution accepts specific second/milli/micro/nano spellings and rejects unknown resolution or out-of-range epoch conversion. [Implementation](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/src/pipeline/src/etl/processor/epoch.rs#L60-L131).

## Limitation that matters

The parser defaults to milliseconds if no resolution is supplied; a trading ingestion contract should require an explicit unit instead. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Require a declared unit per timestamp column, reject out-of-range conversions and test s/ms confusion using known fixtures.

## Why this score

Resolution accepts specific second/milli/micro/nano spellings and rejects unknown resolution or out-of-range epoch conversion. The parser defaults to milliseconds if no resolution is supplied; a trading ingestion contract should require an explicit unit instead.

## Source trail

[README](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/README.md) - [Implementation](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/src/pipeline/src/etl/processor/epoch.rs#L60-L131) - [License](https://github.com/GreptimeTeam/greptimedb/blob/6e1a1374111887fa31df1b9573e27d37a2b06329/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
