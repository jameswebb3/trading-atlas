# Vibe-Trading: reject unsupported figures before an agent answer ships

**Decision question:** What happens when a research agent writes a number that its tools did not support?

| Field | Review |
| --- | --- |
| Upstream | [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) |
| Primary area | Agents & Decision Systems |
| Source commit | [5e9ffd1a73e71b4a1be45c5b5e330b6877fee849](https://github.com/HKUDS/Vibe-Trading/commit/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/LICENSE) |
| Review depth | 2/3: README, release gate, figure parser, and release tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Validates numerical claims in a generated answer against tool evidence, asks for correction, and can remove unsupported figures before release. The redacted answer is rechecked and records a content hash. The approach helps control unsupported research prose, but its broad agent stack is not a trading execution control. |

## Mechanism worth inspecting

The [research workflow](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/README.md#L441-L461) puts validation between tool use and delivery. The [figure parser](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/agent/src/agent/grounding/figures.py#L1-L9) maps visible numeric prose to declared figures. The [release gate](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/agent/src/agent/grounding/release.py#L155-L208) returns precise evidence feedback for a rejected draft. Its [redaction path](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/agent/src/agent/grounding/release.py#L493-L557) revalidates the released note and persists the released text hash; [span handling](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/agent/src/agent/grounding/release.py#L559-L625) fails closed when a flagged figure cannot be located. A [release test](https://github.com/HKUDS/Vibe-Trading/blob/5e9ffd1a73e71b4a1be45c5b5e330b6877fee849/agent/tests/test_grounding_release.py#L388-L403) asserts that unsupported prose is removed while other analysis survives.

## Important limit

The gate relies on the tool ledger's own evidence quality, figure classification, and source identity. Replacing a number with an omission marker can leave surrounding qualitative prose too confident; review of the full claim remains necessary. No part of this review validates generated trading returns or authorizes an agent to place orders.

## Questions to take into your own design

- Are numeric claims tied to concrete observed values and source identities?
- Does a failed evidence check block release or visibly remove the unsupported claim?
- Can a reviewer inspect the draft, correction, final text, and release hash?

## Why this score for a trading system

The evidence gate offers a concrete transferable safeguard against unsupported agent research claims; its broad finance-agent workflow is not a direct exchange or backtest mechanism.

**Scope of this review:** We read the pinned README and selected figure, release, and test code. We did not run the agent or test every language and numeric format.
