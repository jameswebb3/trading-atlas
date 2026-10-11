# SciAtlas - Show what supports a research claim

**Decision question:** Can an automated research summary reveal which part of a claim its evidence covers?

| Field | Review |
| --- | --- |
| Upstream | [zjunlp/SciAtlas](https://github.com/zjunlp/SciAtlas) |
| Primary area | Agents & Decision Systems |
| Source commit | [e8873a96bda28df56b0ede7cf1052821bb2ed486](https://github.com/zjunlp/SciAtlas/commit/e8873a96bda28df56b0ede7cf1052821bb2ed486) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The grounding result separates the supporting span, shared points, mismatches and an explicit coverage level; its run artifact records corpus signature, model, retrieval status and fallbacks. Coverage and the evidence-span field are produced by an LLM, not independently checked quotations. The cache signature uses path, size and modification time rather than content hashes; the headline service depends on a hosted API. |

## What this project does

SciAtlas packages literature retrieval, paragraph-level grounding and report generation around a scientific knowledge graph. [README](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/README.md).

## Mechanism inspected

The grounding result separates the supporting span, shared points, mismatches and an explicit coverage level; its run artifact records corpus signature, model, retrieval status and fallbacks. [Implementation](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/sciatlas/evidence/grounding.py#L1157-L1192). [Related path](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/sciatlas/evidence/grounding.py#L2240-L2283).

## Limitation that matters

Coverage and the evidence-span field are produced by an LLM, not independently checked quotations. The cache signature uses path, size and modification time rather than content hashes; the headline service depends on a hosted API. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For each research claim, store source span, claimed overlap, missing aspects and retrieval/model provenance; verify decisive claims by a separate human or deterministic check.

## Why this score

The grounding result separates the supporting span, shared points, mismatches and an explicit coverage level; its run artifact records corpus signature, model, retrieval status and fallbacks. Coverage and the evidence-span field are produced by an LLM, not independently checked quotations. The cache signature uses path, size and modification time rather than content hashes; the headline service depends on a hosted API.

## Source trail

[README](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/README.md) - [Implementation](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/sciatlas/evidence/grounding.py#L1157-L1192) - [Related path](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/sciatlas/evidence/grounding.py#L2240-L2283) - [License](https://github.com/zjunlp/SciAtlas/blob/e8873a96bda28df56b0ede7cf1052821bb2ed486/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
