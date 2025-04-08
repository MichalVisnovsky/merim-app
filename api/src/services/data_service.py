from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import menu, vat_rate, external_data
from src.db.schemas.data import DataAInput, DataCResponse
from src.db.schemas.menu import MenuResponse
from src.db.schemas.vat_rate import VatRateResponse


async def save_data_a(session: AsyncSession, data: DataAInput) -> None:
    """
    Save Data A (menus and VAT rates) to the database
    """
    
    # Save menus
    for menu_data in data.menus:
        await menu.create_menu(session, {
            "id": menu_data.id,
            "sys_name": menu_data.sysName,
            "name": menu_data.name.model_dump(),
            "price": menu_data.price,
            "vat_rate": menu_data.vatRate
        })
    
    # Save VAT rates
    for rate_type, rate_data in data.vatRates.items():
        await vat_rate.create_vat_rate(session, {
            "rate_type": rate_type,
            "rate_pct": rate_data.ratePct,
            "is_default": rate_data.isDefault
        })

async def get_combined_data(session: AsyncSession) -> DataCResponse:
    """
    Get combined data (Data C) from menus, VAT rates, and external data
    """
    # Get menus
    menus = await menu.get_all_menus(session)
    menu_responses = [
        MenuResponse(
            id=m.id,
            sys_name=m.sys_name,
            name=m.name,
            price=m.price,
            vat_rate=m.vat_rate
        ) for m in menus
    ]
    
    # Get VAT rates
    vat_rates = await vat_rate.get_all_vat_rates(session)
    vat_rate_responses = [
        VatRateResponse(
            rate_type=r.rate_type,
            rate_pct=r.rate_pct,
            is_default=r.is_default
        ) for r in vat_rates
    ]
    
    # Get latest external data
    ext_data = await external_data.get_latest_external_data(session)
    
    return DataCResponse(
        menus=menu_responses,
        vat_rates=vat_rate_responses,
        external_data=ext_data
    ) 