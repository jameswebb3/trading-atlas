# hmmlearn — smoothed states are retrospective

**Decision question:** Can a state probability computed on a complete path be used at an earlier trading decision?

| Field | Review |
| --- | --- |
| Upstream | [hmmlearn](https://github.com/hmmlearn/hmmlearn) |
| Primary area | Signals & Models |
| Source commit | [e01a10e99df1042e4c1e6b7c822fd292dd37502f](https://github.com/hmmlearn/hmmlearn/commit/e01a10e99df1042e4c1e6b7c822fd292dd37502f) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/hmmlearn/hmmlearn/blob/e01a10e99df1042e4c1e6b7c822fd292dd37502f/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | An explicit reference for the difference between smoothed and live state probabilities. Full-sequence posteriors use later observations; point-in-time features need a causal inference horizon and a prior fit cutoff. |

## Project overview

hmmlearn implements Hidden Markov Models and sequence inference; its README declares limited-maintenance mode. [Project documentation](https://github.com/hmmlearn/hmmlearn/blob/e01a10e99df1042e4c1e6b7c822fd292dd37502f/README.rst#L23-L29).

## Mechanism worth inspecting

The log scoring path runs both forward and backward passes. Posterior probabilities combine their lattices, so the probability of an earlier state uses evidence from later observations in the supplied sequence. [Forward/backward path](https://github.com/hmmlearn/hmmlearn/blob/e01a10e99df1042e4c1e6b7c822fd292dd37502f/src/hmmlearn/base.py#L253-L270); [posterior calculation](https://github.com/hmmlearn/hmmlearn/blob/e01a10e99df1042e4c1e6b7c822fd292dd37502f/src/hmmlearn/base.py#L513-L521).

## Important limit

Smoothed posteriors are useful for retrospective analysis, but they are not filtered live probabilities. Full-path decoding and refitting on future data introduce separate timing concerns. A prefix-only calculation still needs parameters fitted before the decision. [Sequence-inference documentation](https://github.com/hmmlearn/hmmlearn/blob/e01a10e99df1042e4c1e6b7c822fd292dd37502f/doc/source/tutorial.rst#L144-L155).

## Questions to take into your own design

- Does the state stored at time t remain unchanged when observations after t are perturbed?
- Are both inference horizon and parameter-fit cutoff stored with each state value?

## Why this score for a trading system

3/5: an important, inspectable distinction between retrospective and causal state inference; no evidence here supports a profitable regime strategy.

**Scope of this review:** Posterior smoothing and documented sequence inference; no regime-performance study or runtime test.
