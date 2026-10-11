# Hypothesis: Shrink a failing event sequence to the smallest counterexample

**Decision question:** Which exact sequence breaks an order or timing invariant?

| Field | Review |
| --- | --- |
| Upstream | [HypothesisWorks/hypothesis](https://github.com/HypothesisWorks/hypothesis) |
| Primary area | Testing & Verification |
| Source commit | [6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9](https://github.com/HypothesisWorks/hypothesis/commit/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9) |
| Reviewed | 2026-09-25 |
| Declared license | [MPL-2.0](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Generates state-machine rule sequences and reduces a failing sequence into a reproducible counterexample. It only explores transitions and invariants the test author actually models. |

## Project overview

Property-based testing for Python that generates edge cases and reduces failures to small counterexamples. State-machine tests make it useful for exercising order, inventory, and ledger transitions.

[Project documentation](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/README.md#L13-L24).

## Mechanism worth inspecting

The stateful guide shows rules and invariants over a generated sequence. The state-machine runner constructs tests from those rules, while the project’s conjecture shrinker reduces failures. For trading software, that suggests generating ACK, fill, cancel, restart, and late-data permutations against one reference model.

**Source trail:** [project overview](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/README.md) · [documentation](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/hypothesis/docs/stateful.rst#L1-L55) · [implementation](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/hypothesis/src/hypothesis/stateful.py#L255-L320) · [additional source](https://github.com/HypothesisWorks/hypothesis/blob/6cee8ceb8635f82d1dc1e63fabd40801c3cf08e9/hypothesis/src/hypothesis/internal/conjecture/shrinker.py#L149-L170).

## Important limit

Property-based testing cannot infer the correct venue contract or an omitted event type. Reproducible seeds and minimized sequences should be retained as evidence when a failure is found.

## Questions to take into your own design

- Can a failing order-event sequence be replayed from a saved seed?
- Do the rules include fill-before-ACK and restart states?

## Why this score for a trading system

State-machine generation can expose order-event races if those transitions are modeled; it does not know venue behavior by itself.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
