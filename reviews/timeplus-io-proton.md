# proton - Tell an idle source from a stalled consumer

**Decision question:** When no events arrive, is the source quiet or is ingestion stuck?

| Field | Review |
| --- | --- |
| Upstream | [timeplus-io/proton](https://github.com/timeplus-io/proton) |
| Primary area | Market Data & Ingestion |
| Source commit | [1c47e602465466104a1af86aa0199172e5deaa68](https://github.com/timeplus-io/proton/commit/1c47e602465466104a1af86aa0199172e5deaa68) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its stall detector compares the last processed offset with the observed high watermark, waits longer when caught up, and queries the broker for a fresh watermark before recreating a consumer. Progress resets the stall timers. Kafka provides offsets and a broker watermark; a Hyperliquid stream does not expose the same contract. Recreating a consumer is not proof that skipped events were backfilled. |

## What this project does

Proton implements streaming queries and connectors, including a Kafka source. [README](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/README.md).

## Mechanism inspected

Its stall detector compares the last processed offset with the observed high watermark, waits longer when caught up, and queries the broker for a fresh watermark before recreating a consumer. Progress resets the stall timers. [Implementation](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/src/Storages/ExternalStream/Kafka/KafkaSource.cpp#L71-L155). [Related path](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/src/Storages/FileLog/FileLogSource.cpp#L65-L115).

## Limitation that matters

Kafka provides offsets and a broker watermark; a Hyperliquid stream does not expose the same contract. Recreating a consumer is not proof that skipped events were backfilled. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For an exchange collector, compare local last sequence and receipt heartbeat with an independent source-progress signal, and separate silent market periods from consumer stalls.

## Why this score

The two-sided progress test is a transferable operational idea, bounded by the different semantics of exchange feeds.

## Source trail

[README](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/README.md) - [Implementation](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/src/Storages/ExternalStream/Kafka/KafkaSource.cpp#L71-L155) - [Related path](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/src/Storages/FileLog/FileLogSource.cpp#L65-L115) - [License](https://github.com/timeplus-io/proton/blob/1c47e602465466104a1af86aa0199172e5deaa68/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
