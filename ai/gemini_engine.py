import os
import google.generativeai as genai

from ai.prompt_builder import InstitutionalPromptBuilder


class GeminiEngine:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key:
            genai.configure(api_key=api_key)

            self.model = genai.GenerativeModel(
                "gemini-2.5-pro"
            )
        else:
            self.model = None

    def generate(self):

        if self.model is None:
            return "GEMINI_API_KEY NOT FOUND"

        prompt = InstitutionalPromptBuilder().build()

        response = self.model.generate_content(prompt)

        return response.text