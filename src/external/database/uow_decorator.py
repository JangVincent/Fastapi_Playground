from functools import wraps

from src.external.database.database import SessionLocal
from src.external.database.unit_of_work import AsyncUnitOfWork


def UoW(func):
    """
    Async Unit of Work (UoW) decorator for service-layer methods.

    This decorator creates a new AsyncUnitOfWork instance per method call,
    injects it into the service instance as `self.uow`, executes the method inside
    an `async with` transactional boundary, and removes the UoW afterward.

    IMPORTANT
    ---------
    The service class using this decorator **must not be a singleton**.
    A new service instance **must be created per request**.
    Otherwise:
      - concurrent requests may overwrite `self.uow`
      - AsyncSessions may leak across requests
      - transactions may interfere with each other
      - data corruption or race conditions may occur

    Summary of Behavior
    -------------------
    - Creates a fresh AsyncUnitOfWork for each decorated method call.
    - Binds the UoW instance to `self.uow`.
    - Executes the method inside `async with uow:` (transaction boundary).
    - Automatically commits on success, and rolls back on exceptions.
    - Cleans up `self.uow` after the method finishes.

    Restrictions
    ------------
    - Do NOT call another @UoW method from inside a @UoW method.
      Nested UoWs create multiple independent transactions and break
      transactional consistency. Use `self.uow` directly instead.
    - Service instances must be request-scoped. Do not reuse a single
      service instance across multiple requests.

    Example
    -------
        class UserService:

            @UoW
            async def create_user(self, data):
                # Access repositories through a shared AsyncSession
                exist = await self.uow.users.get_by_email(data.email)
                if exist:
                    raise UserAlreadyExists()

                user = await self.uow.users.create(data)
                return user

    Parameters
    ----------
    func : Callable
        The async service method to wrap in a UoW transactional boundary.
    """

    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        uow = AsyncUnitOfWork(SessionLocal)
        self.uow = uow

        try:
            async with uow:
                return await func(self, *args, **kwargs)
        finally:
            del self.uow

    return wrapper
