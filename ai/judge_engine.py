import os
import json
import google.generativeai as genai


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
        context,
        analyst_report,
        bear_report,
        bull_report,
        risk_report,
    ):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        prompt = f"""
You are the final investment committee judge.

Use only the provided data and internal reports.

Return:

1. Final Executive Summary
2. Final Market Regime
3. Money Flow Interpretation
4. Bull Case Strength
5. Bear Case Strength
6. Risk Manager Assessment
7. Key Contradictions
8. Final Scenario
9. Confidence Score 0~100
10. Final Decision: Buy / Hold / Sell / Risk-Off
11. Portfolio Exposure Recommendation
12. Stop Loss / Risk Control
13. What Would Change This View

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}

Risk Manager Report:

{risk_report}
"""

        response = self.model.generate_content(prompt)

        return response.text