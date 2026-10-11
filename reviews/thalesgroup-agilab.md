# agilab — A successful run needs a manifest and passing validations

**Decision question:** What evidence must exist before a pipeline run is called successful?

| Field | Review |
| --- | --- |
| Upstream | [ThalesGroup/agilab](https://github.com/ThalesGroup/agilab) |
| Primary area | Research & Reproducibility |
| Source commit | [198201f1efd5510c787dec27c73a820ecc15bdf0](https://github.com/ThalesGroup/agilab/commit/198201f1efd5510c787dec27c73a820ecc15bdf0) |
| Reviewed | 2026-10-09 |
| Declared license | BSD-style ([source](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The manifest records artifact existence, size and optional SHA-256; its success predicate requires status pass, at least one validation and every validation passing. Artifact hashing is optional and the manifest writer uses a direct file write; a passing status does not prove the right data cutoff or an atomic durable commit. |

## What this project does

Notebook-to-app workflow with a versioned run manifest covering command, environment, timing, artifacts and validations. [README](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/README.md).

## Mechanism inspected

The manifest records artifact existence, size and optional SHA-256; its success predicate requires status pass, at least one validation and every validation passing. [Implementation](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/src/agilab/evidence/run_manifest.py#L130-L183). [Related implementation](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/src/agilab/evidence/run_manifest.py#L345-L350).

## Limitation that matters

Artifact hashing is optional and the manifest writer uses a direct file write; a passing status does not prove the right data cutoff or an atomic durable commit. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require nonempty validation evidence and hashed input/output artifacts in each weight-moving research run, with a precise cutoff and immutable run identity.

## Why this score

The manifest records artifact existence, size and optional SHA-256; its success predicate requires status pass, at least one validation and every validation passing. Artifact hashing is optional and the manifest writer uses a direct file write; a passing status does not prove the right data cutoff or an atomic durable commit.

## Source trail

[README](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/README.md) · [Implementation](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/src/agilab/evidence/run_manifest.py#L130-L183) · [Related implementation](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/src/agilab/evidence/run_manifest.py#L345-L350) · [License](https://github.com/ThalesGroup/agilab/blob/198201f1efd5510c787dec27c73a820ecc15bdf0/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
