# EPSILON — What exactly does a sensitivity-test verdict certify

**Decision question:** What exactly does a sensitivity-test verdict certify?

| Field | Review |
| --- | --- |
| Upstream | [EPSILON](https://github.com/DresdenGman/EPSILON-trading-simulator) |
| Primary area | Testing & Verification |
| Source commit | [781984262670816f2f566ac7c6b2bbcc41e82602](https://github.com/DresdenGman/EPSILON-trading-simulator/commit/781984262670816f2f566ac7c6b2bbcc41e82602) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Preserves rejection rules and sensitivity results in inspectable artifacts. Useful for explicit verdict semantics, with baseline qualification, preregistration and independent reproduction kept separate. |

## Project overview

Quantitative decision lab that preserves an explicit claim, rejection rule, baseline, perturbations and evidence artifacts. [Project documentation](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/README.md#L12-L23).

## Mechanism worth inspecting

Evidence evaluation applies a declared metric/operator/threshold to the perturbation set, records survival count, nearest failure and sensitivity, and creates canonical checksums. Tests check verdict cases and artifact tampering. [Evaluation](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/instrument/lib/evidence-contract.ts#L66-L103), [artifact](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/instrument/lib/evidence-contract.ts#L119-L147), [tests](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/instrument/tests/evidence-contract.test.ts#L9-L27).

## Important limit

The survival verdict evaluates perturbations, not the baseline; the baseline is reported separately. Its fixed case is not an independently timestamped preregistration, and shifted windows overlap. A checksum proves content consistency, not origin. [Case boundary](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/docs/REFERENCE_CASE.md#L3-L17), [checksum limit](https://github.com/DresdenGman/EPSILON-trading-simulator/blob/781984262670816f2f566ac7c6b2bbcc41e82602/instrument/lib/evidence-contract.ts#L9-L13).

## Questions to take into your own design

- What exactly does a sensitivity-test verdict certify?
- Are baseline performance and perturbation survival both required by the decision rule?

## Why this score for a trading system

3/5: direct research-verdict mechanics and relevant tests, but a small perturbation set cannot replace a trading gauntlet.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
