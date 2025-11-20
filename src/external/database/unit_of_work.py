from contextlib import AbstractContextManager

from sqlalchemy.orm import Session


class UnitOfWork(AbstractContextManager["UnitOfWork"]):
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session: Session | None = None
        self._user_repo = None

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    # repositories
    @property
    def users(self):
        from src.entities.user_model import UserRepository

        if self._user_repo is None:
            self._user_repo = UserRepository(self.session)
        return self._user_repo
