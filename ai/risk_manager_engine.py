import json

from ai.base_ai_engine import BaseAIEngine


class RiskManagerEngine(BaseAIEngine):

    def build_prompt(
        self,
        context,
        analyst_report,
        bear_report,
        bull_report,
    ):

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        return f"""
You are the Chief Risk Manager of a global macro hedge fund.

Your only job is capital protection.

Return:

1. Executive Summary
2. Top Risks
3. Carry Trade Risk
4. Currency Risk
5. Liquidity Risk
6. Volatility Risk
7. Credit Risk
8. Risk Score 0~100
9. Worst Case Scenario
10. Portfolio Exposure Recommendation
11. Position Sizing Guidance
12. Stop Loss / Risk Control

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}
"""