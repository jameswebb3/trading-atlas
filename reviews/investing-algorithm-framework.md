# Polling known open orders is only one part of account reconciliation

**Decision question:** Can an order sync discover an order missing from the local database?

| Field | Review |
| --- | --- |
| Upstream | [Investing Algorithm Framework](https://github.com/coding-kitties/investing-algorithm-framework) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ae8829587986122e4dc938e2d6b637aab664940a](https://github.com/coding-kitties/investing-algorithm-framework/commit/ae8829587986122e4dc938e2d6b637aab664940a) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/coding-kitties/investing-algorithm-framework/blob/ae8829587986122e4dc938e2d6b637aab664940a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its pending-order sync selects local OPEN orders, processes them in stable creation order, and queries each external order. A missing external response is logged and skipped. This is useful polling discipline, but the inspected method is not discovery of unknown exchange orders or proof that missing orders are closed. |

## Mechanism worth inspecting

The [README](https://github.com/coding-kitties/investing-algorithm-framework/blob/ae8829587986122e4dc938e2d6b637aab664940a/README.md#L39-L51) describes a shared research/live framework under v9 development; the [sync guide](https://github.com/coding-kitties/investing-algorithm-framework/blob/ae8829587986122e4dc938e2d6b637aab664940a/docusaurus/docs/Advanced%20Concepts/portfolio-sync.md#L5-L9) distinguishes local and broker balances. The [pending-order method](https://github.com/coding-kitties/investing-algorithm-framework/blob/ae8829587986122e4dc938e2d6b637aab664940a/investing_algorithm_framework/services/order_service/order_service.py#L1010-L1062) filters local OPEN state, sorts by creation time and ID, and skips absent external orders.

## Important limit

This observation is scoped to the pending-order method; other framework paths were not audited for discovery. A warning alone does not close ambiguity or demonstrate persistence across restarts. Current v9 behavior is still described as prerelease.

## Questions to take into your own design

- Which account-wide path discovers orders or fills absent locally?
- How long can an externally missing local order remain unresolved?

## Why this score for a trading system

3/5: Stable known-order polling is directly useful, but complete reconciliation requires discovery and explicit unresolved-state handling beyond this method.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
