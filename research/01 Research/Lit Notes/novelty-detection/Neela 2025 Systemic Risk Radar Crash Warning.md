---
type: lit-note
title: "Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Warning"
authors: [Sandeep Neela]
year: 2025
venue: arXiv (q-fin.RM)
source_url: https://arxiv.org/abs/2512.17185
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.5, RQ1.8, RQ1.4]
family: [novelty-detection, graph]
evidence: Weak
score: 5
tags: [lit-note, family/novelty-detection, family/graph]
---
# Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Warning (Neela, 2025)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1–4, 9, 11–16, 18, 20, 22, 24–25).

**Takeaway:** A correlation-graph GNN crash warner on 44 stocks is no better than logistic regression or a random forest, flags almost every day as a crash day (false-positive rate 1.0), and fails completely on COVID-19 (AUROC 0.000); the paper itself calls the evidence preliminary.

## Problem
Can changes in market network structure (rising correlations, synchronised sectors) warn of crash regimes before prices fall?

## Data and period
44 large stocks and sector ETFs (yfinance), daily, in three separate windows: Dot-com 1998–2003, GFC 2006–2011, COVID 2018–2021 (Table 1, p. 4). Seven price features per node (returns, 20/60-day volatility and drawdown, momentum). The sentiment/news layer is described but **not used** (pp. 3–4).

## Method
Rolling correlation graph (threshold 0.5), two-layer GCN snapshot model and a GCN+GRU "temporal" prototype over 5-day graph sequences; label = node drawdown above a threshold (10%) within a forward horizon (60 days in §6.3, "e.g., 20 days" in §7.1) (pp. 9, 11–12).

## Baselines and validation
Logistic regression and random forest on the same features. Chronological 80/20 split **within each crisis window**; no cross-crisis test (p. 9, p. 20). No volatility-index or simple drawdown-rule baseline.

## Results (with page or section references)
- AUROC, Dot-com: LR 0.463, RF 0.291, GNN 0.412, temporal GNN 0.589; GFC: LR 0.738, RF 0.529, GNN 0.248, temporal 0.232 (Table 2, p. 13; Fig. 4, p. 11).
- GNNs predict the crash class for every test sample: FPR = 1.0 in Dot-com and GFC; COVID test window has no non-crash days, AUROC 0.000 (Table 4, p. 24; pp. 24–25).
- Random forest FPR 0.49 (Dot-com) and 0.45 (GFC) (Table 3, p. 24).
- Lead times: "several days to weeks" for many events, with late and missed warnings; shown only as a figure, no numbers (p. 14).
- COVID failure attributed to an exogenous shock that did not show up in pre-crash correlations (p. 25).

## Limits and risks to validity
_My assessment:_ the warnings are uninformative (a model that always says "crash" in a crisis window gets recall 1.0). Test windows sit inside known crises, so base rates are very high and the setup cannot measure false alarms in calm markets. No news or social input despite the framing. Horizon definition is inconsistent between sections. Useful mainly as a negative example: correlation structure alone did not warn of an exogenous shock.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split per crisis window |
| Baselines | 1 | LR and RF; no VIX/drawdown rule |
| Point-in-time and leakage controls | 1 | Rolling windows stated; no other checks |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 44 stocks; three crises, tested separately |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Public data, no code link found in pages read |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "the models assign the positive (crash) label to nearly all samples" (p. 25)
- "This version of SRR should be interpreted as a proposal paper" (p. 22)
