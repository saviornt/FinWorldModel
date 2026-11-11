---
type: research-paper
paper_id: RP5
title: "RP5 – Review of Existing Project Material"
status: final
research_questions: [RP5.1, RP5.2, RP5.3, RP5.4, RP5.5, RP5.6, RP5.7, RP5.8]
sources_count: 72
evidence_strong: 17
evidence_moderate: 41
evidence_weak: 11
created: 2026-11-09
updated: 2026-11-09
related: ["[[Research Questions]]", "[[Evidence Register]]", "[[Search Log]]", "[[RP1 ML Methods]]", "[[RP2 Data Sources and Storage]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
tags: [research-paper, vault-review]
---
# RP5 – Review of Existing Project Material

## Abstract

RP5 holds eight vault items against [[RP1 ML Methods]], [[RP2 Data Sources and Storage]], [[RP3 Cleaning and Labelling]] and [[RP4 Training and Evaluation]], using only lit notes those papers already scored, plus reading the code in the notes. **Project Thesis (RP5.1): Partly supported.** Its central promise of "consistent profitability" is Not supported: gross gains turn negative at realistic costs in the best tests read. Multi-horizon forecasting is partly supported, and its portfolio, explainability, execution and infrastructure choices are Untested. **Sentiment module (RP5.2): Partly supported.** FinBERT as the main scorer, mean-pooled embeddings and train-only PCA have support. The hand-set domain weights and the 25–50% VADER share do not. **Testing script (RP5.3): Partly supported.** It measures label agreement well, but label accuracy does not predict return value, and it has no return-based test. **Autoencoder imputation plan (RP5.4): Not supported.** **A\*/TD3/MAML prototype (RP5.5): Not supported.** It also feeds the next day's open price into its inputs. **Notebook plan (RP5.6): Partly supported.** Its masters centre on the three weakest-evidenced families. **Research direction note (RP5.7): Partly supported.** Its temporal-integrity and evaluation rules are supported; tokenizer, graph, event and world-state ideas hold only in narrow forms; MAML-inspired adaptation is not supported so far. **Essays (RP5.8):** not reviewed. No archived item is rated Supported. Confidence is Medium overall.

## Research questions

RP5 has no numbered research questions in the guide. Each vault item is treated as one question, "does this item hold up against RP1–RP4?", with IDs RP5.1–RP5.8 so that [[Research Questions]] can link to the answers (see Assumptions).

| ID | Item in the vault | Checked against |
| --- | --- | --- |
| RP5.1 | [[Project Thesis - A Framework for Real-Time Time-Series Forecasting, Portfolio Optimization, and Automated Trading]] | RP1, RP4 |
| RP5.2 | Sentiment module design ([[Sentiment Analysis Source Code]]; project doc `claude/sentiment-module-design.md`) | RP1 RQ1.2, RQ1.3, RQ1.14; RP3 |
| RP5.3 | [[Sentiment Analysis Testing Source Code]] | RP4 (RQ4.2, RQ4.3); RP1 RQ1.3 |
| RP5.4 | Autoencoder imputation plan ([[Autoencoders I]]) | RP3 RQ3.4 |
| RP5.5 | A\*/TD3/MAML prototype ([[Neural Network Architecture Test]], [[Adaptive Trading Agent - Market State-Dependent Algorithm]]) | RP1 RQ1.9; RP4 (RQ4.1, RQ4.9) |
| RP5.6 | Gemini/NotebookLM rebuild plan ([[Broken Notebooks & Research Direction]]) | RP1 method families |
| RP5.7 | [[Financial Foundation Model Research Direction]] | RP1 (RQ1.2, RQ1.4, RQ1.5, RQ1.9–RQ1.15); RP3 (RQ3.8); RP4 (RQ4.5, RQ4.8, RQ4.9) |
| RP5.8 | Algorithmic Trading essays (`99 Archive/Essays/`) | Out of scope |

## Method

- **Date:** 2026-11-09 (session 29). **No new searching.** The guide asks that RP5 be written from the four finished papers and their lit notes, with new searching only to settle a specific gap; no gap needed it (see [[Search Log]], RP5 entry).
- **Material read:** the full text of each vault item listed above (the 99 KB imputation chat was read in its plan, 25-year and "99.999%" sections, located by search); the RP1–RP4 Abstracts, each relevant RQ section's answer and confidence statement, and the properties (evidence, score) of every lit note cited here.
- **Verdict scale (from the guide):** *Supported* – the RP evidence backs the claim or choice; *Partly supported* – some parts are backed, others are contradicted or untested; *Not supported* – the evidence contradicts it, or it fails the RP3/RP4 practice rules; *Untested* – no RP section or lit note bears on it.
- **Rule for weight:** a verdict built only on Weak lit notes is marked as such. A claim is *Not supported* only when Moderate or Strong evidence contradicts it, or when it breaks a leakage or evaluation rule that RP3 or RP4 rates Medium or High confidence, or when reading the code in the note shows it cannot work as described (marked "code inspection").
- **Sources:** 72 lit notes cited (17 Strong, 41 Moderate, 11 Weak, 3 primary documentation), all scored in RP1–RP4 with the guide's rubric. RP5 adds no new lit notes.
- **Review steps:** paper-critique run on the draft and fixed (thesis overall verdict narrowed from Not supported to Partly supported, since only one of its claims is contradicted; code-inspection rule added to the verdict scale; abstract trimmed; §6 verdict reworded). Citation check: all 72 references resolve to existing lit notes, each verified by lookup during RP1–RP4; every reference is cited in the body; each attached claim was re-read against the RP section it came from; two misattributions were fixed (Bergmeir 2018 replaced, since it supports k-fold validity for well-specified autoregressions; Huang 2023 supplemented with Xu 2021 for the GNN-vs-no-graph comparison).

## Findings

### RP5.1 – Project Thesis claims

**Verdict: Partly supported; its central profitability claim is Not supported** (one claim contradicted, one partly supported, four untested). Confidence: Medium.

| Thesis claim | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| Real-time, multi-horizon AI forecasting, with horizons and parameters "dynamically adjusted based on portfolio potential returns" | Partly supported | RP1 RQ1.1, RQ1.12; RP4 RQ4.1, RQ4.2 | Forecasting volatility at several horizons is well supported: random forests and neural nets beat HAR for realised variance, with larger gains at weekly and monthly horizons ([[Christensen 2023 Machine Learning Volatility Forecasting]]), while zero-shot foundation models mostly do not beat Log-HAR ([[Brini 2026 TSFMs vs Econometric Realized Volatility]]). Return forecasts beat a random walk only narrowly (monthly R²oos about 0.3–0.4%; [[Gu 2020 Empirical Asset Pricing Machine Learning]]; [[Rahimikia 2025 ReVisiting TSFMs in Finance]]; [[Noguer i Alonso 2026 Pretrained TSFMs Return Forecasting]]). "Real time" earns nothing on scheduled public news in liquid US stocks, which is priced within milliseconds to minutes ([[Chordia 2018 Low-Latency Trading Macro Announcements]]). Choosing horizons and parameters by realised portfolio returns is a search over many configurations, so it needs nested selection and a trial-count correction ([[Bailey 2014 Deflated Sharpe Ratio]], [[Bailey 2017 Probability of Backtest Overfitting]]). |
| Dynamic portfolio optimisation with Black-Litterman, robust Bayesian allocation and multi-horizon views | Untested | RP4 RQ4.6 (indirect) | No RP studied these methods. Related evidence counsels caution. An end-to-end policy only matched equal weighting net of costs ([[Pollok 2026 End-to-End Policies vs Simple Rules]]). Convex optimisers fed ML forecasts did worse than a passive portfolio ([[Go 2026 FinPILOT Inference-Time Planning RL]]). Models tied on forecast error can differ by up to 58% in turnover ([[Cortesi 2026 Optimizer as Implicit Prior]]). Any optimiser therefore needs 1/N and buy-and-hold baselines (RP4 protocol). |
| Automated execution with stop-loss, buying-power and cash-threshold rules | Untested | — | No RP studied stop-loss or exposure rules. Live-trading evidence shows backtest rankings reversing in paper and live trading ([[Yu 2026 AI Crypto Backtest to Live Gap]]); this argues for staged paper trading before any execution layer. |
| Explainability with Captum | Untested | RP1 RQ1.7 (indirect) | No RP studied attribution methods. Text-on/text-off ablations did not show that models use text content ([[Sridhar 2026 Text Sensitivity Audit Multimodal TS]]). This suggests that attributions need placebo checks too, but nothing read tests Captum. |
| CuPy, Celery, async and multiprocessing stack | Untested | — | Engineering choices, outside the research questions. |
| "Consistent profitability in volatile markets" | Not supported | RP1 RQ1.1, RQ1.9; RP4 RQ4.6 | In the best-designed tests, gross gains turn negative at realistic costs. Every daily-rebalanced model is negative at 20 bps ([[Rahimikia 2025 ReVisiting TSFMs in Finance]]). The best gross ML portfolio could not be implemented ([[Jensen 2026 ML Implementable Efficient Frontier]]). Constrained models have negative net Sharpe at 20 bps ([[Zhang 2026 Deep TS Models Equity Portfolios]]). Predictability vanishes in high-volatility states (RP1 RQ1.1). No source read reports consistent net profits from an automated ML system. |

**What would change it:** a walk-forward, cost-inclusive test of Black-Litterman or robust Bayesian allocation fed by ML views against 1/N. The thesis's architecture and stack could be judged once a v2 states what it wants to forecast, at what horizon and with what success test.

### RP5.2 – Sentiment module design

**Verdict: Partly supported.** Confidence: Medium (several parts rest on Weak notes; marked below).

| Design choice | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| Model roles: FinBERT (finbert-tone), nlptown BERT and VADER score sentiment; LegalBERT and SciBERT give embeddings only | Partly supported | RP1 RQ1.3, RQ1.14 | FinBERT as the main scorer is supported. Fine-tuned FinBERT beat a dictionary net of costs and ran 13× faster than an 8B LLM ([[Kirtac 2026 MFAST News Trading Under Frictions]]). FinBERT had the best one-day rank IC among classifiers in one study ([[Luo 2026 QLoRA Sentiment Return Predictability]], Weak). It also had the largest one-day lead on X posts ([[Aravinthakshan 2026 Human Agreement vs Return Association]]). VADER is not supported: dictionary/lexicon scores are the weakest return signal wherever tested, and VADER carried nothing on r/WallStreetBets ([[Kilian 2026 LLM vs Lexicon Meme Stocks]], Weak; RP1 RQ1.3, High confidence). No source tests the nlptown model, which is trained on product-review star ratings (model card name in the code; not a finance model), or LegalBERT/SciBERT embeddings for market targets: Untested. Keeping LegalBERT and SciBERT out of the sentiment score is consistent with their lack of sentiment training. |
| Hand-set domain weights (financial 0.75 FinBERT / 0.25 VADER; general 0.65 BERT / 0.35 VADER; legal and technical 0.5 / 0.5) mixed by zero-shot domain probabilities | Not supported | RP1 RQ1.3; RP4 RQ4.3 | No source supports fixed weights, and the evidence on lexicons argues against giving VADER a quarter to a half of the score. Weights chosen by judgement or by label accuracy are not chosen for return value. Label accuracy does not rank tools by return association ([[Bisharat 2026 Evaluating Financial Sentiment AI]], Weak; [[Aravinthakshan 2026 Human Agreement vs Return Association]]; RP1 RQ1.3, High confidence). If weights are kept, they should be fitted on a training period against the target and checked out of sample (RP4 RQ4.1). |
| 3,080-value embedding: four 768-d mean-pooled blocks + 4 VADER scores + 4 domain probabilities, unscaled by default | Partly supported | RP1 RQ1.7, RQ1.14, RQ1.15 | Dense embeddings carry more than a scalar score. Mean-pooled frozen FinBERT embeddings beat a scalar FinBERT score by 17% MSE inside a price Transformer, and mean pooling beat attention pooling ([[Jeong 2026 FinBERT Embeddings vs Scalar Sentiment]], Weak). Leaving scaling off by default is consistent with the RQ1.15 finding that corrupted inputs make models worse than price-only. But scalar sentiment adds little to strong price baselines ([[Lis 2026 ModernFinBERT News Volatility HAR]]; [[Foley 2026 NoLBERT News Topics Returns]]), and added inputs help only through a gated or compressed pathway on top of a strong price model (RP1 RQ1.7, RQ1.15, High/Medium). Encoders fine-tuned on return labels gave the clearest cross-sectional signal ([[Kirtac 2026 MFAST News Trading Under Frictions]]); the module's encoders are trained on tone labels, not returns. |
| PCA per block, fitted on the training period only, standardised, saved and reused | Supported | RP3 RQ3.6; RP4 RQ4.1 | Fitting preprocessing on the training period is the correct rule, but RP3 found it to be a small leak: fitting scalers, PCA or encoders on all data changed AUC by under 0.005 across 2,047 iid datasets, far less than choosing models on test results ([[Roth 2026 Which Leakage Types Matter]], non-finance), and random rather than chronological splits inflated news-direction MCC 1.1–6.5× ([[Xue 2026 Temporal Leakage Financial News NLP]]). So this choice is right but not the main risk. The main look-ahead risk sits in the pretrained encoders and the zero-shot classifier. Their training cutoffs must precede the test window, or a dated encoder must be used ([[Lopez-Lira 2025 LLM Memorization Problem]]; [[Foley 2026 NoLBERT News Topics Returns]]; RP1 RQ1.14(c), Medium). The design note does not record those cutoffs. |
| Long text: 512-token chunks, stride 64, max 8 chunks, averaged by token count | Untested | — | No source compares chunking schemes for return or volatility targets. Capping at 8 chunks (about 3,600 tokens) truncates long filings; whether that loses signal is untested. |

**Also from RP1:** daily sentiment decays within one to two days ([[Heston 2017 News vs Sentiment Returns]]; RP1 RQ1.3, High). Social attention and volume carry more than social sentiment ([[Cookson 2024 The Social Signal]]). The module produces one score per text; how scores are aggregated in time and by source is where the evidence says the value is, and it is not yet designed.

**What would change it:** a walk-forward test of the module's score and embeddings against returns and realised volatility, beside a price-only model and a FinBERT-only score, on text after the encoders' cutoffs.

### RP5.3 – Sentiment testing script

**Verdict: Partly supported.** Confidence: Medium.

| Script feature | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| Performance tests: load time, cold vs cached latency, determinism check, throughput at batch 1/8/32 | Supported | RP4 RQ4.7 | Logging seeds and checking that repeated runs give identical outputs is recommended practice (RP4 RQ4.7). The tests suit an engineering check. |
| Accuracy tests: 3-class accuracy, macro F1, Spearman correlation, confusion matrix against human labels, per model and for the ensemble | Partly supported | RP1 RQ1.3; RP4 RQ4.3 | These are the right metrics for label agreement, and macro F1 suits imbalanced classes. But label agreement is not evidence of market value: twelve tools differed widely on labelled accuracy, yet none predicted next-day returns ([[Bisharat 2026 Evaluating Financial Sentiment AI]], Weak); human agreement did not rank return association ([[Aravinthakshan 2026 Human Agreement vs Return Association]]); and the most accurate classifier was not the best predictor ([[Luo 2026 QLoRA Sentiment Return Predictability]], Weak). |
| Fixed neutral band ±0.2 to map scores to classes | Partly supported | RP4 RQ4.1 | A threshold tuned on the evaluation set inflates accuracy; it should be chosen on a separate split. The script keeps it as a parameter, which allows this. |
| Labelled-data needs: small built-in smoke sample; `--labelled` CSV (Financial PhraseBank suggested) | Partly supported | RP1 RQ1.3, RQ1.14(c) | The script itself says the built-in sample is a smoke check, not a benchmark. A public labelled set may overlap the encoders' fine-tuning data; whether finbert-tone saw PhraseBank was not checked (see Assumptions). |
| Missing: any test against market outcomes | Not supported (gap) | RP4 RQ4.2, RQ4.3 | RP4's metric for a return signal is out-of-sample R² or rank IC by horizon, with a Clark–West test against a nested price-only baseline and an FDR or FWER correction across the many model × horizon tests ([[Clark 2007 Tests for Nested Model Predictive Accuracy]]; [[Harvey 2016 Cross-Section Expected Returns Multiple Testing]]). In one study, none of 28 tests survived FDR ([[Luo 2026 QLoRA Sentiment Return Predictability]]). A shuffled-text placebo is also needed ([[Sridhar 2026 Text Sensitivity Audit Multimodal TS]]). |

**What would change it:** adding a return-based test (decay curve by day, IC with FDR, placebo) would make the script a test of the module's purpose rather than of its agreement with annotators.

### RP5.4 – Autoencoder imputation plan

**Verdict: Not supported.** Confidence: Medium (RP3 RQ3.4).

| Part of the plan | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| Hybrid TST-LSTM autoencoder trained on the last 5 days of real 1-minute bars, then used to fill coarser intervals | Not supported | RP3 RQ3.4 | The plan as written fills NaNs with 0 before scaling and fits the scaler on the whole frame (chat code: `scaler.fit_transform(df.fillna(0))`, `df['1m'].fillna(0)`). Zero filling creates false zero returns that cut measured volatility by about 20% ([[Muhammad 2026 Temporal Coverage Bias Panel Data]]). A reconstruction model that sees both sides of a gap uses future values, which leaks the test period ([[Blanchet 2023 Imputation Look-Ahead-Bias Variance Tradeoff]]; [[Bryzgalova 2025 Missing Financial Data]]). |
| Filling 25 years of 1-minute bars from sparser history | Not supported | RP3 RQ3.4 | Daily bars do not pin down the intraday path. Generated history understates tails and hurts direction prediction ([[Dezons 2026 Synthetic Augmentation Financial ML]]; [[He 2026 TimeGAN Scenarios Rachev Portfolios]]). Models trained on data cannot extrapolate to events larger than those seen ([[Sun 2024 AI Weather Gray Swan Cyclones]]). RP3's answer: impute from the past only, flag imputed values, and model at the frequency the data has. |
| The "99.999% accuracy" premise | Not supported | RP1 RQ1.1; RP3 RQ3.4 | Reconstruction accuracy on smooth price levels is not forecasting skill. Out-of-sample return predictability is a fraction of a percent of variance ([[Gu 2020 Empirical Asset Pricing Machine Learning]]). Better imputation buys only a small improvement in prediction (RP3 RQ3.4). |

The archived note stays in `99 Archive/`.

### RP5.5 – A\*/TD3/MAML prototype

**Verdict: Not supported.** Confidence: Medium for the method verdict (RP1 RQ1.9); High for the leakage and data issues, which are visible in the code.

| Component or issue | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| TD3 (deep RL) as the trading policy | Not supported | RP1 RQ1.9 (High) | Five standard pre-trained agents including TD3 had lower Sharpe than buy-and-hold in 2023–2025 ([[Go 2026 FinPILOT Inference-Time Planning RL]]). The best-designed tests find RL matching 1/N at best and losing live ([[Pollok 2026 End-to-End Policies vs Simple Rules]]; [[Yu 2026 AI Crypto Backtest to Live Gap]]). Reported RL wins share look-ahead, survivorship and seed fragility ([[Pippas 2025 RL in Quantitative Finance Survey]], Weak; [[Gort 2022 DRL Crypto Backtest Overfitting]], Weak). |
| A\* search over a graph built from the replay buffer | Not supported (Untested as a method) | RP1 RQ1.9 | No A\* forecasting or trading study was found. Planning helped only where a model of the dynamics exists and the objective is non-convex ([[Maggiolo 2025 Deep Hedging Non-Convexity AlphaZero]], Weak), or as a decision layer on top of a forecast ([[Go 2026 FinPILOT Inference-Time Planning RL]]). |
| Exact-match state graph: nodes are `tuple(state)` of continuous vectors | Not supported | Code inspection | Continuous market states almost never repeat exactly, so the graph has almost no paths and the agent falls back to the actor network. The code logs this fallback. |
| Negative edge costs: edge weight = −reward | Not supported | Code inspection | A\* assumes non-negative edge costs and an admissible heuristic; with negative costs its optimality guarantee fails (standard algorithm property; no lit note, see Assumptions). The heuristic is a grid distance on state coordinates, which has no link to reward. |
| Made-up replay transitions in the MAML inner loop | Not supported | Code inspection | `inner_loop` adds transitions with `action = torch.zeros(1)` and `next_state = torch.rand(5)`, so TD3 trains on invented dynamics. |
| About 21 rows of test data | Not supported | Code inspection; RP4 RQ4.1 | `yf.Ticker("MSFT").history(period='1mo')` gives about 21 daily rows, one fewer after the shift. No test on one stock and one month can show skill (RP4 sample-breadth and validation rules). |
| **New: target leakage in the inputs** | Not supported | Code inspection; RP3 RQ3.1 | `df_history` gains `Target_Open` and `Target_Close` (next day's open and close), and the whole frame becomes the tensor. `create_tasks` takes all columns but the last as inputs, so `Target_Open`, the next day's open, is an input when predicting the next close. This is the decision-time leakage that RP3 ranks largest ([[Zhang 2026 When Alpha Disappears Decision-Time Leakage]]). |
| **New: shuffled support/query split** | Not supported | Code inspection; RP4 RQ4.1 | Support and query sets come from `torch.randperm`, mixing future and past days. RP4 rules out shuffled splits for time series: shuffled k-fold with overlapping labels produced R² 0.83–0.91 on a target built to be unpredictable ([[purgedcv 2026 Purged Cross-Validation Library]]), and random rather than chronological splits inflated news-direction MCC 1.1–6.5× ([[Xue 2026 Temporal Leakage Financial News NLP]]). Selection must also be nested inside an untouched causal test ([[Nikolopoulos 2026 Spurious Predictability Financial ML]]). |
| **New: learning-rate values** | Not supported | Code inspection | Default `inner_lr` and `outer_lr` are 1e4/5e4 (market open) and 1e3/1e4 (market closed). They are probably meant to be 1e-4 and similar; as written they would diverge. |
| MAML meta-learning across tasks | Not supported | RP1 RQ1.9 (Low); RP4 RQ4.9 (Low) | Only two Weak finance studies, both single short windows without costs ([[Liu 2025 Robust Meta-Learning Zero-Shot Financial]]; [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]]). Light adaptation matched or beat heavy adaptation ([[Wu 2026 Test-Time Adaptation Non-stationary Markets]]; [[Pan 2026 ReCAP Regime-Adaptive Continual Learning]]; [[Nguyen 2026 Volatility-Clustering Adaptation]], Weak). |
| Market-open vs market-closed hyperparameter sets | Untested | — | No source tests session-dependent RL settings. |

The archived notes stay in `99 Archive/`.

### RP5.6 – Gemini/NotebookLM notebook rebuild plan

**Verdict: Partly supported.** Confidence: Medium.

The plan merges notebooks into three masters: an automated trading and portfolio framework, "TD3, MAML & Optimization", and "Hybrid TST-LSTM Autoencoder" imputation. Consolidating is sensible. The three topics, though, are the families that the research rates weakest. Deep RL has no robust edge (RP1 RQ1.9, High). MAML evidence is Weak (RP1 RQ1.9, RP4 RQ4.9). The TST-LSTM imputation plan is not supported (RP5.4). None of the families RP1 found evidence for has a notebook: strong price baselines (GBT, HAR), finance foundation and token models (RQ1.1, RQ1.10, RQ1.13), text encoders and their point-in-time control (RQ1.3, RQ1.14), company graphs and neighbour features (RQ1.4), news novelty and fragility (RQ1.5, RQ1.8), tail risk (RQ1.6) and gated fusion (RQ1.7, RQ1.15). The guide's final vault updates will rewrite the plan with one notebook per RP1 family. That step follows the Synthesis and is not done here.

### RP5.7 – Financial Foundation Model Research Direction (2026-11-07)

**Verdict: Partly supported.** The note frames itself as hypotheses, and most of its own caveats match what the research found. Confidence: Medium for most parts, Low for adaptation and pretraining (as in RP4).

| Section of the note | Verdict | Evidence | Note |
| --- | --- | --- | --- |
| §1, §14 Central hypothesis: a joint world + behaviour + information model generalises better than price-only | Partly supported | RP1 RQ1.7, RQ1.15 | Added macro, cross-asset or graph state helps modestly only when compressed and fed through a structured pathway (regime attention, gating, bounded correction to a strong local model). Naive concatenation hurts, and corrupted feeds are worse than price-only ([[Ye 2026 Regime-Gated Residual MoE Volatility]]; [[Merchant 2026 Towards Financial World Modeling]]; [[Zhang 2025 When Multimodality Helps TS Forecasting]]). No combined multi-source world model has been tested against price-only in finance (RQ1.15: thin). |
| §2.1, §5 Tokenizer: discrete tokens vs continuous inputs, bins vs VQ vs hybrid | Partly supported | RP1 RQ1.10, RQ1.13 | A categorical output over volatility-normalised return buckets is a sound target ([[Shi 2025 Kronos Financial Foundation Model]]; [[Ma 2026 VAIOM Continuous-Input Discrete-Output]]). No matched finance test shows token inputs beating continuous ones. Sampled and quantile forecasts from foundation models were off by more than ten times the nominal tail probability at the 1% quantile ([[Decker 2026 Calibration of Probabilistic TSFMs]]). With walk-forward folds and an always-up base rate, TimesFM, zero-shot or LoRA-adapted, showed no directional skill on US equities ([[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]]); RP1 RQ1.13 rates Low the claim that autoregressive token models beat strong per-series baselines. The note's own required ablation (§5, §9.2 continuous vs discrete) is exactly what the evidence says is missing. |
| §2.2 Temporal knowledge graph of companies, people, ownership, supply chains | Partly supported | RP1 RQ1.4; RP2 RQ2.8; RP3 RQ3.7, RQ3.8 | Linked-firm returns predict returns and shocks spread along supply chains ([[Cohen 2008 Economic Links Predictable Returns]]; [[Barrot 2016 Input Specificity Shock Propagation]]; RQ1.4, High). GNNs show no clear gain over simple neighbour features: on CSI 300 a GAT over concept graphs scored IC 0.111 against 0.113 for a GRU with no graph ([[Xu 2021 HIST Concept Graph Stock Forecasting]]), and persistence or moving-average heuristics beat a temporal GNN on all node tasks of a non-market benchmark ([[Huang 2023 Temporal Graph Benchmark]]; RQ1.4, Medium). Customer-supplier and board data are paid, incomplete and carry valid time only (RP2 RQ2.8). |
| §2.3 Behaviour modelling: regimes, distributions, multiple timeframes | Partly supported | RP1 RQ1.1, RQ1.6 | Regime information helps volatility forecasts, and predictability depends on regime (RQ1.1). Volatility-filtered fat-tailed models are the tail baseline. No method stays calibrated at shock onset (RQ1.6, High). |
| §3.4, §4 Global event intelligence and early warning | Partly supported | RP1 RQ1.5, RQ1.8, RQ1.11, RQ1.12 | News novelty forecasts volatility and returns at monthly horizons ([[Glasserman 2023 New News is Bad News]]). Credit and price booms raise crisis probability over months to years ([[Greenwood 2022 Predictable Financial Crises]]). Shock timing is not predictable, and event-level alarms are unreliable ([[Garcia Seuma 2026 Crypto Cascade Early Warning]]; RQ1.8, High). The note's own caveat that a true black swan is hard to predict matches this. |
| §4.3 Corroboration vs repetition; bots and campaigns | Partly supported | RP1 RQ1.11 | Repetition is measurable by textual overlap (RQ1.11, Medium). Fake articles lifted small-firm prices before reversing, and a linguistic deception score missed about 90% of SEC-identified fakes ([[Kogan 2023 Social Media Financial News Manipulation]]). Perplexity filters catch default LLM-written fakes but not ones sampled at higher temperature ([[Lu 2026 Corroboration Illusion News Poisoning]]). Evidence on detecting independent corroboration in finance is thin. |
| §4.5 What is already priced in (derivatives, overseas markets) | Supported | RP1 RQ1.12 | The note's warning holds. Scheduled news in liquid stocks is priced within milliseconds to minutes ([[Chordia 2018 Low-Latency Trading Macro Announcements]]). Pre-announcement drift and option volume carry anticipation ([[Lucca 2015 Pre-FOMC Announcement Drift]]; [[Pan 2006 Option Volume Future Stock Prices]]). |
| §6 Training objectives beyond next-token prediction | Not yet shown (Low) | RP4 RQ4.8 | No objective has been shown to beat next-token or direct training under a strong financial test. Derived-target reconstruction is the most promising lead ([[Chen 2026 DIVINE Indicator Reconstruction Pretraining]]). Pretraining must be compared with a random-init twin ([[Sungu Isiacik 2026 Random Initialization TSFM Baseline]]). |
| §7 MAML-inspired continual adaptation | Not supported so far (Low) | RP1 RQ1.9; RP4 RQ4.9 | No adaptation method reliably improves market forecasts under a leak-free test. Under delayed labels, published test-time adapters gain at most 0.5% ([[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]], non-finance). Periodic retraining is the baseline to beat ([[Dasari 2026 When to Retrain Drift Policies]], non-finance). MAML has only two Weak finance studies ([[Liu 2025 Robust Meta-Learning Zero-Shot Financial]]; [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]]). |
| §7.1, §12 Guardrails: context is not learning; keep foundation and adapted states separate; evaluate adaptation leak-free | Supported | RP4 RQ4.9 | The evidence that cheap, controlled adaptations are the ones that survive ([[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]]), and that leakage creates most reported gains ([[Fujimoto 2026 Leakage-Free Online Adaptation Edge]]), backs these rules. |
| §8 Temporal integrity: valid time vs knowledge time | Supported | RP2 RQ2.3, RQ2.5; RP3 RQ3.1, RQ3.8 | Tickers are reused and names change, so joins need dated permanent IDs ([[Stanford GSB 2026 CRSP Names File FAQ]]). The standard model keeps valid time and record time as separate axes ([[Jensen 1995 TSQL2 Data Model]]). Vendors give valid time but rarely knowledge time, and CRSP rewrites history in place (RP3 RQ3.8), so the project must stamp first-seen times and keep vintages itself (RQ3.8, High/Medium). |
| §9 Evaluation requirements, baselines and ablations | Supported | RP4 RQ4.1–RQ4.6 | RP4's protocol covers every item in §9.1. It adds trial-count corrections, nested baselines (random walk, GBT, HAR, 1/N) and placebo controls that §9.2 does not list. |
| §10–§11 Architecture and build phases | Not reviewed | — | Input to the methodology plan, per the guide. |

