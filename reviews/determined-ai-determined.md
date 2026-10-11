# Determined — Checkpoint metadata can conflict across workers

**Decision question:** How are inconsistent worker checkpoint claims represented?

| Field | Review |
| --- | --- |
| Upstream | [Determined](https://github.com/determined-ai/determined) |
| Primary area | Research & Reproducibility |
| Source commit | [c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e](https://github.com/determined-ai/determined/commit/c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/determined-ai/determined/blob/c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | merge_metadata recursively combines dictionaries and returns a separate map of conflicting metadata keys and reporting ranks when scalar values differ. The merged dictionary and conflict map must both be consumed. |

## Project overview

Deep-learning platform with distributed training, resource management and checkpointing. [Documentation](https://github.com/determined-ai/determined/blob/c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e/README.md).

## Mechanism worth inspecting

merge_metadata recursively combines dictionaries and returns a separate map of conflicting metadata keys and reporting ranks when scalar values differ. [Source](https://github.com/determined-ai/determined/blob/c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e/harness/determined/core/_checkpoint.py#L38-L124).

## Important limit

The merged dictionary and conflict map must both be consumed. The helper's existence does not establish that every downstream reader rejects a conflicted checkpoint. [Evidence 1](https://github.com/determined-ai/determined/blob/c1e9c6d7b821ef246d612bb9922f7fb1b58dcf2e/harness/determined/core/_checkpoint.py#L38-L124).

## Questions to take into your own design

- Does a checkpoint receipt preserve conflicting worker claims?
- Can a checkpoint be admitted if data/config hashes disagree across ranks?

## Why this score for a trading system

A concrete distributed-artifact evidence pattern; the full GPU-training platform is unnecessary for a small experiment ledger.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
