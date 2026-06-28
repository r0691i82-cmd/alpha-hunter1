import pandas as pd


def add_multi_timeframe_features(df: pd.DataFrame) -> pd.DataFrame:
    df["MTF_SHORT_TREND"] = "NEUTRAL"
    df["MTF_MEDIUM_TREND"] = "NEUTRAL"

    df.loc[
        (df["EMA_8"] > df["EMA_32"])
        & (df["close"] > df["VWAP"]),
        "MTF_SHORT_TREND",
    ] = "BULL"

    df.loc[
        (df["EMA_8"] < df["EMA_32"])
        & (df["close"] < df["VWAP"]),
        "MTF_SHORT_TREND",
    ] = "BEAR"

    df.loc[
        (df["EMA_64"] > df["EMA_128"])
        & (df["EMA_128_ANGLE"] > 0),
        "MTF_MEDIUM_TREND",
    ] = "BULL"

    df.loc[
        (df["EMA_64"] < df["EMA_128"])
        & (df["EMA_128_ANGLE"] < 0),
        "MTF_MEDIUM_TREND",
    ] = "BEAR"

    df["MTF_SCORE"] = 0

    df.loc[df["MTF_SHORT_TREND"] == "BULL", "MTF_SCORE"] += 30
    df.loc[df["MTF_MEDIUM_TREND"] == "BULL", "MTF_SCORE"] += 40
    df.loc[df["STRUCTURE_STATE"].isin(["BULL", "STRONG_BULL"]), "MTF_SCORE"] += 30

    df.loc[df["MTF_SHORT_TREND"] == "BEAR", "MTF_SCORE"] -= 30
    df.loc[df["MTF_MEDIUM_TREND"] == "BEAR", "MTF_SCORE"] -= 40
    df.loc[df["STRUCTURE_STATE"] == "WEAK", "MTF_SCORE"] -= 30

    return df