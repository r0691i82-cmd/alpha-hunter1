import pandas as pd


def add_fear_features(df: pd.DataFrame) -> pd.DataFrame:
    df["FEAR_SCORE"] = 0

    df.loc[df["RSI_14"] < 35, "FEAR_SCORE"] += 30
    df.loc[df["MACD_HIST"] < 0, "FEAR_SCORE"] += 20
    df.loc[df["close"] < df["VWAP"], "FEAR_SCORE"] += 20
    df.loc[df["LIQUIDITY_SWEEP_LOW"], "FEAR_SCORE"] += 30

    return df