# Rapid: run invariants after generated state transitions

**Decision question:** Can a generated state-machine test check an invariant after every action?

| Field | Review |
| --- | --- |
| Upstream | [flyingmutant/rapid](https://github.com/flyingmutant/rapid) |
| Primary area | Testing & Verification |
| Source commit | [6706a6fd83736ba24aaf55ef2621fdf00c2c27e8](https://github.com/flyingmutant/rapid/commit/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8) |
| Reviewed | 2026-09-25 |
| Declared license | [MPL-2.0](https://github.com/flyingmutant/rapid/blob/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8/LICENSE) |
| Review depth | 3/3: documentation, implementation, and relevant test code read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Generates Go state-machine actions and runs an invariant after each valid transition, retaining minimized failures. It cannot invent exchange states, and the inspected runner stops if it cannot find a valid action. |

## Mechanism worth inspecting

The [README](https://github.com/flyingmutant/rapid/blob/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8/README.md#L3-L16) describes property generation, shrinking, persisted failures, and state-machine testing. The pinned [Repeat runner](https://github.com/flyingmutant/rapid/blob/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8/statemachine.go#L22-L69) selects actions and invokes the invariant before and after each valid action. The [example test](https://github.com/flyingmutant/rapid/blob/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8/example_statemachine_test.go#L47-L75) compares a queue with an independent slice model, including a size invariant.

For an order-state machine, analogous invariants could require filled size never to exceed accepted size and a canceled order never to become open again without a new identity.

## Important limit

The [runner retries up to 100 candidate actions](https://github.com/flyingmutant/rapid/blob/6706a6fd83736ba24aaf55ef2621fdf00c2c27e8/statemachine.go#L122-L139) and then stops if no action is valid. A passing run covers only transitions and assertions the author supplied. The inspected code is a useful Go example, but it adds little to a trading system already using stateful property tests in another language.

## Questions to take into your own design

- Is an independent model checked after every state change?
- Does a generated run exercise the rare transitions that matter?
- Are failed seeds and minimized sequences kept?

## Why this score for a trading system

Per-action invariants transfer to trading order tests, but the mechanism is general Go test infrastructure and overlaps other reviewed state-machine references.

**Scope of this review:** We read pinned README, state-machine code, and example test. We did not install or run Rapid or audit every generator.
