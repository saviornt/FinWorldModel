---
type: lit-note
title: "When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models"
authors: [Bolin Song, Surui Xiang]
year: 2026
venue: arXiv 2610.30564
source_url: https://arxiv.org/abs/2610.30564
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11, RQ1.12]
family: [novelty-detection]
evidence: Weak
score: 8
tags: [lit-note, family/novelty-detection, news-age]
---
# When News Gets Old: Portfolio Allocation with RL and LLMs (Song, 2026)

**Basis:** v1 (22 Oct 2026), full text via alphaXiv (pp. 1–8).

**Takeaway:** For ten US stocks (2023–2025), giving an RL or LLM portfolio policy the age of each filing-derived news signal, or zeroing signals older than eight weeks, changed decisions but not net returns in a way that survives uncertainty: all paired 95% intervals include zero, and RL on market data alone (19.07%/yr) beat every RL variant that used news.

## Problem
Should aging news signals be kept with timing information or filtered out?

## Data and period
10 DJIA stocks; 277 SEC 10-K/10-Q excerpts 2019–2025; weekly decisions; annual tests 2023, 2024, 2025 with expanding training folds (App. B, pp. 6–7).

## Method
GPT-4.1 mini extracts −1/0/+1 signals with verbatim evidence; Double DQN (10 seeds × 4 settings × 3 folds) or LLM policies choose among 57 portfolios; settings: news, news + age, news filtered at 8 weeks; delivery delays 0/1/4 weeks; 10 bp costs (pp. 2–3).

## Baselines and validation
Equal allocation, buy-and-hold, market-data-only RL and LLM; walk-forward annual folds; paired block-bootstrap intervals (App. A).

## Results (with page or section references)
- 4-week delay: RL news 17.81%, + age 18.02%, filtered 18.03%; RL market-only 19.07%; LLM filtered 18.43% vs news 16.02% (Table II, p. 3).
- Paired differences +0.21% [−3.73, 4.29] and +0.22% [−2.93, 3.44]; none of 36 annual contrasts excludes zero (Table III, App. A).
- Making reports 12 weeks older changed RL news+age choices in 52% of cases (Fig. 2, p. 4).
- At 30 bp costs RL news+age fell from 18.02% to 12.32% (p. 4).

## Limits and risks to validity
_My assessment:_ ten stocks, three years; GPT-4.1 mini reads 2023–24 filings before its training cutoff (memorisation not controlled; assets anonymised in the decision step only); 2024–25 had already been inspected (p. 6). Rubric cap applies. Useful as a negative result: timing features on news did not add net value.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding annual walk-forward |
| Baselines | 1 | Market-only, equal weight, buy-and-hold |
| Point-in-time and leakage controls | 1 | SEC acceptance timestamps; LLM cutoff not controlled |
| Costs and realism | 1 | Flat 10 bp + sensitivity |
| Sample breadth | 1 | 10 stocks, 3 years |
| Statistical testing | 1 | Block-bootstrap CIs, no multiple-testing correction |
| Reproducibility | 1 | Reproduction materials (prompts, requests) |
| **Total** | **8/14 → capped Weak** | Rubric cap: LLM on pre-cutoff events without memorisation control |

## Quotes worth keeping (each under 15 words, with page)
- "responding to news timing and improving investment performance are distinct outcomes" (p. 4)
