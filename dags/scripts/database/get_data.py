from pandas.errors import EmptyDataError
from sqlalchemy import func
from sqlalchemy.orm import Session, DeclarativeBase
from typing import Type

def get_all_filter_by(
        table_schema: Type[DeclarativeBase],
        db: Session,
        filter_by_values: dict,
        return_fields: list
) -> list:
    
    """Retrieves a list of rows based on specified filters. The filters need to be defined as a dict.
    The return fields are the columns you'd like to receive from the database query, and must be defined 
    in a list. Will raise EmptyDataError if no data is found."""

    query = db.query(table_schema).filter_by(**filter_by_values).all()
    if not query:
        raise EmptyDataError
    return [
        {field: getattr(query_row, field) for field in return_fields} for query_row in query
    ]

def get_max_filter_by(
        table_schema: Type[DeclarativeBase],
        db: Session,
        filter_by_values: dict,
        return_field: int | float
) -> int:

    """Retrieves the maximum value within a specified column based on a set of filters.
    The column of which the max needs to be determined must be of type integer or float.
    Only equality based filters may be used."""

    column = getattr(table_schema, return_field)

    max_value = (
        db.query(func.max(column))
        .filter_by(**filter_by_values)
        .scalar()
    )
    
    if not max_value:
        return 0
    return int(max_value)

def get_all_filters(
    query,
    model_schema: Type[DeclarativeBase],
    filters: dict
) -> list[dict]:
    
    """Retrieves a list of entries based on specified filters. Filters may be indicated as follows:

    filters = {\n
    "status": "active",       # equality\n
    "id": [1, 2, 3],          # IN\n
    "age__gt": 18,            # age > 18\n
    "age__lte": 65,           # age <= 65\n
    "name__like": "Jo%",      # LIKE\n
    }"""
    
    for key, value in filters.items():
        column = getattr(model_schema, key)
        if isinstance(value, (list, tuple, set)):
            query = query.filter(column.in_(value))
        else:
            query = query.filter(column == value)
    return query