The Synthesis will set out the evidence for each of §13's ten open decisions and each §9.2 ablation.

### RP5.8 – Algorithmic Trading essays

**Not reviewed** (out of scope, per the guide). Files: `99 Archive/Essays/Algorithmic Trading Ethics and Self-Defense.md` and `Market Transformation - A Vision of Stability and Ethical Investment.md`. They stay in `99 Archive/`.

### Summary of verdicts

| ID | Item | Verdict |
| --- | --- | --- |
| RP5.1 | Project Thesis | Partly supported (profitability claim Not supported; forecasting partly supported; portfolio, explainability, execution and stack Untested) |
| RP5.2 | Sentiment module design | Partly supported |
| RP5.3 | Sentiment testing script | Partly supported |
| RP5.4 | Autoencoder imputation plan | Not supported |
| RP5.5 | A\*/TD3/MAML prototype | Not supported |
| RP5.6 | Notebook rebuild plan | Partly supported |
| RP5.7 | Foundation-model research direction | Partly supported |
| RP5.8 | Algorithmic Trading essays | Not reviewed |

No archived item is rated Supported, so nothing moves out of `99 Archive/`.

## Cross-cutting observations

- **The earliest material is the least supported.** The thesis, the imputation chat and the prototype aim at profit, near-perfect reconstruction and complex agents. The later direction note frames hypotheses, demands ablations and guards against look-ahead, and it holds up best.
- **Leakage is the recurring defect.** It appears as next-day open in the prototype's inputs, shuffled support/query splits, zero filling with whole-frame scaling in the imputation plan, and undocumented encoder cutoffs in the sentiment module. The one strong design choice in the vault, train-only PCA, guards against a small leak while the larger ones are untreated.
- **Tests measure the wrong target.** The sentiment script tests agreement with annotators. The imputation plan targets reconstruction accuracy. The prototype logs critic loss. None tests forecast value against a strong baseline, which RP1–RP4 found to be the deciding comparison.
- **Untested is not refuted.** Black-Litterman, robust Bayesian allocation, Captum, the chunking scheme and the session-dependent settings were never researched. They need their own tests before a v2 relies on them.

