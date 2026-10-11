# Qualitis: successful computation can still fail a data check

**Decision question:** Does a successful quality-check job imply its data passed validation?

| Field | Review |
| --- | --- |
| Upstream | [Qualitis](https://github.com/WeBankFinTech/Qualitis) |
| Primary area | Data Quality & Lineage |
| Source commit | [533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c](https://github.com/WeBankFinTech/Qualitis/commit/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/WeBankFinTech/Qualitis/blob/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Separates a remote job's execution status from the outcome of its data-quality rules. A successful job still undergoes checkout and can become a failed validation, a useful status model for scheduled research and data checks. |

## Project overview

An enterprise data-quality platform schedules verification rules and records application and task outcomes. [Project documentation](https://github.com/WeBankFinTech/Qualitis/blob/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c/docs/en_US/ch1/Architecture%20Design.md#L24-L46).

## Mechanism worth inspecting

[Task completion](https://github.com/WeBankFinTech/Qualitis/blob/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c/core/monitor/src/main/java/com/webank/wedatasphere/qualitis/timer/TaskChecker.java#L279-L338) distinguishes remote failure, successful computation, and passed or failed checkout. [Rule evaluation](https://github.com/WeBankFinTech/Qualitis/blob/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c/core/monitor/src/main/java/com/webank/wedatasphere/qualitis/timer/TaskChecker.java#L382-L455) rejects missing results and records individual alarm outcomes.

## Important limit

The [checkout path](https://github.com/WeBankFinTech/Qualitis/blob/533f52cd0cb5d0fa1d8e8d8bff7b9fb26de9297c/core/monitor/src/main/java/com/webank/wedatasphere/qualitis/timer/TaskChecker.java#L394-L422) returns early for specified cross-cluster templates and evaluates configured alarms. This review does not establish the correctness of every template or distributed status transition. Its service stack is much larger than this reusable status distinction.

## Questions to take into your own design

- Do completed jobs separately report execution, validation, and evidence completeness?
- Can an empty or deferred rule set yield an explicitly indeterminate result?

## Why this score for a trading system

3/5: the status separation transfers directly to reliable data checks, but the enterprise architecture and unreviewed template paths limit its use as a complete solution.

**Scope of this review:** README, architecture documentation, task status and rule-checkout source.
