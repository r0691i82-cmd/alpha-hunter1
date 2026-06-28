import json

from ai.base_ai_engine import BaseAIEngine


class BearEngine(BaseAIEngine):

    def build_prompt(
        self,
        context,
        analyst_report,
    ):

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        return f"""
You are the Chief Risk Officer of a global macro hedge fund.

Your job is to attack the analyst's thesis.

Return:

1. Biggest Analytical Mistakes
2. Hidden Assumptions
3. Missing Risks
4. Liquidity Risks
5. ETF Flow Contradictions
6. COT Contradictions
7. Macro Contradictions
8. Technical Breakdown Risks
9. Bear Scenario
10. Probability
11. Final Bear Opinion

Structured Data:

{context_text}

Analyst Report:

{analyst_report}
"""