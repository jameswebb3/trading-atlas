# pyDVL: Resuming a valuation needs more than row names

**Decision question:** Is a resumed data-valuation run tied to the same dataset contents?

| Field | Review |
| --- | --- |
| Upstream | [aai-institute/pyDVL](https://github.com/aai-institute/pyDVL) |
| Primary area | Signals & Models |
| Source commit | [aae7fa0159cff6c5b64d32e5415f36cbd5e224b5](https://github.com/aai-institute/pyDVL/commit/aae7fa0159cff6c5b64d32e5415f36cbd5e224b5) |
| Reviewed | 2026-09-25 |
| Declared license | [GPL-3.0](https://github.com/aai-institute/pyDVL/blob/aae7fa0159cff6c5b64d32e5415f36cbd5e224b5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Checks row indices and names before reusing a saved valuation result. The inspected check does not hash row values, so corrected data with the same identifiers could reuse stale valuations. |

## Mechanism worth inspecting

pyDVL estimates the value or influence of individual training examples and supports loading a prior result. The resume guard compares the previous result’s indices and names with the current Dataset before returning it. This is a concrete identity check, but it is narrower than content identity.

**Source trail:** [project overview](https://github.com/aai-institute/pyDVL/blob/aae7fa0159cff6c5b64d32e5415f36cbd5e224b5/README.md) · [documentation](https://github.com/aai-institute/pyDVL/blob/aae7fa0159cff6c5b64d32e5415f36cbd5e224b5/docs/index.md#L5-L35) · [implementation](https://github.com/aai-institute/pyDVL/blob/aae7fa0159cff6c5b64d32e5415f36cbd5e224b5/src/pydvl/valuation/base.py#L41-L70).

## Important limit

The inspected guard does not compare data bytes, labels, feature definitions, or evaluation utility. GPL licensing also makes direct reuse a separate decision.

## Questions to take into your own design

- Does a resumed analysis bind to a content hash as well as row IDs?
- Would corrected historical data invalidate cached valuations?

## Why this score for a trading system

Resume validation shows a dataset-identity trap, but per-row valuation and GPL licensing have narrow practical trading-system value.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
