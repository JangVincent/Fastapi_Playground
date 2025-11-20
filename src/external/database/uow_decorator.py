from functools import wraps

from src.external.database.database import SessionLocal
from src.external.database.unit_of_work import UnitOfWork


def UoW(func):
    """
    Decorator that wraps a service method inside a Unit of Work.

    IMPORTANT
    ---------
    The service class using this decorator **must not be a singleton**.
    A new service instance must be created **per request**.
    Otherwise:
      - multiple concurrent requests may overwrite `self.uow`
      - sessions may mix across requests
      - transactions may interfere with each other
      - race conditions and data integrity issues can occur

    Summary of Behavior
    -------------------
    - Creates a fresh UnitOfWork (UoW) per method call.
    - Injects `self.uow` into the service instance.
    - Executes the method inside a transactional `with uow:`.
    - Removes `self.uow` after execution.

    Restrictions
    ------------
    - Do NOT call another @UoW method from inside an @UoW method.
      Use `self.uow` directly instead.
    - Service instances must be request-scoped, not shared.

    Example
    -------
        @UoW
        def create_user(self, name: str):
            exist = self.uow.users.get_user_by_name(name)
            if exist:
                raise UserAlreadyExists()
            return self.uow.users.create_user(name)

    Parameters
    ----------
    func : Callable
        The service method to wrap.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        uow = UnitOfWork(SessionLocal)
        self.uow = uow

        try:
            with uow:
                return func(self, *args, **kwargs)
        finally:
            del self.uow

    return wrapper
