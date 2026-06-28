import pandas as pd

EMA_PERIODS = [2, 4, 8, 16, 32, 64, 128, 360, 720, 1440]


def add_ema_geometry(df: pd.DataFrame) -> pd.DataFrame:

    # EMA 기울기(Angle)
    for period in EMA_PERIODS:
        ema = f"EMA_{period}"
        df[f"{ema}_ANGLE"] = df[ema].diff()

    # EMA 간격(Spread)
    for i in range(len(EMA_PERIODS) - 1):
        fast = EMA_PERIODS[i]
        slow = EMA_PERIODS[i + 1]

        df[f"SPREAD_{fast}_{slow}"] = (
            df[f"EMA_{fast}"] - df[f"EMA_{slow}"]
        )

    # Compression Score
    spread_cols = [c for c in df.columns if c.startswith("SPREAD_")]

    df["EMA_COMPRESSION"] = (
        df[spread_cols]
        .abs()
        .mean(axis=1)
    )

    return df