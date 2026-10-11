# ModelFox — Alert comparisons depend on baseline and sampling

**Decision question:** What can a production-versus-training alert actually establish?

| Field | Review |
| --- | --- |
| Upstream | [ModelFox](https://github.com/modelfoxdotdev/modelfox) |
| Primary area | Operations & Observability |
| Source commit | [ec5d86b0a0557859231fd0a2cf98fa5550828f22](https://github.com/modelfoxdotdev/modelfox/commit/ec5d86b0a0557859231fd0a2cf98fa5550828f22) |
| Reviewed | 2026-09-27 |
| Declared license | [Mixed: MIT outside crates/app; paid production license for reviewed app](https://github.com/modelfoxdotdev/modelfox/blob/ec5d86b0a0557859231fd0a2cf98fa5550828f22/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | The app checker retrieves the latest stored production metric and compares it with a model's training/test metric using absolute difference or percentage change. The percentage branch divides by the training value, so zero baselines need a policy. |

## Project overview

Tabular-model training and prediction tools with a browser monitoring application; the reviewed app component has separate production licensing. [Documentation](https://github.com/modelfoxdotdev/modelfox/blob/ec5d86b0a0557859231fd0a2cf98fa5550828f22/README.md).

## Mechanism worth inspecting

The app checker retrieves the latest stored production metric and compares it with a model's training/test metric using absolute difference or percentage change. [Source](https://github.com/modelfoxdotdev/modelfox/blob/ec5d86b0a0557859231fd0a2cf98fa5550828f22/crates/app/core/monitor_checker.rs#L360-L438).

## Important limit

The percentage branch divides by the training value, so zero baselines need a policy. The root license excludes crates/app from the general MIT grant and requires paid licensing for production use of that component. [Evidence 1](https://github.com/modelfoxdotdev/modelfox/blob/ec5d86b0a0557859231fd0a2cf98fa5550828f22/crates/app/core/monitor_checker.rs#L360-L438). [Evidence 2](https://github.com/modelfoxdotdev/modelfox/blob/ec5d86b0a0557859231fd0a2cf98fa5550828f22/LICENSE#L1-L1).

## Questions to take into your own design

- Are zero baselines and missing production metrics represented explicitly?
- Is the compared window/population the same as the stated baseline?

## Why this score for a trading system

Adjacent ML monitoring with restricted licensing in the exact component reviewed; it is not a trading-risk or alpha monitoring system.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
