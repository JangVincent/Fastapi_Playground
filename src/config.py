import os

from dotenv import load_dotenv
from pydantic import BaseModel

# .env 파일 로딩
load_dotenv()


class Settings(BaseModel):
    database_url: str = os.getenv("DATABASE_URL")
    database_url_sync: str = os.getenv("DATABASE_URL_SYNC")
    environment: str = os.getenv("ENVIRONMENT", "dev")


settings = Settings()
