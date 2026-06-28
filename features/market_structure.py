import pandas as pd


def add_market_structure(df: pd.DataFrame) -> pd.DataFrame:
    df["STRUCTURE_SCORE"] = (
        df["TREND_SCORE"] * 0.30
        + df["MOMENTUM_SCORE"] * 0.20
        + df["COMPRESSION_SCORE"] * 0.20
        + df["LIQUIDITY_SCORE"] * 0.15
        + df["ALPHA_SCORE"] * 0.15
    )

    df["STRUCTURE_STATE"] = "NEUTRAL"

    df.loc[df["STRUCTURE_SCORE"] >= 75, "STRUCTURE_STATE"] = "STRONG_BULL"
    df.loc[
        (df["STRUCTURE_SCORE"] >= 55) & (df["STRUCTURE_SCORE"] < 75),
        "STRUCTURE_STATE",
    ] = "BULL"
    df.loc[
        (df["STRUCTURE_SCORE"] >= 40) & (df["STRUCTURE_SCORE"] < 55),
        "STRUCTURE_STATE",
    ] = "NEUTRAL"
    df.loc[df["STRUCTURE_SCORE"] < 40, "STRUCTURE_STATE"] = "WEAK"

    return df