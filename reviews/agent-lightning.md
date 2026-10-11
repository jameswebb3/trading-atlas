# Agent Lightning: separate agent attempts, completion status, and reward evidence

**Decision question:** Does successful agent execution establish the validity of its reported reward?

| Field | Review |
| --- | --- |
| Upstream | [Agent Lightning](https://github.com/microsoft/agent-lightning) |
| Primary area | Agents & Decision Systems |
| Source commit | [ff9457587fb6ec900e16e93be9ad2d77409afa08](https://github.com/microsoft/agent-lightning/commit/ff9457587fb6ec900e16e93be9ad2d77409afa08) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Captures agent rollouts and model interactions for reinforcement learning. Its schemas separate attempt IDs, terminal execution states, and reward events, offering a useful evidence structure without establishing that an agent's scientific conclusion or reported reward is correct. |

## Project overview

A reinforcement-learning harness separates agent execution, model proxying, and policy training. [Project documentation](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/README.md#L39-L45).

## Mechanism worth inspecting

The [basics documentation](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/docs/05-basics.md#L29-L46) distinguishes rollouts from training examples. [Schemas](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/agentlightning/schemas.py#L13-L26) attach rollout and attempt identities to events, and [state transitions](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/agentlightning/schemas.py#L77-L99) distinguish completion from failure. [Reward data](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/agentlightning/schemas.py#L56-L66) carries source and reason fields.

## Important limit

The [server store](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/agentlightning/server/store.py#L3-L18) is memory-resident. Model-request and reward schemas are [not enforced by the store](https://github.com/microsoft/agent-lightning/blob/ff9457587fb6ec900e16e93be9ad2d77409afa08/agentlightning/schemas.py#L36-L60), so a reward event alone is not verified scientific evidence. Training benchmarks were not independently replicated.

## Questions to take into your own design

- Are attempt identity, execution completion, and independently checked results separate?
- Can a reward be traced to an external evaluator and immutable evidence?

## Why this score for a trading system

2/5: adjacent agent-evidence bookkeeping, with no trading-specific evaluator and limited inspected persistence guarantees.

**Scope of this review:** README, basics documentation, event/reward schemas, store and event routes; training not executed.
