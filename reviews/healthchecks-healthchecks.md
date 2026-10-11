# Healthchecks — What should a collector's success heartbeat actually certify

**Decision question:** What should a collector's success heartbeat actually certify?

| Field | Review |
| --- | --- |
| Upstream | [Healthchecks](https://github.com/healthchecks/healthchecks) |
| Primary area | Operations & Observability |
| Source commit | [3731fc452b0ddca253e48d8ff7968b12539df125](https://github.com/healthchecks/healthchecks/commit/3731fc452b0ddca253e48d8ff7968b12539df125) |
| Reviewed | 2026-09-26 |
| Declared license | [BSD-3-Clause](https://github.com/healthchecks/healthchecks/blob/3731fc452b0ddca253e48d8ff7968b12539df125/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful scheduled-job monitoring reference with run IDs and explicit grace periods. Collector success should be emitted after durable data and coverage checks, so a heartbeat means more than process completion. |

## Project overview

Healthchecks monitors scheduled jobs through start, success and failure pings, with configurable schedules and grace periods. [Project documentation](https://github.com/healthchecks/healthchecks/blob/3731fc452b0ddca253e48d8ff7968b12539df125/README.md#L6-L20).

## Mechanism worth inspecting

Check status moves a started job to down when its grace interval expires. The ping handler can correlate start and completion using a run ID. [Status gate](https://github.com/healthchecks/healthchecks/blob/3731fc452b0ddca253e48d8ff7968b12539df125/hc/api/models.py#L355-L380), [run correlation](https://github.com/healthchecks/healthchecks/blob/3731fc452b0ddca253e48d8ff7968b12539df125/hc/api/models.py#L518-L533), [runtime contract](https://github.com/healthchecks/healthchecks/blob/3731fc452b0ddca253e48d8ff7968b12539df125/templates/docs/measuring_script_run_time.md#L63-L79).

## Important limit

A success ping certifies only the sender's declared success. It does not inspect row counts, data coverage or durable publication; missing run IDs also weaken correlation when jobs overlap.

## Questions to take into your own design

- What should a collector's success heartbeat actually certify?
- Which data-coverage and durable-write checks must pass before a collector emits success?

## Why this score for a trading system

3/5: concrete transferable cadence and run-correlation contract, requiring application-specific output evidence before a trading-data job is declared healthy.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
