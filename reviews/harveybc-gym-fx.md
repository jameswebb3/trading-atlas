# gym-fx — Can two simulator results be compared under the same execution assumptions

**Decision question:** Can two simulator results be compared under the same execution assumptions?

| Field | Review |
| --- | --- |
| Upstream | [gym-fx](https://github.com/harveybc/gym-fx) |
| Primary area | Backtesting & Simulation |
| Source commit | [1eeecb789965f3e01e9e51f479c6f89265b03859](https://github.com/harveybc/gym-fx/commit/1eeecb789965f3e01e9e51f479c6f89265b03859) |
| Reviewed | 2026-09-26 |
| Declared license | [No license declaration identified in inspected tree/package metadata](https://github.com/harveybc/gym-fx/blob/1eeecb789965f3e01e9e51f479c6f89265b03859/setup.py) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Defines an explicit, versioned execution-cost contract for simulator comparisons. Inspect implementation parity separately; identical configuration names do not guarantee identical behavior. |

## Project overview

Plugin-based Gymnasium trading environment with configurable simulation engines, costs and execution diagnostics. [Project documentation](https://github.com/harveybc/gym-fx/blob/1eeecb789965f3e01e9e51f479c6f89265b03859/README.md#L3-L25).

## Mechanism worth inspecting

An engine-neutral cost profile requires version, per-side commission, spread, slippage, latency, collision and limit-fill policies, margin settings and seed. Missing fields and unsupported enum values are rejected. [Profile](https://github.com/harveybc/gym-fx/blob/1eeecb789965f3e01e9e51f479c6f89265b03859/simulation_engines/contracts.py#L23-L107), [diagnostics](https://github.com/harveybc/gym-fx/blob/1eeecb789965f3e01e9e51f479c6f89265b03859/README.md#L93-L102).

## Important limit

A shared schema is not evidence that both engines implement every field identically. The README warns that execution-accounting work exists in a separate snapshot; result interpretation needs the exact environment revision. [Version boundary](https://github.com/harveybc/gym-fx/blob/1eeecb789965f3e01e9e51f479c6f89265b03859/README.md#L14-L25).

## Questions to take into your own design

- Can two simulator results be compared under the same execution assumptions?
- Do both engines reject or implement each execution-profile field consistently?

## Why this score for a trading system

3/5: useful direct simulation contracts, without a verified cross-engine behavioral comparison in this review.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