## Contradictions and evidence gaps

- **Contradiction inside the sentiment module:** the design note states the aim of domain-specific vocabulary, yet the sentiment weights still give VADER, a generic lexicon, 25–50%. The evidence on lexicons (RP1 RQ1.3) argues against that share.
- **Thin evidence behind some verdicts:** VADER, attention vs mean pooling and the sentiment label-vs-return gap rest partly on Weak notes (Kilian 2026, Jeong 2026, Bisharat 2026, Luo 2026). The direction is consistent across studies, so the verdicts stand at Medium.
- **Gaps (no RP evidence):** Black-Litterman and robust Bayesian allocation fed by ML views; attribution methods (Captum) in finance; text chunking for long filings; the nlptown review-star model on financial text; session-dependent RL settings; stop-loss and exposure rules.
- **Gaps carried from RP1–RP4:** the working-paper and abstract-only reads listed in their Assumptions sections also underlie some verdicts here (e.g. Chordia 2018, Lucca 2015, Pan 2006 in RP5.1 and RP5.7).

## Assumptions made during the research

1. **Item IDs.** The guide gives RP5 no numbered RQs. Each vault item is treated as one question with IDs RP5.1–RP5.8, so that [[Research Questions]] can link to the answers.
2. **No new searching.** No gap was judged worth a new search under the guide's rule. The untested thesis components (Black-Litterman, Captum, Celery) are outside the RP1–RP4 questions; searching for them would open a new research question rather than settle a gap. They are listed for the methodology plan instead.
3. **Code inspection as evidence.** The prototype and sentiment verdicts partly rest on reading the code in the vault notes, not on lit notes. Line references are to the archived notes as read on 2026-11-09. The A\* statement about negative edge costs is a standard property of the algorithm. No lit note was written for it, because it is textbook material, not a finance finding.
4. **Sentiment design source.** The design was read from [[Sentiment Analysis Source Code]] (including its "design decisions" section) and the matching project doc `claude/sentiment-module-design.md`; the two agree.
5. **Unchecked fact.** Whether `yiyanghkust/finbert-tone` was fine-tuned on Financial PhraseBank (so that PhraseBank would overstate its accuracy) was not checked. It is flagged as a check for the methodology plan, not asserted.
6. **nlptown model.** The statement that it is trained on product-review star ratings rests on the model's name and its 1–5 star output, which the code parses (`_STAR_RE`). The model card was not opened in this session.
7. **The imputation chat (99 KB)** was read in its workflow, 25-year and "99.999%" sections and code cells, located by search, not line by line. The earlier RP3 RQ3.4 answer, which reviewed the same plan, was relied on for the rest.
8. **Thesis summaries** in `99 Archive/Thesis summaries/` duplicate the thesis (guide Step 0) and were covered by RP5.1, not reviewed separately.

