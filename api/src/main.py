import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.db.db import create_db_and_tables
from src.logging import logger

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

    yield
app = FastAPI(lifespan=lifespan)
app.add_middleware(LoggingMiddleware)


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}