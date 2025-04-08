import httpx

from src.config import get_config
from src.logging import logger


async def fetch_external_data() -> dict:
    """
    Fetch external data from the configured URL
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(get_config().get('external_api_url', 'https://test.sustik.cz/interview/data'))
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching external data: {e}")
        raise