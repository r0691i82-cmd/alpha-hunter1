import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


class JudgeEngine:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.model = None
            return

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-pro"
        )

    def generate(
        self,
        analyst_report,
        bear_report,
        bull_report,
        risk_report,
    ):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = f"""
You are the final investment committee judge.

You are reviewing four internal reports:

1. Analyst Report
2. Bear Report
3. Bull Report
4. Risk Manager Report

Your job is to decide the final institutional view.

Rules:

- Do not invent new data.
- Do not calculate new indicators.
- Use only the reports and structured data provided.
- Identify contradictions.
- Weigh probabilities.
- Choose a final scenario.
- Be conservative with confidence.
- If risks are high, reduce conviction.

Return:

1. Final Executive Summary

2. Final Market Regime

3. Final Money Flow Interpretation

4. Bull Case Strength

5. Bear Case Strength

6. Risk Manager Assessment

7. Key Contradictions

8. Final Scenario

9. Confidence Score (0~100)

10. Final Decision

11. Portfolio Exposure Recommendation

12. Stop Loss / Risk Control

13. What Would Change This View

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}

Risk Manager Report:

{risk_report}

Structured Data:

{InstitutionalPromptBuilder().build()}
"""

        response = self.model.generate_content(prompt)

        return response.text