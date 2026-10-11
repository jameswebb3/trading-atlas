# joblib — a file path is not the contents of that file

**Decision question:** What inputs make a cached research result valid?

| Field | Review |
| --- | --- |
| Upstream | [joblib](https://github.com/joblib/joblib) |
| Primary area | Research & Reproducibility |
| Source commit | [f3f61b27b50f4ed32fadb439f573d00d7ef07cb0](https://github.com/joblib/joblib/commit/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | An inspectable caching reference with a clear dependency boundary. Function arguments determine identity; external data at the same filename needs content or version evidence to prevent stale research results. |

## Project overview

joblib Memory persists function results and reuses them for the same hashed arguments. [Project documentation](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/doc/user_guide/memory.rst#L18-L24).

## Mechanism worth inspecting

The cache key hashes filtered function arguments; named ignored parameters are excluded. A cache-validation callback can invalidate a present entry using its metadata. [Argument key](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/joblib/memory.py#L657-L662); [validation hook](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/joblib/memory.py#L466-L492).

## Important limit

Passing an unchanged filename does not make changed external file bytes part of the key. Global state, ignored parameters and unrecorded dependencies can also escape it. The documentation warns that persisted results load through pickle and require trusted cache storage. [Argument omission](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/joblib/memory.py#L380-L382); [storage warning](https://github.com/joblib/joblib/blob/f3f61b27b50f4ed32fadb439f573d00d7ef07cb0/doc/user_guide/memory.rst#L63-L69).

## Questions to take into your own design

- Does the key include dataset content/version, feature code, target and split identity?
- Can a data file change at the same path without forcing a cache miss?

## Why this score for a trading system

3/5: a concrete cache-dependency reference; research validity depends on explicit external inputs and trusted persistence, not memoization alone.

**Scope of this review:** Memory argument hashing and validation hook; no execution of cached objects or upstream examples.
