from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import settings

engine = create_async_engine(
    settings.database_url,  # postgresql+asyncpg://user:pass@...
    echo=False,
    pool_pre_ping=True,
)


SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db():
    async with SessionLocal() as session:
        yield session
