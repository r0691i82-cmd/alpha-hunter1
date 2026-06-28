import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


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

    def generate(self):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = f"""
You are the Chief Investment Officer of a global macro hedge fund.

Your role:

Analyze the market objectively.

Use ONLY the supplied structured data.

Return:

1 Executive Summary

2 Global Money Flow

3 ETF Rotation

4 COT Analysis

5 Macro Analysis

6 Technical View

7 Primary Scenario

8 Confidence (0~100)

Structured Data

{InstitutionalPromptBuilder().build()}
"""

        response = self.model.generate_content(prompt)

        return response.text