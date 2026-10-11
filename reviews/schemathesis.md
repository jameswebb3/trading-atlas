# Schemathesis: API testing needs linked operations and a retained trace

**Decision question:** Can a valid create request still produce an invalid later state?

| Field | Review |
| --- | --- |
| Upstream | [schemathesis/schemathesis](https://github.com/schemathesis/schemathesis) |
| Primary area | Testing & Verification |
| Source commit | [7a195cd4b1957e0c0b24e8bc10d256846a9b5dce](https://github.com/schemathesis/schemathesis/commit/7a195cd4b1957e0c0b24e8bc10d256846a9b5dce) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/schemathesis/schemathesis/blob/7a195cd4b1957e0c0b24e8bc10d256846a9b5dce/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Discovers linked API operations and records parent-child test cases, interactions, and check results. If no producer links are discoverable, the stateful phase has nothing to run; stored payloads may be truncated. |

## Mechanism worth inspecting

The guide describes inferred links, Location headers, and explicit OpenAPI links for sequencing operations. ScenarioRecorder retains case ancestry, transition, response, and check results. It truncates oversized response bodies only in the stored copy, which is an important evidence distinction.

**Source trail:** [project overview](https://github.com/schemathesis/schemathesis/blob/7a195cd4b1957e0c0b24e8bc10d256846a9b5dce/README.md) · [documentation](https://github.com/schemathesis/schemathesis/blob/7a195cd4b1957e0c0b24e8bc10d256846a9b5dce/docs/guides/stateful-testing.md#L10-L20) · [implementation](https://github.com/schemathesis/schemathesis/blob/7a195cd4b1957e0c0b24e8bc10d256846a9b5dce/src/schemathesis/engine/recorder.py#L62-L124).

## Important limit

A schema or inferred link may not encode asynchronous exchange semantics. The recorded trace can omit full payload bytes after truncation, so exact forensic evidence needs separate retention.

## Questions to take into your own design

- Are ACK, status, and cancel endpoints linked in generated scenarios?
- Does a failed scenario retain the exact request/response evidence needed to replay it?

## Why this score for a trading system

Linked API scenarios can test order-lifecycle endpoints, but inferred links alone do not model asynchronous exchange state.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
