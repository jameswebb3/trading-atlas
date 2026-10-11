# tuva-core - Structural quality must notice missing objects

**Decision question:** Will a data-quality run pass if an expected table was never built?

| Field | Review |
| --- | --- |
| Upstream | [tuva-health/tuva-core](https://github.com/tuva-health/tuva-core) |
| Primary area | Data Quality & Lineage |
| Source commit | [dc3d8563996491940fbb5557f26d5fdeb8a681fb](https://github.com/tuva-health/tuva-core/commit/dc3d8563996491940fbb5557f26d5fdeb8a681fb) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | dq_required_actual_relation fails when an expected physical relation is absent; dq_actual_column also rejects two columns that normalize to the same name. The exact model list is a healthcare contract; it says nothing about event time, coverage, or market data values. |

## What this project does

A healthcare dbt package validates the expected input-layer structure of its warehouse models. [README](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/README.md).

## Mechanism inspected

dq_required_actual_relation fails when an expected physical relation is absent; dq_actual_column also rejects two columns that normalize to the same name. [Implementation](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/macros/data_quality/dq_summary_helpers.sql#L112-L151).

## Limitation that matters

The exact model list is a healthcare contract; it says nothing about event time, coverage, or market data values. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Before value checks, assert that each required source partition/table and its unique columns physically exist.

## Why this score

dq_required_actual_relation fails when an expected physical relation is absent; dq_actual_column also rejects two columns that normalize to the same name. The exact model list is a healthcare contract; it says nothing about event time, coverage, or market data values.

## Source trail

[README](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/README.md) - [Implementation](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/macros/data_quality/dq_summary_helpers.sql#L112-L151) - [License](https://github.com/tuva-health/tuva-core/blob/dc3d8563996491940fbb5557f26d5fdeb8a681fb/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
