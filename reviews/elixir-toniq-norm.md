# Norm — Field validation does not require field presence

**Decision question:** Does validating a map prove that every expected key exists?

| Field | Review |
| --- | --- |
| Upstream | [Norm](https://github.com/elixir-toniq/norm) |
| Primary area | Testing & Verification |
| Source commit | [0e5f68f1143ca0287d2795f13b27c6f886eaa5b7](https://github.com/elixir-toniq/norm/commit/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/elixir-toniq/norm/blob/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7/LICENSE.md) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The plain schema conformer iterates over keys present in the input and checks matching specs. This plain schema path does not itself require all declared keys or reject extra keys. |

## Project overview

Elixir library for structural data validation and generation using reusable predicates. [Documentation](https://github.com/elixir-toniq/norm/blob/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7/README.md).

## Mechanism worth inspecting

The plain schema conformer iterates over keys present in the input and checks matching specs. Keys without a spec pass through; generator construction uses the schema's declared keys. [Source](https://github.com/elixir-toniq/norm/blob/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7/lib/norm/core/schema.ex#L76-L103).

## Important limit

This plain schema path does not itself require all declared keys or reject extra keys. Generated complete maps can miss the malformed input cases that real data admission needs. [Evidence 1](https://github.com/elixir-toniq/norm/blob/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7/lib/norm/core/schema.ex#L76-L103). [Evidence 2](https://github.com/elixir-toniq/norm/blob/0e5f68f1143ca0287d2795f13b27c6f886eaa5b7/lib/norm/core/schema.ex#L110-L138).

## Questions to take into your own design

- Are required keys and unknown keys separate from value predicates?
- Does the negative corpus include omitted clock, unit and identity fields?

## Why this score for a trading system

A concrete validator/generator coverage asymmetry, with limited incremental value beyond existing typed data contracts.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
