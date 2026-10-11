# Open Science — What does a workspace snapshot actually preserve

**Decision question:** What does a workspace snapshot actually preserve?

| Field | Review |
| --- | --- |
| Upstream | [Open Science](https://github.com/ai4s-research/open-science) |
| Primary area | Research & Reproducibility |
| Source commit | [25531642b8f6973629bd21f80c613238c6d39c15](https://github.com/ai4s-research/open-science/commit/25531642b8f6973629bd21f80c613238c6d39c15) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/ai4s-research/open-science/blob/25531642b8f6973629bd21f80c613238c6d39c15/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A practical reference for recording uncommitted research code without disturbing a working branch. Record excluded inputs separately before treating a snapshot as a reproducible experiment. |

## Project overview

A local research workbench with agent sessions and workspace snapshots. [Project documentation](https://github.com/ai4s-research/open-science/blob/25531642b8f6973629bd21f80c613238c6d39c15/docs/rfc/agent-runtime.md).

## Mechanism worth inspecting

The [snapshot implementation](https://github.com/ai4s-research/open-science/blob/25531642b8f6973629bd21f80c613238c6d39c15/crates/osd-core/src/git_snapshot.rs#L580-L624) uses a dedicated Git index and reference to record workspace changes without moving the working branch. [Size limits](https://github.com/ai4s-research/open-science/blob/25531642b8f6973629bd21f80c613238c6d39c15/crates/osd-core/src/git_snapshot.rs#L42-L61) exclude large files and directories.

## Important limit

The snapshot can omit large research inputs. A code snapshot therefore needs a separate data manifest; it cannot by itself reproduce the full experiment.

## Questions to take into your own design

- What does a workspace snapshot actually preserve?
- Which excluded data files are identified in a separate reproducibility manifest?

## Why this score for a trading system

3/5: a specific reproducibility pattern, with explicit exclusions that prevent treating it as a complete dataset archive.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
