# Gopter: shrink a failing stateful sequence while preserving its model

**Decision question:** Can an order-state failure be reduced to a short, reproducible sequence of valid commands?

| Field | Review |
| --- | --- |
| Upstream | [Gopter](https://github.com/leanovate/gopter) |
| Primary area | Testing & Verification |
| Source commit | [967a5004fb702c153283a99f5a3908ee6570c066](https://github.com/leanovate/gopter/commit/967a5004fb702c153283a99f5a3908ee6570c066) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Generates stateful command sequences, compares responses against a model, and shrinks failures. Useful for order and ledger state machines; the inspected runner is sequential and needs deterministic reset plus a correctly specified model. |

## Mechanism worth inspecting

The [README](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/README.md#L16-L30) lists stateful testing and shrinking, and [package documentation](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/commands/doc.go#L1-L11) describes the required interfaces. The [runner](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/commands/actions.go#L30-L53) checks command preconditions, runs each command, advances model state, and combines postconditions. The [generator](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/commands/actions.go#L74-L105) reuses a generated initial-state seed and filters sequences against model preconditions; the [shrinker](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/commands/actions.go#L61-L71) reduces command lists. The [property runner](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/prop/forall.go#L97-L113) filters shrunk candidates through the generator sieve before accepting another failure.

## Important limit

The [runner structure](https://github.com/leanovate/gopter/blob/967a5004fb702c153283a99f5a3908ee6570c066/commands/actions.go#L30-L36) explicitly defers parallel commands. Reproducibility also requires the real system reset, time, and external effects to be controlled; reproducing only the model seed is insufficient. A model that omits partial fills or treats cancel acceptance as completion can make the wrong implementation pass.

## Questions to take into your own design

- Does a reduced failure preserve the exact initial state, event inputs, and command preconditions?
- Which race conditions need a separate concurrent-history test beyond these sequential sequences?

## Why this score for a trading system

3/5: a useful transferable reference for generated state-machine tests and failure reduction. It supplies no trading model and the inspected command runner does not cover concurrent histories.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
