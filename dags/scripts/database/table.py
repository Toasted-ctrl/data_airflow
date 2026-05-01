from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import DeclarativeBase
from typing import Type

def table_exists(table: Type[DeclarativeBase], db_url: str) -> bool:

    """Checks if the table exists in the specified database."""

    engine = create_engine(url=db_url)
    try:
        return inspect(engine).has_table(table_name=table.__tablename__)
    finally:
        engine.dispose()

def create_table(table: Type[DeclarativeBase], db_url) -> bool:

    """Returns False is table creation failed"""

    engine = create_engine(url=db_url)
    try:
        table.__table__.create(bind=engine, checkfirst=True)
        return inspect(engine).has_table(table_name=table.__tablename__)
    finally:
        engine.dispose()