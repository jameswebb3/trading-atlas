# fast-check: shrink a failing asynchronous command sequence

**Decision question:** Can generated asynchronous actions expose an order-state race and leave a smaller replay?

| Field | Review |
| --- | --- |
| Upstream | [dubzzz/fast-check](https://github.com/dubzzz/fast-check) |
| Primary area | Testing & Verification |
| Source commit | [5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a](https://github.com/dubzzz/fast-check/commit/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/LICENSE) |
| Review depth | 3/3: documentation, implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Runs generated commands against a model and real system, with scheduled asynchronous execution and shrinking of executed commands. The author must supply an independent model, relevant transitions, and trading invariants. |

## Mechanism worth inspecting

The [overview](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/packages/fast-check/README.md#L26-L31) introduces generated properties and counterexample shrinking. The [model-based guide](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/website/docs/advanced/model-based-testing.md#L9-L20) explains commands with preconditions and warns against copying the real system into the model. In source, the [runner](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/packages/fast-check/src/check/model/ModelRunner.ts#L47-L93) checks each command before running it on model and real system; [scheduledModelRun](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/packages/fast-check/src/check/model/ModelRunner.ts#L132-L158) schedules asynchronous commands. The [shrinker](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/packages/fast-check/src/arbitrary/_internals/CommandsArbitrary.ts#L67-L120) filters to executed commands and retains the final failure-causing command. [Test code](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/packages/fast-check/src/check/model/ModelRunner.spec.ts#L11-L35) asserts order and skipping for generated sequences; we did not execute it.

For a trading executor, commands could represent send, ACK, fill, cancel, restart, and late status updates, with invariants over quantities and order identity.

## Important limit

The library cannot infer exchange behavior. The [guide explicitly warns](https://github.com/dubzzz/fast-check/blob/5cf866b5ad5834ea6fef7d9a9a8e30c70e201f4a/website/docs/advanced/model-based-testing.md#L17-L20) that a model too similar to the implementation can share its error. A green property test says only that generated commands satisfied the supplied assertions.

## Questions to take into your own design

- Does the model independently express partial fills and replacement identity?
- Are event orders and scheduling seeds retained for replay?
- Does shrinking preserve the sequence that triggered the failure?

## Why this score for a trading system

Its scheduled model runner and command shrinker can expose order-event races in TypeScript tests, but venue semantics and trading invariants must be supplied by the test author.

**Scope of this review:** We read the pinned overview, guide, implementation, and relevant test. We did not install or run fast-check or audit all generators.
