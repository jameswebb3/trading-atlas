# Passivbot — What evidence permits restarting after a hard risk stop

**Decision question:** What evidence permits restarting after a hard risk stop?

| Field | Review |
| --- | --- |
| Upstream | [Passivbot](https://github.com/enarjord/passivbot) |
| Primary area | Portfolio & Risk |
| Source commit | [507dedc68ffee07da047a8b74bea61355625037e](https://github.com/enarjord/passivbot/commit/507dedc68ffee07da047a8b74bea61355625037e) |
| Reviewed | 2026-09-26 |
| Declared license | [Unlicense](https://github.com/enarjord/passivbot/blob/507dedc68ffee07da047a8b74bea61355625037e/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A useful perpetual-trading reference for hard-stop and restart policies. Its risk logic separates cooldown from permanent restart veto, with explicit limits around missing history and account transfers. |

## Project overview

Passivbot trades perpetual markets using a Python live layer and Rust backtesting and risk logic. This review concerns its equity-stop lifecycle, not its grid strategy. [Project documentation](https://github.com/enarjord/passivbot/blob/507dedc68ffee07da047a8b74bea61355625037e/docs/equity_hard_stop_loss_risks.md#L1-L23).

## Mechanism worth inspecting

A pure post-stop transition validates equity and thresholds, then returns a no-restart latch, cooldown deadline or halted state. Its contract puts proof of exchange history with the caller. [Transition](https://github.com/enarjord/passivbot/blob/507dedc68ffee07da047a8b74bea61355625037e/passivbot-rust/src/equity_hard_stop_loss.rs#L297-L383). A reconciliation test checks that flattened inventory does not reappear in later exposure. [Test read](https://github.com/enarjord/passivbot/blob/507dedc68ffee07da047a8b74bea61355625037e/tests/test_hsl_revised_reconciler.py#L105-L116).

## Important limit

The documented replay uses fills, positions, prices and current balance, without a separate authoritative transfer ledger. Deposits and configuration changes can reinterpret drawdown. An incomplete-history waiver weakens restart evidence. [Known risks](https://github.com/enarjord/passivbot/blob/507dedc68ffee07da047a8b74bea61355625037e/docs/equity_hard_stop_loss_risks.md#L37-L60).

## Questions to take into your own design

- What evidence permits restarting after a hard risk stop?
- How are transfers and incomplete fill history distinguished from strategy drawdown at restart?

## Why this score for a trading system

4/5: concrete risk-state transitions plus an inspected reconciliation test. Transfer accounting and history waivers remain consequential limits; no strategy profitability is inferred.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
