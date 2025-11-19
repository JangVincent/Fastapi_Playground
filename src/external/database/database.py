from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings

# 1) Engine 생성 (Sync 방식)
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # DB 연결이 끊겼을 때 자동 재연결
)

# 2) SessionLocal 생성 (ORM 세션)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# 3) FastAPI에서 사용할 DB 세션 DI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
