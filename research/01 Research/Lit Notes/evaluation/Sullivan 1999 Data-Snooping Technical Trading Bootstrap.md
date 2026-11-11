---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- multiple-testing
title: Data-Snooping, Technical Trading Rule Performance, and the Bootstrap
authors:
- Ryan Sullivan
- Allan Timmermann
- Halbert White
year: 1999
venue: Journal of Finance 54(5), 1647–1691
source_url: https://bashtage.github.io/kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf
doi: 10.1111/0022-1082.00163
research_questions:
- RQ4.2
- RQ4.6
evidence: Moderate
score: 9
---
# Data-Snooping, Technical Trading Rule Performance, and the Bootstrap (Sullivan, Timmermann & White, 1999)

**Basis:** Journal article PDF (course-page copy), read 2026-11-08 through a summarising page fetch; tables III, V, VI and pp. 1649–1685 cited.

**Takeaway:** Judged against the full universe of 7,846 technical rules, the best rule's in-sample significance on 100 years of the Dow survives White's Reality Check, but in the held-out 1987–1996 period a nominal p of 0.004 becomes 0.341 after the data-snooping correction, and on S&P 500 futures no rule beats the benchmark (Reality Check p 0.908).

## Problem
Whether technical-rule profits survive once the whole universe of rules that could have been searched is accounted for (pp. 1647–1650).

## Data and period
DJIA daily closes 1897–1996; S&P 500 futures 1984–1996 (p. 1658).

## Method
White's Reality Check bootstrap over 7,846 rules (filters, moving averages, support/resistance, channel breakouts, on-balance volume); mean return and Sharpe criteria (pp. 1654, 1683–1685).

## Baselines and validation
Benchmark: no-trade / buy-and-hold style null of zero excess performance; sub-periods and a 1987–1996 hold-out after the BLL sample (Table III).

## Results (with page or section references)
- Full 100 years: best rule 17.17% mean return, nominal and RC p 0.000 (Table III, p. 1662).
- 1987–1996: best rule 14.41%, nominal p 0.004, RC p 0.341; Sharpe 0.87 with nominal p 0.000 but RC p 0.903 (Tables III, V).
- S&P futures: best rule 9.43%, nominal p 0.042, RC p 0.908; Sharpe RC p 0.987 (Tables III, V).
- Break-even cost of the best DJIA rule 0.27% per trade; with a one-day signal delay the best mean return falls to 7.8% and the Sharpe is no longer significant (pp. 1673–1675).
- Source inconsistency: the introduction gives about 12% probability for the out-of-sample result while Table III shows 0.341 (p. 1649 vs Table III).

## Limits and risks to validity
_My assessment:_ one index and one futures market; rules are simple; the paper is the template for counting the whole search universe and for showing that significance disappears on later data.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Later hold-out period and separate futures market |
| Baselines | 2 | Benchmark plus full rule universe |
| Point-in-time and leakage controls | 1 | Signal-delay (nonsynchronous trading) check |
| Costs and realism | 1 | Break-even cost per trade |
| Sample breadth | 2 | 100 years incl. crises, plus futures |
| Statistical testing | 2 | Data-snooping-corrected p-values |
| Reproducibility | 0 | No code |
| **Total** | 9/14 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "there is no evidence that any trading rule outperforms over the sample period" (p. 1682)
