---
type: lit-note
title: 'Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China'
authors:
- Hiroto Fukada
- Takayuki Mizuno
year: 2026
venue: arXiv (cs.SI)
source_url: https://arxiv.org/abs/2605.27845
doi: 10.1109/CIFEr67845.2026.11692384
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.8
- RQ3.7
family:
- data-sources
evidence: Weak
score: 4
tags:
- lit-note
- family/data-sources
---
# Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China (Hiroto Fukada et al., 2026)

**Takeaway:** An LLM reading web-search snippets found 7.2 times more firms and 9.3 times more supplier-customer links among Chinese listed firms than the disclosure-based CSMAR database, which caps at five suppliers and five customers per firm; precision was not measured.

## Problem
Whether web evidence can fill gaps in disclosure-based supply-chain databases.

## Data and period
130,685 Chinese firms (4,509 listed, 126,176 large unlisted) as of 2024; Google snippets via Serper; CSMAR as benchmark.

## Method
Snippets per firm from five query templates; Qwen3-Next-80B extracts relations as JSON; source-domain credibility tiers; entity resolution with Wikidata and Orbis aliases.

## Baselines and validation
CSMAR disclosure network; full-text extraction on 100 firms.

## Results (with page or section references)
- Listed subset: 7.2x firms, 9.3x links vs CSMAR (sec. V.B).
- CSMAR degree truncates beyond 10 (top-five disclosure rule) (Fig. 4).
- Full text finds 19.8x more relations than snippets at 251x the tokens (Table I).
- Keeping only higher-credibility sources removes 55% of edges (Table III).

## Limits and risks to validity
No ground truth or precision estimate; single country and date (no time dimension); LLM extraction may hallucinate links; web visibility bias toward consumer-facing firms.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Data construction |
| Baselines | 1 | CSMAR benchmark |
| Point-in-time and leakage controls | N/A | – |
| Costs and realism | N/A | – |
| Sample breadth | 1 | One country, one date |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code or data release found |
| **Total** | **4/14** | 2 of 8 on applicable checks, scaled (3.5) |

## Quotes worth keeping (each under 15 words, with page)
- "absence from the graph should not be interpreted as absence of a real relationship" (sec. VI.B; 14 words)
