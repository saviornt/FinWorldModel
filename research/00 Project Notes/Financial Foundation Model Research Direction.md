---
type: project-note
title: "Financial Foundation Model: Research Direction and Questions"
status: exploratory
created: 2026-11-07
updated: 2026-11-07
related: ["[[Research Questions]]", "[[Multimodal Financial AI Step-by-Step Research Guide]]"]
tags: [project-note, research-direction]
---
# Financial Foundation Model: Research Direction and Questions

**Document type:** Research concept and architectural direction  
**Status:** Exploratory — hypotheses and design proposals, not finalized specifications  
**Last updated:** 2026-11-07

## 1. Research vision

Develop a continually adaptable **financial foundation model** that learns both:

1. **The financial world:** entities, institutions, companies, people, ownership, corporate structures, economic systems, events, and their evolving relationships.
2. **Financial behavior:** how markets and financial entities behave over time, including price and volume dynamics, sentiment, correlations, volatility, liquidity, economic cycles, and responses to new information.

These are complementary learning dimensions of one model, not competing philosophies or necessarily separate models.

The model should learn a broad, time-aware representation of the financial ecosystem and use it to support forecasting, risk analysis, event-impact modeling, anomaly detection, scenario analysis, and other downstream capabilities.

A central research objective is to create a foundational model that can **adapt to new, real-time information without requiring full retraining for every new company, event, market regime, or observation**.

## 2. Core research questions

### 2.1 Financial representation learning

- How should heterogeneous financial information be represented in a unified model?
- Which information should be represented as discrete tokens, continuous numerical features, learned embeddings, graph relationships, or combinations of these?
- How can the model preserve the meaning and scale of numerical data while still benefiting from autoregressive next-token prediction?
- Should numerical features use fixed discretization, learned discretization, vector quantization, or a hybrid tokenizer?
- How should the vocabulary represent different domains without creating an unnecessarily large or brittle token space?
- How can the model represent uncertainty, missing observations, stale data, and conflicting reports?
- Can shared representations capture meaningful relationships between macroeconomic conditions, corporate fundamentals, events, and market behavior?

### 2.2 Financial world modeling

The model should represent the financial world as an evolving system rather than a static collection of tickers and indicators.

Research areas:

- Companies, subsidiaries, parent entities, ownership, and corporate structures.
- Sectors, industries, supply chains, customers, suppliers, competitors, and counterparties.
- Executives, directors, board members, employment histories, board memberships, and relevant professional relationships.
- Financial statements, earnings, guidance, debt, liquidity, capital structure, dividends, buybacks, dilution, and valuation.
- Government institutions, central banks, regulators, and policy relationships.
- Macroeconomic indicators, monetary and fiscal policy, currencies, commodities, and economic cycles.
- Corporate actions, mergers, acquisitions, litigation, regulatory investigations, and management changes.

Questions:

- Should these relationships be represented through a temporal knowledge graph, graph embeddings, serialized relationship tokens, or a hybrid architecture?
- How should the model reason about indirect relationships and second-order effects?
- How should entity identity be maintained across name changes, mergers, reorganizations, and other corporate events?
- How can the model distinguish correlation, exposure, influence, and causation rather than treating all observed relationships as equivalent?

### 2.3 Financial behavior modeling

The model should learn how the financial world behaves dynamically.

Potential inputs:

- OHLCV data across multiple timeframes.
- Returns, volatility, liquidity, spreads, and market breadth.
- Technical indicators and derived features.
- Cross-asset relationships and correlations.
- Earnings surprises, analyst revisions, and institutional positioning where reliable data is available.
- Market and investor sentiment.
- Historical reactions to economic, corporate, and geopolitical events.

Questions:

- What temporal resolutions should be supported?
- How should the model learn relationships across different timeframes?
- Can it distinguish persistent relationships from temporary correlations?
- How should market regimes be represented and detected?
- How can the model predict distributions of future states rather than only point estimates or directional labels?
- How should predictions account for uncertainty and changing market conditions?

## 3. Multidomain data architecture

