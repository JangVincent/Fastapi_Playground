from functools import wraps

from src.external.database.database import SessionLocal
from src.external.database.unit_of_work import UnitOfWork


def UoW(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        uow = UnitOfWork(SessionLocal)

        # Inject uow into self
        self.uow = uow

        try:
            with uow:
                return func(self, *args, **kwargs)
        finally:
            # Cleanup
            del self.uow

    return wrapper
