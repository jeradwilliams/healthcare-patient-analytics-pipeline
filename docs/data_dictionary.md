# Data Dictionary - Healthcare Patient Analytics Pipeline

This data dictionary describes the key tables from the synthetic healthcare dataset (generated via Synthea, ~63,000 patients). Data is loaded raw into Snowflake, cleaned in dbt staging models, and transformed into analytics marts.

## Raw Tables (from S3 → Snowflake)

### patients
Core patient demographics.

| Column Name     | Data Type | Description                          | Example Value          |
|-----------------|-----------|--------------------------------------|------------------------|
| patient_id      | VARCHAR   | Unique patient identifier            | 123e4567-e89b-12d3... |
| birth_date      | DATE      | Patient date of birth                | 1950-05-15             |
| gender          | VARCHAR   | Patient gender (M/F)                  | M                      |
| city            | VARCHAR   | City of residence                    | Boston                 |
| state           | VARCHAR   | State of residence                   | MA                     |
| zip_code        | VARCHAR   | ZIP code                             | 02101                  |

### admissions (or encounters)
Hospital admission records.

| Column Name       | Data Type | Description                              | Example Value          |
|-------------------|-----------|------------------------------------------|------------------------|
| admission_id      | VARCHAR   | Unique admission identifier              | abc123-def456...       |
| patient_id        | VARCHAR   | Foreign key to patients                  | 123e4567-e89b-12d3... |
| admission_date    | DATE      | Date of admission                        | 2022-01-10             |
| discharge_date    | DATE      | Date of discharge                        | 2022-01-15             |
| diagnosis_code    | VARCHAR   | Primary ICD-like diagnosis code           | I21.0                  |
| length_of_stay    | INTEGER   | Calculated days (discharge - admission)   | 5                      |

### diagnoses (or conditions)
Patient conditions/diagnoses over time.

| Column Name     | Data Type | Description                        | Example Value    |
|-----------------|-----------|------------------------------------|------------------|
| condition_id    | VARCHAR   | Unique condition record            | ...              |
| patient_id      | VARCHAR   | Foreign key to patients            | ...              |
| start_date      | DATE      | Condition onset date               | 2020-03-01       |
| end_date        | DATE      | Condition resolution date (nullable)| NULL             |
| code            | VARCHAR   | SNOMED or ICD code                 | 44054006         |
| description     | VARCHAR   | Human-readable description         | Diabetes mellitus|

## Marts (dbt Transformations)

### mart_patient_readmissions
Analytics-ready table with readmission flags and metrics.

| Column Name                  | Data Type | Description                                      | Example Value |
|------------------------------|-----------|--------------------------------------------------|---------------|
| patient_id                   | VARCHAR   | Unique patient                                   | ...           |
| readmitted_within_30_days    | INTEGER   | 1 if readmitted ≤30 days after prior discharge   | 1             |
| length_of_stay_days          | INTEGER   | Average or per-admission LOS                     | 4.2           |
| total_admissions             | INTEGER   | Count of admissions                              | 3             |

Data is fully synthetic—no real PHI. Sources: [Synthea GitHub](https://github.com/synthetichealth/synthea)

Last updated: December 2025