The model should ingest information from multiple domains while preserving domain-specific meaning and provenance.

### 3.1 Market data

- Open, high, low, close, and volume.
- Returns and price changes.
- Volatility and liquidity.
- Market breadth and cross-asset behavior.
- Corporate-action-aware historical data.
- Multiple timeframes and sampling frequencies.

### 3.2 Macroeconomic data

- Inflation measures, including CPI, PCE, and PPI.
- Interest rates, yield curves, and central-bank decisions.
- Employment and labor-market data.
- GDP and other growth measures.
- Monetary and fiscal policy.
- Currency and commodity markets.
- Economic releases, revisions, and expectations where available.

Macroeconomic observations must preserve their original publication timestamps and subsequent revisions. The model must not use revised values before they were publicly available.

### 3.3 Corporate data

- Income statements, balance sheets, and cash-flow statements.
- Earnings, guidance, and revisions.
- Debt, maturities, liquidity, and capital structure.
- Dividends, buybacks, dilution, and other corporate actions.
- Sector and industry classifications.
- Ownership, subsidiaries, and corporate relationships.
- Executives, directors, board memberships, and employment histories.

### 3.4 Sentiment and global event intelligence

Sentiment should not be limited to positive or negative opinions. It should be part of a broader **Global Event Intelligence and Risk Modeling** capability.

Relevant sources and event classes include:

**Geopolitical events**
- Armed conflicts and military escalation.
- Political instability, elections, and regime changes.
- Sanctions, tariffs, and trade restrictions.
- Diplomatic breakdowns, treaties, and international alliances.
- Territorial disputes and geopolitical tensions.

**Natural events and acts of God**
- Earthquakes, tsunamis, and volcanic eruptions.
- Hurricanes, typhoons, tornadoes, and extreme weather.
- Floods, droughts, wildfires, and crop failures.
- Temperature anomalies and other climate-related disruptions.

**Infrastructure and systemic events**
- Power-grid and telecommunications failures.
- Cyberattacks and critical infrastructure incidents.
- Port, shipping, pipeline, and transportation disruptions.
- Supply-chain interruptions and industrial accidents.

**Corporate and economic events**
- Unexpected executive departures.
- Fraud allegations and regulatory investigations.
- Product failures, labor strikes, and bankruptcy indicators.
- Contract awards, cancellations, and operational disruptions.

**Information and sentiment sources**
- News reporting and official announcements.
- Social media and public discussion.
- Local reporting and eyewitness accounts.
- Analyst commentary and revisions.
- Changes in narrative, attention, and sentiment.
- Contradictory reports, misinformation, and coordinated campaigns.

## 4. Global Event Intelligence and early-warning research

A major research direction is detecting potentially material events before their effects are fully reflected in market prices.

A true black swan is difficult to predict by definition. The more tractable objective is to identify precursors, emerging situations, unusual signals, and converging evidence that may indicate a low-frequency, high-impact event or a developing disruption.

### 4.1 Event lifecycle

The system should distinguish at least these stages:

1. **Occurrence:** An event happens.
2. **Initial observation:** A source reports or observes it.
3. **Corroboration:** Independent sources provide supporting evidence.
4. **Recognition:** The event is classified and assessed.
5. **Dissemination:** The information becomes more widely known.
6. **Market response:** Relevant assets and markets begin reflecting the information.

These stages are not necessarily sequential or cleanly separated. They provide a useful conceptual framework for modeling how information develops.

### 4.2 Event representation

A structured event representation could include:

- Event identity and event class.
- Location and geographic scope.
- Occurrence time and observation time.
- Publication and ingestion timestamps.
- Source identity, type, and provenance.
- Source reliability and independence.
- Corroboration status and conflicting evidence.
- Estimated confidence and severity.
- Escalation, duration, and potential persistence.
- Potentially affected entities, industries, assets, and regions.
- Evidence supporting and contradicting the event.
- Estimated market exposure and possible transmission paths.

Illustrative representation:

