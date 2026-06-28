from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine
from ai.bull_engine import BullEngine
from ai.risk_manager_engine import RiskManagerEngine
from ai.judge_engine import JudgeEngine


class FinalDecisionEngine:

    def run(self):

        analyst = AnalystEngine().generate()

        bear = BearEngine().generate(
            analyst,
        )

        bull = BullEngine().generate(
            analyst,
            bear,
        )

        risk = RiskManagerEngine().generate(
            analyst,
            bear,
            bull,
        )

        judge = JudgeEngine().generate(
            analyst,
            bear,
            bull,
            risk,
        )

        return {
            "analyst": analyst,
            "bear": bear,
            "bull": bull,
            "risk": risk,
            "judge": judge,
        }