# A cache hit is not proof that an external market dataset stayed unchanged

**Decision question:** Which changes can invalidate a cached research step?

| Field | Review |
| --- | --- |
| Upstream | [ZenML](https://github.com/zenml-io/zenml) |
| Primary area | Research & Reproducibility |
| Source commit | [cc064f1005e444fade353aa521bbce8988a45874](https://github.com/zenml-io/zenml/commit/cc064f1005e444fade353aa521bbce8988a45874) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/zenml-io/zenml/blob/cc064f1005e444fade353aa521bbce8988a45874/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | ZenML can hash artifact content, IDs, parameters, and declared files into a cache key; its policy can also ignore inputs. The guide warns that filesystem and external API changes are not automatically detected. A trading pipeline must explicitly bind mutable sources to the cache contract. |

## Mechanism worth inspecting

The [overview](https://github.com/zenml-io/zenml/blob/cc064f1005e444fade353aa521bbce8988a45874/README.md#L49-L57) describes tracked pipeline steps. The [caching guide](https://github.com/zenml-io/zenml/blob/cc064f1005e444fade353aa521bbce8988a45874/docs/book/user-guide/starter-guide/cache-previous-executions.md#L21-L36) identifies external-input limits. The [cache builder](https://github.com/zenml-io/zenml/blob/cc064f1005e444fade353aa521bbce8988a45874/src/zenml/orchestrators/cache_utils.py#L107-L121) honors ignored inputs and configured artifact identity, and [file dependencies](https://github.com/zenml-io/zenml/blob/cc064f1005e444fade353aa521bbce8988a45874/src/zenml/orchestrators/cache_utils.py#L154-L188) hash declared files.

## Important limit

A corrected feed at the same path or API endpoint can remain invisible to a cache that only sees unchanged parameters. The usefulness is the explicit dependency policy, not a blanket claim of reproducibility.

## Questions to take into your own design

- Does every cached step declare the data vintage that can alter its result?
- Can ignored inputs or undeclared external calls change a reported metric?

## Why this score for a trading system

3/5: Cache invalidation tied to explicit input identity is a strong transferable research pattern, with hidden dependencies left visible.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
