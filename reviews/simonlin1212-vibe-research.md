# Vibe Research — Can fetched evidence disagree with the orchestrator's ledger

**Decision question:** Can fetched evidence disagree with the orchestrator's ledger?

| Field | Review |
| --- | --- |
| Upstream | [Vibe Research](https://github.com/simonlin1212/Vibe-Research) |
| Primary area | Research & Reproducibility |
| Source commit | [85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3](https://github.com/simonlin1212/Vibe-Research/commit/85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/simonlin1212/Vibe-Research/blob/85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A practical reference for cross-checking raw evidence, ledger entries and partial-result status. Make required hashes and excluded control files explicit in your own evidence contract. |

## Project overview

A financial research workbench with staged reports, deterministic calculations and source-linked evidence. [Project documentation](https://github.com/simonlin1212/Vibe-Research/blob/85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3/docs/source-delivery.md).

## Mechanism worth inspecting

The [fetch validator](https://github.com/simonlin1212/Vibe-Research/blob/85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3/orchestrator/src/validator.ts#L131-L175) checks files against orchestrator ledger entries, verifies available hashes, reconciles exit codes with status and checks recorded raw responses. [Evidence references](https://github.com/simonlin1212/Vibe-Research/blob/85ba57191ba28cb9b4eeb4f7c1ed006d58d999c3/orchestrator/src/validator.ts#L176-L194) must resolve inside the run's raw directory.

## Important limit

Hash checks for fetched envelopes are conditional on a recorded hash. The inspected code also excludes named control files, so integrity coverage must be stated explicitly rather than inferred for the entire run directory.

## Questions to take into your own design

- Can fetched evidence disagree with the orchestrator's ledger?
- Are hashes mandatory for all required evidence files and are exclusions listed explicitly?

## Why this score for a trading system

3/5: directly relevant financial evidence checks, with conditional hashing and declared exclusions that need careful adaptation.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
