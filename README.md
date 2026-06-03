# Air Quality ETL Pipeline on GCP

## Project Overview

This project demonstrates an end-to-end Data Engineering pipeline that extracts Taiwan air quality data from the Ministry of Environment (MOENV) Open API, transforms and validates the data using Python, and loads it into Google BigQuery for historical analysis.

The project also implements a Data Warehouse design using a Star Schema model, including Fact and Dimension tables for analytical workloads.

---

## Business Objective

The goal of this project is to simulate a real-world Data Engineering workflow:

- Collect data from external APIs
- Build an automated ETL pipeline
- Store historical data for trend analysis
- Design a scalable Data Warehouse
- Support downstream analytics and BI reporting

---

## Architecture

```text
MOENV Air Quality API
          │
          ▼
      Extract
          │
          ▼
     Transform
          │
          ▼
      Validate
          │
          ▼
 BigQuery History Table
          │
          ▼
   Star Schema Model
     ├── dim_site
     └── air_quality_fact
