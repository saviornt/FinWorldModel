---
type: lit-note
title: "From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems"
authors: [Ruizhe Zhou, Xiaoyang Liu, Gaoyuan Du, Yi Zheng, Shouxi Ren, Deepayan Chakrabarti, Dengdu Jiang]
year: 2026
venue: arXiv (cs.AI) 2605.23955 (v4, Aug 2026)
source_url: https://arxiv.org/abs/2605.23955
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.7]
family: [evaluation]
evidence: Weak
score: 5
tags: [lit-note, family/evaluation, reproducibility, determinism]
---
# Determinism in Financial AI Systems (Zhou et al., 2026)

**Basis:** Full text (pp. 1–2, 4–7) via the alphaXiv PDF reader, read 2026-11-09.

**Takeaway:** Fixing seeds does not make deep financial models reproducible: GPU reduction order, sampling-based explainers and parallel inference settings change outputs; on Elliptic Bitcoin, 15.5–27.5% of nodes flipped their modal label across 50 seeds, and deterministic GPU flags cost about 5× memory for a graph model.

## Problem
Sources and size of run-to-run nondeterminism in tabular, graph and LLM financial models, and how to measure it for audit (pp. 1–2).

## Data and period
Public datasets: Credit Card Default (tabular), Elliptic Bitcoin (203K nodes, ~2% illicit), 100 synthetic SAR narratives (LLM) (pp. 4–6).

## Method
Literature survey (2018–2025) plus own experiments: 30 KernelSHAP runs; 50 seeds × 10 splits of GCN, GraphSAGE, GAT; LLM extraction at tensor-parallel sizes 1, 2, 4 (pp. 2, 4–6).

## Baselines and validation
Exact methods as references (TreeSHAP; deterministic aggregation) (pp. 2, 4).

## Results (with page or section references)
- KernelSHAP (n = 100): median rank span 10–14 positions per feature across 30 runs; TreeSHAP span 0 (Fig. 1, p. 4).
- Elliptic: flip rates 27.5% (GCN, deterministic), 15.5% (GraphSAGE), 25.7% (GAT); expected pairwise disagreement 1.7–6.5%; deterministic full-batch GCN needs 5.0 GB vs 1.0–1.3 GB (Table 3, p. 5).
- `torch.use_deterministic_algorithms(True)` forces deterministic scatter operations at a memory cost (p. 5).
- Greedy LLM decoding was bit-identical within a configuration but 30–36% of prompts changed text across tensor-parallel widths (Table 4, p. 6).
- Recommends logging snapshots of weights, hyperparameters and seeds for audit replay (p. 7).

## Limits and risks to validity
_My assessment:_ v3–v4 correct several errors from v1–v2 (flip rates on one split, a halved divergence rate, a withdrawn mechanism) (p. 1), so reliability is a concern; tasks are credit, fraud and AML, not forecasting. Cited for mechanisms and the seeds-are-not-enough point only.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Reproducibility study |
| Baselines | N/A | Exact-method references |
| Point-in-time and leakage controls | N/A | Not relevant |
| Costs and realism | N/A | Not relevant |
| Sample breadth | 1 | Three datasets, three modalities |
| Statistical testing | 1 | Dispersion statistics over seeds and splits |
| Reproducibility | 0 | Code release not stated; prior versions had errors |
| **Total** | 2/6 → **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "Inference determinism is a systems property" (p. 6)
