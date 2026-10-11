# SQLBucket — Zero checks and zero violations are different

**Decision question:** What does an empty integrity-check result mean?

| Field | Review |
| --- | --- |
| Upstream | [SQLBucket](https://github.com/socialpoint-labs/sqlbucket) |
| Primary area | Data Quality & Lineage |
| Source commit | [72aa1d8eb627d8822e629aeed531367b5ae41ca0](https://github.com/socialpoint-labs/sqlbucket/commit/72aa1d8eb627d8822e629aeed531367b5ae41ca0) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/socialpoint-labs/sqlbucket/blob/72aa1d8eb627d8822e629aeed531367b5ae41ca0/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The integrity runner treats an empty query result as passing and reports the number of checks executed. An empty anti-violation query can be correct; selecting no checks is a separate coverage state. |

## Project overview

Lightweight SQL pipeline templating, orchestration and integrity checks. [Documentation](https://github.com/socialpoint-labs/sqlbucket/blob/72aa1d8eb627d8822e629aeed531367b5ae41ca0/README.rst).

## Mechanism worth inspecting

The integrity runner treats an empty query result as passing and reports the number of checks executed. Prefix filtering can leave zero checks while the final log still reports all passed. [Source](https://github.com/socialpoint-labs/sqlbucket/blob/72aa1d8eb627d8822e629aeed531367b5ae41ca0/sqlbucket/integrity.py#L29-L115).

## Important limit

An empty anti-violation query can be correct; selecting no checks is a separate coverage state. A generic success string cannot distinguish them. [Evidence 1](https://github.com/socialpoint-labs/sqlbucket/blob/72aa1d8eb627d8822e629aeed531367b5ae41ca0/sqlbucket/integrity.py#L29-L115).

## Questions to take into your own design

- Is an empty result valid for this specific query contract?
- Does a run with zero selected checks remain unevaluated?

## Why this score for a trading system

A focused admission-state example, largely duplicating common pipeline checks rather than providing a new data platform.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
