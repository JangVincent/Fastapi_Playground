from contextlib import AbstractContextManager

from sqlalchemy.orm import Session


class UnitOfWork(AbstractContextManager["UnitOfWork"]):
    """
    Unit of Work (UoW) implementation for SQLAlchemy sessions.

    This class provides a transactional boundary around a group of operations.
    When used as a context manager, it automatically:
      - opens a new SQLAlchemy session on __enter__
      - commits the session if no exception occurred
      - rolls back the session if an exception was raised
      - closes the session on exit

    It also exposes lazy-loaded repository properties (e.g., `users`) that are
    created only once per UoW lifecycle and share the same session.

    Example:
        with UnitOfWork(SessionLocal) as uow:
            user = uow.users.get_user_by_id(1)
            uow.users.update_user(user, "new name")

    Parameters
    ----------
    session_factory : Callable[[], Session]
        A function (ex: sessionmaker instance) that returns a new SQLAlchemy Session.
    """

    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session: Session | None = None
        self._user_repo = None

    def __enter__(self):
        """
        Create a new SQLAlchemy session and return the UnitOfWork itself.

        Returns
        -------
        UnitOfWork
        """
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc, tb):
        """
        Commit or roll back the session depending on whether an exception occurred.
        Finally closes the session.

        Parameters
        ----------
        exc_type : type | None
            Exception type if raised inside the context block.
        exc : Exception | None
            Exception instance if raised.
        tb : traceback | None
            Traceback object.
        """
        if exc:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()

    @property
    def users(self):
        """
        Lazily initialized UserRepository that shares this UnitOfWork's session.

        Returns
        -------
        UserRepository
        """
        from src.entities.user_model import UserRepository

        if self._user_repo is None:
            self._user_repo = UserRepository(self.session)
        return self._user_repo
