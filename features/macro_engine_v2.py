import pandas as pd
from pathlib import Path

from core.base_engine import BaseEngine


class MacroEngineV2(BaseEngine):
    def __init__(self):
        super().__init__("macro_engine_v2")

    def process(self, data=None):
        rows = []

        files = list(Path("database/macro").glob("*.csv"))

        for file in files:
            df = pd.read_csv(file)

            if len(df) < 22 or "Close" not in df.columns:
                continue

            close = df["Close"]

            rows.append({
                "asset": file.stem,
                "last": close.iloc[-1],
                "ret_5d": (close.iloc[-1] / close.iloc[-6] - 1) * 100,
                "ret_20d": (close.iloc[-1] / close.iloc[-21] - 1) * 100,
            })

        result = pd.DataFrame(rows)

        if result.empty:
            return result

        result["risk_on_score"] = 0.0

        risk_assets = ["NASDAQ", "SP500", "BTC", "SPY", "QQQ", "IWM"]
        risk_off_assets = ["VIX", "DXY", "UUP"]
        defensive_assets = ["GOLD", "TLT", "GLD"]

        result.loc[
            result["asset"].isin(risk_assets),
            "risk_on_score",
        ] = result["ret_20d"]

        result.loc[
            result["asset"].isin(risk_off_assets),
            "risk_on_score",
        ] = -result["ret_20d"]

        result.loc[
            result["asset"].isin(defensive_assets),
            "risk_on_score",
        ] = -result["ret_20d"] * 0.5

        macro_score = result["risk_on_score"].mean()

        if macro_score > 1:
            macro_state = "RISK_ON"
        elif macro_score < -1:
            macro_state = "RISK_OFF"
        else:
            macro_state = "NEUTRAL"

        result["MACRO_SCORE"] = macro_score
        result["MACRO_STATE"] = macro_state

        return result