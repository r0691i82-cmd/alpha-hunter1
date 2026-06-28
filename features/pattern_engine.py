import pandas as pd


def add_pattern_features(df: pd.DataFrame) -> pd.DataFrame:
    df["BODY"] = (df["close"] - df["open"]).abs()
    df["RANGE"] = (df["high"] - df["low"]).replace(0, 1)

    df["UPPER_WICK"] = df["high"] - df[["open", "close"]].max(axis=1)
    df["LOWER_WICK"] = df[["open", "close"]].min(axis=1) - df["low"]

    df["BODY_RATIO"] = df["BODY"] / df["RANGE"]
    df["UPPER_WICK_RATIO"] = df["UPPER_WICK"] / df["RANGE"]
    df["LOWER_WICK_RATIO"] = df["LOWER_WICK"] / df["RANGE"]

    df["BULLISH_CANDLE"] = df["close"] > df["open"]
    df["BEARISH_CANDLE"] = df["close"] < df["open"]

    df["HAMMER"] = (
        (df["LOWER_WICK_RATIO"] > 0.55)
        & (df["BODY_RATIO"] < 0.35)
    )

    df["SHOOTING_STAR"] = (
        (df["UPPER_WICK_RATIO"] > 0.55)
        & (df["BODY_RATIO"] < 0.35)
    )

    df["ENGULFING_BULL"] = (
        (df["close"] > df["open"])
        & (df["close"].shift(1) < df["open"].shift(1))
        & (df["close"] > df["open"].shift(1))
        & (df["open"] < df["close"].shift(1))
    )

    df["ENGULFING_BEAR"] = (
        (df["close"] < df["open"])
        & (df["close"].shift(1) > df["open"].shift(1))
        & (df["close"] < df["open"].shift(1))
        & (df["open"] > df["close"].shift(1))
    )

    df["PATTERN_SCORE"] = 0
    df.loc[df["HAMMER"], "PATTERN_SCORE"] += 25
    df.loc[df["ENGULFING_BULL"], "PATTERN_SCORE"] += 35
    df.loc[df["SHOOTING_STAR"], "PATTERN_SCORE"] -= 25
    df.loc[df["ENGULFING_BEAR"], "PATTERN_SCORE"] -= 35

    return df