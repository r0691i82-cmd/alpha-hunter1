import pandas as pd


def add_liquidity_features(df: pd.DataFrame) -> pd.DataFrame:
    df["PREV_HIGH_20"] = df["high"].rolling(20).max().shift(1)
    df["PREV_LOW_20"] = df["low"].rolling(20).min().shift(1)

    df["LIQUIDITY_SWEEP_HIGH"] = (
        (df["high"] > df["PREV_HIGH_20"])
        & (df["close"] < df["PREV_HIGH_20"])
    )

    df["LIQUIDITY_SWEEP_LOW"] = (
        (df["low"] < df["PREV_LOW_20"])
        & (df["close"] > df["PREV_LOW_20"])
    )

    df["ROUND_NUMBER"] = (df["close"] / 100).round() * 100
    df["ROUND_DISTANCE"] = df["close"] - df["ROUND_NUMBER"]
    df["ROUND_DISTANCE_PCT"] = (df["ROUND_DISTANCE"] / df["close"]) * 100

    df["LIQUIDITY_SCORE"] = 0

    df.loc[df["LIQUIDITY_SWEEP_HIGH"], "LIQUIDITY_SCORE"] += 40
    df.loc[df["LIQUIDITY_SWEEP_LOW"], "LIQUIDITY_SCORE"] += 40
    df.loc[df["ROUND_DISTANCE_PCT"].abs() < 0.15, "LIQUIDITY_SCORE"] += 20

    return df