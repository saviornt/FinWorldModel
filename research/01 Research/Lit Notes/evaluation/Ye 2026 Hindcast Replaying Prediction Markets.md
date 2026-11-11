---
type: lit-note
title: "HINDCAST: Replaying Prediction Markets to Evaluate LLM Forecasters"
authors: [Xiao Ye, Jacob Dineen, Evan Zhu, Shijie Lu, Kevin Song, Ben Zhou]
year: 2026
venue: arXiv (cs.CL) 2607.14051
source_url: https://arxiv.org/abs/2607.14051
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.5]
family: [evaluation]
evidence: Weak
score: 9
tags: [lit-note, family/evaluation, look-ahead, hindsight-free-evaluation]
---
# HINDCAST (Ye et al., 2026)

**Basis:** Full text (pp. 1–5, 8–10, 14) via the alphaXiv PDF reader, read 2026-11-08. Not financial returns; prediction markets.

**Takeaway:** Backtests of forecasters leak the answer through two channels — retrieval of post-event text and training data that now contains the event — and a replay against an immutable archive with a per-event cutoff t₀, scored against both the outcome and the market price at t₀, closes the retrieval channel; under that control, retrieval still lowered Brier for 8 of 9 models but hurt where the archive carried only speculation.

## Problem
Evaluating forecasts on resolved questions grades recall rather than foresight unless the information available at the forecast time is pinned (§1).

## Data and period
7,913 binary Polymarket markets narrowed to 216 (106 YES, 110 NO) with strong pre-event coverage; frozen Pushshift Reddit archive of 20 subreddits, Jan 2024–Jan 2026 (≈18.3M documents) (§3.1, §4.1).

## Method
Every retrieval call carries a strict `created_at < t₀` row-level predicate plus monthly partition guards; t₀ pinned to the day before each market closes; zero-shot baseline vs retrieval agent across 9 open-weight models, 5 runs each; scored by accuracy, Brier and distance to the market-implied probability at t₀ (§3.3, §4.2, §5).

## Baselines and validation
Zero-shot model (parametric memory floor) and the market price at t₀ (human forecast from the same information) (§1, Fig. 2).

## Results (with page or section references)
- Retrieval lowers Brier on eight of nine models, by up to 23% (§8).
- Net per-topic effect of retrieval: Sports +16, Awards +12, Trading +7; Entertainment −31, Other −10 (Fig. 6, p. 8).
- Event-set construction matters: 83% of resolved markets are NO, so outcomes were rebalanced to stop a constant guess from scoring well (§4.1).
- Median gap between t₀ and close only 23 days, limiting long-horizon conclusions (Limitations, p. 9).

## Limits and risks to validity
_My assessment:_ closes the retrieval channel only; the parametric channel is handled by re-running on markets that resolve after each model's release, but most of the 216 markets predate the tested models' training cutoffs, so the rubric's LLM-memorisation cap applies. Its value for RQ4.5 is the protocol: immutable archive, per-event cutoff enforced in the data layer, matched-time market benchmark, and balancing of event outcomes.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Replay at a pinned t₀ per market |
| Baselines | 2 | Zero-shot model and matched-time market price |
| Point-in-time and leakage controls | 2 | Strict cutoff predicate, immutable snapshot |
| Costs and realism | N/A |  |
| Sample breadth | 1 | 216 markets, two years |
| Statistical testing | 1 | Five runs with spread; no formal tests |
| Reproducibility | 1 | Pipeline and identifiers released; raw text not |
| **Total** | 8/12 → 9/14 → **capped Weak** | Pre-cutoff events for parametric memory |

## Quotes worth keeping (each under 15 words, with page)
- "the test grades recall while claiming to grade foresight" (p. 1)
