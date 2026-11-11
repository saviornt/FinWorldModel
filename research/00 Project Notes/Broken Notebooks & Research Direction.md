---
type: project-note
status: current
updated: 2026-11-09
---
# Notebook rebuild plan (revised 2026-11-09)

Revised after the research phase, as the guide's final vault updates require: one notebook per RP1 method family. Each notebook's sources are the lit notes for that family in `01 Research/Lit Notes/` (filter the [[Evidence Register]] by family), and its summary is the RP1 section named. Why the old plan changed: [[RP5 Vault Review#RP5.6 – Gemini/NotebookLM notebook rebuild plan|RP5.6]] found its three masters centred on the weakest-evidenced families. Cross-paper findings: [[Multimodal Financial Forecasting and Shock Detection (Final)]].

| # | Notebook (RP1 method family) | Evidence strength (RP1) | Seed with | RP sections |
| --- | --- | --- | --- | --- |
| 1 | Statistical and econometric baselines (random walk, AR, HAR, GARCH-t, EVT, logit) | Strong | `price-time-series`, `tail-risk` lit notes | [[RP1 ML Methods]] RQ1.1, RQ1.6, RQ1.8 |
| 2 | Gradient-boosted trees and random forests | Strong (returns), Moderate (volatility) | `price-time-series` | RP1 RQ1.1, RQ1.4 |
| 3 | Deep nets trained from scratch | Moderate | `price-time-series` | RP1 RQ1.1 |
| 4 | Time-series foundation models | Strong that generic ones mostly fail; Moderate otherwise | `price-time-series` | RP1 RQ1.1, RQ1.13 |
| 5 | Autoregressive token models and tokenization | Moderate studies, Low confidence | `price-time-series` (tag `tokenization`) | RP1 RQ1.10, RQ1.13; [[RP4 Training and Evaluation]] RQ4.8 |
| 6 | Text encoders and sentiment (incl. point-in-time encoders) | Strong for both the positive and the null | `sentiment`, `llm-text` | RP1 RQ1.2, RQ1.3, RQ1.14 |
| 7 | Novelty, repetition and event detection | Moderate | `novelty-detection` | RP1 RQ1.5, RQ1.11, RQ1.12 |
| 8 | Company graphs | Moderate | `graph` | RP1 RQ1.4; [[RP3 Cleaning and Labelling]] RQ3.7 |
| 9 | Tail and uncertainty methods | Strong | `tail-risk` | RP1 RQ1.6 |
| 10 | Fusion and world state | Medium | `fusion` (tag `world-model`) | RP1 RQ1.7, RQ1.15 |
| 11 | RL, meta-learning and planning | Strong (negative) | `rl-planning` | RP1 RQ1.9; RP4 RQ4.9 |

Supporting notebooks (not RP1 families, optional): data sources and storage ([[RP2 Data Sources and Storage]]; `data-sources`, `storage`), cleaning and labelling (RP3; `cleaning`), evaluation (RP4; `evaluation`).

## Old notebooks no longer needed for the research

Nothing is deleted here; whether to delete the Gemini notebooks is your call.

| Old notebook | Status | Why |
| --- | --- | --- |
| Automated Trading Framework: Real-Time Forecasting & Portfolio Optimization (old master) | No longer needed as a master | Built on the thesis's profitability aim, which is Not supported (RP5.1); its forecasting material moves to notebooks 1–4 |
| AI-Driven Dynamic Portfolio Management System | No longer needed | Duplicates the thesis (RP5.1); portfolio methods are Untested |
| AI-Driven Algorithmic Trading System | No longer needed | Same as above; trading-agent evidence goes to notebook 11 |
| Meta-Learning, TD3, for Financial Modeling (old master) | Superseded by notebook 11 | The A\*/TD3/MAML prototype is Not supported (RP5.5) |
| Hybrid TST-LSTM Autoencoder for Time Series Imputation and Forecasting (old master) | No longer needed | The imputation plan is Not supported (RP5.4; RP3 RQ3.4) |
| Missing Data Imputation Methods | Optional; fold into the cleaning notebook | Imputation evidence lives in RP3 RQ3.4 |

## Previous plan (2026-11-07, kept for reference)

To help you consolidate these thematic clusters smoothly, the best approach is to pick your primary "master" notebook for each cluster and manually pull over your key sources or notes from the overlapping ones.

  

Here are the target master notebooks you can use to centralize each group:

### 2. Algorithmic Trading & Financial Modeling

- **Master Destination:** 📈 [Automated Trading Framework: Real-Time Forecasting & Portfolio Optimization](https://gemini.google.com/notebook/c3b9b12b-25b1-41cb-bcb2-2c8665e124ae)
    
      
    
- **Notebooks to merge in:**
    
      
    - 📈 [AI-Driven Dynamic Portfolio Management System](https://gemini.google.com/notebook/1466b0a8-022b-47ea-93d6-8d652a1bc9b8)
        
          
        
    - 🤖 [AI-Driven Algorithmic Trading System](https://gemini.google.com/notebook/31ce0f94-59a2-4d6f-af75-9f7eddd746f6)
        
          
        

### 3. TD3, MAML & Optimization

- **Master Destination:** 🤖 [Meta-Learning, TD3, for Financial Modeling](https://gemini.google.com/notebook/4e4d8316-1fdc-47e8-a153-d7fb5312368f)

### 4. Time Series & Imputation Methods

- **Master Destination:** ⚖️ [Hybrid TST-LSTM Autoencoder for Time Series Imputation and Forecasting](https://gemini.google.com/notebook/4a1ab578-8f79-4a22-8f6b-974718174398)
    
      
    
- **Notebooks to merge in:**
    
      
    - 📊 [Missing Data Imputation Methods](https://gemini.google.com/notebook/4d70c302-1177-45b5-9d61-68f7ed10828c)
        