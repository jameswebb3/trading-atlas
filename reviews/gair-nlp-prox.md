# ProX - Can transformed examples retain their raw content and transformation recipe?

**Decision question:** Can transformed examples retain their raw content and transformation recipe?

| Field | Review |
| --- | --- |
| Upstream | [GAIR-NLP/ProX](https://github.com/GAIR-NLP/ProX) |
| Primary area | Data Quality & Lineage |
| Source commit | [0a8287ca915007eff0acd641ecfba18c563fde9b](https://github.com/GAIR-NLP/ProX/commit/0a8287ca915007eff0acd641ecfba18c563fde9b) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The chunk-refining stage writes raw_content, original document text and the generated chunk program alongside transformed text. The transformation is model-generated; retaining the program does not prove deterministic replay or suitability for trading labels. |

## What this project does

A programmatic pretraining-data refinement pipeline.

## Mechanism inspected

The chunk-refining stage writes raw_content, original document text and the generated chunk program alongside transformed text.

## Limitation that matters

The transformation is model-generated; retaining the program does not prove deterministic replay or suitability for trading labels.

## Practical check for a trading system

Keep raw inputs, transformation instructions and derived outputs linked by immutable experiment identity.

## Why this score

2/5. It provides a concrete provenance pattern with limited causal transfer.

## Source trail

[README](https://github.com/GAIR-NLP/ProX/blob/0a8287ca915007eff0acd641ecfba18c563fde9b/README.md#L1); [data_gen/tasks/apply_chunk_refining.py](https://github.com/GAIR-NLP/ProX/blob/0a8287ca915007eff0acd641ecfba18c563fde9b/data_gen/tasks/apply_chunk_refining.py#L141); [data_gen/tasks/apply_chunk_refining.py](https://github.com/GAIR-NLP/ProX/blob/0a8287ca915007eff0acd641ecfba18c563fde9b/data_gen/tasks/apply_chunk_refining.py#L143); [data_gen/tasks/apply_chunk_refining.py](https://github.com/GAIR-NLP/ProX/blob/0a8287ca915007eff0acd641ecfba18c563fde9b/data_gen/tasks/apply_chunk_refining.py#L154).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
