import pandas as pd
from scripts.logger import logger
from datetime import datetime

def transform_data(df):

    cols = [
        "county",
        "sitename",
        "aqi",
        "pm2.5",
        "status",
        "publishtime"
    ]

    df = df[cols]

    df.columns = [
        "county",
        "site",
        "aqi",
        "pm25",
        "status",
        "time"
    ]

    df["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")
    df["pm25"] = pd.to_numeric(df["pm25"], errors="coerce")

    df = df.dropna()

    df = df.reset_index(drop=True)

    logger.info(f"transform rows: {len(df)}")

    df["ingestion_time"] = datetime.now()

    return df