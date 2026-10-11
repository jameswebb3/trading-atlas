# fg-data-profiling — Can an observed average interval conceal a missing-data problem

**Decision question:** Can an observed average interval conceal a missing-data problem?

| Field | Review |
| --- | --- |
| Upstream | [fg-data-profiling](https://github.com/Data-Centric-AI-Community/fg-data-profiling) |
| Primary area | Data Quality & Lineage |
| Source commit | [98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0](https://github.com/Data-Centric-AI-Community/fg-data-profiling/commit/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/Data-Centric-AI-Community/fg-data-profiling/blob/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Profiles time-series gaps and distributions. Use its interval diagnostic alongside an explicit feed schedule; the observed mean cannot establish completeness. |

## Project overview

Generates exploratory dataset profiles, including time-series diagnostics and report comparisons. [Project documentation](https://github.com/Data-Centric-AI-Community/fg-data-profiling/blob/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0/README.md#L31-L33).

## Mechanism worth inspecting

Gap detection takes positive timestamp differences and flags those exceeding a multiple of their observed mean. This is a concrete exploratory diagnostic rather than a feed-calendar contract. [Time-series docs](https://github.com/Data-Centric-AI-Community/fg-data-profiling/blob/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0/docs/features/time_series_datasets.md#L94-L111), [implementation](https://github.com/Data-Centric-AI-Community/fg-data-profiling/blob/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0/src/data_profiling/model/pandas/describe_timeseries_pandas.py#L147-L183).

## Important limit

The threshold adapts to the observed sample. Widespread gaps can move that baseline; expected trading cadence, session boundaries and publication delays must be supplied separately. [Threshold](https://github.com/Data-Centric-AI-Community/fg-data-profiling/blob/98b1abaf5b629d31fcfe6b0cb85c4ca9782e21a0/src/data_profiling/model/pandas/describe_timeseries_pandas.py#L150-L157).

## Questions to take into your own design

- Can an observed average interval conceal a missing-data problem?
- Is the feed's expected cadence defined independently of the sample being audited?

## Why this score for a trading system

3/5: useful transferable profiling logic, but missing-data guarantees require market-specific cadence and coverage rules.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
