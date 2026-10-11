# OpenScience — Can a research trace be bounded without opening its attachments

**Decision question:** Can a research trace be bounded without opening its attachments?

| Field | Review |
| --- | --- |
| Upstream | [OpenScience](https://github.com/synthetic-sciences/openscience) |
| Primary area | Agents & Decision Systems |
| Source commit | [dea8f770aedceba03d4306b246a1e6aed03f79c5](https://github.com/synthetic-sciences/openscience/commit/dea8f770aedceba03d4306b246a1e6aed03f79c5) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/synthetic-sciences/openscience/blob/dea8f770aedceba03d4306b246a1e6aed03f79c5/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful reference for bounded, inspectable agent traces with explicit truncation. Define what may be recorded and shared separately from redaction and size limits. |

## Project overview

A local scientific-agent workbench with tools, durable sessions and trace handling. [Project documentation](https://github.com/synthetic-sciences/openscience/blob/dea8f770aedceba03d4306b246a1e6aed03f79c5/ARCHITECTURE.md).

## Mechanism worth inspecting

The [trace serializer](https://github.com/synthetic-sciences/openscience/blob/dea8f770aedceba03d4306b246a1e6aed03f79c5/backend/cli/src/session/trace-payload.ts#L8-L61) bounds recursion, element counts and byte size, replaces binary payloads with size metadata, marks truncation and applies credential redaction before returning the trace.

## Important limit

Known-secret redaction is not a guarantee that all sensitive research content is removed. The [architecture documentation](https://github.com/synthetic-sciences/openscience/blob/dea8f770aedceba03d4306b246a1e6aed03f79c5/ARCHITECTURE.md#L80-L82) separately describes trace sharing and consent behavior; bounding payloads does not determine sharing policy.

## Questions to take into your own design

- Can a research trace be bounded without opening its attachments?
- Can a truncated or redacted trace still disclose proprietary research content?

## Why this score for a trading system

3/5: concrete trace handling can transfer to research evidence, while most scientific tools are outside trading's requirements.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
