from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Sources(Base):
    __tablename__ = 'sources'

    item_id = Column(Integer, primary_key=True)
    base_url = Column(String(100), nullable=False)
    url_ext = Column(String(100), nullable=True)
    params = Column(JSON, nullable=True)
    type = Column(String(10), nullable=False)
    credentials = Column(JSON, nullable=True)
    sequence = Column(String(20), nullable=False)
    inserted = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    is_active = Column(Boolean, nullable=False)