import http

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.exception.exceptions import BaseError


class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except BaseError as exc:
            return self._wrap(exc)

        except RequestValidationError as exc:
            errors = exc.errors()[0]

            part = errors["loc"][0]
            parameter = errors["loc"][1]
            msg = errors["msg"]

            parsed_message = f"{parameter} in {part} : {msg}"
            wrapped = BaseError(
                status=422,
                message=http.HTTPStatus(422).phrase,
                optional_message=parsed_message,
            )
            return self._wrap(wrapped)

        except StarletteHTTPException as exc:
            wrapped = BaseError(
                status=exc.status_code,
                message=http.HTTPStatus(exc.status_code).phrase,
                optional_message=exc.detail,
            )
            return self._wrap(wrapped)

        except Exception as exc:
            wrapped = BaseError(
                status=500,
                message=http.HTTPStatus(500).phrase,
                optional_message=str(exc),
            )
            return self._wrap(wrapped)

    def _wrap(self, exc: BaseError):
        return JSONResponse(
            status_code=exc.status,
            content={
                "success": False,
                "status": exc.status,
                "message": http.HTTPStatus(exc.status_code).phrase,
                "optional_message": exc.optional_message,
                "data": exc.data,
            },
        )
