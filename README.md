# Healthcare Patient Analytics Pipeline

A HIPAA-aware, production-grade data pipeline for analyzing synthetic patient data (~63,000 patients). Demonstrates end-to-end modern data engineering practices: ingestion, warehousing, transformation, validation, observability, and alerting.

## Overview & Motivation
This project processes synthetic healthcare data (mimicking real datasets like MIMIC-III but fully synthetic for privacy) to enable analytics such as:
- Patient readmission rates
- Length of stay trends
- Demographic insights
- Diagnosis patterns

Built with HIPAA compliance in mind: no real PHI, encrypted storage/transit, role-based access.

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

    subgraph Observability
        G & H
    end
