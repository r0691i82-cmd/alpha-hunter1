import os
from google import genai


class GeminiClient:

    def __init__(self, model_name):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            self.client = None
            self.model_name = model_name
            return

        self.client = genai.Client(
            api_key=api_key,
        )

        self.model_name = model_name

    def generate(self, prompt):

        if self.client is None:
            return "GEMINI_API_KEY NOT FOUND"

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        return response.text