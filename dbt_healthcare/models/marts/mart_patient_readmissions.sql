{{ config(materialized='table') }}

with admissions as (
    select * from {{ ref('stg_admissions') }}
),

patients as (
    select * from {{ ref('stg_patients') }}
),

readmissions as (
    select
        a1.patient_id,
        a1.admission_date,
        a1.discharge_date,
        a2.admission_date as readmission_date,
        case when a2.admission_date <= dateadd(day, 30, a1.discharge_date) then 1 else 0 end as readmitted_within_30_days
    from admissions a1
    left join admissions a2
        on a1.patient_id = a2.patient_id
        and a2.admission_date > a1.discharge_date
)

select
    p.*,
    r.readmission_date,
    r.readmitted_within_30_days,
    datediff(day, admission_date, discharge_date) as length_of_stay_days
from patients p
left join readmissions r on p.patient_id = r.patient_id
