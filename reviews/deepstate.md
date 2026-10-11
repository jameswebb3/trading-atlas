# A saved failure corpus makes rare state bugs replayable

**Decision question:** Can a rare protocol failure be reproduced after the fuzzer finds it?

| Field | Review |
| --- | --- |
| Upstream | [DeepState](https://github.com/trailofbits/deepstate) |
| Primary area | Testing & Verification |
| Source commit | [e68b98e552ab7d59d369a26569562f74a13caa02](https://github.com/trailofbits/deepstate/commit/e68b98e552ab7d59d369a26569562f74a13caa02) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/trailofbits/deepstate/blob/e68b98e552ab7d59d369a26569562f74a13caa02/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | DeepState uses a common test harness across fuzzing and symbolic engines and organizes saved inputs into a replayable corpus. Its built-in fuzzer retains failures by default; passing inputs need an explicit option. The corpus discipline transfers to trading state machines, though the framework targets C and C++. |

## Mechanism worth inspecting

The [README](https://github.com/trailofbits/deepstate/blob/e68b98e552ab7d59d369a26569562f74a13caa02/README.md#L5-L6) describes a common harness across engines. The [fuzzing guide](https://github.com/trailofbits/deepstate/blob/e68b98e552ab7d59d369a26569562f74a13caa02/docs/fuzzing.md#L20-L32) says the built-in fuzzer saves failing or crashing tests by default and needs an option to save passing tests. The [fuzzer runner](https://github.com/trailofbits/deepstate/blob/e68b98e552ab7d59d369a26569562f74a13caa02/bin/deepstate/core/fuzz.py#L480-L507) manages seed, output, and crash directories.

## Important limit

A saved corpus only tests cases that are replayed against a meaningful oracle. Passing seeds can also matter for coverage regression, but storing them requires a policy for size and provenance.

## Questions to take into your own design

- Can every saved failure be replayed deterministically against a pinned build?
- Will accepted passing cases also be kept when they explore new protocol states?

## Why this score for a trading system

2/5: Corpus retention and replay are useful for rare order-state failures. The framework targets C/C++, and it does not provide trading event models, causal test cases, or assertions.

**Scope of this review:** We read the README, fuzzing guide, and fuzzer runner.
