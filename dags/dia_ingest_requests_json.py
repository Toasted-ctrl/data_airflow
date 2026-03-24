from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.core.configs import dia_config
from scripts.custom.DIA.dia_fetch_sources import fetch_sources
from scripts.database.session import get_db
from scripts.requests import dia_request_json

with DAG(
    dag_id="dia_ingest_hourly_json",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag_hourly:
    
    @task.python
    def get_sources():
        db = get_db(engine_url=dia_config.db_url)
        return fetch_sources(db=db, type="hourly")
    
    @task.python
    def request_json(source):
        return dia_request_json()
    
    _sources = get_sources()
    _data = request_json.expand(source=_sources)

with DAG(
    dag_id="dia_ingest_daily_json",
    start_date=datetime(2026, 3, 1),
    schedule="@daily",
    catchup=False
) as dag_daily:
    
    @task.python
    def get_sources():
        db = get_db(engine_url=dia_config.db_url)
        return fetch_sources(db=db, type="daily")
    
    @task.python
    def request_json(source):
        return dia_request_json()
    
    _sources = get_sources()
    _data = request_json.expand(source=_sources)