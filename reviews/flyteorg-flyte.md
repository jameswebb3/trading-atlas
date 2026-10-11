# Flyte — Cache population has an owner

**Decision question:** Can two workers populate the same cache key at once?

| Field | Review |
| --- | --- |
| Upstream | [Flyte](https://github.com/flyteorg/flyte) |
| Primary area | Research & Reproducibility |
| Source commit | [15dc7d4a922bb34d4ee1cac23347bda7f88757ee](https://github.com/flyteorg/flyte/commit/15dc7d4a922bb34d4ee1cac23347bda7f88757ee) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/flyteorg/flyte/blob/15dc7d4a922bb34d4ee1cac23347bda7f88757ee/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The cache manager tracks owner IDs and expiry, refreshes reservations only when expired or owned, and rereads the holder when another caller wins a create/update race. The coordination method is not a proof that every result publication is fenced against a stale owner. |

## Project overview

Workflow runtime for data, ML and agent jobs; the pinned default branch describes Flyte 2. [Documentation](https://github.com/flyteorg/flyte/blob/15dc7d4a922bb34d4ee1cac23347bda7f88757ee/README.md).

## Mechanism worth inspecting

The cache manager tracks owner IDs and expiry, refreshes reservations only when expired or owned, and rereads the holder when another caller wins a create/update race. [Source](https://github.com/flyteorg/flyte/blob/15dc7d4a922bb34d4ee1cac23347bda7f88757ee/cache_service/manager/manager.go#L150-L233).

## Important limit

The coordination method is not a proof that every result publication is fenced against a stale owner. A cache key also needs enough input identity to represent the intended experiment. [Evidence 1](https://github.com/flyteorg/flyte/blob/15dc7d4a922bb34d4ee1cac23347bda7f88757ee/cache_service/manager/manager.go#L150-L233).

## Questions to take into your own design

- Does a stale worker lose authority to publish after its reservation expires?
- Are cached result identity and execution ownership validated separately?

## Why this score for a trading system

A clear transferable coordination path; operating the complete workflow runtime would be excessive for this isolated pattern.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
