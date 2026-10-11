# ClearML: a commit is incomplete without the working-tree diff

**Decision question:** What must an experiment capture beyond its Git commit?

| Field | Review |
| --- | --- |
| Upstream | [ClearML](https://github.com/clearml/clearml) |
| Primary area | Research & Reproducibility |
| Source commit | [6201e091cfd607ebf4d0f34604425e6e70c8a69d](https://github.com/clearml/clearml/commit/6201e091cfd607ebf4d0f34604425e6e70c8a69d) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/clearml/clearml/blob/6201e091cfd607ebf4d0f34604425e6e70c8a69d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Records repository identity, commit, local changes, packages, parameters, and outputs for an experiment. Its detector can include a diff and distinguish local from remote commit state. This is valuable run provenance, though broad automatic capture needs privacy and retention controls. |

## Mechanism worth inspecting

The [experiment overview](https://github.com/clearml/clearml/blob/6201e091cfd607ebf4d0f34604425e6e70c8a69d/README.md#L99-L115) explicitly includes non-committed changes, package versions, parameters, and outputs. The [repository detector](https://github.com/clearml/clearml/blob/6201e091cfd607ebf4d0f34604425e6e70c8a69d/clearml/backend_interface/task/repo/detectors.py#L113-L165) optionally captures a diff and can compare against remote branch state. The relevant design is to record a code identity that includes dirty state, then tie it to the run's input and output artifacts.

## Important limit

Automatic collection can include sensitive code or paths and requires deliberate retention. Capturing a diff still does not pin remote data revisions or guarantee that external APIs return identical values. The self-hosted server and agent add operational cost.

## Questions to take into your own design

- Does every result identify both commit and uncommitted patch?
- Are environment and data identities captured without exposing secrets?

## Why this score for a trading system

Capturing code diff and environment alongside parameters addresses a common reproducibility gap; the full platform is heavier than a local run manifest.

**Scope of this review:** We read the pinned README and repository-detection implementation. We did not run an experiment or assess server deployment.
