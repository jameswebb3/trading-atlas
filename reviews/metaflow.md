# Metaflow: Join branches only when their artifacts agree

**Decision question:** What happens if two experiment branches return the same artifact name with different contents?

| Field | Review |
| --- | --- |
| Upstream | [Netflix/metaflow](https://github.com/Netflix/metaflow) |
| Primary area | Research & Reproducibility |
| Source commit | [8b500daaaf57eabad507cb76936676b9ee7e4bff](https://github.com/Netflix/metaflow/commit/8b500daaaf57eabad507cb76936676b9ee7e4bff) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/Netflix/metaflow/blob/8b500daaaf57eabad507cb76936676b9ee7e4bff/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Compares artifact hashes at a join and requires an explicit resolution when branches disagree. Equal artifact hashes address byte identity, not whether the underlying result is methodologically valid. |

## Project overview

Python framework for data and ML workflows with versioned runs and artifacts. Its branch-and-join model supports parallel experiments and explicit resolution when branch outputs disagree.

[Project documentation](https://github.com/Netflix/metaflow/blob/8b500daaaf57eabad507cb76936676b9ee7e4bff/README.md#L13-L20).

## Mechanism worth inspecting

The datastore design treats artifacts as persisted objects. At a join, merge_artifacts considers incoming branch artifacts and records conflicts if the same name carries different hashes; the flow must resolve that merge explicitly. This avoids accidental last-writer-wins evidence.

**Source trail:** [project overview](https://github.com/Netflix/metaflow/blob/8b500daaaf57eabad507cb76936676b9ee7e4bff/README.md) · [documentation](https://github.com/Netflix/metaflow/blob/8b500daaaf57eabad507cb76936676b9ee7e4bff/docs/datastore.md#L43-L64) · [implementation](https://github.com/Netflix/metaflow/blob/8b500daaaf57eabad507cb76936676b9ee7e4bff/metaflow/flowspec.py#L738-L830).

## Important limit

The comparison is only for artifacts present on incoming branches. It cannot identify a shared upstream error or prove that either branch used valid data.

## Questions to take into your own design

- Can a parallel experiment silently overwrite a sibling’s result?
- Does the merge receipt record how a conflict was resolved?

## Why this score for a trading system

Artifact-hash conflict detection prevents silent branch overwrites in experiments, but equal bytes do not validate a result.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
