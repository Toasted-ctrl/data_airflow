from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.configs.DIA import dia_config, Sources
from scripts.database.get_data import get_all_filter_by
from scripts.database.session import get_db
from scripts.api_requests.requests import api_get_request, api_post_request

@task.python # Fetching all sources for which an API call needs to be made.
def get_sources(sequence: str) -> list:
    db = get_db(engine_url=dia_config.db_url)

    filter_by_values = {
        "is_active": True,
        "sequence": sequence
    }

    return_fields = [
        "source_id",
        "base_url",
        "url_ext",
        "headers",
        "params",
        "content_type"
    ]

    return get_all_filter_by(
        table_schema=Sources,
        db=next(db),
        filter_by_values=filter_by_values,
        return_fields=return_fields)
    
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
    dag_display_name="DIA: Ingest, hourly",
    start_date=datetime(2026, 3, 1),
    schedule="@hourly",
    catchup=False
) as dag_hourly:
    
    _sources = get_sources(sequence="hourly")
    _data = fetch_api_response.expand(source=_sources)
    results = post_results.expand(data=_data)

with DAG(
    dag_id="DIA.Ingest.Minutes.30",
    dag_display_name="DIA: Ingest, every 30 minutes",
    start_date=datetime(2026, 3, 1),
    schedule="*/30 * * * *", # Cron expression, every 30 minutes
    catchup=False
) as dag_interval_minutes_30:
    
    _sources = get_sources(sequence="30 minute interval")
    _data = fetch_api_response.expand(source=_sources)
    results = post_results.expand(data=_data)