```text
EVENT_TYPE: MARITIME_DISRUPTION
EVENT_LOCATION: REGION_001

OCCURRENCE_TIME: UNKNOWN
FIRST_OBSERVED_TIME: T_001
FIRST_PUBLISHED_TIME: T_002

SOURCE_TYPES:
  - SOCIAL_MEDIA
  - LOCAL_NEWS
  - SHIPPING_TRACKER

SOURCE_INDEPENDENCE: UNDER_REVIEW
CORROBORATION_STATUS: PARTIAL

EVENT_CONFIDENCE: 0.72
EVENT_SEVERITY: HIGH
EVENT_ESCALATION: INCREASING

POTENTIAL_EXPOSURES:
  - SHIPPING
  - ENERGY
  - INSURANCE
  - COMMODITIES

MARKET_REACTION: NOT_YET_ESTABLISHED
```

Values are illustrative only. The system should preserve original evidence and uncertainty rather than treating extracted values as established facts.

### 4.3 Signal convergence and source reliability

Research questions:

- How can the system identify independent corroboration rather than count repeated copies of one report?
- How should it identify bots, coordinated campaigns, manipulated narratives, and source dependencies?
- How should it evaluate source reliability by event category and geographic region?
- Can changes in social-media discussion, news volume, shipping data, weather observations, or other external signals provide useful early indicators?
- How should contradictory reports affect confidence?
- How can the system distinguish an unusual information spike from a genuinely significant event?
- How should confidence change as evidence arrives, is corrected, or is disproven?

A thousand reposts of one unverified claim must not be treated as a thousand independent observations.

### 4.4 Event-to-market transmission

The model should reason about how an event could affect the financial system through direct and indirect relationships.

For example:

Geopolitical disruption → shipping routes → transportation costs → commodity supply → corporate input costs → margins and earnings → valuations and market behavior.

Potential modeling dimensions:

- Geographic exposure.
- Operational and supply-chain exposure.
- Revenue and cost exposure.
- Insurance and credit exposure.
- Commodity and currency sensitivity.
- Expected propagation speed and duration.
- Direct versus indirect impact.
- Alternative outcomes and escalation scenarios.

### 4.5 Information asymmetry and market response

The model should learn the difference between an event being real, being reported, being corroborated, becoming widely known, and being reflected in market prices.

A possible research objective is to estimate:

`P(material_market_response | event, evidence, exposure, time, market_context)`

The system must not assume that an absence of visible price movement means the market is unaware. Information may already be reflected in derivatives, institutional positioning, overseas markets, or other channels.

## 5. Tokenization and unified representations

The proposed tokenizer should support heterogeneous financial information rather than treating all inputs as text.

Potential representation families:

- Numerical tokens for normalized market and financial measurements.
- Categorical tokens for market regimes, event classes, sectors, and other discrete features.
- Temporal tokens for timeframes, event timing, and sequence relationships.
- Text-derived embeddings for news, filings, and other documents.
- Entity embeddings for companies, people, institutions, and instruments.
- Relationship representations for ownership, employment, supply chains, and other graph edges.
- Learned representations for combinations and patterns that are not adequately captured by predefined categories.

### Tokenizer research questions

- What information should be discretized, and what should remain continuous?
- Should the system use fixed bins, adaptive bins, learned codebooks, vector quantization, or a hybrid?
- How should token vocabularies be versioned as the feature schema evolves?
- How can tokenization preserve economically meaningful magnitudes and differences?
- How should missing values, outliers, and uncertainty be represented?
- Should different domains have separate token namespaces and encoders before being mapped into a shared representation?
- Can the model learn higher-level representations of recurring financial patterns without losing interpretability?

A key experimental requirement is to compare discrete-token approaches against models that consume continuous numerical features directly. Tokenization may simplify sequence modeling but can also discard information.

## 6. Foundation-model training objectives

Autoregressive next-token prediction is the central proposed training objective, but it should not be the only learning signal.

Potential complementary objectives:

