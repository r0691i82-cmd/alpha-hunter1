import os
import json
import google.generativeai as genai


class AnalystEngine:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.model = None
            return

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, context):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        prompt = f"""
You are the Chief Investment Officer of a global macro hedge fund.

Use only the supplied structured data.

Return:

1. Executive Summary
2. Global Money Flow
3. Market Regime
4. ETF Rotation
5. COT Positioning
6. Macro Risk
7. Technical View
8. Primary Scenario
9. Alternative Scenario
10. Confidence Score 0~100

Structured Data:

{context_text}
"""

        response = self.model.generate_content(prompt)

        return response.text