## Open questions for the methodology plan

1. Should the thesis v2 drop "consistent profitability" in favour of a stated forecasting target, horizon and success test (e.g. Clark–West against a random walk, QLIKE against HAR, net Sharpe against 1/N)?
2. Should the sentiment score's model weights be learned on a training period against returns and volatility, with VADER's share tested rather than fixed?
3. Which encoders have documented training cutoffs before the intended test window, or should dated encoders be used?
4. Should the sentiment testing script gain a return-based test (decay curve, rank IC with FDR, shuffled-text placebo), so that it tests the module's purpose?
5. Is any portfolio layer (Black-Litterman, robust Bayesian, simple risk parity) needed at all in the first build, given that 1/N is the baseline that most methods fail to beat net of costs?
6. Does anything in the A\*/TD3/MAML prototype survive into the build, given that every component is Not supported, or is it fully superseded by the direction note's adaptation plan?
7. Which of the direction note's §9.2 ablations come first, given the evidence gaps (continuous vs token inputs; with vs without the knowledge graph; context vs parameter adaptation)?

## References

All sources were scored in RP1–RP4; scores are in each lit note's properties and the [[Evidence Register]].

- [[Aravinthakshan 2026 Human Agreement vs Return Association]]
- [[Bailey 2014 Deflated Sharpe Ratio]]
- [[Bailey 2017 Probability of Backtest Overfitting]]
- [[Barrot 2016 Input Specificity Shock Propagation]]
- [[Bisharat 2026 Evaluating Financial Sentiment AI]]
- [[Blanchet 2023 Imputation Look-Ahead-Bias Variance Tradeoff]]
- [[Brini 2026 TSFMs vs Econometric Realized Volatility]]
- [[Bryzgalova 2025 Missing Financial Data]]
- [[Chen 2026 DIVINE Indicator Reconstruction Pretraining]]
- [[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]]
- [[Chordia 2018 Low-Latency Trading Macro Announcements]]
- [[Christensen 2023 Machine Learning Volatility Forecasting]]
- [[Clark 2007 Tests for Nested Model Predictive Accuracy]]
- [[Cohen 2008 Economic Links Predictable Returns]]
- [[Cookson 2024 The Social Signal]]
- [[Cortesi 2026 Optimizer as Implicit Prior]]
- [[Dasari 2026 When to Retrain Drift Policies]]
- [[Decker 2026 Calibration of Probabilistic TSFMs]]
- [[Dezons 2026 Synthetic Augmentation Financial ML]]
- [[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]]
- [[Foley 2026 NoLBERT News Topics Returns]]
- [[Fujimoto 2026 Leakage-Free Online Adaptation Edge]]
- [[Garcia Seuma 2026 Crypto Cascade Early Warning]]
- [[Glasserman 2023 New News is Bad News]]
- [[Go 2026 FinPILOT Inference-Time Planning RL]]
- [[Gort 2022 DRL Crypto Backtest Overfitting]]
- [[Greenwood 2022 Predictable Financial Crises]]
- [[Gu 2020 Empirical Asset Pricing Machine Learning]]
- [[Harvey 2016 Cross-Section Expected Returns Multiple Testing]]
- [[He 2026 TimeGAN Scenarios Rachev Portfolios]]
- [[Heston 2017 News vs Sentiment Returns]]
- [[Huang 2023 Temporal Graph Benchmark]]
- [[Jensen 1995 TSQL2 Data Model]]
- [[Jensen 2026 ML Implementable Efficient Frontier]]
- [[Jeong 2026 FinBERT Embeddings vs Scalar Sentiment]]
- [[Kilian 2026 LLM vs Lexicon Meme Stocks]]
- [[Kirtac 2026 MFAST News Trading Under Frictions]]
- [[Kogan 2023 Social Media Financial News Manipulation]]
- [[Lis 2026 ModernFinBERT News Volatility HAR]]
- [[Liu 2025 Robust Meta-Learning Zero-Shot Financial]]
- [[Lopez-Lira 2025 LLM Memorization Problem]]
- [[Lu 2026 Corroboration Illusion News Poisoning]]
- [[Lucca 2015 Pre-FOMC Announcement Drift]]
- [[Luo 2026 QLoRA Sentiment Return Predictability]]
- [[Ma 2026 VAIOM Continuous-Input Discrete-Output]]
- [[Maggiolo 2025 Deep Hedging Non-Convexity AlphaZero]]
- [[Merchant 2026 Towards Financial World Modeling]]
- [[Muhammad 2026 Temporal Coverage Bias Panel Data]]
- [[Nguyen 2026 Volatility-Clustering Adaptation]]
- [[Nikolopoulos 2026 Spurious Predictability Financial ML]]
- [[Noguer i Alonso 2026 Pretrained TSFMs Return Forecasting]]
- [[Pan 2006 Option Volume Future Stock Prices]]
- [[Pan 2026 ReCAP Regime-Adaptive Continual Learning]]
- [[Pippas 2025 RL in Quantitative Finance Survey]]
- [[purgedcv 2026 Purged Cross-Validation Library]]
- [[Pollok 2026 End-to-End Policies vs Simple Rules]]
- [[Rahimikia 2025 ReVisiting TSFMs in Finance]]
- [[Roth 2026 Which Leakage Types Matter]]
- [[Shi 2025 Kronos Financial Foundation Model]]
- [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]]
- [[Stanford GSB 2026 CRSP Names File FAQ]]
- [[Sun 2024 AI Weather Gray Swan Cyclones]]
- [[Sungu Isiacik 2026 Random Initialization TSFM Baseline]]
- [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]]
- [[Wu 2026 Test-Time Adaptation Non-stationary Markets]]
- [[Xue 2026 Temporal Leakage Financial News NLP]]
- [[Ye 2026 Regime-Gated Residual MoE Volatility]]
- [[Yu 2026 AI Crypto Backtest to Live Gap]]
- [[Xu 2021 HIST Concept Graph Stock Forecasting]]
- [[Zhang 2025 When Multimodality Helps TS Forecasting]]
- [[Zhang 2026 Deep TS Models Equity Portfolios]]
- [[Zhang 2026 When Alpha Disappears Decision-Time Leakage]]
