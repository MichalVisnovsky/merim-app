from typing import Dict

from pydantic import BaseModel, Field

from src.db.models.menu import VatRateType


class MenuName(BaseModel):
    """
    Menu name model for different languages.
    @param en_GB: English name
    @param fr_FR: French name
    """
    en_GB: str = Field(..., description="English name")
    fr_FR: str = Field(..., description="French name")

class MenuInput(BaseModel):
    """
    Menu input model for creating or updating menu items.
    @param id: Menu ID
    @param sysName: System name of the menu
    @param name: Menu names in different languages
    @param price: Menu price
    @param vatRate: VAT rate type
    """
    id: int = Field(..., gt=0, description="Menu ID")
    sysName: str = Field(..., description="System name of the menu")
    name: MenuName = Field(..., description="Menu names in different languages")
    price: float = Field(..., gt=0, description="Menu price")
    vatRate: VatRateType = Field(..., description="VAT rate type")

class MenuResponse(BaseModel):
    """
    Menu response model for returning menu data.
    @param id: Menu ID
    @param sys_name: System name of the menu
    @param name: Menu names in different languages
    @param price: Menu price
    @param vat_rate: VAT rate type
    """
    id: int
    sys_name: str
    name: Dict[str, str]
    price: float
    vat_rate: VatRateType 