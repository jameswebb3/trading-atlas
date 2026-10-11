# HFTENGINE — Can a replay explain why a modeled maker order filled

**Decision question:** Can a replay explain why a modeled maker order filled?

| Field | Review |
| --- | --- |
| Upstream | [HFTENGINE](https://github.com/mirkovicdev/HFTENGINE) |
| Primary area | Backtesting & Simulation |
| Source commit | [8d7e2904d86d40265b05a366d57e296ee0cd5d98](https://github.com/mirkovicdev/HFTENGINE/commit/8d7e2904d86d40265b05a366d57e296ee0cd5d98) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/mirkovicdev/HFTENGINE/blob/8d7e2904d86d40265b05a366d57e296ee0cd5d98/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Makes a replay's queue, latency and order decisions inspectable frame by frame. A useful execution-debugging reference whose modeled queue and latency remain explicit assumptions. |

## Project overview

Replay console showing order books, resting orders, queue estimates, latency and execution events from hftbacktest. [Project documentation](https://github.com/mirkovicdev/HFTENGINE/blob/8d7e2904d86d40265b05a366d57e296ee0cd5d98/README.md#L3-L7).

## Mechanism worth inspecting

A recording wrapper delegates queue updates to the underlying model and mirrors queue-ahead estimates, initial depth, trades and depth changes into a shared map. The recorder observes the model rather than deciding fills itself. [State](https://github.com/mirkovicdev/HFTENGINE/blob/8d7e2904d86d40265b05a366d57e296ee0cd5d98/runner/src/queue.rs#L1-L34), [delegation](https://github.com/mirkovicdev/HFTENGINE/blob/8d7e2904d86d40265b05a366d57e296ee0cd5d98/runner/src/queue.rs#L71-L107).

## Important limit

The displayed queue is a model estimate. The documented session uses no-partial-fill exchange behavior and derived order latency; the console deliberately omits P&L. Session statistics in the README are author-reported, not replicated here. [Observed versus modeled](https://github.com/mirkovicdev/HFTENGINE/blob/8d7e2904d86d40265b05a366d57e296ee0cd5d98/README.md#L53-L64).

## Questions to take into your own design

- Can a replay explain why a modeled maker order filled?
- Can queue diagnostics record the model's assumptions without influencing fill decisions?

## Why this score for a trading system

4/5: directly useful tracing of maker-replay decisions with clear evidence boundaries; it does not validate the underlying fill model.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
