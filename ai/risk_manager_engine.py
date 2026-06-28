import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


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

    def generate(
        self,
        analyst_report,
        bear_report,
        bull_report,
    ):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = f"""
You are the Chief Risk Manager of a global macro hedge fund.

You are NOT bullish.

You are NOT bearish.

Your only responsibility is protecting capital.

Evaluate:

1. Liquidity Risk

2. Carry Trade Risk

3. Currency Risk

4. Interest Rate Risk

5. Credit Risk

6. ETF Flow Risk

7. COT Positioning Risk

8. Technical Breakdown Risk

9. Geopolitical Risk

10. Black Swan Risk

Return:

Executive Summary

Top Risks

Risk Score (0~100)

Probability

Worst Case Scenario

Capital Preservation Strategy

Portfolio Exposure Recommendation

Analyst Report

{analyst_report}

Bear Report

{bear_report}

Bull Report

{bull_report}

Structured Data

{InstitutionalPromptBuilder().build()}
"""

        response = self.model.generate_content(prompt)

        return response.text