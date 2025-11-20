import logging

from src.config import settings


def init_logger():
    logging.basicConfig(
        level=logging.INFO if settings.environment == "prod" else logging.DEBUG,
        format="%(levelname)s:     %(name)s - %(asctime)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
