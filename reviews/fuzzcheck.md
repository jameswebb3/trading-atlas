# Fuzzcheck: retain small counterexamples by failure identity

**Decision question:** Can a generated failure become a replayable regression case rather than a one-off log?

| Field | Review |
| --- | --- |
| Upstream | [Fuzzcheck](https://github.com/loiclec/fuzzcheck-rs) |
| Primary area | Testing & Verification |
| Source commit | [816f44962aa46dfbbb6dcc35875c3826cf037340](https://github.com/loiclec/fuzzcheck-rs/commit/816f44962aa46dfbbb6dcc35875c3826cf037340) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Searches structured inputs and retains failing cases by error identity and complexity. Useful for parsers and event reducers; failure grouping and input complexity must preserve the economic condition being tested, and low coverage is not proof of safety. |

## Mechanism worth inspecting

The [overview](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/README.md#L8-L19) and [official design guide](https://fuzzcheck.neocities.org/#design-) separate mutator, sensor, and pool. The [minification guide](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/README.md#L147-L169) describes persistent reduced artifacts. The [failure pool](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/fuzzcheck/src/sensors_and_pools/test_failure_pool.rs#L158-L205) groups observations by error ID and accepts lower-complexity cases. Its [corpus delta](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/fuzzcheck/src/sensors_and_pools/test_failure_pool.rs#L207-L236) emits an artifact path containing error identity and complexity. This is a concrete pattern for retaining executable counterexamples.

## Important limit

Complexity is supplied to the pool, and failure identity is supplied by the sensor: neither automatically represents a financial invariant. The [README](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/README.md#L147-L153) distinguishes recoverable failures from cases needing separate minification. The tool also requires [nightly Rust](https://github.com/loiclec/fuzzcheck-rs/blob/816f44962aa46dfbbb6dcc35875c3826cf037340/README.md#L21-L28). No amount of parser coverage establishes order lifecycle correctness without a meaningful oracle and state reset.

## Questions to take into your own design

- Are corpus cases indexed by the violated invariant, schema version, and replay environment?
- Does minimising an event sequence preserve balances, identity links, and the same failure classification?

## Why this score for a trading system

3/5: a transferable way to preserve and reduce failures, with a specific source implementation. Trading semantics, state reset, and regression oracles must be designed separately.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
