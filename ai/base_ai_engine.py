from ai.gemini_client import GeminiClient


class BaseAIEngine:

    MODEL = "gemini-2.5-flash"

    def __init__(self):
        self.gemini = GeminiClient(
            self.MODEL,
        )

    def build_prompt(self, context, *reports):
        raise NotImplementedError

    def generate(self, context, *reports):
        prompt = self.build_prompt(
            context,
            *reports,
        )

        return self.gemini.generate(prompt)