from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine
from ai.bull_engine import BullEngine
from ai.risk_manager_engine import RiskManagerEngine
from ai.judge_engine import JudgeEngine


class FinalDecisionEngine:

    def __init__(self):

        self.analyst = AnalystEngine()
        self.bear = BearEngine()
        self.bull = BullEngine()
        self.risk = RiskManagerEngine()
        self.judge = JudgeEngine()

    def run(self):

        analyst_report = self.analyst.generate()

        bear_report = self.bear.generate(
            analyst_report,
        )

        bull_report = self.bull.generate(
            analyst_report,
            bear_report,
        )

        risk_report = self.risk.generate(
            analyst_report,
            bear_report,
            bull_report,
        )

        judge_report = self.judge.generate(
            analyst_report,
            bear_report,
            bull_report,
            risk_report,
        )

        return {
            "analyst": analyst_report,
            "bear": bear_report,
            "bull": bull_report,
            "risk": risk_report,
            "judge": judge_report,
        }