from sqlalchemy.orm import Session

from scripts.custom.DIA.dia_schema import Sources

def fetch_sources(db: Session, sequence: str, type: str) -> list:
    
    # NOTE: Distinct can't be used as  postgres cannot compare JSON entries.
    # NOTE: We'll just need to make sure that every entry in the sources table is unique.

    # NOTE: We'll also need to create a dictionary as we cannot return a list of sqlalchemy objects
    # NOTE: in airflow.

    query = db.query(Sources).filter(Sources.sequence == sequence, Sources.type == type).all()
    if not query:
        return ['test_1', 'test_2']
    return [
        {
            "item_id": row.item_id,
            "base_url": row.base_url,
            "url_ext": row.url_ext,
            "params": row.params,
            "credentials": row.credentials
        }
        for row in query
    ]