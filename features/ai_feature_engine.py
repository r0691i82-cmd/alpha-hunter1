import pandas as pd


def add_ai_features(df: pd.DataFrame) -> pd.DataFrame:
    df["AI_BASE_SCORE"] = (
        df["ALPHA_SCORE"] * 0.25
        + df["STRUCTURE_SCORE"] * 0.25
        + df["TREND_ENGINE_SCORE"] * 0.20
        + df["SMART_MONEY_SCORE"] * 0.15
        + df["MTF_SCORE"] * 0.15
    )

    df["AI_SIGNAL"] = "WAIT"

    df.loc[df["AI_BASE_SCORE"] >= 70, "AI_SIGNAL"] = "BUY"
    df.loc[df["AI_BASE_SCORE"] <= 30, "AI_SIGNAL"] = "SELL"

    df["RISK_LEVEL"] = "MEDIUM"

    df.loc[df["FEAR_SCORE"] >= 70, "RISK_LEVEL"] = "HIGH"
    df.loc[df["ATR_14"] < df["ATR_14"].rolling(100).mean(), "RISK_LEVEL"] = "LOW"

    return df