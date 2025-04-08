from pydantic import BaseModel, Field

from src.db.models.menu import VatRateType


class VatRateInput(BaseModel):
    """
    VAT rate input model for creating or updating VAT rates.
    @param rate_type: Type of VAT rate (e.g., "standard", "reduced", etc.)
    @param rate_pct: VAT rate percentage (e.g., 0.21 for 21%)
    """
    ratePct: float = Field(..., gt=0, description="VAT rate percentage")
    isDefault: bool = Field(False, description="Whether this is the default VAT rate")

class VatRateResponse(BaseModel):
    """
    VAT rate response model for returning VAT rate data.
    @param rate_type: Type of VAT rate (e.g., "standard", "reduced", etc.)
    @param rate_pct: VAT rate percentage (e.g., 0.21 for 21%)
    @param is_default: Whether this is the default VAT rate
    """
    rate_type: VatRateType
    rate_pct: float
    is_default: bool 