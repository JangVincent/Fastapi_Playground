import logging

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from src.config import settings
from src.core.exception.global_exception_filter import GlobalExceptionFilter
from src.core.logger import init_logger
from src.domains.user.router import router as user_router

init_logger()

app = FastAPI(
    redoc_url=None if settings.environment == "prod" else "/redoc",
    docs_url=None if settings.environment == "prod" else "/docs",
)


app.include_router(
    router=user_router,
)

app.add_exception_handler(RequestValidationError, GlobalExceptionFilter())
app.add_exception_handler(HTTPException, GlobalExceptionFilter())
app.add_exception_handler(Exception, GlobalExceptionFilter())

logger = logging.getLogger(__name__)


@app.get("/")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
