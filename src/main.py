import logging

from fastapi import FastAPI

from src.config import settings
from src.core.logger import init_logger
from src.domains.user.router import router as user_router

init_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    redoc_url=None if settings.environment == "prod" else "/redoc",
    docs_url=None if settings.environment == "prod" else "/docs",
)

app.include_router(
    router=user_router,
)


@app.get("/")
def health():
    return {"status": "ok"}
