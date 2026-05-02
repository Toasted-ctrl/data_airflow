from sqlalchemy import Column, Integer, String, DateTime, func, BigInteger
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class StageHiscores(Base):
    __tablename__ = 'stg_1_hiscores'

    item_id = Column(Integer, primary_key=True)          # id of item in stg_hiscores
    ingest_item_id = Column(Integer, nullable=False)       # item id of item in ingest table
    source_id = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)
    inserted = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)      # When item got inserted into 'stg_hiscores
    ingested = Column(DateTime(timezone=False), nullable=False)       # When the item got ingested into the ingest table
    name = Column(String(20), nullable=False)
    rank = Column(Integer, nullable=False)          # Unranked defaults to -1
    level = Column(Integer, nullable=True)          # Not every hiscore item includes a level, i.e.: activities
    exp_score = Column(BigInteger, nullable=False)  # Unregistered score exp/score defaults to -1