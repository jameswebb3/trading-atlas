# FAROS — What does an artifact verifier actually verify

**Decision question:** What does an artifact verifier actually verify?

| Field | Review |
| --- | --- |
| Upstream | [FAROS](https://github.com/OpenNSWM-Lab/FAROS) |
| Primary area | Agents & Decision Systems |
| Source commit | [4e4e96fde842ced39b5bfd805b5666b4ce7cca0e](https://github.com/OpenNSWM-Lab/FAROS/commit/4e4e96fde842ced39b5bfd805b5666b4ce7cca0e) |
| Reviewed | 2026-09-26 |
| Declared license | [No license identified in inspected release files](https://github.com/OpenNSWM-Lab/FAROS/blob/4e4e96fde842ced39b5bfd805b5666b4ce7cca0e/README.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Provides explicit artifact contracts instead of relying on an agent's completion message. Add content hashes and domain-specific evidence checks before interpreting a structural pass as research validation. |

## Project overview

A research-agent runtime connecting idea generation, experiments, papers and review. [Project documentation](https://github.com/OpenNSWM-Lab/FAROS/blob/4e4e96fde842ced39b5bfd805b5666b4ce7cca0e/docs/DEVELOPER_GUIDE.md).

## Mechanism worth inspecting

The [verification rules](https://github.com/OpenNSWM-Lab/FAROS/blob/4e4e96fde842ced39b5bfd805b5666b4ce7cca0e/backend/app/faros/verification/rules.py#L61-L134) check required artifact types, registered schemas, metadata keys, producer identity and permitted URI prefixes. [Run creation](https://github.com/OpenNSWM-Lab/FAROS/blob/4e4e96fde842ced39b5bfd805b5666b4ce7cca0e/backend/app/faros/runtime/orchestrator.py#L62-L84) rejects a failed preflight.

## Important limit

These are structural and provenance checks. The inspected rules do not establish that an artifact's contents support a scientific claim; a matching URI prefix is not content integrity.

## Questions to take into your own design

- What does an artifact verifier actually verify?
- Which separate checks establish content integrity and claim validity after a schema passes?

## Why this score for a trading system

3/5: concrete artifact verification is transferable, but the general research platform does not replace trading experiment controls.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
