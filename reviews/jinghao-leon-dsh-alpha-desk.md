# Alpha Desk — Does the risk filter deny unknown actions

**Decision question:** Does the risk filter deny unknown actions?

| Field | Review |
| --- | --- |
| Upstream | [Alpha Desk](https://github.com/JingHao-Leon/dsh-alpha-desk) |
| Primary area | Agents & Decision Systems |
| Source commit | [1fe6dec5307d4a49168d09c319a1e012d6efd5e8](https://github.com/JingHao-Leon/dsh-alpha-desk/commit/1fe6dec5307d4a49168d09c319a1e012d6efd5e8) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/JingHao-Leon/dsh-alpha-desk/blob/1fe6dec5307d4a49168d09c319a1e012d6efd5e8/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Worth reading as a caution about agent permissions. A trading boundary needs explicit allowed actions and isolated credentials; keyword filtering should not carry that responsibility. |

## Project overview

An agent-oriented trading research desk with a tool-call risk filter. [Project documentation](https://github.com/JingHao-Leon/dsh-alpha-desk/blob/1fe6dec5307d4a49168d09c319a1e012d6efd5e8/README.md).

## Mechanism worth inspecting

The [risk gate](https://github.com/JingHao-Leon/dsh-alpha-desk/blob/1fe6dec5307d4a49168d09c319a1e012d6efd5e8/plugins/risk-gate/index.ts#L18-L59) searches serialized tool inputs for broker, order and credential patterns. If none match, it calls the next tool handler.

## Important limit

A denylist based on text patterns allows unmatched calls. It is not evidence that every money-moving action requires explicit authorization or that credentials are isolated.

## Questions to take into your own design

- Does the risk filter deny unknown actions?
- Must every permitted money-moving tool have a typed action and explicit authorization?

## Why this score for a trading system

2/5: exposes a concrete permission-boundary weakness rather than a reusable safety guarantee.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
