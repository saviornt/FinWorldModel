---
type: decision-log
updated: 2026-11-09
tags: [decisions]
---
# Decisions Log

Newest first. During the research phase this logs findings and vault changes only; design decisions belong to the methodology plan.

## 2026-11-09 – Research phase complete
[[Multimodal Financial Forecasting and Shock Detection (Final)]] saved (status final), drawn from [[RP1 ML Methods]], [[RP2 Data Sources and Storage]], [[RP3 Cleaning and Labelling]], [[RP4 Training and Evaluation]] and [[RP5 Vault Review]]: 357 unique lit notes (27 Strong, 157 Moderate, 100 Weak, 73 primary documentation). No new search. Final vault updates done: [[Thesis v2 – proposed changes]] created (v1 untouched); [[Broken Notebooks & Research Direction]] revised to one notebook per RP1 method family, listing the old notebooks no longer needed (none deleted); a "Research findings" section added to both notes in `03 Models/Sentiment/`; every RQ in [[Research Questions]] links to its answer; nothing moves out of `99 Archive/` (no archived item rated Supported). Findings only; decisions belong to the methodology plan.
- Strong simple baselines (random walk and GBT for returns, HAR for volatility, GARCH-t/EVT for tails, logit for crisis risk, 1/N for portfolios) are rarely beaten; risk is forecastable, direction barely is, and shock timing is not.
- The project's central premise, an autoregressive token model conditioned on world state, is untested where it matters; added inputs help only through gated, bounded pathways, and the matched token-vs-continuous ablation is the first open experiment.
- Licences (training bans at FRED, Massive, X, ACLED; silence elsewhere) and protocol (knowledge-time stamping, no shuffled splits, counted trials, placebos) constrain the build more than method choice.

## 2026-11-09 – RP5 complete
[[RP5 Vault Review]] set to final: eight vault items reviewed against RP1–RP4 from 72 existing lit notes (17 Strong, 41 Moderate, 11 Weak, 3 primary documentation); no new search. paper-critique run and fixed; citation check: every reference resolves to a lit note verified in RP1–RP4, two misattributions fixed. Verdicts: Project Thesis Partly supported (profitability claim Not supported); sentiment module Partly supported; sentiment testing script Partly supported; autoencoder imputation plan Not supported; A*/TD3/MAML prototype Not supported; notebook rebuild plan Partly supported; research direction note Partly supported; essays not reviewed. No archived item rated Supported, so nothing leaves `99 Archive/`. Findings only; decisions belong to the methodology plan.
- The archived prototype leaks the future: its inputs include the next day's open (`Target_Open`) when predicting the next close, its support/query split is shuffled, and its default meta-learning rates are 1e3–5e4.
- The sentiment module's strongest choice (train-only PCA) guards a small leak; its hand-set weights give VADER 25–50% against the evidence on lexicons, and its encoders' training cutoffs are not recorded.
- The research direction note holds up best: its temporal-integrity and evaluation rules are supported; MAML-inspired adaptation and non-next-token objectives are not yet shown to help.

