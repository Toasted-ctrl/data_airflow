from sqlalchemy.orm import Session

def get_all_filter_by(table_schema, db: Session, filter_by_values: dict, return_fields: list) -> list:
    
    """Retrieves list of items for a given set of filters. The required return values must be specified."""

    query = db.query(table_schema).filter_by(**filter_by_values).all()
    if not query:
        raise ValueError("No data.")
    return [
        {field: getattr(query_row, field) for field in return_fields} for query_row in query
    ]