---
type: lit-note
title: "Machine Learning vs. Economic Restrictions: Evidence from Stock Return Predictability"
authors: [Doron Avramov, Si Cheng, Lior Metzker]
year: 2023
venue: Management Science 69(5), 2587–2619
source_url: https://cris.huji.ac.il/en/publications/machine-learning-vs-economic-restrictions-evidence-from-stock-ret/
doi: 10.1287/mnsc.2022.4449
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.6]
family: [evaluation]
evidence: Weak
score: 5
tags: [lit-note, family/evaluation, economic-value, transaction-costs, abstract-only]
---
# Machine Learning vs. Economic Restrictions (Avramov, Cheng & Metzker, 2023)

**Basis:** Abstract only (Hebrew University CRIS record and SSRN 3450322 abstract page, opened 2026-11-09). Full text not opened (journal paywalled). Scored Weak under the vault's abstract-only convention.

**Takeaway:** Deep-learning return signals earn most of their profit in hard-to-arbitrage stocks and high limits-to-arbitrage periods; excluding microcaps, distressed stocks or high-volatility episodes considerably reduces profitability, and reasonable trading costs erode it further because of high turnover and extreme positions.

## Problem
Whether machine-learning stock-return predictability survives economic restrictions: tradable universes, market states and trading costs (abstract).

## Data and period
Not in the part read (US stocks; details in the full paper).

## Method
Deep learning and other ML return predictors compared with traditional methods, with universe filters and cost adjustment (abstract).

## Baselines and validation
Not in the part read.

## Results (with page or section references)
- Profitability comes from difficult-to-arbitrage stocks and high limits-to-arbitrage states (abstract).
- Excluding microcaps, distressed stocks or high market volatility "considerably attenuates profitability" (abstract).
- Performance deteriorates further with reasonable trading costs, due to high turnover and extreme tangency-portfolio positions (abstract).
- Signals remain profitable in long positions and recent years, with low downside risk (abstract).
- Replication files are posted with the journal supplement (INFORMS supplemental page, seen in search; not opened).

## Limits and risks to validity
_My assessment:_ magnitudes unknown from the abstract; numbers must be taken from the full text before citing sizes. Direction agrees with [[Zhang 2026 Deep TS Models Equity Portfolios]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Out-of-sample stated; scheme not seen |
| Baselines | 1 | Traditional methods (per abstract) |
| Point-in-time and leakage controls | N/A | Not seen |
| Costs and realism | 2 | Universe restrictions, turnover, costs |
| Sample breadth | 1 | US cross-section; regimes not seen |
| Statistical testing | N/A | Not seen |
| Reproducibility | 1 | Replication files |
| **Total** | 6/10 → 8 partial; recorded **Weak (5)**, abstract only | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept (abstract only).
