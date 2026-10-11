# Apache Flink — Can pipeline backpressure make an active source look idle

**Decision question:** Can pipeline backpressure make an active source look idle?

| Field | Review |
| --- | --- |
| Upstream | [Apache Flink](https://github.com/apache/flink) |
| Primary area | Data Quality & Lineage |
| Source commit | [3aed2634768aec6f72763a9c6bebd7e70d9fc2c9](https://github.com/apache/flink/commit/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/apache/flink/blob/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Uses an activity clock that pauses during backpressure, avoiding an idle-source decision based on time the pipeline could not process available input. Useful for separating collector lag from source silence. |

## Project overview

A stream-processing framework with event-time handling, out-of-order processing, windowing and backpressure. [Project documentation](https://github.com/apache/flink/blob/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9/README.md#L3-L22).

## Mechanism worth inspecting

WatermarksWithIdleness measures elapsed inactivity through a RelativeClock whose contract excludes periods where available input cannot progress. The runtime operator supplies a pausable clock and registers it as a backpressure listener. [Idleness detector](https://github.com/apache/flink/blob/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9/flink-core/src/main/java/org/apache/flink/api/common/eventtime/WatermarksWithIdleness.java#L47-L83), [timer](https://github.com/apache/flink/blob/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9/flink-core/src/main/java/org/apache/flink/api/common/eventtime/WatermarksWithIdleness.java#L123-L141); [runtime clock](https://github.com/apache/flink/blob/3aed2634768aec6f72763a9c6bebd7e70d9fc2c9/flink-runtime/src/main/java/org/apache/flink/streaming/runtime/operators/TimestampsAndWatermarksOperator.java#L85-L109).

## Important limit

Marking a stream idle affects watermark progress; it does not establish that the source is healthy or its data complete. Reappearing data still needs a lateness policy.

## Questions to take into your own design

- Does the source-idle timer exclude time blocked by the consumer?
- Are source silence, processing lag and missing coverage reported separately?

## Why this score for a trading system

3/5: a concrete transferable distinction between source inactivity and internal processing pressure.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
