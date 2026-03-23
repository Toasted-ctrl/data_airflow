import os

from airflow.sdk import task
from dotenv import load_dotenv

from core.config import config

@task
def request_json():
    print(config.ingest_db_url)