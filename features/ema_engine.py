import pandas as pd

EMA_PERIODS = [2, 4, 8, 16, 32, 64, 128, 360, 720, 1440]


def add_ema(df: pd.DataFrame) -> pd.DataFrame:
    for period in EMA_PERIODS:
        df[f"EMA_{period}"] = df["close"].ewm(
            span=period,
            adjust=False
        ).mean()

    return df