| Objective | Intended capability |
|---|---|
| Next-token prediction | Learn financial sequence structure |
| Next-feature or next-candle prediction | Learn short-horizon market behavior |
| Multi-step future-state prediction | Model possible future trajectories |
| Masked feature reconstruction | Learn cross-feature dependencies |
| Entity and relationship prediction | Learn financial-world structure |
| Temporal reconstruction | Learn how entities and relationships evolve |
| Event prediction | Learn event development and consequences |
| Cross-domain prediction | Learn macro-to-sector-to-company relationships |
| Regime prediction | Learn changing market environments |
| Anomaly detection | Recognize deviations from expected behavior |

The research should determine which objectives share representations, which require specialized heads or pathways, and how to balance their loss functions.

## 7. Meta-learning and continual adaptation

The model should have a stable foundational capability while adapting to new information and changing conditions.

MAML (Model-Agnostic Meta-Learning) is a useful starting point because it trains a model to adapt quickly to new tasks using relatively few examples. The intended application is a financial model that can adapt to new companies, sectors, instruments, and market regimes without full foundation-model retraining.

### 7.1 Separate observation updates from parameter updates

Not every new observation should trigger gradient-based learning.

Distinguish three cases:

**New observations**
- New price and volume data.
- New earnings releases.
- New macroeconomic releases.
- New news or event reports.

These can update the model's temporal context or memory without changing learned parameters.

**New relationships**
- Executive or board changes.
- Mergers and acquisitions.
- New supplier or customer relationships.
- Changes in ownership or corporate structure.

These should update the temporal knowledge graph and associated representations.

**New behavioral evidence**
- A company responds differently to interest rates than previously expected.
- An industry develops a new volatility pattern.
- A market regime changes.
- Prediction errors reveal persistent changes in behavior.

These may justify adaptation through parameter-efficient or gradient-based updates.

### 7.2 Hierarchical adaptation

Investigate adaptation at multiple levels:

- Global market context.
- Macroeconomic regime.
- Sector.
- Industry or subsector.
- Company.
- Individual financial instrument.

The architecture should allow information to flow across levels while preventing noisy or isolated observations from indiscriminately changing broader representations.

### 7.3 Candidate adaptation architecture

- Frozen or slowly updated foundation parameters.
- MAML-trained initialization or adaptation strategy.
- Parameter-efficient adapters, such as LoRA, where appropriate.
- Sector- and company-specific adaptation states.
- Rapidly updated temporal context and memory.
- A controlled mechanism for promoting validated learning into future foundation-model versions.

Research questions:

- Should MAML operate on the entire model, selected layers, adapters, or task-specific heads?
- What constitutes an adaptation task: a company, a sector, a regime, an event class, or a forecasting horizon?
- How much recent evidence is required before adaptation?
- How should the system detect distribution shift?
- How can it prevent catastrophic forgetting?
- How should adaptation be rolled back when it degrades performance?
- How can adaptation be evaluated without leaking future information?
- How should the model distinguish a temporary anomaly from a persistent change in behavior?

The foundational model and its adapted states should remain distinct. An adapted state must not silently become a permanent foundation-weight update.

## 8. Temporal integrity and point-in-time data

This is a non-negotiable research and engineering requirement.

Every piece of information should preserve at least two notions of time:

- **Valid time:** When the fact was true in the real world.
- **Knowledge time:** When the information became available to the model or public.

For example, an executive may leave a company on October 1, but the departure may not be publicly announced until October 5. A prediction made on October 3 must not use the October 5 announcement.

The data system should preserve:

- Event occurrence time, where known.
- Source publication time.
- First-observed time.
- Ingestion time.
- Effective or valid time.
- Revision and correction history.
- Original and revised macroeconomic values.
- Corporate filing and announcement availability.
- Historical classifications and entity relationships.

All training, evaluation, and backtesting must reconstruct what the system could actually have known at the time.

## 9. Evaluation and experimental methodology

The model must be evaluated against realistic historical and forward-looking conditions.

### 9.1 Core evaluation requirements

