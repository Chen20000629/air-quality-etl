import os
from scripts.logger import logger

def load_data(df):

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/air_quality.csv", index=False)

    df.to_parquet("output/air_quality.parquet", index=False)

    logger.info("csv load completed")

    logger.info("parquet load completed ")