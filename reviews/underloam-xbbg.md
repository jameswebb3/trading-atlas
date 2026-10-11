# xbbg — A failed schema lookup is not an empty schema

**Decision question:** What happens when request-schema discovery fails?

| Field | Review |
| --- | --- |
| Upstream | [xbbg](https://github.com/underloam/xbbg) |
| Primary area | Market Data & Ingestion |
| Source commit | [cb33260075f12138c80789b1438cf4994aae840f](https://github.com/underloam/xbbg/commit/cb33260075f12138c80789b1438cf4994aae840f) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/underloam/xbbg/blob/cb33260075f12138c80789b1438cf4994aae840f/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The asynchronous element lookup caches successful schema responses by service and operation. An empty result can mean either no elements or failed discovery. |

## Project overview

Bloomberg client with Python and Node interfaces backed by a shared Rust engine. [Documentation](https://github.com/underloam/xbbg/blob/cb33260075f12138c80789b1438cf4994aae840f/README.md).

## Mechanism worth inspecting

The asynchronous element lookup caches successful schema responses by service and operation. Its exception branch logs a debug message and returns an empty set. [Source](https://github.com/underloam/xbbg/blob/cb33260075f12138c80789b1438cf4994aae840f/py-xbbg/src/xbbg/blp.py#L1262-L1280).

## Important limit

An empty result can mean either no elements or failed discovery. This helper alone does not establish how every downstream request handles that ambiguity; Bloomberg access requires separate authorization. [Evidence 1](https://github.com/underloam/xbbg/blob/cb33260075f12138c80789b1438cf4994aae840f/py-xbbg/src/xbbg/blp.py#L1262-L1280). [Evidence 2](https://github.com/underloam/xbbg/blob/cb33260075f12138c80789b1438cf4994aae840f/README.md#L28-L28).

## Questions to take into your own design

- Can request admission distinguish empty schema from unavailable schema?
- Are cache entries scoped to the provider context that produced them?

## Why this score for a trading system

A specific data-admission fallback to inspect, with vendor-access constraints and downstream behavior outside this review.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
