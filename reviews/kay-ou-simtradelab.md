# SimTradeLab — Does broker API compatibility mean every operation is supported

**Decision question:** Does broker API compatibility mean every operation is supported?

| Field | Review |
| --- | --- |
| Upstream | [SimTradeLab](https://github.com/kay-ou/SimTradeLab) |
| Primary area | Backtesting & Simulation |
| Source commit | [54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6](https://github.com/kay-ou/SimTradeLab/commit/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0 + commercial option](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Documents partial PTrade compatibility and enforces broker-specific availability profiles. Useful for designing explicit support matrices rather than assuming API names imply matching behavior. |

## Project overview

Local simulator for a documented subset of PTrade APIs, including market profiles and lifecycle rules. [Project documentation](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/README.md#L14-L37).

## Mechanism worth inspecting

Broker profiles define unsupported API sets and reject unknown profile names. An explicit profile can deny a method that the permissive auto profile allows. [Profile guard](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/src/simtradelab/ptrade/broker_profile.py#L7-L61), [compatibility boundary](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/docs/STRATEGY_RUNTIME_BOUNDARIES.md#L57-L61).

## Important limit

Auto returns true in this broker-specific availability helper; that is not proof of full API implementation. Namespace restrictions are also explicitly described as weaker than OS/process isolation. [Auto branch](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/src/simtradelab/ptrade/broker_profile.py#L56-L61), [runtime boundary](https://github.com/kay-ou/SimTradeLab/blob/54403e7c21563d2bb0b4ed25ee16ac27c5b32cc6/docs/STRATEGY_RUNTIME_BOUNDARIES.md#L3-L16).

## Questions to take into your own design

- Does broker API compatibility mean every operation is supported?
- Does the selected broker profile have an explicit support matrix instead of permissive auto detection?

## Why this score for a trading system

3/5: direct broker-simulation support checks, with equity-specific API semantics and deliberately limited sandbox guarantees.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
