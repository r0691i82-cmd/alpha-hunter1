from features.macro_engine_v2 import MacroEngineV2
from features.etf_flow_engine import ETFFlowEngine
from features.cot_engine import COTEngine


class MoneyFlowEngine:
    def __init__(self):
        self.macro_engine = MacroEngineV2()
        self.etf_engine = ETFFlowEngine()
        self.cot_engine = COTEngine()

    def run(self):
        macro = self.macro_engine.run(None)
        etf = self.etf_engine.run(None)
        cot = self.cot_engine.run(None)

        score = 50

        macro_state = "UNKNOWN"
        if macro is not None and not macro.empty:
            macro_score = float(macro["MACRO_SCORE"].iloc[-1])
            macro_state = macro["MACRO_STATE"].iloc[-1]
            score += macro_score * 5

        if etf is not None and not etf.empty:
            qqq = etf[etf["ETF"] == "QQQ"]
            tlt = etf[etf["ETF"] == "TLT"]
            gld = etf[etf["ETF"] == "GLD"]

            if not qqq.empty and qqq["FLOW_SCORE"].iloc[0] > 0:
                score += 10

            if not tlt.empty and tlt["FLOW_SCORE"].iloc[0] > 0:
                score -= 10

            if not gld.empty and gld["FLOW_SCORE"].iloc[0] > 0:
                score -= 5

        if cot is not None and not cot.empty:
            jpy = cot[cot["ASSET"] == "JPY"]

            if not jpy.empty:
                if jpy["COT_MOMENTUM"].iloc[0] == "IMPROVING":
                    score -= 10
                elif jpy["COT_MOMENTUM"].iloc[0] == "DETERIORATING":
                    score += 10

        score = max(0, min(100, score))

        if score >= 70:
            regime = "RISK_ON"
        elif score <= 35:
            regime = "RISK_OFF"
        else:
            regime = "NEUTRAL"

        return {
            "MONEY_FLOW_SCORE": round(score, 2),
            "MARKET_REGIME": regime,
            "MACRO_STATE": macro_state,
        }