import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, func, BigInteger
from sqlalchemy.orm import DeclarativeBase

class RuneScapeConfig:
    print("Initializing Config: RuneScape")

    load_dotenv()

    db_protocol: str = os.getenv("RUNESCAPE_DB_PROTOCOL")
    db_connection: str = os.getenv("RUNESCAPE_DB_CONNECTION")
    db_hostname: str = os.getenv("RUNESCAPE_DB_HOSTNAME")
    db_password: str = os.getenv("RUNESCAPE_DB_PASSWORD")
    db_username: str = os.getenv("RUNESCAPE_DB_USERNAME")
    db_database: str = os.getenv("RUNESCAPE_DB_DATABASE")
    db_port: str = os.getenv("RUNESCAPE_DB_PORT")

    description_hiscores: str = "Runescape Player Hiscores"
    description_runemetrics: str = "Runescape Player Runemetrics Profile"

    @property
    def db_url(self) -> str:
        return f"{self.db_protocol}+{self.db_connection}://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"

runescape_config = RuneScapeConfig()

# RUNESCAPE SCHEMAS

class Base(DeclarativeBase):
    pass

class StageHiscores(Base):
    __tablename__ = 'stg_hiscores'

    id = Column(Integer, primary_key=True)          # id of item in stg_hiscores
    item_id = Column(Integer, nullable=False)       # item id of item in ingest table
    source_id = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)
    inserted = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)      # When item got inserted into 'stg_hiscores
    ingested = Column(DateTime(timezone=False), nullable=False)       # When the item got ingested into the ingest table
    name = Column(String(20), nullable=False)
    rank = Column(Integer, nullable=False)          # Unranked defaults to -1
    level = Column(Integer, nullable=True)          # Not every hiscore item includes a level, i.e.: activities
    exp_score = Column(BigInteger, nullable=False)  # Unregistered score exp/score defaults to -1