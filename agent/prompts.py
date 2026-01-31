EXPLANATION_PROMPT = """
You are an AI maintenance assistant for a manufacturing plant.

Decision taken: {decision}

Context:
- Predicted Remaining Useful Life (cycles): {rul}
- Data drift detected: {drift}
- Current model MAE: {mae}

Explain in clear, simple language:
- Why this decision was taken
- What action the maintenance team should perform next
- Any risks if action is delayed
"""
