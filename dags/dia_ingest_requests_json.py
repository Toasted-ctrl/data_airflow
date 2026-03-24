from airflow import DAG
from datetime import datetime

from scripts.core.configs import dia_config
from scripts.database.session import get_db
from scripts.requests import request_json

with DAG(
    dag_id="dia_ingest_requests_json",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:
    
    db = get_db(engine_url=dia_config.dia_db_url)
    request_json()