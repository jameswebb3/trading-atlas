# MLRun: distinguish artifact identity from content hashes and latest tags

**Decision question:** Does an artifact version identify immutable content or only its metadata?

| Field | Review |
| --- | --- |
| Upstream | [MLRun](https://github.com/mlrun/mlrun) |
| Primary area | Research & Reproducibility |
| Source commit | [0ce504a87b64b0b998721cbdddbf8d36d30e5884](https://github.com/mlrun/mlrun/commit/0ce504a87b64b0b998721cbdddbf8d36d30e5884) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Tracks experiment artifacts with producer metadata, version identifiers, and optional content hashes. Its documentation makes the distinction between immutable versions, mutable latest tags, and run-specific storage paths explicit. |

## Project overview

An ML orchestration framework manages jobs, artifact tracking, and deployment workflows. [Project documentation](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/README.md#L25-L45).

## Mechanism worth inspecting

The [artifact documentation](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/docs/store/artifacts.md#L95-L132) explains run-specific paths, artifact UIDs, and the default latest tag. [Upload code](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/mlrun/artifacts/base.py#L392-L438) computes a content hash conditionally, while [target naming](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/mlrun/artifacts/base.py#L470-L493) can incorporate that hash. [Object hashing](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/mlrun/artifacts/base.py#L872-L898) uses selected metadata fields for a separate artifact identity.

## Important limit

A reusable file path can be overwritten unless the [run-specific layout](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/docs/store/artifacts.md#L95-L97) is used. [Conditional hashing](https://github.com/mlrun/mlrun/blob/0ce504a87b64b0b998721cbdddbf8d36d30e5884/mlrun/artifacts/base.py#L402-L405) means consumers must verify whether bytes were hashed rather than infer it from a version label.

## Questions to take into your own design

- Do experiment inputs resolve to immutable content digests rather than latest tags?
- Are metadata identity and byte-level content identity stored separately?

## Why this score for a trading system

3/5: useful artifact identity semantics, with configurable guarantees and a substantial orchestration stack that is unnecessary for adopting this pattern.

**Scope of this review:** README, artifact documentation, upload/hash source; orchestrator not run.
