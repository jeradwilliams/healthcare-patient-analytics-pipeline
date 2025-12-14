{{ config(materialized='view') }}

select
    patient_id,
    cast(birthdate as date) as birth_date,
    upper(sex) as gender,
    city,
    state
from {{ source('raw', 'patients') }}  -- assumes raw data loaded to Snowflake
where patient_id is not null
