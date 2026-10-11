# Polars — grouped as-of joins need an ordering contract

**Decision question:** Who validates ordering when an as-of join is grouped by instrument?

| Field | Review |
| --- | --- |
| Upstream | [Polars](https://github.com/pola-rs/polars) |
| Primary area | Data Quality & Lineage |
| Source commit | [750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717](https://github.com/pola-rs/polars/commit/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/pola-rs/polars/blob/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful grouped as-of reference with an explicit validation boundary. The documented sortedness checks differ by engine, so instrument-level order validation should be a separate ingestion invariant. |

## Project overview

Polars is a dataframe engine with lazy execution and time-aware as-of joins. [Project documentation](https://github.com/pola-rs/polars/blob/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717/py-polars/src/polars/lazyframe/frame.py#L5557-L5606).

## Mechanism worth inspecting

The lazy-frame API exposes strategy, tolerance, exact-match policy and sortedness checking, forwarding them into the native join. Its documentation explicitly distinguishes the ordering checks available to different engines. [Parameters](https://github.com/pola-rs/polars/blob/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717/py-polars/src/polars/lazyframe/frame.py#L5557-L5575); [native dispatch](https://github.com/pola-rs/polars/blob/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717/py-polars/src/polars/lazyframe/frame.py#L5927-L5956).

## Important limit

At this pin, the documented in-memory engine cannot check as-of sortedness with `by` groups; the streaming engine checks the rows it processes. `check_sortedness=True` is therefore not a universal proof that the complete instrument histories satisfy the application's order invariant. [Engine-specific limit](https://github.com/pola-rs/polars/blob/750bbaa9054c88cf3c3f2c0fcc0e2e5e3c2f8717/py-polars/src/polars/lazyframe/frame.py#L5673-L5677).

## Questions to take into your own design

- Does ingestion explicitly verify monotonic usable timestamps within each instrument?
- Can the same fixture detect a grouped out-of-order record across execution engines?

## Why this score for a trading system

3/5: a concrete grouped-join validation boundary; the useful pattern is independent order validation, not a blanket dataframe-engine recommendation.

**Scope of this review:** Lazy as-of API, dispatch and documented sortedness limits; native engine internals were not fully audited.
