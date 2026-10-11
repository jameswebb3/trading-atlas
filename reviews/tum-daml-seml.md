# SEML — Parameter overrides can collapse experiments

**Decision question:** Can different search-space entries resolve to the same configuration?

| Field | Review |
| --- | --- |
| Upstream | [SEML](https://github.com/TUM-DAML/seml) |
| Primary area | Research & Reproducibility |
| Source commit | [48175e861a784e524a9992181f90ed8119790218](https://github.com/TUM-DAML/seml/commit/48175e861a784e524a9992181f90ed8119790218) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/TUM-DAML/seml/blob/48175e861a784e524a9992181f90ed8119790218/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | After parameter overrides, config generation deduplicates the flattened resulting dictionaries and logs how many identical configurations were removed. Configuration identity is not statistical independence. |

## Project overview

Experiment management linking Slurm scheduling, Sacred configuration and MongoDB tracking. [Documentation](https://github.com/TUM-DAML/seml/blob/48175e861a784e524a9992181f90ed8119790218/README.md).

## Mechanism worth inspecting

After parameter overrides, config generation deduplicates the flattened resulting dictionaries and logs how many identical configurations were removed. The CLI also exposes duplicate detection and code-checkpoint choices. [Source](https://github.com/TUM-DAML/seml/blob/48175e861a784e524a9992181f90ed8119790218/src/seml/experiment/config.py#L331-L344).

## Important limit

Configuration identity is not statistical independence. Equal configs on changed data or code are different computations, while retries or seed replicas need explicit family accounting. [Evidence 1](https://github.com/TUM-DAML/seml/blob/48175e861a784e524a9992181f90ed8119790218/src/seml/experiment/config.py#L331-L344). [Evidence 2](https://github.com/TUM-DAML/seml/blob/48175e861a784e524a9992181f90ed8119790218/docs.md#L71-L77).

## Questions to take into your own design

- Is identity computed after resolving defaults and overrides?
- Are hypothesis family, data/code identity and attempt identity stored separately?

## Why this score for a trading system

Highly applicable experiment-identity bookkeeping; Slurm, Sacred and MongoDB are not required to implement the inspected rule.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
