from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.core.configs import dia_config
from scripts.custom.DIA.dia_fetch_sources import fetch_sources
from scripts.database.session import get_db
from scripts.requests import dia_request_json

with DAG(
    dag_id="dia_ingest_requests_json",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:
    
    @task
    def get_sources():
        db = get_db(engine_url=dia_config.db_url)
        return fetch_sources(db=db, type="hourly")
    
    @task
    def request_json(sources):
        return dia_request_json()
    
    sources = get_sources()

    request_json(sources=sources)

    "sources >> request_json"