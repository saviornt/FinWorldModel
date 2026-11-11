---
type: lit-note
title: "Nonstandard Errors"
authors: [Albert J. Menkveld, Anna Dreber, Felix Holzmeister, Juergen Huber, Magnus Johannesson, Michael Kirchler, Sebastian Neusüß, Michael Razen, Utz Weitzel, et al.]
year: 2024
venue: Journal of Finance 79(3), 2339–2390
source_url: https://public.econ.duke.edu/~ap172/Menkveld_et_al_2024_Nonstandard%20Errors
doi: 10.1111/jofi.13337
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.7]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation, reproducibility, many-analysts]
---
# Nonstandard Errors (Menkveld et al., 2024)

**Basis:** Published version (open-access PDF copy), read 2026-11-09 through a summarising page fetch (first ~100,000 of 103,095 characters). Page numbers as reported by the fetch.

**Takeaway:** When 164 teams tested the same six hypotheses on the same 720 million EuroStoxx 50 futures trades, the spread of their estimates (the "nonstandard error") was about double the typical standard error; more reproducible and higher-rated work had smaller spread, peer feedback cut it by 47%, and most teams underestimated it.

## Problem
How much uncertainty comes from researchers' analysis choices (the evidence-generating process), on top of sampling error (abstract).

## Data and period
EuroStoxx 50 index futures trade records 2002–2018, 720 million trades; 164 teams; 34 peer evaluators (pp. 2343, 2348).

## Method
Many-analysts design: same data and hypotheses for every team; dispersion across teams measured by IQR; four rounds of peer feedback (pp. 2343–2346).

## Baselines and validation
Standard-error-implied dispersion as the benchmark for nonstandard errors (p. 2345).

## Results (with page or section references)
- Market-efficiency hypothesis: median SE 2.5% (SE-implied IQR ~3.4%) vs observed nonstandard error 6.7% (p. 2345).
- One-SD higher reproducibility → NSE 25.0% smaller; one-SD higher peer rating → 33.3% smaller (p. 2345).
- Four rounds of peer feedback reduced NSEs by 47.2%, though most single stages were not significant (pp. 2345, 2361–2362).
- "the vast majority of teams underestimate dispersion in estimates" (p. 2364).
- Suggests multiverse analysis to find which analysis forks drive dispersion; IQR rather than SD (pp. 2346, 2352).

## Limits and risks to validity
_My assessment:_ one dataset and market microstructure questions; numbers via summarising fetch. Strong design for its question; the lesson transfers: one analysis path understates uncertainty, so the project should vary its pipeline choices and report the spread.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Meta-research |
| Baselines | N/A | Meta-research |
| Point-in-time and leakage controls | N/A | Meta-research |
| Costs and realism | N/A | Meta-research |
| Sample breadth | 1 | One dataset, 164 teams |
| Statistical testing | 2 | Formal inference on dispersion and its determinants |
| Reproducibility | 1 | Data and team results described; code not checked |
| **Total** | 4/6 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the vast majority of teams underestimate dispersion in estimates" (p. 2364)
