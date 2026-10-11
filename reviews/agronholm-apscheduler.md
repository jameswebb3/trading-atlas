# APScheduler — Should overdue scheduled work run after its decision window has passed

**Decision question:** Should overdue scheduled work run after its decision window has passed?

| Field | Review |
| --- | --- |
| Upstream | [APScheduler](https://github.com/agronholm/apscheduler) |
| Primary area | Operations & Observability |
| Source commit | [81e9fdcaac8d6c72f4318cb7ff393c913c7f9440](https://github.com/agronholm/apscheduler/commit/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/agronholm/apscheduler/blob/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Rejects overdue jobs and checks ownership leases and concurrency separately. Useful for time-sensitive work that should expire rather than execute after a scheduler outage. |

## Project overview

A Python scheduler with tasks, schedules, start deadlines and limits on concurrent jobs; the inspected branch documents its V4 series as a prerelease. [Project documentation](https://github.com/agronholm/apscheduler/blob/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440/README.rst#L11-L16).

## Mechanism worth inspecting

The memory datastore skips leased jobs until the lease expires, discards jobs whose start deadline has passed and respects per-task running-job limits. This makes start validity distinct from the fact that a schedule was due. [Acquisition policy](https://github.com/agronholm/apscheduler/blob/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440/src/apscheduler/datastores/memory.py#L225-L256); [deadline documentation](https://github.com/agronholm/apscheduler/blob/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440/docs/userguide.rst#L275-L284).

## Important limit

A start deadline does not cancel an already-running action or fence a worker that outlived its lease. The inspected datastore is memory-based, and the README warns the V4 prerelease may change incompatibly. [Prerelease notice](https://github.com/agronholm/apscheduler/blob/81e9fdcaac8d6c72f4318cb7ff393c913c7f9440/README.rst#L11-L16).

## Questions to take into your own design

- Can overdue work be marked expired without invoking its action?
- Can a worker whose lease expired still write an authoritative result?

## Why this score for a trading system

3/5: a concrete transferable expiry policy; durable leases, fencing and live-action authority require additional design.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
