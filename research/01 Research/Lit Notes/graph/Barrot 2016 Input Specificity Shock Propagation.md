---
type: lit-note
title: "Input Specificity and the Propagation of Idiosyncratic Shocks in Production Networks"
authors: [Jean-Noël Barrot, Julien Sauvagnat]
year: 2016
venue: Quarterly Journal of Economics 131(3), 1543–1592
source_url: https://finance.unibocconi.eu/sites/default/files/files/media/attachments/JMP-JulienSauvagnat20150109105100.pdf
doi: 10.1093/qje/qjw018
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP2 Data Sources and Storage]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.4, RQ1.5, RQ1.12, RQ2.8]
family: [graph]
evidence: Moderate
score: 8
tags: [lit-note, family/graph]
---
# Input Specificity and the Propagation of Idiosyncratic Shocks (Barrot, 2016)

**Basis:** December 2014 job-market version read through alphaXiv page excerpts (pp. 1–4, 10, 15, 17, 20, 23, 25, 27–28, 31–32, Fig. 4, Tables 2 and 12). The published QJE PDF could not be fetched; numbers may differ slightly from the published version.

**Takeaway:** When a natural disaster hits a supplier, its customers lose about 2 percentage points of sales growth and about 1% of equity value, almost all within 21 trading days, and only when the supplier's input is hard to replace; the shock also spills over to the customer's other suppliers.

## Problem
Do firm-level shocks propagate along supply chains, or are they absorbed?

## Data and period
35 major US natural disasters 1978–2010 (SHELDUS: under 30 days, damages above $1 bn); supplier–customer links from Compustat segment files; customer sample 60,682 firm-quarters (2,014 firms), supplier sample 92,977 (4,112 firms) (pp. 15, 17, Table 2).

## Method
Difference-in-differences on sales growth with firm, year-quarter, industry×year and state×year fixed effects; event study of daily four-factor abnormal returns for 1,039 customer–disaster events; specificity proxies: differentiated goods, R&D intensity, patents (pp. 10, 15, 25).

## Baselines and validation
Placebos: untreated customers and inactive (past or future) links show no effect; pre-trends checked; small vs large disasters (pp. 3, 20, 23). Causal identification rather than a forecasting test.

## Results (with page or section references)
- Customer sales growth falls 2.0–2.9 pp after a supplier is hit (about 20% of the mean), though suppliers are about 3% of customers' input costs (p. 20).
- Customer CAR about −1% over [−10, 30]; virtually all in [0, 20]; directly hit suppliers −2.4% (p. 27).
- Effect only for specific suppliers (−1.3% to −2.6% CAR); none for non-specific ones (pp. 23, 27).
- $1 of lost supplier sales goes with $3.5–3.6 of lost customer sales (pp. 4, 31).
- Customer CAR[0, 20] predicts later sales growth (coef. 0.25); placebo on untreated customers ≈ 0 (Table 12, p. 75).

## Limits and risks to validity
_My assessment:_ evidence that shocks travel along supply chains and that prices react within weeks; not a trading test. Hurricanes may be partly anticipated (p. 27). Only listed firms with disclosed major customers.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Causal event study, not a forecast |
| Baselines | 1 | Untreated and inactive-link placebos |
| Point-in-time and leakage controls | 2 | Exogenous dates; pre-trend checks |
| Costs and realism | N/A | No strategy |
| Sample breadth | 2 | 1978–2010, 35 disasters, thousands of firms |
| Statistical testing | 1 | Clustered errors, standard event-study tests |
| Reproducibility | 0 | Licensed data |
| **Total** | **6/10 → 8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "input specificity is a key driver of the propagation of firm-level shocks" (p. 3)
