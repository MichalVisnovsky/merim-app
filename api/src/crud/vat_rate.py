from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.vat_rate import VatRate


async def create_vat_rate(session: AsyncSession, vat_rate_data: dict) -> VatRate:
    """ Create or update a VAT rate in the database. """

    exists = await session.execute(
        select(VatRate).where(VatRate.rate_type == vat_rate_data["rate_type"])
    )
    exists = exists.scalar_one_or_none()
    if exists is not None:
        vat_rate = exists
        vat_rate.rate_pct = vat_rate_data["rate_pct"]
        vat_rate.is_default = vat_rate_data["is_default"]
    else:
        vat_rate = VatRate(**vat_rate_data)

    session.add(vat_rate)
    await session.commit()
    await session.refresh(vat_rate)
    return vat_rate

async def get_all_vat_rates(session: AsyncSession) -> list[VatRate]:
    """ Retrieve all VAT rates from the database. """
    result = await session.execute(select(VatRate))
    return result.scalars().all()