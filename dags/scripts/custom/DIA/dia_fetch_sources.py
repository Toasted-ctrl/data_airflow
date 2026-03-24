from airflow.sdk import task
from sqlalchemy.orm import Session

from scripts.core.configs import dia_config

@task
def fetch_sources(db: Session, type: str=None) -> list[dict]:
    print("Success")
    return ["test_item_1", "test_item_2"]