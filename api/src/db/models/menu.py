import enum

from sqlalchemy import Column, Integer, String, Float, Enum, JSON

from src.db.models import Base


class VatRateType(str, enum.Enum):
    NORMAL = "normal"
    REDUCED = "reduced"
    NONE = "none"

class Menu(Base):
    __tablename__ = "menus"
    
    id = Column(Integer, primary_key=True, index=True)
    sys_name = Column(String, nullable=False)
    name = Column(JSON, nullable=False)  # Stores the language mappings
    price = Column(Float, nullable=False)
    vat_rate = Column(Enum(VatRateType), nullable=False) 