from airflow import DAG
from datetime import datetime

from scripts.requests import request_json

with DAG(
    dag_id="ingest_requests_json",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    
    request_json()