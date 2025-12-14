# Healthcare Patient Analytics Pipeline

A HIPAA-aware, production-grade data pipeline for analyzing synthetic patient data (~63,000 patients from Synthea). Demonstrates end-to-end modern data engineering practices: ingestion, warehousing, transformation, validation, observability, and alerting.

## Overview & Motivation

This project processes fully synthetic healthcare data to enable safe analytics such as:
- 30-day patient readmission rates
- Length of stay (LOS) trends
- Demographic breakdowns
- Diagnosis patterns

Built with HIPAA compliance in mind: no real PHI, encrypted storage/transit, role-based access, and data quality checks.

## Architecture

```mermaid
graph TD
    A["S3 Raw Zone\n(CSV/JSON synthetic data)"] --> B["AWS Glue Crawlers\n(Infer schema)"]
    B --> C["AWS Glue Jobs\n(ETL to Parquet)"]
    C --> D["Snowflake Data Warehouse\n(Staging → Analytics schemas)"]
    D --> E["dbt Models\n(Transformations & Tests)"]
    E --> F["Great Expectations\n(Data Validation)"]
    F -->|Failure| G["Slack Alerts\n(via Snowflake Tasks/Lambda)"]
    F -->|Success| H["Analytics Marts\n(Ready for BI tools)"]

    subgraph "Core Orchestration (Serverless)"
        D --> I[Snowflake Tasks\n(Scheduling & Retries)]
        I --> E
        I --> F
        I --> G
    end

    subgraph "Optional Enhancement"
        J[Apache Airflow\n(Advanced DAG orchestration,\nvisual monitoring, complex dependencies)]
        J -.-> D
        J -.-> E
        J -.-> F
        J -.-> G
    end

    style J fill:#f9f,stroke:#333,stroke-dasharray: 5 5
