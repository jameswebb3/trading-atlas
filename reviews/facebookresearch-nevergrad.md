# Nevergrad — Do optimiser counters represent every research attempt

**Decision question:** Do optimiser counters represent every research attempt?

| Field | Review |
| --- | --- |
| Upstream | [Nevergrad](https://github.com/facebookresearch/nevergrad) |
| Primary area | Research & Reproducibility |
| Source commit | [617a3b0bcd9b7faa89f68ed6f17b59bec58f2360](https://github.com/facebookresearch/nevergrad/commit/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/facebookresearch/nevergrad/blob/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Distinguishes requested candidates, supplied results and repeated evaluations. Useful for linking asynchronous optimiser calls to a research ledger that also retains failed and manually introduced attempts. |

## Project overview

A gradient-free optimisation platform supporting asynchronous ask-and-tell evaluation. [Project documentation](https://github.com/facebookresearch/nevergrad/blob/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360/docs/optimization.rst#L55-L64).

## Mechanism worth inspecting

The optimiser tracks asked candidate identities separately from tell counts and tell-not-asked counts. A tell freezes the candidate, removes known identities from the pending set or records an external result. The archive can combine repeated evaluations at the same parameter point. [Counters](https://github.com/facebookresearch/nevergrad/blob/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360/nevergrad/optimization/base.py#L129-L134); [candidate freeze](https://github.com/facebookresearch/nevergrad/blob/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360/nevergrad/optimization/base.py#L368-L370), [result identity and repeated evaluations](https://github.com/facebookresearch/nevergrad/blob/617a3b0bcd9b7faa89f68ed6f17b59bec58f2360/nevergrad/optimization/base.py#L425-L455).

## Important limit

Those counters describe optimiser interactions, not complete experimental multiplicity. Crashed evaluations, retries, manual variants and changed data or evaluation rules need an independent attempt ledger.

## Questions to take into your own design

- Can a requested candidate that crashes remain visible in the attempt ledger?
- Are repeated seeds and manual candidates distinct from unique parameter settings?

## Why this score for a trading system

3/5: a precise transferable experiment-identity pattern; its counters cannot replace the complete research-attempt record.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
