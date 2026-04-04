import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, func
from sqlalchemy.orm import DeclarativeBase

# DIA CONFIGURATION

class DiaConfig:
    print("Initializing Config: DIA")

    load_dotenv()

    db_protocol: str = os.getenv("DIA_DB_PROTOCOL")
    db_connection: str = os.getenv("DIA_DB_CONNECTION")
    
    db_hostname: str = os.getenv("DIA_DB_HOSTNAME")
    db_password: str = os.getenv("DIA_DB_PASSWORD")
    db_username: str = os.getenv("DIA_DB_USERNAME")
    db_database: str = os.getenv("DIA_DB_DATABASE")
    db_port: str = os.getenv("DIA_DB_PORT")

    DIA_API_KEY: str = os.getenv("DIA_API_KEY")
    DIA_API_KEY_NAME: str = os.getenv("DIA_API_KEY_NAME")
    DIA_API_POST_URL: str = os.getenv("DIA_API_POST_URL")

    @property
    def db_url(self) -> str:
        return f"{self.db_protocol}+{self.db_connection}://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"
    
    print("Initialized Config: DIA")

dia_config = DiaConfig()

# DIA SOURCES SCHEMA

class Base(DeclarativeBase):
    pass

class Sources(Base):
    __tablename__ = 'sources'

    source_id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    base_url = Column(String(100), nullable=False)
    url_ext = Column(String(100), nullable=True)
    params = Column(JSON, nullable=True)
    content_type = Column(String(40), nullable=False)
    sequence = Column(String(20), nullable=False)
    headers = Column(JSON, nullable=True)
    inserted = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    is_active = Column(Boolean, nullable=False)