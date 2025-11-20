# src/core/exception/global_exception_filter.py

import http

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.core.exception.exceptions import BaseError


class GlobalExceptionFilter:
    async def __call__(self, request: Request, exc: Exception):
        # 1) 이미 BaseError라면 그대로 처리
        if isinstance(exc, BaseError):
            return self._response(exc)

        # 2) HTTPException (FastAPI built-in)
        if isinstance(exc, StarletteHTTPException):
            wrapped = BaseError(
                status=exc.status_code,
                message=http.HTTPStatus(exc.status_code).phrase,
                optional_message=exc.detail,
            )
            return self._response(wrapped)

        # 3) ValidationError (Pydantic request validation)
        if isinstance(exc, RequestValidationError):
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
            return self._response(wrapped)

        # 4) 그 외 모든 예외 → Internal Server Error
        wrapped = BaseError(
            status=500,
            message=http.HTTPStatus(500).phrase,
            optional_message=str(exc),
        )
        return self._response(wrapped)

    def _response(self, exc: BaseError):
        return JSONResponse(
            status_code=exc.status,
            content={
                "success": False,
                "status": exc.status,
                "message": exc.message,
                "optional_message": exc.optional_message,
                "data": exc.data,
            },
        )
