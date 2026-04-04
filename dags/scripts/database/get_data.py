from pandas.errors import EmptyDataError
from sqlalchemy.orm import Session

def get_all_filter_by(table_schema, db: Session, filter_by_values: dict, return_fields: list) -> list:
    
    """Retrieves a list of rows based on specified filters. The filters need to be defined as a dict.
    The return fields are the columns you'd like to receive from the database query, and must be defined 
    in a list. Will raise an error if no data is found."""

    query = db.query(table_schema).filter_by(**filter_by_values).all()
    if not query:
        raise EmptyDataError
    return [
        {field: getattr(query_row, field) for field in return_fields} for query_row in query
    ]