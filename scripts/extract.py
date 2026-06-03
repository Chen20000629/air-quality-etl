import requests
import pandas as pd
import os
from dotenv import load_dotenv
from scripts.logger import logger

load_dotenv()

API_KEY = os.getenv("AIR_API_KEY")

URL = "https://data.moenv.gov.tw/api/v2/aqx_p_432"


def extract_data(limit=100):

    params = {
        "api_key": API_KEY,
        "limit": limit
    }

    response = requests.get(URL, params=params)

    logger.info(f"extract status: {response.status_code}")

    data = response.json()

    if isinstance(data, dict):
        records = data.get("records", [])
    else:
        records = data

    df = pd.DataFrame(records)

    logger.info(f"extract rows: {len(df)}")

    return df