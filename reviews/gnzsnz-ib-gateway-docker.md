# IB Gateway Docker — Separate process modes and shutdown state

**Decision question:** Can live and paper processes share startup assumptions?

| Field | Review |
| --- | --- |
| Upstream | [IB Gateway Docker](https://github.com/gnzsnz/ib-gateway-docker) |
| Primary area | Operations & Observability |
| Source commit | [8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10](https://github.com/gnzsnz/ib-gateway-docker/commit/8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/gnzsnz/ib-gateway-docker/blob/8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The startup script explicitly selects single or dual trading modes, supplies distinct settings for the two gateway processes and traps shutdown to terminate children. Process startup and an open port do not prove that authentication, account identity and API readiness are correct. |

## Project overview

Container packaging and startup scripts for Interactive Brokers Gateway and its automation controller. [Documentation](https://github.com/gnzsnz/ib-gateway-docker/blob/8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10/README.md).

## Mechanism worth inspecting

The startup script explicitly selects single or dual trading modes, supplies distinct settings for the two gateway processes and traps shutdown to terminate children. [Source](https://github.com/gnzsnz/ib-gateway-docker/blob/8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10/image-files/scripts/run.sh#L1-L150).

## Important limit

Process startup and an open port do not prove that authentication, account identity and API readiness are correct. Broker software and credentials remain external prerequisites. [Evidence 1](https://github.com/gnzsnz/ib-gateway-docker/blob/8a22deaa6cab86f9ad5c86ff4f0d6efbef718f10/image-files/scripts/run.sh#L1-L150).

## Questions to take into your own design

- Are mode, account identity and persistent state bound together?
- Does readiness require account evidence rather than only a listening socket?

## Why this score for a trading system

Portable process-lifecycle patterns, but the broker container is outside the trading venues assessed here.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
