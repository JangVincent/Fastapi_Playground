from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import settings

# 1) Async Engine 생성
engine = create_async_engine(
    settings.database_url,  # postgresql+asyncpg://user:pass@...
    echo=False,
    pool_pre_ping=True,
)


# 2) Async SessionLocal 생성
SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


# 3) FastAPI Dependency
# async def get_db():
#     async with SessionLocal() as session:
#         yield session
