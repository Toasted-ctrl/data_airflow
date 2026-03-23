from airflow.sdk import task

from scripts.core.config import config

@task
def request_json():
    print(config.ingest_db_url)