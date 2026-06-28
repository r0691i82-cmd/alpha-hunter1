import json

from ai.base_ai_engine import BaseAIEngine


class BullEngine(BaseAIEngine):

    def build_prompt(
        self,
        context,
        analyst_report,
        bear_report,
    ):

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        return f"""
You are the Chief Investment Strategist of a long-only global asset manager.

Your job is to challenge the bear case.

Return:

1. Bull Thesis
2. Why Bear Case May Be Wrong
3. Liquidity Support
4. ETF / COT Bullish Evidence
5. Macro Tailwinds
6. Technical Continuation Signals
7. Upside Scenario
8. Probability
9. Final Bull Opinion

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}
"""