# A simulation seed needs a contract for every random component

**Decision question:** Does a seeded simulation reproduce all paths or only one source of noise?

| Field | Review |
| --- | --- |
| Upstream | [RustQuant](https://github.com/avhz/RustQuant) |
| Primary area | Signals & Models |
| Source commit | [44c0250c52597f7ffd171bec1843c9da9054743a](https://github.com/avhz/RustQuant/commit/44c0250c52597f7ffd171bec1843c9da9054743a) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT OR Apache-2.0](https://github.com/avhz/RustQuant/blob/44c0250c52597f7ffd171bec1843c9da9054743a/LICENSE-MIT.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | RustQuant seeds the normal-noise generator per path using base_seed plus path index in both serial and parallel modes. Its jump counts are sampled separately before the path loop. A reproducibility contract should name every random component, rather than assume one configured seed governs all of them. |

## Mechanism worth inspecting

The [overview](https://github.com/avhz/RustQuant/blob/44c0250c52597f7ffd171bec1843c9da9054743a/README.md#L54-L61) lists stochastic models and numerical tools; the [stochastics guide](https://github.com/avhz/RustQuant/blob/44c0250c52597f7ffd171bec1843c9da9054743a/book/src/Modules/stochastics.md#L1-L11) points to process examples. The [simulation source](https://github.com/avhz/RustQuant/blob/44c0250c52597f7ffd171bec1843c9da9054743a/crates/RustQuant_stochastics/src/simulation.rs#L28-L45) samples jump counts once, while the [path loops](https://github.com/avhz/RustQuant/blob/44c0250c52597f7ffd171bec1843c9da9054743a/crates/RustQuant_stochastics/src/simulation.rs#L142-L159) seed the dynamic normal generator by path index.

## Important limit

We did not establish independence of jump paths or complete seed determinism across every supported scheme. Synthetic price paths do not validate an alpha model, exchange execution, or realistic tail behavior.

## Questions to take into your own design

- Which stochastic components actually consume the supplied seed?
- Are parallel and serial paths compared with identical model and numerical settings?

## Why this score for a trading system

2/5: Seed-scope auditing is a useful numerical research caution, but these stochastic models are indirect references for a live trading system.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
