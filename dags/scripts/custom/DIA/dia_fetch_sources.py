from sqlalchemy.orm import Session

from scripts.custom.DIA.dia_schema import Sources

def fetch_sources(db: Session, sequence: str) -> list:

    # NOTE: Distinct can't be used as  postgres cannot compare JSON entries.
    # NOTE: We'll just need to make sure that every entry in the sources table is unique.
    # NOTE: We'll also need to create a dictionary as we cannot return a list of sqlalchemy objects in Airflow.

    query = db.query(Sources).filter(Sources.sequence == sequence, Sources.is_active == True).all()
    if not query:
        return None
    return [
        {
            "source_id": row.source_id,
            "base_url": row.base_url,
            "url_ext": row.url_ext,
            "params": row.params,
            "headers": row.headers,
            "content_type": row.content_type
        }
        for row in query
    ]