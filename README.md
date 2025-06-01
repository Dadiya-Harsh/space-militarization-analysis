# Space Militarization and Orbital Risk Analysis (SMORA)

This project uses machine learning and orbital mechanics to analyze the impact of military space assets on orbital congestion, collision risk, and space sustainability. It leverages TLE (Two-Line Element) data, satellite metadata, and space weather events to detect patterns, forecast risks, and propose data-driven recommendations.

## 🛰️ Key Features

- Parse and simulate satellite orbits using public TLE data
- Classify satellites by country and purpose (military, civil, commercial)
- Detect orbital congestion and anomalies using ML
- Predict collision likelihood between satellites
- Create a risk scoring system for orbital sustainability

## 📂 Folder Structure

space-militarization-analysis/
│
├── data/                       # Raw and processed data
│   ├── raw/                   # Raw TLE, satellite metadata, etc.
│   ├── processed/             # Cleaned, engineered, or resampled data
│   └── external/              # Manually sourced datasets (CelesTrak, etc.)
│
├── notebooks/                 # Exploratory notebooks for each module
│   ├── 01-data-exploration.ipynb
│   ├── 02-orbit-clustering.ipynb
│   ├── 03-collision-prediction.ipynb
│   └── 04-risk-metric-modeling.ipynb
│
├── src/                       # Source code and modular ML pipeline
│   ├── data_loader/           # TLE parsing, metadata loading
│   ├── preprocessing/         # Cleaning, TLE to features
│   ├── modeling/              # ML models: clustering, prediction, anomaly
│   ├── visualization/         # Orbital maps, cluster plots, time series
│   └── utils/                 # Shared helpers (e.g., TLE propagation)
│
├── reports/                   # Paper drafts, diagrams, figures
│   ├── figures/
│   └── research_draft.md
│
├── configs/                   # YAML/JSON config for model, data paths
│
├── tests/                     # Unit and integration tests
│
├── requirements.txt           # Python dependencies
├── environment.yml            # Optional: conda environment
├── README.md                  # Project overview and instructions
└── .gitignore
