from airflow import DAG
from airflow.decorators import task
from datetime import datetime

from scripts.requests import request_json

with DAG(
    dag_id="debug_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    @task
    def hello():
        print("Hello Airflow")

    for i in range(5):
        hello()

    request_json()