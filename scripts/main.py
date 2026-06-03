from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.logger import logger
from scripts.validate import validate_data
from scripts.bigquery_loader import (
    upload_to_bigquery,
    update_dim_site,
    build_fact_table
)

def main():

    try:

        logger.info("pipeline started")

        raw_df = extract_data()

        clean_df = transform_data(raw_df)

        validate_data(clean_df)

        load_data(clean_df)

        upload_to_bigquery(clean_df)

        update_dim_site()
        build_fact_table()

        logger.info("pipeline completed")

    except Exception as e:  

        logger.exception(f"pipeline failed: {e}")

        raise