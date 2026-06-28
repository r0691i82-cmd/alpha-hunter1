import os
import json
import google.generativeai as genai


class BearEngine:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.model = None
            return

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, context, analyst_report):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        prompt = f"""
You are the Chief Risk Officer of a global macro hedge fund.

Your job is to attack the analyst's thesis.

Return:

1. Biggest Analytical Mistakes
2. Hidden Assumptions
3. Missing Risks
4. Liquidity Risks
5. ETF Flow Contradictions
6. COT Contradictions
7. Macro Contradictions
8. Technical Breakdown Risks
9. Bear Scenario
10. Probability
11. Final Bear Opinion

Structured Data:

{context_text}

Analyst Report:

{analyst_report}
"""

        response = self.model.generate_content(prompt)

        return response.text