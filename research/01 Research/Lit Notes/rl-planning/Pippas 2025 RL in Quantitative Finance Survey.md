---
type: lit-note
title: "The Evolution of Reinforcement Learning in Quantitative Finance: A Survey"
authors: [Nikolaos Pippas, Elliot A. Ludvig, Cagatay Turkay]
year: 2025
venue: ACM Computing Surveys (submitted manuscript; arXiv v3)
source_url: https://arxiv.org/abs/2408.10932
doi: 10.1145/3733714
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ4.1]
family: [rl-planning]
evidence: Weak
score: 0
tags: [lit-note, family/rl-planning, review]
---
# RL in Quantitative Finance: A Survey of 167 Papers (Pippas, 2025)

**Basis:** arXiv v3 PDF read through alphaXiv excerpts (pp. 1, 24–25, 27, references). Sections 2–7 on RL components read only where they touched evaluation.

**Takeaway:** Across 167 RL-in-finance papers, RL agents "generally exceeded their respective benchmarks", but the authors flag why that is weak evidence: unequal information sets versus benchmarks, implausible Sharpe ratios (21.2 and 217.68) that point to same-bar look-ahead, survivorship-biased single-stock tests, little factor adjustment and a habit of treating RL as an engineering exercise.

## Problem
Map RL applications in quantitative finance (portfolio management, execution, market making, hedging, allocation) and critique methods (p. 1).

## Data and period
Literature review of 167 publications up to 2024–25.

## Method
Narrative survey organised by RL component (environment, reward, action) and application; no systematic quality scoring or meta-analysis.

## Baselines and validation
Not applicable (review).

## Results (with page or section references)
- RL agents generally beat the benchmarks chosen by their authors, across regions and asset classes (pp. 24–25).
- Comparisons are often unbalanced: RL uses richer inputs than the Markowitz benchmark it is compared to (p. 25).
- Sharpe ratios of 21.2 (Deng et al.) and 217.68 (Xu et al.) are cited as likely forward-looking bias from acting at the same bar's price (p. 25).
- Survivorship bias from testing on winners such as Apple; few studies control for known factors (p. 25).
- Strategic asset allocation and market timing with RL are under-explored (p. 24).

## Limits and risks to validity
_My assessment:_ publication bias means "RL usually beats benchmarks" is the expected pattern of a literature, not evidence; the survey's own critique is the useful part. Lead author is employed by HSBC Asset Management, which part-funded the work (p. 1).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| All checks | N/A | Review with no empirical test; scored Weak by the RP1 rule for reviews |

## Quotes worth keeping (each under 15 words, with page)
- "excessively high SR values warrant careful scrutiny" (p. 25)

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
