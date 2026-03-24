from sqlalchemy.orm import Session

from scripts.custom.DIA.dia_schema import Sources

def fetch_sources(db: Session, sequence: str) -> list:
    query = db.query(Sources).filter(Sources.sequence == sequence).distinct().all()
    if len(query) == 0:
        return ['test_1', 'test_2']
    return query