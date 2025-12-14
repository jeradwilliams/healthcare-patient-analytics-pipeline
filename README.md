# Healthcare Patient Analytics Pipeline

A HIPAA-aware, production-grade data pipeline for analyzing synthetic patient data (~63,000 patients). Demonstrates end-to-end modern data engineering practices: ingestion, warehousing, transformation, validation, observability, and alerting.

## Overview & Motivation
This project processes synthetic healthcare data (generated with Synthea, mimicking real datasets like MIMIC-III but fully synthetic for privacy) to enable key analytics such as:
- 30-day patient readmission rates
- Length of stay (LOS) trends
- Demographic breakdowns
- Diagnosis patterns

Built with HIPAA compliance in mind: no real PHI, encrypted storage/transit, role-based access.

## Architecture

The core pipeline is serverless (Glue → Snowflake Tasks → Slack), but includes an **optional enhancement: orchestrated with Apache Airflow** for advanced scheduling, retries, dependency management, and visual DAG monitoring.

```mermaid
graph TD
    A["S3 Raw Zone\n(CSV/JSON synthetic data)"] --> B["AWS Glue Crawlers\n(Infer schema)"]
    B --> C["AWS Glue Jobs\n(ETL to Parquet)"]
    C --> D["Snowflake Data Warehouse\n(Raw → Staging → Analytics)"]
    D --> E["dbt Models\n(Staging → Marts\nTransformations & Tests)"]
    E --> F["Great Expectations\n(Data Validation Suite)"]
    F -->|Failure| G["Slack Alerts\n(via Webhook / Snowflake Task)"]
    F -->|Success| H["Analytics Marts\n(Ready for BI / Reporting)"]
    H --> I["Optional: Airflow Orchestration\n(Full DAG scheduling & monitoring)"]

    subgraph Observability
        G & H
    end
