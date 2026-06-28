from pathlib import Path

from ai.gemini_client import GeminiClient


class BaseAIEngine:

    MODEL = "gemini-2.5-flash"

    PROMPT_FILE = None

    def __init__(self):

        self.gemini = GeminiClient(
            self.MODEL,
        )

    def load_prompt(self):

        if self.PROMPT_FILE is None:
            return ""

        return Path(
            self.PROMPT_FILE
        ).read_text(
            encoding="utf-8",
        )

    def build_prompt(
        self,
        context,
        *reports,
    ):
        raise NotImplementedError

    def generate(
        self,
        context,
        *reports,
    ):

        prompt = self.build_prompt(
            context,
            *reports,
        )

        return self.gemini.generate(
            prompt,
        )