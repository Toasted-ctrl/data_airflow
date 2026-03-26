from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.core.configs import dia_config
from scripts.custom.DIA.dia_fetch_sources import fetch_sources
from scripts.custom.DIA.dia_insert_results import insert_results
from scripts.database.session import get_db
from scripts.requests import api_request_json

@task.python # Get sources from DIA ingest table
def get_sources(type: str, sequence: str) -> list:
    db = get_db(engine_url=dia_config.db_url)
    return fetch_sources(db=next(db), type=type, sequence=sequence)
    
@task.python # Making the api request with json response
def api_request(source: dict) -> dict:
    return api_request_json(request_data=source)

@task.python # Posting API results through DIA
def post_results(entry: dict) -> None:
    insert_results(entry=entry)

with DAG(
    dag_id="dia_ingest_daily_json",
    start_date=datetime(2026, 3, 1),
    schedule="@daily",
    catchup=False
) as dag_daily:
    
    _sources = get_sources(dtype="json", sequence="daily")
    _data = api_request.expand(source=_sources)
    post_results.expand(entry=_data)

with DAG(
    dag_id="dia_ingest_hourly",
    start_date=datetime(2026, 3, 1),
    schedule="@hourly",
    catchup=False
) as dag_hourly:
    
    _sources = get_sources(dtype="json", sequence="hourly")
    _data = api_request.expand(source=_sources)
    post_results.expand(entry=_data)