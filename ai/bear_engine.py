import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


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

    def generate(self, analyst_report):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = f"""
You are the Chief Risk Officer of a global macro hedge fund.

Your ONLY job is to DISAGREE with the analyst.

Find every weakness.

Find hidden assumptions.

Find missing macro risks.

Find liquidity risks.

Find ETF flow contradictions.

Find COT contradictions.

Find technical contradictions.

Find Black Swan risks.

Return:

1 Biggest Mistakes

2 Missing Risks

3 Bear Scenario

4 Probability

5 Portfolio Risks

6 Final Bear Opinion

Analyst Report

{analyst_report}

Structured Data

{InstitutionalPromptBuilder().build()}
"""

        response = self.model.generate_content(prompt)

        return response.text