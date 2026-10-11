# KitOps — Bundle identity is stronger than a mutable tag

**Decision question:** Can a package name establish which bytes were reviewed?

| Field | Review |
| --- | --- |
| Upstream | [KitOps](https://github.com/kitops-ml/kitops) |
| Primary area | Research & Reproducibility |
| Source commit | [d04583d6d2b6a6f48b1070f10bea637dc9c3b74a](https://github.com/kitops-ml/kitops/commit/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | SaveModel constructs a manifest from configuration and layer descriptors. A digest identifies packaged content, not data completeness or a valid experiment. |

## Project overview

OCI-based packaging for code, datasets, models and related AI/ML artifacts. [Documentation](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/README.md).

## Mechanism worth inspecting

SaveModel constructs a manifest from configuration and layer descriptors. Configuration descriptors hash the serialized bytes; the pack command reports the resulting digest and applies tags separately. [Source](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/pkg/lib/filesystem/local-storage.go#L61-L149).

## Important limit

A digest identifies packaged content, not data completeness or a valid experiment. External resources, selection scope and the checks that admitted the bundle still need a receipt. [Evidence 1](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/pkg/lib/filesystem/local-storage.go#L61-L149). [Evidence 2](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/pkg/cmd/pack/pack.go#L45-L75). [Evidence 3](https://github.com/kitops-ml/kitops/blob/d04583d6d2b6a6f48b1070f10bea637dc9c3b74a/pkg/artifact/kitfile.md#L1-L56).

## Questions to take into your own design

- Is the receipt bound to a digest rather than only a mutable name?
- Does the manifest identify every data/code input actually used?

## Why this score for a trading system

A precise artifact-identity reference; a local manifest can capture the principle without introducing OCI packaging infrastructure.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
