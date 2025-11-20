# src/core/exceptions.py


class BaseError(Exception):
    def __init__(self, status: int, message: str, optional_message: str = None, data=None):
        self.success = False
        self.status = status
        self.message = message
        self.optional_message = optional_message
        self.data = data
        super().__init__(message)


class BadRequestError(BaseError):
    def __init__(self, message="Bad Request", optional_message=None, data=None):
        super().__init__(400, message, optional_message, data)


class UnauthorizedError(BaseError):
    def __init__(self, message="Unauthorized", optional_message=None, data=None):
        super().__init__(401, message, optional_message, data)


class ForbiddenError(BaseError):
    def __init__(self, message="Forbidden", optional_message=None, data=None):
        super().__init__(403, message, optional_message, data)


class NotFoundError(BaseError):
    def __init__(self, message="Not Found", optional_message=None, data=None):
        super().__init__(404, message, optional_message, data)


class ConflictError(BaseError):
    def __init__(self, message="Conflict", optional_message=None, data=None):
        super().__init__(409, message, optional_message, data)


class UnprocessableEntityError(BaseError):
    def __init__(self, message="Unprocessable Entity", optional_message=None, data=None):
        super().__init__(422, message, optional_message, data)


class TooManyRequestsError(BaseError):
    def __init__(self, message="Too Many Requests", optional_message=None, data=None):
        super().__init__(429, message, optional_message, data)


class InternalServerError(BaseError):
    def __init__(self, message="Internal Server Error", optional_message=None, data=None):
        super().__init__(500, message, optional_message, data)
