from sqlalchemy import Column, Integer, JSON

from src.db.models import Base


class ExternalData(Base):
    __tablename__ = "external_data"
    
    id = Column(Integer, primary_key=True)
    data = Column(JSON, nullable=False)  # Stores the complete external data
    created_at = Column(Integer, nullable=False)  # Unix timestamp 