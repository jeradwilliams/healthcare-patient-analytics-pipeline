# Great Expectations: Healthcare Patient Data Validation

This folder contains the **Great Expectations** configuration and suites for ensuring data quality in the Healthcare Patient Analytics Pipeline.

- **Datasource**: Connected to Snowflake (raw schema with ~63,000 synthetic patients from Synthea)
- **Key Focus**: HIPAA-minded validations (no real PHI, null checks, date ranges, gender sets, diagnosis code patterns)
- **Integration**: Validation runs post-dbt, with failures triggering Slack alerts (self-healing pipeline)

## Key Expectations in the Suite
- Row count between 50k–100k for admissions table
- No null patient_ids
- Birth dates between 1900–2025
- Gender values only 'M' or 'F'
- Diagnosis codes follow basic ICD-like pattern

Example from `expectations/patient_admissions_suite.json`:
```json
{
  "expectation_type": "expect_column_values_to_be_in_set",
  "kwargs": {
    "column": "gender",
    "value_set": ["M", "F"]
  }
}
