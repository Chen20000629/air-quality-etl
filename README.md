# Air Quality ETL Pipeline

A Python-based ETL pipeline that extracts air quality data from the Taiwan Ministry of Environment API, transforms and validates the data, and loads it into Google BigQuery for historical analysis.

---

## Architecture

API
↓
Extract
↓
Transform
↓
Validate
↓
BigQuery History Table
↓
Star Schema
├─ dim_site
└─ air_quality_fact

---

## Tech Stack

- Python
- Pandas
- SQL
- Google BigQuery
- GCP
- Schedule
- Git

---

