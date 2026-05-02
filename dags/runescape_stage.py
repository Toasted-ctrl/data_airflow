from airflow import DAG
from airflow.sdk import task
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from typing import Type

from scripts.database.get_data import get_all_filter_by, get_max_filter_by
from scripts.database.session import get_db
from scripts.database.table import table_exists, create_table

from sources.DIA.config import dia_config
from sources.DIA.schemas import Sources

from sources.runescape.config import runescape_config
from sources.runescape.schemas import StageHiscores_1

@task.python
def get_source_ids(description: str) -> list[dict[str, int]]:
    db = get_db(engine_url=dia_config.db_url)
    
    filter_by_values = {
        "description": description
    }

    return_fields = [
        "source_id"
    ]

    source_ids: list[dict] = get_all_filter_by(
        table_schema=Sources,
        db=next(db),
        filter_by_values=filter_by_values,
        return_fields=return_fields
    )

    return [source_id.get("source_id") for source_id in source_ids]

@task.python
def get_max_ingested_record(
    table_schema: Type[DeclarativeBase],
    min_record_name: str
) -> int:
    
    """We're using this to get which record we ingested into stage-1 last.
    This way we only have to focus on the new entried in ingest > incremental load."""

    is_table_present: bool = table_exists(table_schema=table_schema, db_url=runescape_config.db_url)
    if not is_table_present:
        create_table(table_schema=table_schema, db_url=runescape_config.db_url)
        return 0
    db = get_db(engine_url=runescape_config.db_url)
    return get_max_filter_by(
        table_schema=table_schema,
        db=next(db),
        filter_by_values={},    # Leave this empty, just getting the max is enough.
        return_field=min_record_name
    )

with DAG(
    dag_id="runescape.stage.1.hiscores.incremental",
    start_date=datetime(2026, 4, 15),
    schedule="15 2 * * *", # Reloading every day at 02:15 AM
    dag_display_name="RuneScape: Stage (1) Hiscores, Incremental"
) as dag_hiscores_stage_1:
    
    # NOTE: Determine the max ingest_item_id we've already loaded into stage-1.
    # NOTE: If the table does not exist, create table and 0.

    _source_ids = get_source_ids(description=runescape_config.description_hiscores)
    _max_ingested_item_id = get_max_ingested_record(table_schema=StageHiscores_1, min_record_name="ingest_item_id")

    # TODO: Only test to check if we're getting the correct values and to see if the table gets created.