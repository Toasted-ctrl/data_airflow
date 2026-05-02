from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import DeclarativeBase
from typing import Type

class TableCreationError(RuntimeError):
    """Raised when a database table could not be created."""

def table_exists(table_schema: Type[DeclarativeBase], db_url: str) -> bool:

    """Checks if the table exists in the specified database."""

    engine = create_engine(url=db_url)
    try:
        table = table_schema.__table__
        return inspect(engine).has_table(table.name)
    finally:
        engine.dispose()

def create_table(table_schema: Type[DeclarativeBase], db_url: str) -> None:

    """Returns False is table creation failed"""

    engine = create_engine(url=db_url)
    try:
        table_schema.__table__.create(bind=engine, checkfirst=True)
        if not inspect(engine).has_table(table_name=table_schema.__tablename__):
            raise TableCreationError(f"Could not create {table_schema.__tablename__}")
    finally:
        engine.dispose()