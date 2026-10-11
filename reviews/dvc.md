# DVC: A failed stage changes which descendants may run

**Decision question:** What happens downstream after an experiment stage fails?

| Field | Review |
| --- | --- |
| Upstream | [treeverse/dvc](https://github.com/treeverse/dvc) |
| Primary area | Research & Reproducibility |
| Source commit | [56e59829512ff134aa269099a2099587b810b4dd](https://github.com/treeverse/dvc/commit/56e59829512ff134aa269099a2099587b810b4dd) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Reproduces stages along a dependency graph and skips descendants after a failed upstream stage in keep-going mode. Its explicit ignore-error mode can continue without that skip; callers must choose failure semantics deliberately. |

## Project overview

Git-connected versioning for data, models, and experiments. Links inputs, parameters, and outputs to pipeline steps, making research changes and their reproduction requirements visible.

[Project documentation](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/README.rst#L20-L32).

## Mechanism worth inspecting

The README describes code, data, outputs, and metrics as stage dependencies. The reproduction loop records failures and, except in ignore mode, identifies dependent stages to skip; it raises after the run if failures remain. The useful pattern is failure propagation tied to the graph, not merely a final process exit code.

**Source trail:** [project overview](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/README.rst) · [documentation](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/README.rst#L27-L59) · [implementation](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/reproduce.py#L176-L205) · [additional source](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/reproduce.py#L135-L149).

## Important limit

A dependency graph only captures dependencies that were declared. If data files, code revisions, or external side inputs are omitted, a reproducible-looking stage may still be irreproducible.

## Questions to take into your own design

- Can a failed upstream artifact be consumed by a downstream scoring step?
- Are all data and code inputs part of the stage identity?

## Why this score for a trading system

Dependency-aware failure propagation helps trading research pipelines; undeclared external inputs still break reproducibility.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
