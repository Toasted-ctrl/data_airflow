from airflow.sdk import task

from scripts.core.config import config

@task
def request_json():
    print(f"DB url: {config.dia_db_url}")
    print(f"Key: {config.dia_api_key}")