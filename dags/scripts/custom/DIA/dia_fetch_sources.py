from airflow.sdk import task
from sqlalchemy.orm import Session

from scripts.core.configs import dia_config

def fetch_sources(db: Session, type: str=None) -> list[dict]:
    print("Success")
    return ["test_item_1", "test_item_2"]