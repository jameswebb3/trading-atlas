# QuickCheck State Machine — Shrinking must preserve command validity

**Decision question:** Can shrinking delete the operation that created a later reference?

| Field | Review |
| --- | --- |
| Upstream | [QuickCheck State Machine](https://github.com/advancedtelematic/quickcheck-state-machine) |
| Primary area | Testing & Verification |
| Source commit | [644e3ac4eca061da43885cb4d6d06184f049abca](https://github.com/advancedtelematic/quickcheck-state-machine/commit/644e3ac4eca061da43885cb4d6d06184f049abca) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/advancedtelematic/quickcheck-state-machine/blob/644e3ac4eca061da43885cb4d6d06184f049abca/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | shrinkAndValidate remaps symbolic references, checks command preconditions against the current model and advances the model while validating a reduced sequence. Correctness depends on the model, generators and preconditions supplied by the test author. |

## Project overview

Haskell model-based testing library for stateful systems using preconditions, transitions and postconditions. [Documentation](https://github.com/advancedtelematic/quickcheck-state-machine/blob/644e3ac4eca061da43885cb4d6d06184f049abca/README.md).

## Mechanism worth inspecting

shrinkAndValidate remaps symbolic references, checks command preconditions against the current model and advances the model while validating a reduced sequence. [Source](https://github.com/advancedtelematic/quickcheck-state-machine/blob/644e3ac4eca061da43885cb4d6d06184f049abca/src/Test/StateMachine/Sequential.hs#L283-L320).

## Important limit

Correctness depends on the model, generators and preconditions supplied by the test author. This sequential path alone is not a proof of concurrent exchange behavior. [Evidence 1](https://github.com/advancedtelematic/quickcheck-state-machine/blob/644e3ac4eca061da43885cb4d6d06184f049abca/src/Test/StateMachine/Sequential.hs#L283-L320).

## Questions to take into your own design

- Does the reducer reject cancel/fill references whose creating order was removed?
- Are model transitions independent of the implementation being tested?

## Why this score for a trading system

A concrete, transferable stateful-test mechanism; the Haskell library itself is not required for Python trading fixtures.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
