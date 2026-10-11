# Soda Core: fail when freshness cannot be measured

**Decision question:** Does a freshness check fail when its latest timestamp is unavailable?

| Field | Review |
| --- | --- |
| Upstream | [sodadata/soda-core](https://github.com/sodadata/soda-core) |
| Primary area | Data Quality & Lineage |
| Source commit | [ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04](https://github.com/sodadata/soda-core/commit/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04) |
| Reviewed | 2026-09-25 |
| Declared license | [Elastic-2.0](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/LICENSE) |
| Review depth | 3/3: documentation, implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Evaluates a contract against the latest timestamp and records the tested-row count in its diagnostics. A missing or unparsable timestamp fails, but a recent maximum alone cannot establish continuous trading-feed coverage. |

## Mechanism worth inspecting

The [README](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/README.md#L9-L19) and [contract reference](https://docs.soda.io/reference/contract-language-reference) describe checks for schema, counts, missing values, and freshness. In the implementation, the [freshness path](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/soda-core/src/soda_core/contracts/impl/check_types/freshness_check.py#L194-L242) reads the maximum timestamp, converts it to UTC, records rows tested, and returns FAILED when either the latest timestamp or reference time is unavailable. It does not turn an unmeasured check into a pass. The [integration test](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/soda-tests/tests/integration/test_freshness_check.py#L31-L78) specifies the timestamp and diagnostic units expected by reporting; we read the test but did not run it.

A trading feed could adopt the distinction between measured freshness and unavailable evidence, with the checked denominator visible.

## Important limits

Freshness is [reference time minus MAX(timestamp)](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/soda-core/src/soda_core/contracts/impl/check_types/freshness_check.py#L66-L70). One recent row can pass despite a missing interval, asset, or partition. The contract must separately define expected coverage. The [repository license](https://github.com/sodadata/soda-core/blob/ac8c7474b0542b14f48c9a4a5c3a9de9075fcd04/LICENSE#L1-L20) is Elastic License 2.0, a source-available license; this review extracts a pattern and does not recommend embedding the engine.

## Questions to take into your own design

- Does an unavailable metric fail instead of becoming zero or pass?
- Is the checked row population included with the result?
- Are interior gaps checked independently of latest-row age?

## Why this score for a trading system

Failing an unavailable freshness measurement and retaining its denominator are useful trading-data gates; the latest-row metric still needs a separate gap check and the source-available license limits reuse.

**Scope of this review:** We read the pinned README, contract documentation, implementation, and relevant test. We did not install or run Soda Core, inspect every backend, or establish later-commit behavior.
