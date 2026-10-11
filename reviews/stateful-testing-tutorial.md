# Stateful Systems Testing Tutorial: validate the fake before trusting the consumer test

**Decision question:** Does a passing integration test merely agree with an incorrect mock?

| Field | Review |
| --- | --- |
| Upstream | [Stateful Systems Testing Tutorial](https://github.com/stevana/property-based-testing-stateful-systems-tutorial) |
| Primary area | Testing & Verification |
| Source commit | [65fbef07c33c12bab8a857080eadbcc31b1116cc](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/commit/65fbef07c33c12bab8a857080eadbcc31b1116cc) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/blob/65fbef07c33c12bab8a857080eadbcc31b1116cc/LICENSE) |
| Review depth | 3/3: tutorial documentation, fake implementation, and contract-test source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Explains how to derive a stateful fake from a model and compare it with the real dependency before testing consumers. Strong design guidance, but the inspected queue contract loop reports mismatches without an explicit failing assertion. |

## Mechanism worth inspecting

The [overview](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/blob/65fbef07c33c12bab8a857080eadbcc31b1116cc/README.md#L79-L89) connects state models, concurrency, contracts, and faults. The [contract-testing chapter](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/blob/65fbef07c33c12bab8a857080eadbcc31b1116cc/docs/Part03SMContractTesting.md#L13-L21) first compares a dependency with a model, then reuses that model as a fake. The [service implementation](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/blob/65fbef07c33c12bab8a857080eadbcc31b1116cc/src/Part03/Service.hs#L47-L68) wraps the same queue operations behind real and fake interfaces. The [queue test](https://github.com/stevana/property-based-testing-stateful-systems-tutorial/blob/65fbef07c33c12bab8a857080eadbcc31b1116cc/src/Part03/QueueTest.hs#L110-L127) generates commands and compares real responses with model responses.

## Important limit

In the cited queue loop, a response mismatch triggers monitor(counterexample(...)), then recursion continues to a True result; no assert or explicit failing result appears on that branch. This is a source-level limitation of that example, not a runtime finding or a claim about every test in the tutorial. The model also covers only the declared queue behaviour; an exchange fake needs separately checked acknowledgement, cancellation, fill, and failure semantics.

## Questions to take into your own design

- Has the fake been compared with recorded or sandbox dependency behaviour under the same command sequences?
- Does a deliberately injected contract mismatch fail the gate instead of only enriching its report?

## Why this score for a trading system

3/5: a transferable design pattern for reliable integration tests, supported by the fake and test code. The observed assertion gap rules out treating the example as a ready-made verification gate.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
