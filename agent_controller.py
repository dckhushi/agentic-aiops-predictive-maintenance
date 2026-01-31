from agent.rules import decide_action
from agent.prompts import EXPLANATION_PROMPT


class MaintenanceAgent:
    def __init__(self, llm=None):
        self.llm = llm  # optional LLM (can be None)

    def run(self, predicted_rul, drift_detected, mae):
        decision = decide_action(
            predicted_rul=predicted_rul,
            drift_detected=drift_detected,
            mae=mae
        )

        explanation = self._generate_explanation(
            decision, predicted_rul, drift_detected, mae
        )

        return decision, explanation

    def _generate_explanation(self, decision, rul, drift, mae):
        prompt = EXPLANATION_PROMPT.format(
            decision=decision,
            rul=rul,
            drift=drift,
            mae=mae
        )

        # If no LLM connected, return rule-based explanation
        if self.llm is None:
            return prompt

        return self.llm(prompt)
