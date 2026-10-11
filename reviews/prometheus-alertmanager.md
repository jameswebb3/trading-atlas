# Alertmanager — Does notification deduplication imply that a risk incident is handled

**Decision question:** Does notification deduplication imply that a risk incident is handled?

| Field | Review |
| --- | --- |
| Upstream | [Alertmanager](https://github.com/prometheus/alertmanager) |
| Primary area | Operations & Observability |
| Source commit | [47ebf60b0a6db138ff6903dcfe9fbe08f5fad008](https://github.com/prometheus/alertmanager/commit/47ebf60b0a6db138ff6903dcfe9fbe08f5fad008) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/prometheus/alertmanager/blob/47ebf60b0a6db138ff6903dcfe9fbe08f5fad008/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful operational reference for reducing repeated alerts without losing state changes. Notification delivery, human acknowledgment and restoration of a trading invariant should remain separate records. |

## Project overview

Alertmanager groups, deduplicates and routes alerts, with silencing and inhibition controls. [Project documentation](https://github.com/prometheus/alertmanager/blob/47ebf60b0a6db138ff6903dcfe9fbe08f5fad008/README.md#L6-L8).

## Mechanism worth inspecting

The dedup stage compares firing and resolved alert sets with the notification log and checks an explicit repeat interval. Missing log state triggers an initial notification when alerts are firing. [Dedup decision](https://github.com/prometheus/alertmanager/blob/47ebf60b0a6db138ff6903dcfe9fbe08f5fad008/notify/dedup_stage.go#L52-L95).

## Important limit

Dedup tracks notification history, not an operator acknowledgment or recovery of the trading state. Repetition also depends on group interval and notification-log retention. [Timing contract](https://github.com/prometheus/alertmanager/blob/47ebf60b0a6db138ff6903dcfe9fbe08f5fad008/docs/configuration.md#L307-L334).

## Questions to take into your own design

- Does notification deduplication imply that a risk incident is handled?
- What durable incident state remains open until the affected trading invariant is restored?

## Why this score for a trading system

3/5: precise transferable alert lifecycle, but it supplies no trading incident closure policy or account reconciliation.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
