from datetime import datetime
from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.slack.operators.slack import SlackAPIPostOperator
from airflow.operators.python import PythonOperator
# Assume dbt & GE tasks via bash or custom operators

with DAG(
    dag_id='healthcare_patient_analytics_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args={'retries': 2}
) as dag:

    trigger_glue_job = GlueJobOperator(
        task_id='run_glue_etl',
        job_name='your_glue_job_name',
        # script_location='s3://your-bucket/scripts/'
    )

    run_dbt_models = SnowflakeOperator(  # Or use BashOperator for dbt CLI
        task_id='run_dbt_transformations',
        sql="CALL dbt_run_procedure()",  # If using dbt Cloud/Snowflake integration
        snowflake_conn_id='snowflake_conn'
    )

    run_ge_validation = PythonOperator(
        task_id='great_expectations_validation',
        python_callable=lambda: __import__('great_expectations').checkpoint.run(...)  # Simplified
    )

    slack_alert_on_failure = SlackAPIPostOperator(
        task_id='slack_failure_alert',
        channel='#data-alerts',
        text='Healthcare pipeline failed at {{ task_instance.task_id }}!',
        trigger_rule='one_failed'
    )

    slack_success_alert = SlackAPIPostOperator(
        task_id='slack_success',
        channel='#data-alerts',
        text='Healthcare pipeline completed successfully! ~63k patients processed.'
    )

    trigger_glue_job >> run_dbt_models >> run_ge_validation >> [slack_success_alert, slack_alert_on_failure]