## 2026-11-09 – RP4 complete
[[RP4 Training and Evaluation]] set to final: 9 research questions answered from 106 sources (18 Strong, 61 Moderate, 25 Weak, 2 primary documentation). Evaluation protocol per output type, metrics table, statistical-test guide, shock-study protocol and leak-free adaptation protocol written. paper-critique run and fixed (Abstract's pretraining/adaptation claim narrowed and confidence levels added; tail-ranking rule corrected to several years of daily data; one missing citation added). citation-check: 101 of 104 scholarly references verified by lookup, 3 partial (Avramov 2023 year, Saly-Kaufmann 2026 DOI not in OpenAlex, Aich 2025 retitled); none invented, mismatched or orphaned; seven published DOIs added. Findings only; decisions belong to the methodology plan.
- The protocol moves results more than the method: shuffled CV, label leakage in adaptation and uncounted search each create effects larger than the method gains they are used to show; quote results only from an untouched walk-forward segment with every trial counted.
- Economic value is decided by turnover, tradable universe and investor size; gross gains, including the best published ML portfolios, often turn negative at realistic costs on liquid universes.
- No pretraining objective or adaptation method has been shown to beat next-token or direct training, periodic retraining or a frozen model under a leak-free financial test; derived-target reconstruction and adaptive window choice are the most promising leads.
- Open gaps carried forward: 18 classics read as working papers or abstracts (numbers not checked against published versions); no finance study of adaptation under delayed labels, of pretraining objectives under walk-forward, or of token/multimodal models net of costs.

## 2026-11-08 – RP3 complete
[[RP3 Cleaning and Labelling]] set to final: 8 research questions answered from 92 sources (3 Strong, 46 Moderate, 26 Weak, 17 primary documentation). paper-critique run and fixed (abstract leakage ranking reworded as a judgement across studies in different units; timestamp, normalisation and vendor-history claims narrowed; Zhang 2026 ranges made consistent; Croushore survey score flagged). citation-check: 72 of 75 scholarly references verified by lookup, 1 partial (Bradley 2014, online-first year), 1 not in OpenAlex (Lyle 2024, authors' PDF opened), 1 web page; no invented or orphaned references. Findings only; decisions belong to the methodology plan.
- The largest measured leaks come from inside the pipeline (future-reaching feature windows, same-bar execution, test-set selection, overlapping labels), not from vendors; full-sample scaling is a small leak by comparison.
- Vendors give valid time but rarely knowledge time (CRSP rewrites history; FactSet links carry no first-seen date), so the project must stamp first-seen times and keep vintages itself, keyed on dated permanent IDs.
- Reconstructing 25 years of 1-minute bars from daily data is not supported; impute from the past only, flag it, and model at the frequency the data has.
- Open gaps carried forward: top-up lists in each RQ (López de Prado books unopened; Shumway 1997 originals); no one-panel leakage comparison; no test of identity or graph look-ahead on forecasts.

## 2026-11-08 – RP2 complete
[[RP2 Data Sources and Storage]] set to final: 9 research questions answered from 80 sources (65 primary documentation; 15 scored: 1 Strong, 8 Moderate, 6 Weak). paper-critique run and fixed; citation check: 16 of 17 scholarly references verified by lookup, the 17th (Lyle 2024) from the authors' PDF; the six licence pages behind the main claims re-opened and confirmed. Findings only; decisions belong to the methodology plan.
- Licence terms bind more than price: FRED/ALFRED, Massive, X (foundation models) and ACLED ban model training; Alpaca, Alpha Vantage and EODHD are silent. Clearly usable for storage and training: EDGAR, BLS, GDELT, USGS, GLEIF, MarineCadastre AIS.
- No affordable price API documents delisted coverage except Massive (which bans training); the low-confidence API shortlist is Alpaca, Databento, EODHD, each needing a survivorship-free daily reference (Norgate or CRSP).
- Sources almost never record knowledge time and no storage engine read covers both knowledge and valid time, so the ingestion layer must stamp retrieval time and keep every version itself.
- Open gaps carried forward: top-up lists for RQ2.2, RQ2.3, RQ2.8, RQ2.9 (infrastructure events, measured latency) and the vendor-quote list in RP2.

## 2026-11-08 – RQ2.5 scope: MongoDB, SurrealDB and RocksDB added
User asked that the RP2 storage-engine comparison also cover MongoDB, SurrealDB and RocksDB. Added to RQ2.5 and its starting queries in the guide (Claude doc, rev 39), the local guide export, [[Research Questions]], [[RP2 Data Sources and Storage]] and the Search Log. Research scope only; no design decision.

## 2026-11-08 – RP1 complete
[[RP1 ML Methods]] set to final: 15 research questions answered from 163 sources (14 Strong, 85 Moderate, 64 Weak); paper-critique and citation check run (159 of 163 references verified, 2 partial, 2 could not be confirmed; no invented or mismatched references). Findings only; decisions belong to the methodology plan.
- Strong simple baselines decide the verdict: a random walk and gradient-boosted trees for returns, HAR for volatility, and 1/N or buy-and-hold for trading rules match or beat most complex models in the best-designed tests, including deep RL and token/foundation models.
- Added inputs (text, macro, cross-asset, graphs) help only when compressed and fed through a gated or bounded pathway on top of a strong price model; naive concatenation and corrupted feeds make forecasts worse than price-only.
- Shock timing is not predictable from prices; what holds up is a slow fragility gauge (credit and price booms, news novelty) over months to years, plus fast detection after onset. No tail method stays calibrated at shock onset; volatility-filtered fat-tailed models are the baseline.
- Open gap carried forward: 21 journal papers were read as working papers or summaries; their numbers are not checked against the published versions (see RP1 Assumptions).

## 2026-11-07 – Research scope: autoregressive, LLM-inspired model (no actual LLM)
User clarified the target: an autoregressive sequence model trained with next-token-style prediction on market and world data, "LLM-inspired" (as the adaptation plan is MAML-inspired), not a model that uses an actual LLM. Text will be an input; its form is a research question.
- Guide (Claude doc) and [[Research Questions]] updated: RQ1.13 (autoregressive next-token market models), RQ1.14 (form of text and event inputs), RQ1.15 (world-model hypothesis vs price-only).
- LLM-specific searching stopped; LLMs kept only as a comparison baseline; RQ1.2 and RQ1.3 evidence kept for memorisation and look-ahead lessons.
- RP1 order from here: RQ1.10, RQ1.13, RQ1.14, RQ1.15, RQ1.11, RQ1.12.

## 2026-11-08 – Foundation-model research direction added to the research plan
Added [[Financial Foundation Model Research Direction]] to `00 Project/` and folded its questions into the research guide (Claude doc) as hypotheses to test.
- Seven new RQs: RQ1.10–RQ1.12 (tokenization, source corroboration, information diffusion), RQ2.8–RQ2.9 (corporate-structure and global-event sources), RQ3.8 (entity identity, valid vs knowledge time), RQ4.8–RQ4.9 (pretraining objectives, continual adaptation).
- Overlapping questions mapped to existing RQs; section 13 open decisions routed to the Synthesis and methodology plan; RP5 now reviews the note.

## 2026-11-07 – Vault restructured for research
Vault restructured for research; prototype and essays archived pending RP1 and RP5.
- Created `00 Project`, `01 Research/Papers`, `01 Research/Lit Notes`, `02 Data`, `03 Models`, `04 Decisions`, `99 Archive`.
- Moved notes per guide Step 0.2; removed the four emptied folders; no wikilinks pointed at the moved notes.
- Added minimal `type`/`status` properties to moved notes (bodies unchanged).
