# Keep valid-message coverage separate from random-input coverage

**Decision question:** Can a fuzzer spend all its effort on malformed exchange messages?

| Field | Review |
| --- | --- |
| Upstream | [JQF](https://github.com/rohanpadhye/JQF) |
| Primary area | Testing & Verification |
| Source commit | [01803ecfd57d78363ae02bcd9a56448b91b154c0](https://github.com/rohanpadhye/JQF/commit/01803ecfd57d78363ae02bcd9a56448b91b154c0) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/rohanpadhye/JQF/blob/01803ecfd57d78363ae02bcd9a56448b91b154c0/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | JQF's Zest guidance tracks coverage for all generated inputs separately from inputs that satisfy validity assumptions. That distinction can sharpen fuzz tests for order and market-data parsers: malformed bytes matter, but valid exchange events must also drive new state paths. Its harness is Java-focused. |

## Mechanism worth inspecting

The [README](https://github.com/rohanpadhye/JQF/blob/01803ecfd57d78363ae02bcd9a56448b91b154c0/README.md#L12-L19) introduces semantic fuzzing. [Zest guidance](https://github.com/rohanpadhye/JQF/blob/01803ecfd57d78363ae02bcd9a56448b91b154c0/jqf-core/src/main/java/edu/berkeley/cs/jqf/fuzz/ei/ZestGuidance.java#L77-L86) maintains coverage for all inputs and valid inputs, and the [save path](https://github.com/rohanpadhye/JQF/blob/01803ecfd57d78363ae02bcd9a56448b91b154c0/jqf-core/src/main/java/edu/berkeley/cs/jqf/fuzz/ei/ZestGuidance.java#L863-L900) retains inputs that improve valid coverage.

## Important limit

Coverage is a search signal, not an oracle. The trading system still needs explicit assertions for duplicate fills, out-of-order ACKs, partial executions, and restart behavior.

## Questions to take into your own design

- Which generated messages count as valid according to the exchange schema?
- Which state invariants are asserted after each message sequence?

## Why this score for a trading system

2/5: Separate coverage for valid inputs is a concrete testing pattern for protocol and state-machine code. JQF is a Java fuzzing framework and supplies no trading-specific validity rules or recovery invariants.

**Scope of this review:** We read the README and Zest guidance source.
