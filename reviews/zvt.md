# ZVT: make provider and time scope visible in feature reads

**Decision question:** Can a rolling feature query accidentally read beyond its requested end time?

| Field | Review |
| --- | --- |
| Upstream | [ZVT](https://github.com/zvtvz/zvt) |
| Primary area | Signals & Models |
| Source commit | [8509990e6608750d0c08fa748682cc997d2813cc](https://github.com/zvtvz/zvt/commit/8509990e6608750d0c08fa748682cc997d2813cc) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/zvtvz/zvt/blob/8509990e6608750d0c08fa748682cc997d2813cc/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Organizes market entities, providers, schemas, and readers in a quantitative-research framework. The main reader exposes provider and time bounds, while its separate window loader reveals why helper queries must carry the same cutoff. |

## Project overview

A market research framework models tradable entities and provider-specific data contracts. [Project documentation](https://github.com/zvtvz/zvt/blob/8509990e6608750d0c08fa748682cc997d2813cc/docs/source/data/data_concepts.rst#L8-L13).

## Mechanism worth inspecting

The [main reader](https://github.com/zvtvz/zvt/blob/8509990e6608750d0c08fa748682cc997d2813cc/src/zvt/contract/reader.py#L132-L162) passes provider, entity, start/end timestamps, and column selection to queries. Its [window helper](https://github.com/zvtvz/zvt/blob/8509990e6608750d0c08fa748682cc997d2813cc/src/zvt/contract/reader.py#L113-L130) instead requests descending timestamps with a row limit and no end bound.

## Important limit

A latest-row helper needs an explicit as-of constraint before serving historical features. The [README](https://github.com/zvtvz/zvt/blob/8509990e6608750d0c08fa748682cc997d2813cc/README.md#L15-L19) also warns that backward compatibility and continued maintenance of individual components are not guaranteed.

## Questions to take into your own design

- Does every helper query inherit the caller's as-of time?
- Are provider identity and dataset version carried into each resulting feature?

## Why this score for a trading system

2/5: a useful reader-contract inspection, with an unbounded window helper and explicit compatibility uncertainty.

**Scope of this review:** README, data concepts documentation, reader source.
