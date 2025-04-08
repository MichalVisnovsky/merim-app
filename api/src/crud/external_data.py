import time

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.external_data import ExternalData


async def create_external_data(session: AsyncSession, data: dict) -> ExternalData:
    """ Create or update external data in the database. """
    external_data = ExternalData(
        data=data,
        created_at=int(time.time())
    )
    session.add(external_data)
    await session.commit()
    await session.refresh(external_data)
    return external_data

async def get_latest_external_data(session: AsyncSession) -> dict:
    """ Retrieve the latest external data from the database. """
    result = await session.execute(
        select(ExternalData)
        .order_by(ExternalData.created_at.desc())
        .limit(1)
    )
    latest = result.scalar_one_or_none()
    return latest.data if latest else {} 