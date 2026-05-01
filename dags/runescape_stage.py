from airflow import DAG
from airflow.sdk import task
from datetime import datetime

from scripts.configs.DIA import dia_config, Sources
from scripts.configs.runescape import runescape_config, StageHiscores
from scripts.database.get_data import get_all_filter_by
from scripts.database.session import get_db
from scripts.database.table import table_exists

@task.python
def get_min_ingest_record(table, item_name: str) -> int:
    is_table_present: bool = table_exists(table=table)
    if not is_table_present:
        return 0 # TODO: Create function above to create table if it does not exist yet
    return 88 # For testing purposes, remove later

@task.python
def get_source_ids(description: str) -> list[dict[str, int]]:
    db = get_db(engine_url=dia_config.db_url)
    
    filter_by_values = {
        "description": description
    }

    return_fields = [
        "source_id"
    ]

    return get_all_filter_by(
        table_schema=Sources,
        db=next(db),
        filter_by_values=filter_by_values,
        return_fields=return_fields
    )

with DAG(
    dag_id="Runescape.Stage.Hiscores",
    start_date=datetime(2026, 4, 30),
    dag_display_name="Runescape: Stage (Hiscores), daily",
    schedule="daily",
    catchup=False
) as dag_stg_hiscores_daily:
    
    min_record = get_min_ingest_record(table=StageHiscores, item_name="test")