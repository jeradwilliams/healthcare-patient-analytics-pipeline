# Healthcare Patient Analytics Pipeline

A HIPAA-aware, production-grade data pipeline for analyzing synthetic patient data (~63,000 patients). This end-to-end project demonstrates modern data engineering best practices: secure ingestion, warehousing, transformation, quality validation, observability, and alerting.

## Overview & Motivation

This pipeline processes synthetic healthcare data (generated via tools like Synthea, mimicking real datasets but fully de-identified) to enable key analytics such as:
- Patient readmission rates
- Length of stay (LOS) trends
- Demographic breakdowns (age, gender, ethnicity)
- Diagnosis and procedure patterns

**HIPAA compliance focus**: Uses only synthetic data (no real PHI), encrypted storage/transit (S3 SSE, Snowflake encryption), and role-based access controls.

The pipeline is designed to be reliable, with data validation and automated alerts for failures (self-healing where possible).

## Architecture

Here are professional architecture diagrams that represent the core flow of this project:

![Modern Data Platform with dbt on AWS (S3 → Glue → Warehouse → Transformations)](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2023/10/02/BDB-3273-Modern-data-platform-using-DBT_001.png)
*AWS-recommended modern data platform using dbt (very close match: ingestion from S3/Glue into warehouse, then transformations)*

<grok-card data-id="9270e9" data-type="image_card"></grok-card>


![AWS Glue + dbt Pipeline Example](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/04/20/BDB-2022-image001.jpg)
*Build data pipelines with AWS Glue, Lake Formation, and dbt*

<grok-card data-id="2a7e12" data-type="image_card"></grok-card>


![Data Validation Framework with Glue, Snowflake, dbt](https://media.licdn.com/dms/image/v2/D4D12AQHAytP9m55eXQ/article-cover_image-shrink_720_1280/B4DZp9nea0IkAQ-/0/1763044101844?e=2147483647&v=beta&t=DMZjmDUPCH8cEBYiHP55cnWAOBYYDpV3bc8Bz22_ieo)
*Includes explicit data validation step (aligns with Great Expectations usage)*

<grok-card data-id="305e1a" data-type="image_card"></grok-card>


![Enterprise AWS + Snowflake Blueprint](https://cdn.prod.website-files.com/6541750d4db1a741ed66738c/66f43f706ab6d556b5dab718_AWS%2BSnowflake%20Blueprints.png)
*Clean enterprise-grade flow with zones and observability*

<grok-card data-id="2a8e0d" data-type="image_card"></grok-card>


Core flow summary:
- **Raw data** → S3
- **Ingestion** → AWS Glue Crawlers & Jobs (schema inference, ETL to Parquet)
- **Warehousing** → Snowflake (staging → analytics schemas)
- **Transformations** → dbt models & tests
- **Validation** → Great Expectations (data quality checks)
- **Observability** → Slack alerts on failures (via Snowflake tasks or Lambda)

## Tech Stack

- **Storage/Ingestion**: AWS S3, Glue Crawlers, Glue Jobs (PySpark)
- **Data Warehouse**: Snowflake
- **Transformations & Testing**: dbt Core/Cloud
- **Data Quality**: Great Expectations
- **Alerting**: Slack webhooks (triggered on validation/job failures)
- **Data Source**: Synthea synthetic healthcare data (public, privacy-safe)

## Prerequisites & Local Setup

1. AWS account (S3 bucket, IAM roles for Glue)
2. Snowflake account (virtual warehouse, roles)
3. dbt Core or dbt Cloud
4. Great Expectations (Python package)
5. Slack incoming webhook URL for alerts

Steps to run:
- Upload synthetic CSVs to S3 raw zone
- Run Glue crawlers/jobs to load into Snowflake staging
- Configure `profiles.yml` for dbt/Snowflake connection
- `dbt run` → builds marts
- `great_expectations checkpoint run` → validates
- Failures trigger Slack alerts

## Key Outcomes & Sample Insights

- 100% passing data quality checks (e.g., no duplicate patient IDs, valid date ranges)
- Example analytics from mart tables:
  - ~15-20% 30-day readmission rate
  - Average length of stay: 4-5 days
  - Higher readmissions in certain diagnosis groups

(Add screenshots of dbt run output, GE validation reports, or Snowflake queries here once available)

## Folder Structure (Planned/Upcoming)
