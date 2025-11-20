import logging

from src.config import settings


def init_logger():
    logging.basicConfig(
        level=logging.INFO if settings.environment == "prod" else logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
