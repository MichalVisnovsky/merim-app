import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.db import create_db_and_tables, get_async_session
from src.db.schemas.data import DataAInput, DataCResponse
from src.logging import logger
from src.scheduler import run_background_tasks
from src.services.data_service import save_data_a, get_combined_data


class LoggingMiddleware(BaseHTTPMiddleware):
    """ Middleware to log incoming requests and outgoing responses. """
    @staticmethod
    async def dispatch(request: Request, call_next):
        client_ip = request.client.host
        logger.debug(f"Incoming request: {request.method} {request.url} from {client_ip}")
        response: Response = await call_next(request)
        logger.debug(f"Response status: {response.status_code} for {client_ip}")
        return response

# runs on startup
@asynccontextmanager
async def lifespan(_app: FastAPI):
    await create_db_and_tables()

    # Fetch and save external data periodically
    asyncio.create_task(run_background_tasks())
    yield

app = FastAPI(
    title="Merim API",
    version="1.0.0",
    lifespan=lifespan
)
app.add_middleware(LoggingMiddleware)

@app.post("/api/v1/data-a", response_model=DataCResponse)
async def create_data_a(
    data: DataAInput,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Endpoint to accept and validate Data A (menus and VAT rates)
    @param data: Data A input
    :return : Data C response
    """
    try:
        await save_data_a(session, data)
        return await get_combined_data(session)
    except Exception as e:
        logger.error(f"Error processing Data A: {e}")
        raise

@app.get("/api/v1/data-c", response_model=DataCResponse)
async def get_data_c(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Endpoint to get combined data (Data C)
    :return : Data C response
    """
    try:
        # Possible Etag implementation or redis cache
        return await get_combined_data(session)
    except Exception as e:
        logger.error(f"Error getting Data C: {e}")
        raise