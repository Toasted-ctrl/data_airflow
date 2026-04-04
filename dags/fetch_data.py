from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.configs.DIA import dia_config, Sources
from scripts.database.get_data import get_all_filter_by
from scripts.database.session import get_db

@task.python
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

with DAG(
    dag_id="test.get.all",
    dag_display_name="TEST: DB Fetch All",
    start_date=datetime(2026, 3, 1),
    catchup=False,
    schedule="@hourly"
) as test_dag:
    
    _results = get_sources(sequence="hourly")