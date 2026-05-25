# The Structural Outlier Detector
### Financial Fraud & Network Anomaly Engine

An unsupervised machine learning pipeline designed to detect financial anomalies and trace systemic fraud rings across high-throughput enterprise transaction records. 

---

##  System Architecture & Engineering Philosophy

Standard transaction alert frameworks fail because financial crime is highly dynamic and heavily imbalanced (fraud typically constitutes <0.1% of ledger records). This architecture shifts the paradigm from deterministic, rules-based pattern matching to structural, unsupervised isolation across a two-layer processing pipeline.

1. **Unsupervised Vector Processing Engine**: Projects transaction matrices into high-dimensional space, regularizes scales to balance currency magnitudes against millisecond velocity signals via Z-score standardization, and partitions data geometries using an **Isolation Forest** ensemble.
2. **Topological Graph Analyser**: Reconstructs transaction directional flows as a **Directed Network Graph ($nx.DiGraph$)**. It abstracts vector anomaly flags, converts them to undirected isolated network sub-graphs, and runs topological filters to isolate systemic multi-node financial fraud rings.

---

##  Repository Layout

```text
├── src/
│   ├── __init__.py
│   ├── data_generator.py     # Layer 1: Adversarial Synthetic Data Simulation Pipeline
│   ├── anomaly_engine.py     # Layer 2: Vector Space Optimization & Hyperplane Partitioning
│   ├── network_analyser.py   # Layer 3: Topological Graph Construction & Ring Extraction
│   └── app.py                # Layer 4: Interactive Dashboard Frontend Visualization Cockpit
├── requirements.txt          # Complete Production System Dependencies Matrix
├── .gitignore                # System Cache File Disclusion Strategy
└── README.md                 # Professional Technical Dossier Documentation
