import json

from ai.base_ai_engine import BaseAIEngine


class JudgeEngine(BaseAIEngine):

    MODEL = "gemini-2.5-pro"

    def build_prompt(
        self,
        context,
        analyst_report,
        bear_report,
        bull_report,
        risk_report,
    ):

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        return f"""
You are the final investment committee judge.

Use only the provided data and internal reports.

Return:

1. Final Executive Summary
2. Final Market Regime
3. Money Flow Interpretation
4. Bull Case Strength
5. Bear Case Strength
6. Risk Manager Assessment
7. Key Contradictions
8. Final Scenario
9. Confidence Score 0~100
10. Final Decision: Buy / Hold / Sell / Risk-Off
11. Portfolio Exposure Recommendation
12. Stop Loss / Risk Control
13. What Would Change This View

Structured Data:

{context_text}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}

Risk Manager Report:

{risk_report}
"""