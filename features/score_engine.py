import pandas as pd


def add_score_engine(df: pd.DataFrame) -> pd.DataFrame:
    df["TREND_SCORE"] = 0

    df.loc[df["EMA_8"] > df["EMA_32"], "TREND_SCORE"] += 25
    df.loc[df["EMA_32"] > df["EMA_128"], "TREND_SCORE"] += 25
    df.loc[df["close"] > df["VWAP"], "TREND_SCORE"] += 25
    df.loc[df["MACD"] > df["MACD_SIGNAL"], "TREND_SCORE"] += 25

    df["COMPRESSION_SCORE"] = (
        100 - df["EMA_COMPRESSION"].rank(pct=True) * 100
    )

    df["MOMENTUM_SCORE"] = 0
    df.loc[df["RSI_14"] > 50, "MOMENTUM_SCORE"] += 40
    df.loc[df["MACD_HIST"] > 0, "MOMENTUM_SCORE"] += 40
    df.loc[df["RS_SCORE"] > 0, "MOMENTUM_SCORE"] += 20

    df["ALPHA_SCORE"] = (
        df["TREND_SCORE"] * 0.4
        + df["COMPRESSION_SCORE"] * 0.3
        + df["MOMENTUM_SCORE"] * 0.3
    )

    return df