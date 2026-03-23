from airflow import DAG, task
from datetime import datetime

with DAG(
    dag_id="simple_print_dag_v3",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    @task
    def print_message(i: int):
        print(f"Hello from task {i}")

    # Dynamically create tasks
    for i in range(5):
        print_message.override(task_id=f"print_task_{i}")(i)