import json

from ai.base_ai_engine import BaseAIEngine


class JudgeEngine(BaseAIEngine):

    MODEL = "gemini-2.5-pro"

    PROMPT_FILE = "ai/prompts/judge.txt"

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

        system_prompt = self.load_prompt()

        return f"""
{system_prompt}

You are the final investment committee judge.

Use only the provided data, internal reports, and institutional memory.

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
14. Memory Comparison
15. Regime Change From Previous Reports
16. Repeated Mistakes To Avoid

Structured Data:

{context_text}

Institutional Memory:

{context.get("market_memory", [])}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}

Risk Manager Report:

{risk_report}

Compare today's market with previous reports.

Find:
- Recurring mistakes
- Regime changes
- Probability changes
- Whether today's conclusion is stronger or weaker than the past week
- Whether current risks are increasing or decreasing
- Whether confidence should be raised or lowered

Avoid repeating previous mistakes.
"""