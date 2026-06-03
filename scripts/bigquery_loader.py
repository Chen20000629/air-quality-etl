from google.cloud import bigquery
from scripts.logger import logger


def upload_to_bigquery(df):

    client = bigquery.Client(project="air-quality-etl-497717")

    table_id = (
        "air-quality-etl-497717.air_quality.air_quality_history"
    )

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    logger.info("uploaded to BigQuery")

    print("uploaded to BigQuery successfully")

def build_dim_site():

    client = bigquery.Client()

    query = """
    CREATE OR REPLACE TABLE `air-quality-etl-497717.air_quality.dim_site` AS
    SELECT
        ROW_NUMBER() OVER() AS site_id,
        site,
        county
    FROM (
        SELECT DISTINCT site, county
        FROM `air-quality-etl-497717.air_quality.air_quality_history`
    )
    """

    client.query(query).result()

    print("dim_site built")

def build_fact_table():

    client = bigquery.Client()

    query = """
    CREATE OR REPLACE TABLE `air-quality-etl-497717.air_quality.air_quality_fact` AS
    SELECT
        h.ingestion_time,
        d.site_id,
        h.aqi,
        h.pm25
    FROM `air-quality-etl-497717.air_quality.air_quality_history` h
    JOIN `air-quality-etl-497717.air_quality.dim_site` d
    ON h.site = d.site
    AND h.county = d.county
    """

    client.query(query).result()

    print("fact table built")

def update_dim_site():
    
    client = bigquery.Client()
    
    query = """
    INSERT INTO `air-quality-etl-497717.air_quality.dim_site`
    (site_id, site, county)

    SELECT
        (
            SELECT COALESCE(MAX(site_id),0)
            FROM `air-quality-etl-497717.air_quality.dim_site`
        )
        + ROW_NUMBER() OVER() AS site_id,

        h.site,
        h.county

    FROM (
        SELECT DISTINCT
            site,
            county
        FROM `air-quality-etl-497717.air_quality.air_quality_history`
    ) h

    LEFT JOIN `air-quality-etl-497717.air_quality.dim_site` d

    ON h.site = d.site
    AND h.county = d.county

    WHERE d.site IS NULL
    """

    client.query(query).result()