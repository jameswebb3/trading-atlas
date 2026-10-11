# DVCLive — resume needs an experiment identity

**Decision question:** Does continuing a metrics directory preserve the same experiment?

| Field | Review |
| --- | --- |
| Upstream | [DVCLive](https://github.com/iterative/dvclive) |
| Primary area | Research & Reproducibility |
| Source commit | [3225786990a767e5d616ac080b428b0a9d94e94a](https://github.com/iterative/dvclive/commit/3225786990a767e5d616ac080b428b0a9d94e94a) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/iterative/dvclive/blob/3225786990a767e5d616ac080b428b0a9d94e94a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A lightweight local logging reference with explicit resume and cleanup paths. Directory continuity needs a manifest check so a recovered step cannot silently join different experiments or overwrite useful history. |

## Project overview

DVCLive records machine-learning metrics and metadata in simple local file formats compatible with DVC. [Project documentation](https://github.com/iterative/dvclive/blob/3225786990a767e5d616ac080b428b0a9d94e94a/README.md#L13-L14).

## Mechanism worth inspecting

Construction chooses either resume or cleanup. Resume reads existing parameters, summary and step, then advances a nonzero recovered step. Normal initialization removes prior logging outputs. [Initialization](https://github.com/iterative/dvclive/blob/3225786990a767e5d616ac080b428b0a9d94e94a/src/dvclive/live.py#L92-L100); [resume/cleanup branch](https://github.com/iterative/dvclive/blob/3225786990a767e5d616ac080b428b0a9d94e94a/src/dvclive/live.py#L165-L190).

## Important limit

Continuing a directory and step counter does not itself prove data, code, target or split identity. Reusing a directory without resume also removes history. An experiment ledger needs a manifest comparison and immutable attempt records before it interprets either behavior as continuation.

## Questions to take into your own design

- Can a changed dataset or preregistration be appended to an existing run?
- Does recovery preserve the previous incomplete attempt before creating a new one?

## Why this score for a trading system

3/5: a practical local-run recovery pattern, with experiment identity and retention requiring a stronger application contract.

**Scope of this review:** Resume initialization and step recovery; hosted integrations and complete file lifecycle were not reviewed.
