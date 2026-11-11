---
type: lit-note
title: "Not All News Is Equal: Topic- and Event-Conditional Sentiment from Finetuned LLMs for Aluminum Price Forecasting"
authors: [Alvaro Paredes Amorin, Andre Python, Christoph Weisser]
year: 2026
venue: arXiv 2603.09085
source_url: https://arxiv.org/abs/2603.09085
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14, RQ1.11]
family: [sentiment]
evidence: Weak
score: 4
tags: [lit-note, family/sentiment]
---
# Not All News Is Equal: Topic- and Event-Conditional Sentiment for Aluminum Price Forecasting (Paredes Amorin, 2026)

**Basis:** v2 (31 Mar 2026), page excerpts via alphaXiv (pp. 1, 3, 5–6, 8–9, 17–19).

**Takeaway:** Monthly headline sentiment (fine-tuned Qwen3 or FinBERT) for Shanghai aluminium 2007–2024 helped mainly in high-volatility months (LSTM Sharpe 1.04 vs 0.23 tabular-only), and the type of news mattered more than the model: sentiment from reports of events that had happened earned Sharpe 0.62 while forward-looking headlines earned −0.01, and Reuters headlines (0.80) beat Dow Jones (0.18) and China News Service (0.15).

## Problem
Which sources, topics and event types make headline sentiment useful for a commodity price forecaster?

## Data and period
WIND tabular data (base metal indices, FX, inflation, energy) and Factiva headlines: Reuters (4,963), Dow Jones (11,581), China News Service (8,970), Mar 2007–Apr 2024, aggregated monthly (p. 3).

## Method
Headlines labelled +1/0/−1 by FinBERT or a Qwen3 model fine-tuned on five sentiment datasets; monthly net score; LSTM, GRU, BiLSTM, ConvLSTM and TFT with and without sentiment; zero-shot Qwen3-8B topic (12 classes) and forward-looking vs occurred-event tags (pp. 3, 5).

## Baselines and validation
Tabular-only models, sentiment-only rule, buy-and-hold (App. D). Split details not in the pages read; best-of-grid hyperparameters reported per model (App. E, Table 7). Hit-rate p-values vs 50% (App. F, Table 8). No costs.

## Results (with page or section references)
- High-volatility regime: tabular + Qwen sentiment Sharpe 1.04 vs tabular-only 0.23; medium regime: sentiment-only 1.19 beats combined 0.51 (p. 5).
- Occurred events 0.62 vs forward-looking −0.01; within Price Movement topic 0.89 vs 0.20 (p. 6, Fig. 3).
- Supply Disruption headlines Sharpe −0.07; Geopolitical −0.26, Trade Policy −0.25 (pp. 5–6).
- Best of 4,094 topic subsets Sharpe 1.00 vs all-topics 0.81 (p. 5).
- In grid-search tables, adding sentiment barely changes RMSE for LSTM, BiLSTM, ConvLSTM or TFT (App. E, pp. 17–18).

## Limits and risks to validity
_My assessment:_ one asset, monthly frequency (~200 points), regime labels assigned ex post, best topic subset chosen from 4,094 tries on the same data (data mining), Qwen3 and FinBERT applied to pre-cutoff text with no memorisation control, no costs. The occurred-vs-forward-looking split and the source-quality gap are plausible, cheap-to-test hypotheses, not established facts.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Train/test split (details not read) |
| Baselines | 1 | Tabular-only, buy-and-hold |
| Point-in-time and leakage controls | 0 | Pre-cutoff fine-tuned LLM; ex-post regimes; subset search |
| Costs and realism | 0 | None |
| Sample breadth | 1 | One asset, 17 years |
| Statistical testing | 1 | Hit-rate p-values only |
| Reproducibility | 0 | Code for the sentiment model; data not redistributable |
| **Total** | **4/14 → capped Weak** | Rubric cap: LLM used on events before its cutoff without memorisation control |

## Quotes worth keeping (each under 15 words, with page)
- "actual outcomes carry substantially more predictive content than expectations or forecasts" (p. 6)
