import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


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

    def generate(self, analyst_report, bear_report):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = f"""
You are the Chief Investment Strategist of a long-only global asset manager.

Your job is to challenge the bear case.

Find why the market can continue rising.

Find liquidity support.

Find ETF inflow support.

Find macro tailwinds.

Find positioning squeeze opportunities.

Find COT-based bullish setups.

Find technical continuation signals.

Return:

1 Bull Thesis

2 Why Bear Case May Be Wrong

3 Liquidity Support

4 ETF / COT Bullish Evidence

5 Upside Scenario

6 Probability

7 Final Bull Opinion

Analyst Report

{analyst_report}

Bear Report

{bear_report}

Structured Data

{InstitutionalPromptBuilder().build()}
"""

        response = self.model.generate_content(prompt)

        return response.text