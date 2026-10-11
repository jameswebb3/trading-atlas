# AutoHedge — Is a named risk agent an enforceable trading control

**Decision question:** Is a named risk agent an enforceable trading control?

| Field | Review |
| --- | --- |
| Upstream | [AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) |
| Primary area | Agents & Decision Systems |
| Source commit | [c549c7950da112286e76725d49f6a25de8fa99bd](https://github.com/The-Swarm-Corporation/AutoHedge/commit/c549c7950da112286e76725d49f6a25de8fa99bd) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/The-Swarm-Corporation/AutoHedge/blob/c549c7950da112286e76725d49f6a25de8fa99bd/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | The inspected implementation is primarily a prompted agent conversation. It offers little new engineering value for trading risk controls; inspect enforceable limits and execution evidence before crediting the hedge-fund framing. |

## Project overview

A trading-themed multi-agent application with director, quantitative, risk and execution roles. [Project documentation](https://github.com/The-Swarm-Corporation/AutoHedge/blob/c549c7950da112286e76725d49f6a25de8fa99bd/README.md).

## Mechanism worth inspecting

The [worker definitions](https://github.com/The-Swarm-Corporation/AutoHedge/blob/c549c7950da112286e76725d49f6a25de8fa99bd/autohedge/workers.py#L35-L68) request risk assessments and proposed orders as string outputs. The [main cycle](https://github.com/The-Swarm-Corporation/AutoHedge/blob/c549c7950da112286e76725d49f6a25de8fa99bd/autohedge/main.py#L33-L63) delegates a task to the director and returns conversation messages.

## Important limit

The inspected cycle does not independently enforce numeric exposure limits, order authorization or verified execution evidence. Role names and generated risk prose do not establish those controls.

## Questions to take into your own design

- Is a named risk agent an enforceable trading control?
- Which independent calculation rejects an oversized proposed order before execution?

## Why this score for a trading system

1/5: trading terminology is visible, but the reviewed core supplies no independently enforced risk-control mechanism.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