1. **Point-in-time data:** No future information in features, labels, or entity relationships.
2. **Survivorship-bias control:** Include delisted, acquired, bankrupt, and failed companies.
3. **Historical revision control:** Preserve original macroeconomic releases and later revisions.
4. **Corporate-action handling:** Account for splits, dividends, mergers, and other adjustments.
5. **Walk-forward evaluation:** Train on earlier periods and evaluate on strictly later periods.
6. **Leakage-resistant validation:** Prevent overlapping windows, labels, and duplicated source information from contaminating evaluation.
7. **Transaction-cost-aware testing:** Include realistic costs, slippage, liquidity, and execution constraints where relevant.
8. **Calibration:** Evaluate the reliability of predicted probabilities and uncertainty.
9. **Robustness:** Test across assets, sectors, time periods, and market regimes.

### 9.2 Required baselines and ablations

Compare at least:

- Continuous-feature model versus discrete-token model.
- Fixed tokenizer versus learned tokenizer versus hybrid tokenizer.
- Foundation model alone versus foundation plus contextual memory.
- Foundation plus context versus foundation plus parameter adaptation.
- MAML-inspired adaptation versus simpler adaptation methods.
- Model with and without temporal knowledge-graph information.
- Model with and without global event intelligence.
- Individual domains versus combined multidomain training.

### 9.3 Forecasting and risk metrics

Potential evaluation measures:

- Directional accuracy.
- Return-distribution accuracy.
- Probability calibration.
- Prediction interval coverage.
- Volatility and regime prediction.
- Drawdown and tail-risk estimates.
- Risk-adjusted performance.
- Performance after transaction costs.
- Stability under distribution shift.

### 9.4 Event-intelligence metrics

Evaluate event detection separately from financial forecasting.

Potential metrics:

- Time from first credible observation to detection.
- Detection lead time relative to material market response.
- Precision and recall by event class and severity.
- False-positive rate.
- Confidence calibration.
- Source corroboration quality.
- Event classification accuracy.
- Exposure identification accuracy.
- Impact-forecast calibration.
- Performance when reports are contradictory, incomplete, or later disproven.

Historical event studies should reconstruct source availability and information timing, not simply feed the model a retrospective summary of what happened.

## 10. Proposed modular research architecture

The following is a conceptual decomposition, not a finalized implementation specification.

| Component | Responsibility |
|---|---|
| Data ingestion | Acquire market, macro, corporate, sentiment, and event data |
| Data provenance and temporal store | Preserve source, timestamps, revisions, and point-in-time availability |
| Entity resolution | Maintain identities across companies, people, instruments, and institutions |
| Temporal knowledge graph | Represent evolving entities and relationships |
| Feature engineering | Calculate deterministic financial and statistical features |
| Domain encoders | Process numerical, categorical, textual, temporal, and relational inputs |
| Financial tokenizer | Map suitable features into discrete token representations |
| Unified representation layer | Combine domain representations |
| Foundation transformer | Learn financial-world and financial-behavior representations |
| Event intelligence engine | Detect, corroborate, classify, and track emerging events |
| Meta-learning engine | Support rapid, controlled adaptation |
| Online state manager | Maintain current context, graph state, and adapted parameters |
| Prediction and task heads | Produce forecasts, risk estimates, scenarios, and other outputs |
| Evaluation framework | Run point-in-time, walk-forward, and ablation experiments |

## 11. Initial research phases

A practical research sequence could be:

### Phase 1 — Data and temporal foundations

- Define canonical schemas for market, macro, corporate, event, and entity data.
- Establish provenance and point-in-time requirements.
- Design the temporal knowledge graph.
- Build historical data snapshots.
- Define leakage-resistant evaluation datasets.

### Phase 2 — Financial representation and tokenization

- Prototype OHLCV and derived-feature tokenization.
- Compare fixed, learned, and hybrid tokenizers.
- Add macroeconomic and corporate financial representations.
- Explore entity and relationship embeddings.
- Establish continuous-feature baselines.

### Phase 3 — Foundation-model pretraining

- Train autoregressive financial sequence models.
- Add complementary reconstruction and relationship objectives.
- Evaluate cross-asset and cross-domain learning.
- Test whether shared representations improve generalization.

