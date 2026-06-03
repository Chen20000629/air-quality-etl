from scripts.logger import logger


def validate_data(df):

    # 檢查是否空資料
    if df.empty:
        logger.error("validation failed: dataframe is empty")
        raise ValueError("dataframe is empty")

    # 檢查必要欄位
    required_cols = [
        "county",
        "site",
        "aqi",
        "pm25",
        "status",
        "time"
    ]

    missing_cols = [
        col for col in required_cols
        if col not in df.columns
    ]

    if missing_cols:
        logger.error(f"missing columns: {missing_cols}")
        raise ValueError(f"missing columns: {missing_cols}")

    # 檢查缺值
    null_count = df.isnull().sum().sum()

    logger.info(f"null values count: {null_count}")

    # AQI合理範圍檢查
    invalid_aqi = df[
        (df["aqi"] < 0) |
        (df["aqi"] > 500)
    ]

    if len(invalid_aqi) > 0:
        logger.warning(
            f"invalid AQI rows: {len(invalid_aqi)}"
        )

    logger.info("validation passed")