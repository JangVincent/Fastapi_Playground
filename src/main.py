import logging

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from src.config import settings
from src.core.exception.global_exception_filter import GlobalExceptionFilter
from src.core.logger import init_logger
from src.core.middleware.response_middleware import UnifiedResponseMiddleware
from src.domains.router_aggregator import aggregated_router

init_logger()

app: FastAPI = FastAPI(
    redoc_url=None if settings.environment == "prod" else "/redoc",
    docs_url=None if settings.environment == "prod" else "/docs",
)


app.include_router(
    router=aggregated_router,
)

app.add_exception_handler(RequestValidationError, GlobalExceptionFilter())
app.add_exception_handler(HTTPException, GlobalExceptionFilter())
app.add_exception_handler(Exception, GlobalExceptionFilter())

app.add_middleware(UnifiedResponseMiddleware)

logger = logging.getLogger(__name__)


@app.get("/")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
