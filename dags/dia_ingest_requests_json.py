from airflow import DAG
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
    
    db = get_db(engine_url=dia_config.db_url)
    sources = fetch_sources(db=db, type="hourly")
    dia_request_json()

    db >> sources >> dia_request_json