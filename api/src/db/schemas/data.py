import time
from typing import List, Dict

from pydantic import BaseModel, Field

from src.db.models.menu import VatRateType
from src.db.schemas.menu import MenuInput, MenuResponse
from src.db.schemas.vat_rate import VatRateInput, VatRateResponse


class DataAInput(BaseModel):
    """
    Data A input model for menus and VAT rates.
    @param menus: List of menu items
    @param vatRates: Dictionary of VAT rates
    """
    menus: List[MenuInput] = Field(..., description="List of menus")
    vatRates: Dict[VatRateType, VatRateInput] = Field(..., description="VAT rates configuration")

class DataCResponse(BaseModel):
    """
    Data C response model for combined data.
    @param menus: List of menu items
    @param vat_rates: List of VAT rates
    @param external_data: External data fetched from the API
    @param timestamp: Timestamp of the response
    """
    menus: List[MenuResponse]
    vat_rates: List[VatRateResponse]
    external_data: Dict
    timestamp: int = Field(default_factory=lambda: int(time.time())) 