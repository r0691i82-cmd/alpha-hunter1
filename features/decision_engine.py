import pandas as pd


def add_decision_features(df: pd.DataFrame) -> pd.DataFrame:
    df["FINAL_DECISION"] = "WAIT"

    df.loc[
        (df["AI_SIGNAL"] == "BUY")
        & (df["RISK_LEVEL"] != "HIGH")
        & (df["SMART_MONEY_SCORE"] > 0),
        "FINAL_DECISION",
    ] = "BUY"

    df.loc[
        (df["AI_SIGNAL"] == "SELL")
        | (df["STRUCTURE_STATE"] == "WEAK")
        | (df["FEAR_SCORE"] >= 80),
        "FINAL_DECISION",
    ] = "SELL"

    df["POSITION_SIZE_LEVEL"] = "NONE"

    df.loc[df["FINAL_DECISION"] == "BUY", "POSITION_SIZE_LEVEL"] = "SMALL"
    df.loc[
        (df["FINAL_DECISION"] == "BUY")
        & (df["AI_BASE_SCORE"] >= 80)
        & (df["RISK_LEVEL"] == "LOW"),
        "POSITION_SIZE_LEVEL",
    ] = "MEDIUM"

    df["STOP_LOSS"] = df["close"] - (df["ATR_14"] * 1.5)
    df["TAKE_PROFIT"] = df["close"] + (df["ATR_14"] * 2.5)

    return df