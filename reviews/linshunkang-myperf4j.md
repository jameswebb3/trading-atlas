# MyPerf4J - Can a latency-calculation failure look like a valid empty metric?

**Decision question:** Can a latency-calculation failure look like a valid empty metric?

| Field | Review |
| --- | --- |
| Upstream | [LinShunKang/MyPerf4J](https://github.com/LinShunKang/MyPerf4J) |
| Primary area | Operations & Observability |
| Source commit | [9846842704821d26ce1f44fd5896b654ae4d326f](https://github.com/LinShunKang/MyPerf4J/commit/9846842704821d26ce1f44fd5896b654ae4d326f) |
| Reviewed | 2026-10-11 |
| Declared license | BSD-3-Clause |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It calculates metrics from sorted records and catches exceptions around the calculation. On exception it returns a default MethodMetrics instance, so consumers need a failure flag to distinguish no data from failed computation. |

## What this project does

A JVM method profiler that computes sorted latency distributions.

## Mechanism inspected

It calculates metrics from sorted records and catches exceptions around the calculation.

## Limitation that matters

On exception it returns a default MethodMetrics instance, so consumers need a failure flag to distinguish no data from failed computation.

## Practical check for a trading system

Mark metric computation failures explicitly before using latency percentiles in an alert.

## Why this score

2/5. The fallback path is a useful observability caution.

## Source trail

[README](https://github.com/LinShunKang/MyPerf4J/blob/9846842704821d26ce1f44fd5896b654ae4d326f/README.md#L1); [MyPerf4J-Core/src/main/java/cn/myperf4j/core/MethodMetricsCalculator.java](https://github.com/LinShunKang/MyPerf4J/blob/9846842704821d26ce1f44fd5896b654ae4d326f/MyPerf4J-Core/src/main/java/cn/myperf4j/core/MethodMetricsCalculator.java#L27); [MyPerf4J-Core/src/main/java/cn/myperf4j/core/MethodMetricsCalculator.java](https://github.com/LinShunKang/MyPerf4J/blob/9846842704821d26ce1f44fd5896b654ae4d326f/MyPerf4J-Core/src/main/java/cn/myperf4j/core/MethodMetricsCalculator.java#L36); [Root license](https://github.com/LinShunKang/MyPerf4J/blob/9846842704821d26ce1f44fd5896b654ae4d326f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
