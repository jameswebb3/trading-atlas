# Hypothesis GU Funcs — Compatible shapes need shared dimension identities

**Decision question:** Can random matrices respect a multi-input numerical signature?

| Field | Review |
| --- | --- |
| Upstream | [Hypothesis GU Funcs](https://github.com/uber/hypothesis-gufunc) |
| Primary area | Testing & Verification |
| Source commit | [65aaf717b9b57f3aa6379a836fe28dfc9b4f671b](https://github.com/uber/hypothesis-gufunc/commit/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The generator assigns one drawn size to each named dimension, then substitutes that mapping into every argument shape. Shape compatibility does not establish finite values, economic units or asset/time alignment. |

## Project overview

Experimental Hypothesis strategies for NumPy generalized-ufunc-compatible argument shapes. [Documentation](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/README.rst).

## Mechanism worth inspecting

The generator assigns one drawn size to each named dimension, then substitutes that mapping into every argument shape. Numeric dimensions remain fixed constants. [Source](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/hypothesis_gufunc/gufunc.py#L174-L209).

## Important limit

Shape compatibility does not establish finite values, economic units or asset/time alignment. The implementation uses private NumPy and Hypothesis APIs, increasing compatibility risk. [Evidence 1](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/hypothesis_gufunc/gufunc.py#L174-L209). [Evidence 2](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/hypothesis_gufunc/gufunc.py#L23-L27). [Evidence 3](https://github.com/uber/hypothesis-gufunc/blob/65aaf717b9b57f3aa6379a836fe28dfc9b4f671b/README.rst#L8-L14).

## Questions to take into your own design

- Are shared dimensions drawn once across all inputs?
- Does the numerical oracle check labels, units and nonfinite values as well as shape?

## Why this score for a trading system

A narrow numerical-generator pattern in an experimental package; a few local shape fixtures are preferable to another compatibility-sensitive dependency.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
