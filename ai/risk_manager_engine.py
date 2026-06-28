import os
import json
import google.generativeai as genai


class RiskManagerEngine:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.model = None
            return

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, context, analyst_report, bear_report, bull_report):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        prompt = f"""
You are the Chief Risk Manager of a global macro hedge fund.

Your only job is capital protection.

Return:

1. Executive Summary
2. Top Risks
3. Carry Trade Risk
4. Currency Risk
5. Liquidity Risk
6. Volatility Risk
7. Credit Risk
8. Risk Score 0~100
9. Worst Case Scenario
10. Portfolio Exposure Recommendation

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}
"""

        response = self.model.generate_content(prompt)

        return response.text