### Phase 4 — Global event intelligence

- Build event extraction and structured event representations.
- Integrate news, social, official, and other available sources.
- Model source reliability, independence, and corroboration.
- Build event-to-entity and event-to-market exposure paths.
- Reconstruct historical information timelines.

### Phase 5 — Meta-learning and adaptation

- Define adaptation tasks and evaluation protocols.
- Compare MAML-inspired methods with parameter-efficient alternatives.
- Implement isolated company, sector, and regime adaptation states.
- Test update frequency, stability, rollback, and forgetting.
- Separate context updates from parameter updates.

### Phase 6 — Integrated evaluation

- Combine the world model, behavior model, and event intelligence.
- Run historical walk-forward experiments.
- Evaluate event detection lead time and market-response forecasts.
- Compare against simpler models and domain-specific baselines.
- Document limitations and failure modes before considering deployment.

## 12. Design principles and guardrails

- **One foundation, multiple capabilities:** Financial-world understanding and financial-behavior understanding should reinforce one another.
- **Preserve source evidence:** Derived tokens and embeddings must not replace access to original data and provenance.
- **Time-aware by design:** No component may use information unavailable at the prediction timestamp.
- **Uncertainty is first-class:** Conflicting reports and incomplete data should remain uncertain rather than being forced into confident labels.
- **Context is not learning:** Incorporating a new observation does not automatically justify a parameter update.
- **Adaptation is controlled:** Keep foundation weights, adapted parameters, graph state, and contextual memory distinct.
- **Interpret relationships carefully:** Correlation, exposure, influence, and causation are different concepts.
- **Evaluate incremental value:** Every additional data domain and architectural component must demonstrate measurable benefit.
- **Avoid hindsight:** Historical event research must reconstruct the information available at the time.
- **Probabilistic outputs:** Prefer calibrated distributions and conditional scenarios over unsupported single-point predictions.

## 13. Open architectural decisions

These questions should remain open until supported by experiments:

1. What is the optimal balance between autoregressive token prediction and continuous numerical modeling?
2. Should the foundation transformer be a single shared model with specialized pathways, or a coordinated set of encoders and shared transformer layers?
3. Which graph operations should happen outside the transformer, and which relationships should be learned internally?
4. How should text-derived representations and structured event tokens interact?
5. Which pretraining objectives provide measurable improvements beyond next-token prediction?
6. What should constitute an adaptation task for MAML?
7. How should company- and sector-specific adaptation interact with global market adaptation?
8. How can the system identify genuine early-warning signals without overfitting to historical black swan examples?
9. How should the model represent market awareness and information already priced in?
10. What evidence is required before an adapted state or learned capability is promoted into a new foundation-model release?

## 14. Long-term objective

The intended result is not merely a stock-price predictor.

It is a financial foundation model that learns a time-aware representation of the financial world, models how that world behaves, recognizes emerging events and disruptions, and adapts its interpretation as new evidence arrives.

Forecasting is one capability built on that foundation. Risk analysis, anomaly detection, event-impact modeling, scenario analysis, and portfolio-related applications can share the same underlying representation.

The central research hypothesis is:

> A model that jointly learns the structure of the financial world, the behavior of financial markets, and the evolution of information may generalize and adapt more effectively than models trained solely on historical prices or isolated financial indicators.

This is a hypothesis to test, not an assumed result. The research program should be designed to establish where the approach works, where it fails, and whether its additional complexity produces measurable predictive and analytical value.


## Where these questions are researched

Folded into the research guide on 2026-11-07 as hypotheses to test. New research questions: RQ1.10–RQ1.12 ([[RP1 ML Methods]]), RQ2.8–RQ2.9 (RP2), RQ3.8 (RP3), RQ4.8–RQ4.9 (RP4); the mapping from each section to its RQs is in the guide's "Foundation-model research direction" section and in [[Research Questions]]. Section 13's open decisions go to the Synthesis and the methodology plan. RP5 reviews this note.
