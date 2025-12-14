{{ config(materialized='view') }}

select
    admission_id,
    patient_id,
    cast(admission_date as date) as admission_date,
    cast(discharge_date as date) as discharge_date,
    diagnosis_code
from {{ source('raw', 'admissions') }}
