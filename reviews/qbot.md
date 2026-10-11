# Qbot: inspect a rolling SSA signal rather than a full-series fit

**Decision question:** How does a singular-spectrum signal choose its input window at each bar?

| Field | Review |
| --- | --- |
| Upstream | [Qbot](https://github.com/UFund-Me/Qbot) |
| Primary area | Signals & Models |
| Source commit | [f0425ae4ae8bd02b79656b8f7039f4cd6874095e](https://github.com/UFund-Me/Qbot/commit/f0425ae4ae8bd02b79656b8f7039f4cd6874095e) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT (root declaration)](https://github.com/UFund-Me/Qbot/blob/f0425ae4ae8bd02b79656b8f7039f4cd6874095e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Collects quantitative-trading tools and strategy examples. Its inspected SSA indicator builds a trailing window, reconstructs the dominant singular component, and emits only the final value, providing a concrete example to compare against full-series smoothing. |

## Project overview

A broad quantitative-trading collection includes data, strategy, backtesting, and broker-interface examples. [Project documentation](https://github.com/UFund-Me/Qbot/blob/f0425ae4ae8bd02b79656b8f7039f4cd6874095e/README.md#L106-L110).

## Mechanism worth inspecting

The [SSA indicator](https://github.com/UFund-Me/Qbot/blob/f0425ae4ae8bd02b79656b8f7039f4cd6874095e/qbot/strategies/ssa_strategy_bt.py#L11-L68) sets a minimum history, constructs a trajectory matrix, keeps the dominant singular component, and evaluates the latest reconstructed value from a trailing window. [Strategy steps](https://github.com/UFund-Me/Qbot/blob/f0425ae4ae8bd02b79656b8f7039f4cd6874095e/qbot/strategies/ssa_strategy_bt.py#L138-L156) compare that value with the current close.

## Important limit

The [order callback](https://github.com/UFund-Me/Qbot/blob/f0425ae4ae8bd02b79656b8f7039f4cd6874095e/qbot/strategies/ssa_strategy_bt.py#L101-L129) is a small example, not an audited production order lifecycle. The repository bundles extensive material and integrations; a root MIT declaration does not establish the license of every embedded component. The strategy taxonomy document is attributed to an external article.

## Questions to take into your own design

- Does perturbing future input leave every earlier indicator output unchanged?
- Are smoother quality and net trading performance evaluated as separate questions?

## Why this score for a trading system

2/5: a readable rolling signal mechanism in a heterogeneous collection; no verified alpha, execution realism, or comprehensive component licensing.

**Scope of this review:** README, strategy taxonomy documentation, SSA indicator and example strategy source.
