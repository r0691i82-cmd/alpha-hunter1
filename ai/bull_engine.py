import os
import json
import google.generativeai as genai


class BullEngine:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.model = None
            return

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, context, analyst_report, bear_report):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        prompt = f"""
You are the Chief Investment Strategist of a long-only global asset manager.

Your job is to challenge the bear case.

Return:

1. Bull Thesis
2. Why Bear Case May Be Wrong
3. Liquidity Support
4. ETF / COT Bullish Evidence
5. Macro Tailwinds
6. Technical Continuation Signals
7. Upside Scenario
8. Probability
9. Final Bull Opinion

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}
"""

        response = self.model.generate_content(prompt)

        return response.text