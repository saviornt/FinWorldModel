---
type: lit-note
title: "Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing"
authors: [Linsen Zhu, Mengqing Cai]
year: 2026
venue: arXiv (cs.AI)
source_url: https://arxiv.org/abs/2609.04917
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ1.1, RQ1.2, RQ3.1, RQ4.6]
family: [evaluation]
evidence: Weak
score: 0
tags: [lit-note, family/evaluation, review]
---
# AI in Equity and Crypto Markets: the Limits of Automated Investing (Zhu, 2026)

**Basis:** full text via alphaXiv (Abstract, §1–3, §4.1–4.2, §8, §9.7, §10, references). Literature cutoff 31 August 2026.

**Takeaway:** A critical (not systematic) review concluding that no general AI architecture has been shown to deliver persistent, cross-regime, capacity-aware net alpha; progress is real but mostly upstream of profit.

## Problem
Whether technical progress in ML, TSFMs, LLMs, RL and agents translates into net investment profit (§1).

## Data and period
Review of public research to 31 August 2026 across equities, ETFs, crypto spot, perpetuals and on-chain markets (Abstract, §2.1). No new data.

## Method
"Alpha-translation chain": point-in-time information → stable signal → feasible positions → executable orders → risk-adjusted net returns; evaluation-design archetypes CAP, TASK, OOS, GROSS, NET, PROSP, LIVE, EXT (§3, Table 1).

## Baselines and validation
Not applicable (review). The authors state it is not a systematic review and has no formal risk-of-bias scores (§2.1).

## Results (with page or section references)
- "Out of sample" is not the same as point-in-time; the condition is that decision-time information excludes later-only information, for features, membership, preprocessing and model parameters (§3, p. 7).
- Cites Zhang et al. (2025): removing look-ahead alignment erased a published monthly ML alpha; RFS issued an expression of concern (§8.2, p. 20).
- Cites Lopez-Lira et al. (2026): LLMs recall pretraining-period financial facts that look like forecasts (§1, §8.2).
- Cites Jensen et al. (2026): cost-unaware ML favours fleeting, low-capacity signals; cost-aware learning changes the frontier (§3, §4.2).
- Affirmative record: Gu et al. (2020), Chen et al. (2024) for nonlinear equity models; Lopez-Lira and Tang (2026) post-cutoff text; Kelly et al. (2026) point-in-time LLMs (§8.1).
- Generative AI assisted drafting; authors state they verified sources (Declaration, p. 26).

## Limits and risks to validity
_My assessment:_ a review: use it to find primary studies, not as evidence itself. Claims above must be checked in the primary papers before RP1/RP3 rely on them.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| All checks | N/A | Review with no empirical test; scored Weak as proof by assumption (see RP1 Assumptions) |

## Quotes worth keeping (each under 15 words, with page)
- "Technical capability, however, is not evidence of investment profitability." (Abstract, p. 1)
