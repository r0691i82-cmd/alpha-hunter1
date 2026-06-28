import pandas as pd


def add_trend_features(df: pd.DataFrame) -> pd.DataFrame:
    df["EMA_FAN_BULL"] = (
        (df["EMA_2"] > df["EMA_4"])
        & (df["EMA_4"] > df["EMA_8"])
        & (df["EMA_8"] > df["EMA_16"])
        & (df["EMA_16"] > df["EMA_32"])
        & (df["EMA_32"] > df["EMA_64"])
    )

    df["EMA_FAN_BEAR"] = (
        (df["EMA_2"] < df["EMA_4"])
        & (df["EMA_4"] < df["EMA_8"])
        & (df["EMA_8"] < df["EMA_16"])
        & (df["EMA_16"] < df["EMA_32"])
        & (df["EMA_32"] < df["EMA_64"])
    )

    df["TREND_EXHAUSTION"] = (
        (df["RSI_14"] > 70)
        & (df["VWAP_DISTANCE_PCT"] > 0.3)
    )

    df["TREND_ENGINE_SCORE"] = 0

    df.loc[df["EMA_FAN_BULL"], "TREND_ENGINE_SCORE"] += 40
    df.loc[df["EMA_64_ANGLE"] > 0, "TREND_ENGINE_SCORE"] += 25
    df.loc[df["EMA_128_ANGLE"] > 0, "TREND_ENGINE_SCORE"] += 25
    df.loc[df["TREND_EXHAUSTION"], "TREND_ENGINE_SCORE"] -= 30

    df.loc[df["EMA_FAN_BEAR"], "TREND_ENGINE_SCORE"] -= 40

    return df