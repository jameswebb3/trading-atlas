# TensorFlow Quant Finance — Random permutations with explicit seeds

**Decision question:** Can a permutation be reproduced without global RNG state?

| Field | Review |
| --- | --- |
| Upstream | [TensorFlow Quant Finance](https://github.com/google/tf-quant-finance) |
| Primary area | Research & Reproducibility |
| Source commit | [003229c11852349ce1f95efd6e4d8d8199da04e6](https://github.com/google/tf-quant-finance/commit/003229c11852349ce1f95efd6e4d8d8199da04e6) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The stateless shuffle generates random ordering keys from a two-part seed and gathers along the first axis. The README states that the project is no longer maintained. |

## Project overview

Archived TensorFlow library for quantitative-finance calculations and numerical methods. [Documentation](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/README.md).

## Mechanism worth inspecting

The stateless shuffle generates random ordering keys from a two-part seed and gathers along the first axis. Tests check permutations, repeated evaluation and independence from input values. [Source](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/tf_quant_finance/math/random_ops/stateless.py#L15-L52).

## Important limit

The README states that the project is no longer maintained. Reproducible shuffling does not make an IID permutation an appropriate null for autocorrelated trading observations. [Evidence 1](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/tf_quant_finance/math/random_ops/stateless.py#L15-L52). [Evidence 2](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/tf_quant_finance/math/random_ops/stateless_test.py#L28-L80). [Evidence 3](https://github.com/google/tf-quant-finance/blob/003229c11852349ce1f95efd6e4d8d8199da04e6/README.md#L1-L5).

## Questions to take into your own design

- Is the seed family recorded separately from the hypothesis family?
- Does the null preserve the temporal dependence your test needs?

## Why this score for a trading system

A useful reproducibility detail in an unmaintained, heavyweight stack; its shuffle is not a trading placebo design.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
