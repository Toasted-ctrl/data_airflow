from airflow.sdk import task

from scripts.core.configs import dia_config

@task
def request_json(type: str=None):
    print(f"DB url: {dia_config.dia_db_url}")
    print(f"Key: {dia_config.dia_api_key}")