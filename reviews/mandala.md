# Mandala: cached results depend on the code actually called

**Decision question:** When is a past experiment result safe to reuse?

| Field | Review |
| --- | --- |
| Upstream | [Mandala](https://github.com/amakelov/mandala) |
| Primary area | Research & Reproducibility |
| Source commit | [f9b74695f5add8e3382eb984c1dfca605c7ef106](https://github.com/amakelov/mandala/commit/f9b74695f5add8e3382eb984c1dfca605c7ef106) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/amakelov/mandala/blob/f9b74695f5add8e3382eb984c1dfca605c7ef106/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Memoizes function calls and versions their observed code dependencies and inputs. The dependency guide says non-memoized helpers need explicit tracking for reliable versioning; a cache hit is only as sound as that dependency boundary. |

## Mechanism worth inspecting

The [overview](https://github.com/amakelov/mandala/blob/f9b74695f5add8e3382eb984c1dfca605c7ef106/README.md#L91-L108) makes a function call the persistence and versioning unit. The [versioning guide](https://github.com/amakelov/mandala/blob/f9b74695f5add8e3382eb984c1dfca605c7ef106/docs/docs/topics/04_versions.md#L5-L34) records dependencies actually reached during a call and compares content versions before reuse. The [versioner](https://github.com/amakelov/mandala/blob/f9b74695f5add8e3382eb984c1dfca605c7ef106/mandala/deps/versioner.py#L32-L42) hashes the content hashes of the dependency support set. This is more precise than treating an entire experiment as one undifferentiated cache key.

## Important limit

The [guide notes that non-memoized dependencies require explicit tracking](https://github.com/amakelov/mandala/blob/f9b74695f5add8e3382eb984c1dfca605c7ef106/docs/docs/topics/04_versions.md#L53-L58). External files, data vintages, and nondeterministic services also need explicit identities; code hashing alone cannot make their outputs reproducible.

## Questions to take into your own design

- Which exact function and data versions produced a stored result?
- Can a changed dependency invalidate only the affected computations?

## Why this score for a trading system

Per-call code dependency tracking is a concrete reproducibility pattern, with explicit decorator and global-tracking limitations.

**Scope of this review:** We read the pinned README, versioning guide, and dependency versioner. We did not execute memoized calls.
