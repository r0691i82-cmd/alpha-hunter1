import pandas as pd


def add_quarter_zone(df: pd.DataFrame) -> pd.DataFrame:
    range_high = df["high"].rolling(96).max()
    range_low = df["low"].rolling(96).min()

    price_range = (range_high - range_low).replace(0, 1)
    position = (df["close"] - range_low) / price_range

    df["DAY_QUARTER_POSITION"] = position

    df["DAY_QUARTER_ZONE"] = "UNKNOWN"
    df.loc[position <= 0.25, "DAY_QUARTER_ZONE"] = "Q1"
    df.loc[(position > 0.25) & (position <= 0.50), "DAY_QUARTER_ZONE"] = "Q2"
    df.loc[(position > 0.50) & (position <= 0.75), "DAY_QUARTER_ZONE"] = "Q3"
    df.loc[position > 0.75, "DAY_QUARTER_ZONE"] = "Q4"

    return df