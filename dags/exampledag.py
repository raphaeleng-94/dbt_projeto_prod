from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
import os

my_dbt_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/projeto_prod"),
    profile_config=ProfileConfig(
        profile_name="projeto_prod",
        target_name="dev",
        profiles_yml_filepath="/usr/local/airflow/dags/dbt/projeto_prod/profiles.yml"
    ),
    execution_config=ExecutionConfig(
        dbt_executable_path=f'{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt'
    ),
    schedule='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id='projeto_prod'
)
