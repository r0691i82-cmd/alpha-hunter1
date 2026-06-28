from features.money_flow_engine import MoneyFlowEngine
from features.carry_risk_engine import build_carry_risk_score


class MarketRegimeEngine:
    def __init__(self):
        self.money_flow_engine = MoneyFlowEngine()

    def run(self):
        money_flow = self.money_flow_engine.run()
        carry = build_carry_risk_score()

        money_score = money_flow.get("MONEY_FLOW_SCORE", 50)
        carry_score = carry.get("CARRY_RISK_SCORE", 50)

        regime = "NEUTRAL"

        if money_score >= 70 and carry_score < 55:
            regime = "RISK_ON"

        elif money_score <= 35 or carry_score >= 75:
            regime = "RISK_OFF"

        elif 55 <= money_score < 70 and carry_score < 65:
            regime = "RECOVERY"

        elif money_score >= 60 and carry_score >= 55:
            regime = "LATE_CYCLE"

        elif money_score < 50 and carry_score >= 55:
            regime = "LIQUIDITY_STRESS"

        return {
            "MARKET_REGIME": regime,
            "MONEY_FLOW_SCORE": money_score,
            "CARRY_RISK_SCORE": carry_score,
            "CARRY_RISK_STATE": carry.get("CARRY_RISK_STATE", "UNKNOWN"),
            "MACRO_STATE": money_flow.get("MACRO_STATE", "UNKNOWN"),
        }