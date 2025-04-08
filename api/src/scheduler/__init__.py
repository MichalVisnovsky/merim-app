import asyncio
import contextlib

from fastapi_utilities import repeat_every

from src.crud import external_data
from src.db import get_async_session
from src.services.external_api import fetch_external_data

get_async_session_context = contextlib.asynccontextmanager(get_async_session)

async def run_background_tasks():
    """Run background tasks to fetch cryptocurrency data."""
    asyncio.create_task(fetch_and_save_external_data())

@repeat_every(seconds=5)
async def fetch_and_save_external_data():
    """
    Fetch and save external data in the background.
    This function is called in the background periodicaly.
    """
    async with get_async_session_context() as session:
        # Fetch and save external data
        ext_data = await fetch_external_data()
        await external_data.create_external_data(session, ext_data)
