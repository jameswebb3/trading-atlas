# Giskard: An unevaluated check should say SKIP, not PASS

**Decision question:** Can an agent evaluation go green when no check actually ran?

| Field | Review |
| --- | --- |
| Upstream | [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) |
| Primary area | Agents & Decision Systems |
| Source commit | [1abcde10aea89da2c7213dc7bffc776f1c507525](https://github.com/Giskard-AI/giskard-oss/commit/1abcde10aea89da2c7213dc7bffc776f1c507525) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/Giskard-AI/giskard-oss/blob/1abcde10aea89da2c7213dc7bffc776f1c507525/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Emits an explicit SKIP result for a step with no checks and stops a scenario on check failure or error. A SKIP is still unevaluated evidence; it must not be collapsed into success in a decision gate. |

## Mechanism worth inspecting

The scenario runner says an empty result list would be reported as PASS, so it synthesizes a SKIP result when a step has no checks. It then runs interactions and checks sequentially, stopping on the first failure or error. This is a precise defense against vacuous success.

**Source trail:** [project overview](https://github.com/Giskard-AI/giskard-oss/blob/1abcde10aea89da2c7213dc7bffc776f1c507525/README.md) · [documentation](https://github.com/Giskard-AI/giskard-oss/blob/1abcde10aea89da2c7213dc7bffc776f1c507525/README.md#L61-L85) · [implementation](https://github.com/Giskard-AI/giskard-oss/blob/1abcde10aea89da2c7213dc7bffc776f1c507525/libs/giskard-checks/src/giskard/checks/scenarios/runner.py#L78-L123).

## Important limit

The check framework can only judge configured checks and observed traces. A passing scenario does not certify all agent behavior or the correctness of an LLM judge.

## Questions to take into your own design

- Does zero executed checks produce a distinct non-pass state?
- Does a decision receipt include counts of pass, fail, error, and skip?

## Why this score for a trading system

SKIP instead of vacuous PASS is a sound agent-evaluation invariant, but the inspected path tests no market data, orders, or portfolio decisions.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
