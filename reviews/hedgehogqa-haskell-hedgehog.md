# Hedgehog — Can shrinking preserve a valid order-event sequence

**Decision question:** Can shrinking preserve a valid order-event sequence?

| Field | Review |
| --- | --- |
| Upstream | [Hedgehog](https://github.com/hedgehogqa/haskell-hedgehog) |
| Primary area | Testing & Verification |
| Source commit | [75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b](https://github.com/hedgehogqa/haskell-hedgehog/commit/75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b) |
| Reviewed | 2026-09-26 |
| Declared license | [BSD-3-Clause](https://github.com/hedgehogqa/haskell-hedgehog/blob/75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b/hedgehog/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful reference for reducing failing state-machine traces without leaving invalid symbolic dependencies. Trading models must still generate hostile exchange events rather than filter them out as illegal commands. |

## Project overview

Hedgehog supports generated tests, integrated shrinking and abstract state-machine testing in Haskell. [Project documentation](https://github.com/hedgehogqa/haskell-hedgehog/blob/75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b/README.md#L20-L31).

## Mechanism worth inspecting

Command callbacks separate preconditions, model updates and postconditions. dropInvalid walks a candidate sequence, retains commands only when their preconditions and symbolic dependencies remain valid, and advances the model for retained commands. [Callbacks](https://github.com/hedgehogqa/haskell-hedgehog/blob/75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b/hedgehog/src/Hedgehog/Internal/State.hs#L275-L298), [sequence repair](https://github.com/hedgehogqa/haskell-hedgehog/blob/75e06fb4e1dea4c1bd11d88c610f1dcd41005c6b/hedgehog/src/Hedgehog/Internal/State.hs#L529-L550).

## Important limit

The model defines validity. Preconditions that forbid malformed or out-of-order exchange events can remove exactly the cases an execution engine must handle; adversarial event classes need their own generators.

## Questions to take into your own design

- Can shrinking preserve a valid order-event sequence?
- Which hostile exchange events remain valid test inputs even when they violate normal command order?

## Why this score for a trading system

3/5: concrete transferable stateful shrinking, with model fidelity and adversarial coverage left to the test author.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
