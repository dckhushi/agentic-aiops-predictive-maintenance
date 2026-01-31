import streamlit as st
import numpy as np
import torch
import sys

sys.path.append(".")

from agent.agent_controller import MaintenanceAgent
from aiops.drift_detection import detect_drift


# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Agentic AIOps – Predictive Maintenance",
    layout="centered"
)

st.title("🛠️ Agentic AIOps Predictive Maintenance Dashboard")
st.write("Real-time maintenance decision support for smart manufacturing")

# ------------------------
# Load Model (Transformer preferred)
# ------------------------
@st.cache_resource
def load_model():
    model = torch.load(
        "models/transformer/transformer_rul_model.pth",
        map_location=torch.device("cpu")
    )
    return model

# NOTE:
# For demo purposes, we simulate predictions
# In production, this will use model inference

# ------------------------
# Sidebar Inputs
# ------------------------
st.sidebar.header("Simulation Controls")

predicted_rul = st.sidebar.slider(
    "Predicted Remaining Useful Life (cycles)",
    min_value=0,
    max_value=150,
    value=28
)

drift_detected = st.sidebar.selectbox(
    "Data Drift Detected?",
    [True, False],
    index=0
)

mae = st.sidebar.slider(
    "Current Model MAE",
    min_value=10.0,
    max_value=60.0,
    value=29.7
)

# ------------------------
# Agent Decision
# ------------------------
agent = MaintenanceAgent(llm=None)

decision, explanation = agent.run(
    predicted_rul=predicted_rul,
    drift_detected=drift_detected,
    mae=mae
)

# ------------------------
# Display Results
# ------------------------
st.subheader("📊 System Status")

col1, col2, col3 = st.columns(3)

col1.metric("Predicted RUL", f"{predicted_rul} cycles")
col2.metric("Data Drift", str(drift_detected))
col3.metric("Model MAE", f"{mae:.1f}")

st.subheader("🤖 Agent Decision")

if decision == "SCHEDULE_MAINTENANCE":
    st.error("🚨 SCHEDULE MAINTENANCE IMMEDIATELY")
elif decision == "TRIGGER_RETRAINING":
    st.warning("♻️ TRIGGER MODEL RETRAINING")
elif decision == "MONITOR_CLOSELY":
    st.info("👀 MONITOR SYSTEM CLOSELY")
else:
    st.success("✅ NORMAL OPERATION")

st.subheader("🧠 Explanation")
st.write(explanation)

st.markdown("---")
st.caption("Agentic AIOps System | Final Year Data Science Project (2026)")
