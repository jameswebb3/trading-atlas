# Freezegun — frozen civil time can stall asynchronous deadlines

**Decision question:** Does freezing time also freeze the clock used by the event loop?

| Field | Review |
| --- | --- |
| Upstream | [Freezegun](https://github.com/spulec/freezegun) |
| Primary area | Testing & Verification |
| Source commit | [92d61b3f5c31942a1039713574487bdcfcdbbfff](https://github.com/spulec/freezegun/commit/92d61b3f5c31942a1039713574487bdcfcdbbfff) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/spulec/freezegun/blob/92d61b3f5c31942a1039713574487bdcfcdbbfff/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its real-asyncio mode keeps event-loop deadlines moving while civil time is frozen. Useful for avoiding timer hangs, but a trading test must explicitly account for the distinct clocks involved. |

## Project overview

Freezegun freezes Python time functions and offers manual ticks and a real-asyncio mode. [Project documentation](https://github.com/spulec/freezegun/blob/92d61b3f5c31942a1039713574487bdcfcdbbfff/freezegun/api.py#L587-L600).

## Mechanism worth inspecting

The implementation patches `time.monotonic` along with wall-clock functions. With `real_asyncio=True`, it replaces the event-loop clock with the saved real monotonic function so asyncio timers can continue. [Patched functions](https://github.com/spulec/freezegun/blob/92d61b3f5c31942a1039713574487bdcfcdbbfff/freezegun/api.py#L782-L786); [asyncio accommodation](https://github.com/spulec/freezegun/blob/92d61b3f5c31942a1039713574487bdcfcdbbfff/freezegun/api.py#L834-L851).

## Important limit

A test can now contain frozen civil time, fake direct monotonic calls and a real event-loop clock. That deliberate split prevents hangs but is not a unified simulated exchange clock. Deadline, retry and freshness assertions need to identify which clock drives them.

## Questions to take into your own design

- Does every timeout assertion identify the clock used by the code under test?
- Can a test prove both stale-data behavior and cancel deadlines without waiting in real time?

## Why this score for a trading system

3/5: a concrete asynchronous clock-mismatch reference, useful for designing deterministic tests rather than assuming freeze_time simulates every timer.

**Scope of this review:** Time patching and real-asyncio clock behavior; not exhaustive compatibility testing.
