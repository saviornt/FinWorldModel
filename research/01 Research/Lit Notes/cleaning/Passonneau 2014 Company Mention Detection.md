---
type: lit-note
title: Company Mention Detection for Large Scale Text Mining
authors:
- Rebecca J. Passonneau
- Tifara Ramelson
- Boyi Xie
year: 2014
venue: KDIR 2014 (SSTM), pp. 512–520
source_url: https://www.scitepress.org/PublishedPapers/2014/51744/51744.pdf
doi: 10.5220/0005174405120520
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.2
family:
- cleaning
evidence: Weak
score: 5
tags:
- lit-note
- family/cleaning
- entity-linking
---
# Company Mention Detection for Large Scale Text Mining (Passonneau, Ramelson & Xie, 2014)

**Basis:** paper PDF read through a summarising page fetch on 2026-11-08.

**Takeaway:** Adding coreference and division-name rules to NER raised company-mention recall from 57% to 77% (precision 100% → 90%) and found 21% more sentences about S&P 500 firms, but price-direction prediction improved significantly only in one of three sectors and never beat the majority class.

## Problem
Does better company-mention detection improve news-based price prediction?

## Data and period
Reuters news, 2007, 124 S&P 500 firms in energy, materials and industrials (about 16,000 items).

## Method
NER plus coreference and subsidiary/division matching; several text representations; direction classification at a 2% threshold.

## Baselines and validation
Original NER vs improved detection; majority-class baseline.

## Results (with page or section references)
- Manual probe (54 mentions): recall 57.4% → 76.6%, precision 100% → 90% (errors were company sub-units).
- Sentences with mentions: 29,377 → 35,453 (+20.7%; energy +30%).
- Prediction: significant gains only for industrials with bag-of-words (56.7% → 60.1%); none beat the majority class.

## Limits and risks to validity
One year, tiny manual probe, no gold standard for the full set; read through a summarising tool.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single evaluation setup |
| Baselines | 1 | Majority class |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | |
| Sample breadth | 1 | Three sectors, one year |
| Statistical testing | 1 | Significance tests |
| Reproducibility | 0 | No code or data |
| **Total** | 4/12 → **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read through a summarising tool).
