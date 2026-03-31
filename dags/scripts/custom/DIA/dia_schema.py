from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Sources(Base):
    __tablename__ = 'sources'

    source_id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    base_url = Column(String(100), nullable=False)
    url_ext = Column(String(100), nullable=True)
    params = Column(JSON, nullable=True)
    content_type = Column(String(10), nullable=False)
    sequence = Column(String(20), nullable=False)
    headers = Column(JSON, nullable=True)
    inserted = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    is_active = Column(Boolean, nullable=False)