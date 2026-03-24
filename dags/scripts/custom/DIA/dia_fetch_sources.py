from sqlalchemy.orm import Session

from scripts.custom.DIA.dia_schema import Sources

def fetch_sources(db: Session, sequence: str, type: str) -> list:
    # NOTE: Distinct can't be used as  postgres cannot compare JSON entries.
    # NOTE: We'll just need to make sure that every entry in the sources table is unique.
    query = db.query(
        Sources).filter(Sources.sequence == sequence, Sources.type == type).all()
    if len(query) == 0:
        return ['test_1', 'test_2']
    return query