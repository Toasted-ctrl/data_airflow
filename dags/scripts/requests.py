from airflow.sdk import task

from scripts.core.configs import dia_config

@task
def dia_request_json(str=None):
    print(f"DB url: {dia_config.db_url}")
    print(f"Key: {dia_config.api_key}")