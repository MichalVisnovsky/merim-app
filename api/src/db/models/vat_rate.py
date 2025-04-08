from sqlalchemy import Column, Float, Boolean, Enum

from src.db.models import Base
from src.db.schemas.menu import VatRateType


class VatRate(Base):
    __tablename__ = "vat_rates"
    
    rate_type = Column(Enum(VatRateType), primary_key=True)
    rate_pct = Column(Float, nullable=False)
    is_default = Column(Boolean, default=False) 