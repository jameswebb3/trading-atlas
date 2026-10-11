# OpenAlice: inspect the unknown-exposure branch of an agent guard

**Decision question:** What happens when a pre-trade guard cannot estimate a proposed position's value?

| Field | Review |
| --- | --- |
| Upstream | [OpenAlice](https://github.com/TraderAlice/OpenAlice) |
| Primary area | Agents & Decision Systems |
| Source commit | [0d4faa90c67d6c24685c7b40679bea5a5742a215](https://github.com/TraderAlice/OpenAlice/commit/0d4faa90c67d6c24685c7b40679bea5a5742a215) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/LICENSE) |
| Review depth | 3/3: documentation, guard implementation, and focused guard tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Places deterministic guards between agent operations and broker dispatch, using an account snapshot for the checks. A concrete architecture to study, but the inspected position-size guard allows a quantity order for a new symbol when added exposure cannot be estimated. |

## Project overview

Agent workspace for market research, scheduled follow-ups, and staged trading operations. Combines research history with a broker interface and deterministic pre-trade guards.

[Project documentation](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/README.md#L24-L27).

## Mechanism worth inspecting

The [overview](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/README.md#L24-L27) introduces agent research workspaces. The [trading-domain guide](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/services/uta/src/domain/trading/README.md#L5-L13) describes broker, staged-operation history, and guards. The [pipeline](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/services/uta/src/domain/trading/guards/guard-pipeline.ts#L13-L35) obtains positions and account information, checks guards, and only then dispatches. The [position-size guard](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/services/uta/src/domain/trading/guards/max-position-size.ts#L15-L47) estimates added value from cash quantity or an existing position's market price. The [focused test](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/services/uta/src/domain/trading/guards/guards.spec.ts#L112-L117) confirms the new-symbol unknown-value branch is allowed.

## Important limit

A guard chain is only as restrictive as its unknown-data policy. The cited guard returns null when added value is zero or cannot be estimated, and it compares positions by symbol. The pipeline's account snapshot does not by itself reserve budget across concurrent operations or prove snapshot freshness. These limits matter before treating the architecture as a pre-trade risk guarantee.

## Questions to take into your own design

- Should missing price, contract multiplier, or stale account evidence reject a new exposure instead of passing it to the broker?
- How are outstanding orders and concurrent operations included in the exposure budget?

## Why this score for a trading system

3/5: directly useful for inspecting the boundary between agents and broker operations, with a documented, tested limitation. The unknown-exposure allowance prevents a higher rating as a capital-protection reference.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
