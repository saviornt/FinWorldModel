---
type: lit-note
title: "Computational Reproducibility in Finance: Evidence from 1,000 Tests"
authors: [Christophe Pérignon, Olivier Akmansoy, Christophe Hurlin, Anna Dreber, Felix Holzmeister, Jürgen Huber, Magnus Johannesson, Michael Kirchler, Albert J. Menkveld, Michael Razen, Utz Weitzel]
year: 2024
venue: Review of Financial Studies 37(11), 3558–3593
source_url: https://papers.ssrn.com/abstract=4064172
doi: 10.1093/rfs/hhae029
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.7]
family: [evaluation]
evidence: Weak
score: 5
tags: [lit-note, family/evaluation, reproducibility, abstract-only]
---
# Computational Reproducibility in Finance (Pérignon et al., 2024)

**Basis:** Abstract only (SSRN 4064172 page, opened 2026-11-09 via page fetch). Full text not opened (journal paywalled). Scored Weak under the vault's abstract-only convention.

**Takeaway:** When 168 teams' code for six finance questions (1,000+ results) was rerun on the same raw data, it reproduced exactly the same results only 52% of the time; reproducibility rose with coding skill and effort, fell with technical and code complexity and for tail results, and researchers strongly overestimated how reproducible their own work was.

## Problem
How often finance results can be regenerated from the authors' own code and data (abstract).

## Data and period
Results submitted to the Finance Crowd Analysis Project (#fincap) by 168 teams on six research questions (abstract).

## Method
Re-execution of each team's code on the same raw data; regression of reproducibility on team and task characteristics (abstract).

## Baselines and validation
Not applicable (meta-research).

## Results (with page or section references)
- Exact reproduction 52% of the time (abstract).
- Higher with better coding skills and more effort; lower for more technical questions, more complex code and results in the tails (abstract).
- Neither seniority nor peer-review ratings related to reproducibility; strong overconfidence about own reproducibility (abstract).
- Guidelines for researchers and journal policies are given in the paper (not in the part read).

## Limits and risks to validity
_My assessment:_ abstract only; the failure causes (bugs, documentation, computation) are reported in a library abstract seen in search, not opened. The 52% figure is from the abstract and safe to cite.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Meta-research |
| Baselines | N/A | Meta-research |
| Point-in-time and leakage controls | N/A | Meta-research |
| Costs and realism | N/A | Meta-research |
| Sample breadth | 2 | 168 teams, 1,000+ results, six questions |
| Statistical testing | 1 | Determinant regressions (per abstract) |
| Reproducibility | N/A | Subject of the study |
| **Total** | 3/4 → 10 partial; recorded **Weak (5)**, abstract only | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept (abstract only).
