# StreamData — Can a constrained generator run out of meaningful test inputs

**Decision question:** Can a constrained generator run out of meaningful test inputs?

| Field | Review |
| --- | --- |
| Upstream | [StreamData](https://github.com/whatyouhide/stream_data) |
| Primary area | Testing & Verification |
| Source commit | [7e161eb7f3bd5486d22e91e0aa46fe8684fefc42](https://github.com/whatyouhide/stream_data/commit/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/whatyouhide/stream_data/blob/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42/README.md#L102-L116) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful property-testing reference for making narrow generators fail visibly. Trading fixtures still need explicit event-class coverage and stored failing examples, especially for rare execution races. |

## Project overview

StreamData provides Elixir data generators and property-based tests, including composed and filtered generators. [Project documentation](https://github.com/whatyouhide/stream_data/blob/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42/README.md#L67-L100).

## Mechanism worth inspecting

filter delegates to bounded bind_filter generation; too many consecutive rejected candidates raise FilterTooNarrowError rather than yielding an arbitrary substitute. The docs recommend constructing valid values instead of heavy filtering. [Filter](https://github.com/whatyouhide/stream_data/blob/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42/lib/stream_data.ex#L483-L490), [exhaustion](https://github.com/whatyouhide/stream_data/blob/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42/lib/stream_data.ex#L345-L367), [generation advice](https://github.com/whatyouhide/stream_data/blob/7e161eb7f3bd5486d22e91e0aa46fe8684fefc42/lib/stream_data.ex#L133-L158).

## Important limit

Generating accepted values does not show that rare trading-event classes were exercised. The README also distinguishes this API from frameworks with built-in stateful testing and persisted counterexamples.

## Questions to take into your own design

- Can a constrained generator run out of meaningful test inputs?
- What event-class counts demonstrate that filtering did not remove the risky cases?

## Why this score for a trading system

3/5: specific transferable input-generation contract; no trading model or built-in stateful execution protocol is established here.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
