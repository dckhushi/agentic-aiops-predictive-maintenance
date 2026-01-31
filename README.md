# Agentic AIOps Predictive Maintenance System

An end-to-end, production-oriented predictive maintenance system that estimates the Remaining Useful Life (RUL) of industrial machines and autonomously recommends maintenance actions using AIOps monitoring and agentic AI.

This project focuses not only on prediction accuracy, but also on **reliability, monitoring, explainability, and real-world deployability**.

---

## 🚀 Project Overview

Unexpected machine failures can lead to high operational costs and downtime in industrial environments.  
This system addresses the problem by combining:

- Deep learning–based RUL prediction  
- AIOps-driven monitoring (data drift detection)  
- Rule-first agentic AI for safe, autonomous decision-making  
- A human-in-the-loop dashboard for transparency  

The result is a **decision intelligence system**, not just a machine learning model.

---

## 🧠 System Architecture

Sensor Time-Series Data
↓
Preprocessing & Sliding Window Generation
↓
LSTM / Temporal Transformer (RUL Prediction)
↓
AIOps Layer (Data Drift Detection, Performance Signals)
↓
Rule-Based Agentic AI
↓
Maintenance Decision + Explanation
↓
Streamlit Dashboard (Human-in-the-Loop)



Each layer is modular and decoupled to support scalability, monitoring, and future production deployment.

---

## ✨ Key Features

- **Predictive Maintenance**  
  Estimates Remaining Useful Life (RUL) using LSTM and Temporal Transformer models.

- **AIOps Monitoring**  
  Detects data distribution shifts using statistical drift detection (KS-test).

- **Agentic AI Decision Engine**  
  Rule-first agent that autonomously decides when to:
  - Schedule maintenance
  - Monitor the system closely
  - Trigger model retraining

- **Explainability by Design**  
  Every decision is accompanied by a clear, human-readable explanation.

- **Interactive Dashboard**  
  Streamlit-based UI for real-time system status, decisions, and explanations.

---

## 🛠️ Technologies Used

- **Programming:** Python  
- **Deep Learning:** PyTorch, LSTM, Temporal Transformer  
- **Data Processing:** NumPy, Pandas  
- **Monitoring & AIOps:** SciPy (KS-test for drift detection)  
- **Agentic AI:** Rule-based decision engine with explainability  
- **Visualization:** Streamlit  

---

## 📂 Repository Structure

agentic-aiops-predictive-maintenance/
│
├── agent/ # Agentic AI decision logic
│ ├── rules.py
│ ├── prompts.py
│ └── agent_controller.py
│
├── aiops/ # Monitoring and retraining logic
│ ├── drift_detection.py
│ └── retraining_trigger.py
│
├── dashboard/ # Streamlit dashboard
│ └── app.py
│
├── models/ # Saved trained models
│ └── transformer/
│
├── notebooks/ # Experiments and model training
│
├── data/ # Raw and processed datasets
│
├── utils/ # Utility modules (scaffolded for extensibility)
│
└── README.md



---

## ▶️ How to Run the Dashboard

1. Clone the repository
2. Install dependencies
3. Launch the Streamlit app



📊 Dataset

CMAPSS FD001 Dataset (NASA)

Simulated turbofan engine degradation data widely used for predictive maintenance research.

🧪 Current Status

Core prediction, monitoring, and decision logic are fully implemented.

Some modules (e.g., extended monitoring and retraining orchestration) are intentionally scaffolded to demonstrate production-ready architecture and extensibility.

🎯 Use Cases

Smart Manufacturing

Industry 4.0 Reliability Engineering

Predictive Maintenance Systems

AIOps & Decision Intelligence Applications

📌 Author

Final-year Integrated M.Sc. Data Science student (2026)
Focused on building reliable, explainable, and production-oriented AI systems.

📜 License

This project is intended for academic, research, and portfolio use.
