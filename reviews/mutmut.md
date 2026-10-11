# mutmut: A passing test suite can miss an inverted decision

**Decision question:** Would tests catch a changed comparison or branch in a risk gate?

| Field | Review |
| --- | --- |
| Upstream | [boxed/mutmut](https://github.com/boxed/mutmut) |
| Primary area | Testing & Verification |
| Source commit | [14a7230049a5c8abd90c2bb0f7438e30da6471f5](https://github.com/boxed/mutmut/commit/14a7230049a5c8abd90c2bb0f7438e30da6471f5) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/boxed/mutmut/blob/14a7230049a5c8abd90c2bb0f7438e30da6471f5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Generates small code mutations such as operator swaps, assignment replacement, and ternary branch forcing. A surviving mutant reveals a test gap or equivalent behavior; mutation score is not a safety certificate. |

## Mechanism worth inspecting

The mutator changes comparisons and arithmetic operators, can replace an assignment with None, and forces both ternary arms by modifying its condition. These are concrete adversarial changes for a fail-closed gate or PnL rule.

**Source trail:** [project overview](https://github.com/boxed/mutmut/blob/14a7230049a5c8abd90c2bb0f7438e30da6471f5/README.rst) · [documentation](https://github.com/boxed/mutmut/blob/14a7230049a5c8abd90c2bb0f7438e30da6471f5/README.rst#L1-L36) · [implementation](https://github.com/boxed/mutmut/blob/14a7230049a5c8abd90c2bb0f7438e30da6471f5/src/mutmut/mutation/mutators.py#L210-L265).

## Important limit

Some mutants are behaviorally equivalent or irrelevant to production paths. Running a broad mutation campaign can be expensive; only high-risk functions should be targeted.

## Questions to take into your own design

- Would changing a > to >= alter a test outcome at the boundary?
- Are surviving mutants investigated individually rather than hidden in a score?

## Why this score for a trading system

Mutation testing can probe a few high-risk trading gates, but broad mutation scores are costly and can include equivalent cases.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
