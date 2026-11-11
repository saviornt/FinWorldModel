---
type: lit-note
title: "Stock Movement Prediction with Multimodal Stable Fusion via Gated Cross-Attention Mechanism"
authors: [Chang Zong, Hang Zhou]
year: 2024
venue: "arXiv (q-fin.CP), v2"
source_url: https://arxiv.org/abs/2406.06594
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7, RQ1.4]
family: [fusion]
evidence: Weak
score: 7
tags: [lit-note, family/fusion]
---
# Stock Movement Prediction with Multimodal Stable Fusion via Gated Cross-Attention (Zong & Zhou, 2024)

**Basis:** arXiv v2 (2 Dec 2024), pp. 1–3, 8–11, via the alphaXiv PDF reader.

**Takeaway:** On four small benchmarks (38–369 stocks, one or two years each), naively adding tweet or news embeddings to an attentive LSTM lowered accuracy on three of four datasets; a gated cross-attention that lets the price modality guide fusion recovered small gains (MCC 0.06–0.11), and plain cross-attention was hurt by noisy text — price was the indispensable modality.

## Problem
Fuse price indicators, documents (tweets/news) and an industry graph for up/flat/down prediction without the instability caused by sparse and conflicting modalities (pp. 1–2).

## Data and period
InnoStock (369 China STAR stocks, 2022), BigData22 (50 US stocks, 2019–2020), CIKM18 (38, 2017), ACL18 (87, 2014–2015); chronological train/validation/test (p. 8, Table III).

## Method
MLP for indicators, OpenAI Ada embeddings for documents, GAT for the industry graph; two gated cross-attention blocks with the price (then price+text) as primary modality guiding fusion (pp. 2–3, 8).

## Baselines and validation
LSTM, ALSTM, DTML, ESTIMATE, ALSTM-W, SLOT; five seeds; accuracy and MCC (pp. 8–9).

## Results (with page or section references)
- MCC of MSGCA: 0.055 (InnoStock), 0.111 (BigData22), 0.059 (ACL18), 0.081 (CIKM18); best baselines 0.051, 0.105, 0.049, 0.061 (p. 9, Table IV).
- Adding documents to ALSTM (ALSTM-W) lowered accuracy versus ALSTM on BigData22, CIKM18 (and ACL18 relative to unimodal frameworks per authors) (p. 9).
- Replacing the gated block with plain cross-attention cut performance (noisy aggregation); GLU too simple (p. 9, Fig. 3).
- Removing price (MSGCA-DG) dropped MCC sharply (e.g. 0.019 vs 0.059 on ACL18); removing graph or text cost little (p. 11, Table V).
- Larger text encoders helped (Ada > BERT > Word2Vec) (p. 10).

## Limits and risks to validity
_My assessment:_ short single-period tests, no random-walk or GBT baseline, no costs or portfolio test, MCC near zero. Ada embeddings applied to 2014–2022 text predate the model, with no memorisation control (rubric cap). Code and data public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Chronological single split |
| Baselines | 1 | Deep baselines only |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | Classification only |
| Sample breadth | 1 | Four datasets, US and China, short periods |
| Statistical testing | 1 | Five seeds with variances |
| Reproducibility | 2 | Code and data released |
| **Total** | **6/12 → 7/14, capped** | Weak (LLM embeddings on pre-cutoff text) |

## Quotes worth keeping (each under 15 words, with page)
- "Introducing more modalities may damage accuracy" (p. 9)
