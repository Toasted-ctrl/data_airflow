from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.configs.DIA import dia_config
from scripts.custom.DIA.dia_fetch_sources import fetch_sources
from scripts.database.session import get_db
from scripts.api_requests.requests import api_get_request, api_post_request

@task.python # Get sources from DIA ingest table
def get_sources(sequence: str) -> list:
    db = get_db(engine_url=dia_config.db_url)
    return fetch_sources(db=next(db), sequence=sequence)
    
@task.python # Making the api request
def fetch_api_response(source: dict) -> dict:
    return api_get_request(request_data=source)

@task.python # Posting API results through DIA
def post_results(data: dict) -> None:
    return api_post_request(
        data=data,
        api_url=dia_config.DIA_API_POST_URL,
        api_key=dia_config.DIA_API_KEY,
        api_key_name=dia_config.DIA_API_KEY_NAME
    )

with DAG(
    dag_id="DIA.Ingest.Daily",
    start_date=datetime(2026, 3, 1),
    schedule="@daily",
    catchup=False
) as dag_daily:
    
    _sources = get_sources(sequence="daily")
    _data = fetch_api_response.expand(source=_sources)
    results = post_results.expand(data=_data)

with DAG(
    dag_id="DIA.Ingest.Hourly",
    start_date=datetime(2026, 3, 1),
    schedule="@hourly",
    catchup=False
) as dag_hourly:
    
    _sources = get_sources(sequence="hourly")
    _data = fetch_api_response.expand(source=_sources)
    results = post_results.expand(data=_data)

with DAG(
    dag_id="DIA.Ingest.Interval.Minutes.30",
    start_date=datetime(2026, 3, 1),
    schedule="*/30 * * * *", # Cron expression, every 30 minutes
    catchup=False
) as dag_interval_minutes_30:
    
    _sources = get_sources(sequence="30 minute interval")
    _data = fetch_api_response.expand(source=_sources)
    results = post_results.expand(data=_data)