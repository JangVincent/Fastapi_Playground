from contextlib import AbstractAsyncContextManager

from sqlalchemy.ext.asyncio import AsyncSession


class AsyncUnitOfWork(AbstractAsyncContextManager):
    """
    Async Unit of Work for SQLAlchemy AsyncSession.

    - async __aenter__ → 세션 생성
    - async __aexit__ → commit or rollback 후 close
    - lazy repo 제공
    """

    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session: AsyncSession | None = None
        self._user_repo = None

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc:
            await self.session.rollback()
        else:
            await self.session.commit()

        await self.session.close()

    # --- Lazy repositories ---
    @property
    def users(self):
        from src.entities.user_model import UserRepository

        if self._user_repo is None:
            self._user_repo = UserRepository(self.session)
        return self._user_repo
