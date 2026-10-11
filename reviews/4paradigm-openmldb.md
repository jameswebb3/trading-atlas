# OpenMLDB — Exclude a timestamp, not just one row

**Decision question:** Do equal-time observations enter an online feature window?

| Field | Review |
| --- | --- |
| Upstream | [OpenMLDB](https://github.com/4paradigm/OpenMLDB) |
| Primary area | Data Quality & Lineage |
| Source commit | [82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7](https://github.com/4paradigm/OpenMLDB/commit/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/4paradigm/OpenMLDB/blob/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The request-window runner changes the end bound to timestamp minus one when exclude_current_time applies. Excluding equal event time is different from excluding only the current row. |

## Project overview

Feature-computation database supporting SQL-based training and online inference workflows. [Documentation](https://github.com/4paradigm/OpenMLDB/blob/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7/README.md).

## Mechanism worth inspecting

The request-window runner changes the end bound to timestamp minus one when exclude_current_time applies. At timestamp zero, it represents the end as empty rather than wrapping the bound. [Source](https://github.com/4paradigm/OpenMLDB/blob/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7/hybridse/src/vm/runner.cc#L2020-L2074).

## Important limit

Excluding equal event time is different from excluding only the current row. Event-time window bounds alone do not establish that all included data was known when the decision was made. [Evidence 1](https://github.com/4paradigm/OpenMLDB/blob/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7/hybridse/src/vm/runner.cc#L2020-L2074). [Evidence 2](https://github.com/4paradigm/OpenMLDB/blob/82dc6d894086f4c3699b6b6dca4a0cf4fb8d1fd7/docs/en/openmldb_sql/dql/WINDOW_CLAUSE.md#L121-L179).

## Questions to take into your own design

- Are equal-time peers included or excluded by the declared feature contract?
- Is local receipt or publication time checked separately from event time?

## Why this score for a trading system

A precise, portable window-boundary implementation; the database's broad batch/online consistency claims were not independently replicated.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
