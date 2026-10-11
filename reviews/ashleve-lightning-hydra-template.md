# Lightning-Hydra Template — Fallback weights change what was evaluated

**Decision question:** Does test evaluation use the selected checkpoint?

| Field | Review |
| --- | --- |
| Upstream | [Lightning-Hydra Template](https://github.com/ashleve/lightning-hydra-template) |
| Primary area | Research & Reproducibility |
| Source commit | [bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144](https://github.com/ashleve/lightning-hydra-template/commit/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144) |
| Reviewed | 2026-09-27 |
| Declared license | [Not established in the inspected root](https://github.com/ashleve/lightning-hydra-template/tree/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The training function seeds only when cfg.seed is truthy. Seed zero is a valid value but skips this conditional, and fallback weights are not the selected best checkpoint. |

## Project overview

Template combining PyTorch Lightning training with Hydra-based experiment configuration. [Documentation](https://github.com/ashleve/lightning-hydra-template/blob/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144/README.md).

## Mechanism worth inspecting

The training function seeds only when cfg.seed is truthy. During testing, an empty best-checkpoint path triggers a warning and falls back to current weights; test metrics then overwrite matching training metric keys. [Source](https://github.com/ashleve/lightning-hydra-template/blob/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144/src/train.py#L53-L55).

## Important limit

Seed zero is a valid value but skips this conditional, and fallback weights are not the selected best checkpoint. No root license text was found in the inspected tree. [Evidence 1](https://github.com/ashleve/lightning-hydra-template/blob/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144/src/train.py#L53-L55). [Evidence 2](https://github.com/ashleve/lightning-hydra-template/blob/bddbc24b82ab6ccfa6243e815a49dc5bfe8d4144/src/train.py#L89-L104).

## Questions to take into your own design

- Does seed=0 survive admission as an explicit seed?
- Is evaluation refused or distinctly labeled when the approved checkpoint is missing?

## Why this score for a trading system

Useful reproducibility counterexamples in a training template; neither the template nor generic training metrics establish trading-model validity.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
