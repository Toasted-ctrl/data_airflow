import os

from airflow.decorators import task
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("INGEST_DB_HOSTNAME")

@task
def request_json():
    print(hostname)