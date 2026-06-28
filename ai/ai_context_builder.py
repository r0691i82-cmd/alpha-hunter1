from datetime import datetime

from features.money_flow_engine import MoneyFlowEngine
from features.market_regime_engine import MarketRegimeEngine
from features.etf_flow_engine import ETFFlowEngine
from features.cot_engine import COTEngine
from features.macro_engine_v2 import MacroEngineV2


class AIContextBuilder:
    def build(self):
        money_flow = MoneyFlowEngine().run()
        regime = MarketRegimeEngine().run()
        etf = ETFFlowEngine().run(None)
        cot = COTEngine().run(None)
        macro = MacroEngineV2().run(None)

        context = {
            "generated_at": datetime.now().isoformat(),
            "money_flow": money_flow,
            "market_regime": regime,
            "etf_flow": [],
            "cot_positioning": [],
            "macro_snapshot": [],
        }

        if etf is not None and not etf.empty:
            for _, row in etf.iterrows():
                context["etf_flow"].append({
                    "etf": row["ETF"],
                    "flow_score": round(float(row["FLOW_SCORE"]), 2),
                    "flow_state": row["FLOW_STATE"],
                })

        if cot is not None and not cot.empty:
            for _, row in cot.iterrows():
                context["cot_positioning"].append({
                    "asset": row["ASSET"],
                    "bias": row["COT_BIAS"],
                    "momentum": row["COT_MOMENTUM"],
                    "noncomm_net": round(float(row["NONCOMM_NET"]), 2),
                })

        if macro is not None and not macro.empty:
            for _, row in macro.iterrows():
                context["macro_snapshot"].append({
                    "asset": row["asset"],
                    "ret_20d": round(float(row["ret_20d"]), 2),
                    "risk_on_score": round(float(row["risk_on_score"]), 2),
                })

        return context