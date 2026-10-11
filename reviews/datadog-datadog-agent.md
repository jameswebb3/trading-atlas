# Datadog Agent — Sample time and collection time are different

**Decision question:** Which timestamp decides the metric bucket?

| Field | Review |
| --- | --- |
| Upstream | [DataDog/datadog-agent](https://github.com/DataDog/datadog-agent) |
| Primary area | Operations & Observability |
| Source commit | [b127655e57ebcfd7c1c2fa567594924fd278d43a](https://github.com/DataDog/datadog-agent/commit/b127655e57ebcfd7c1c2fa567594924fd278d43a) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The sampler uses a supplied metric timestamp when present and otherwise falls back to its processing timestamp before resolving the bucket. A missing source timestamp can therefore shift a delayed market observation into a current bucket. |

## What this project does

A general telemetry agent with a time-bucketed metric aggregator. [Project README](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/README.md#L1).

## Mechanism inspected

The sampler uses a supplied metric timestamp when present and otherwise falls back to its processing timestamp before resolving the bucket. [Implementation](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/pkg/aggregator/time_sampler.go#L94).

## Limitation that matters

A missing source timestamp can therefore shift a delayed market observation into a current bucket. The telemetry agent does not enforce market publication-time semantics. This is a source review, not a runtime or security test.

## Practical check for a trading system

Reject or quarantine market observations without explicit source time before aggregation.

## Why this score

A concrete timestamp fallback illustrates a common market-data timing trap.

## Source trail

[README](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/README.md#L1); [Implementation](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/pkg/aggregator/time_sampler.go#L94) - [License](https://github.com/DataDog/datadog-agent/blob/b127655e57ebcfd7c1c2fa567594924fd278d43a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
