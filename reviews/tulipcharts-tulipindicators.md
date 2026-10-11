# Tulip Indicators — Does the first output of every indicator correspond to the first input bar

**Decision question:** Does the first output of every indicator correspond to the first input bar?

| Field | Review |
| --- | --- |
| Upstream | [Tulip Indicators](https://github.com/TulipCharts/tulipindicators) |
| Primary area | Signals & Models |
| Source commit | [be18abb13e075ba866898dcc7cb52399603302a6](https://github.com/TulipCharts/tulipindicators/commit/be18abb13e075ba866898dcc7cb52399603302a6) |
| Reviewed | 2026-09-27 |
| Declared license | [LGPL-3.0-or-later](https://github.com/TulipCharts/tulipindicators/blob/be18abb13e075ba866898dcc7cb52399603302a6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Exposes per-function output offsets and differing warm-up conventions. Useful for catching timestamp shifts when a compact output array is joined back to input bars. |

## Project overview

An ANSI C technical-analysis library with a compact function API and language bindings. [Project documentation](https://github.com/TulipCharts/tulipindicators/blob/be18abb13e075ba866898dcc7cb52399603302a6/README.md#L7-L19).

## Mechanism worth inspecting

SMA advertises a start offset of period minus one and emits only the usable suffix. EMA instead advertises offset zero, seeds from the first input and emits every input position. [SMA alignment](https://github.com/TulipCharts/tulipindicators/blob/be18abb13e075ba866898dcc7cb52399603302a6/indicators/sma.c#L29-L59); [EMA initialization](https://github.com/TulipCharts/tulipindicators/blob/be18abb13e075ba866898dcc7cb52399603302a6/indicators/ema.c#L28-L54).

## Important limit

The array functions do not attach timestamps. A consumer must align each output using that function's start offset; EMA initialization also differs from the SMA-seeded implementation inspected in TA-Lib Core.

## Questions to take into your own design

- Is the first output timestamp derived from the function's actual start offset?
- Do comparisons use the same warm-up and initialization convention?

## Why this score for a trading system

2/5: a direct alignment caution with limited incremental value beyond existing feature libraries.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
