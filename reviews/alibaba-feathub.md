# FeatHub — Window boundaries and empty outputs

**Decision question:** Do local windows include their end timestamp?

| Field | Review |
| --- | --- |
| Upstream | [FeatHub](https://github.com/alibaba/feathub) |
| Primary area | Data Quality & Lineage |
| Source commit | [15d63821262fe1cd1e2e665144e39af1bc8e4130](https://github.com/alibaba/feathub/commit/15d63821262fe1cd1e2e665144e39af1bc8e4130) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/alibaba/feathub/blob/15d63821262fe1cd1e2e665144e39af1bc8e4130/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The local sliding-window loop advances the right bound strictly below window_end and the left bound below window_end minus window_size. The inspected interval is [end-size,end). |

## Project overview

Feature store with declarative transformations and local, streaming and batch processing interfaces. [Documentation](https://github.com/alibaba/feathub/blob/15d63821262fe1cd1e2e665144e39af1bc8e4130/README.md).

## Mechanism worth inspecting

The local sliding-window loop advances the right bound strictly below window_end and the left bound below window_end minus window_size. Its tests distinguish empty-window output and unchanged-output suppression policies. [Source](https://github.com/alibaba/feathub/blob/15d63821262fe1cd1e2e665144e39af1bc8e4130/python/feathub/processors/local/sliding_window_utils.py#L234-L295).

## Important limit

The inspected interval is [end-size,end). A feature value alone cannot reveal whether an empty or unchanged window was emitted or skipped; cross-engine parity was not established here. [Evidence 1](https://github.com/alibaba/feathub/blob/15d63821262fe1cd1e2e665144e39af1bc8e4130/python/feathub/processors/local/sliding_window_utils.py#L234-L295). [Evidence 2](https://github.com/alibaba/feathub/blob/15d63821262fe1cd1e2e665144e39af1bc8e4130/python/feathub/feature_views/transforms/tests/test_sliding_window_transform.py#L67-L119).

## Questions to take into your own design

- Is the endpoint convention stored with each feature definition?
- Can an unchanged value be distinguished from a missing observation?

## Why this score for a trading system

Transferable temporal-feature contracts with readable implementation and policy tests; deploying another feature store is a separate decision.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
