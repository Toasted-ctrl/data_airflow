import os

from airflow.sdk import task
from dotenv import load_dotenv

@task
def request_json():
    load_dotenv()
    hostname = os.getenv("INGEST_DB_HOSTNAME")
    print(hostname)