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


class PaymentRequiredError(BaseError):
    def __init__(self, message="Payment Required", optional_message=None, data=None):
        super().__init__(402, message, optional_message, data)


class ForbiddenError(BaseError):
    def __init__(self, message="Forbidden", optional_message=None, data=None):
        super().__init__(403, message, optional_message, data)


class NotFoundError(BaseError):
    def __init__(self, message="Not Found", optional_message=None, data=None):
        super().__init__(404, message, optional_message, data)


class MethodNotAllowedError(BaseError):
    def __init__(self, message="Method Not Allowed", optional_message=None, data=None):
        super().__init__(405, message, optional_message, data)


class NotAcceptableError(BaseError):
    def __init__(self, message="Not Acceptable", optional_message=None, data=None):
        super().__init__(406, message, optional_message, data)


class ProxyAuthenticationRequiredError(BaseError):
    def __init__(self, message="Proxy Authentication Required", optional_message=None, data=None):
        super().__init__(407, message, optional_message, data)


class RequestTimeoutError(BaseError):
    def __init__(self, message="Request Timeout", optional_message=None, data=None):
        super().__init__(408, message, optional_message, data)


class ConflictError(BaseError):
    def __init__(self, message="Conflict", optional_message=None, data=None):
        super().__init__(409, message, optional_message, data)


class GoneError(BaseError):
    def __init__(self, message="Gone", optional_message=None, data=None):
        super().__init__(410, message, optional_message, data)


class LengthRequiredError(BaseError):
    def __init__(self, message="Length Required", optional_message=None, data=None):
        super().__init__(411, message, optional_message, data)


class PreconditionFailedError(BaseError):
    def __init__(self, message="Precondition Failed", optional_message=None, data=None):
        super().__init__(412, message, optional_message, data)


class PayloadTooLargeError(BaseError):
    def __init__(self, message="Payload Too Large", optional_message=None, data=None):
        super().__init__(413, message, optional_message, data)


class URITooLongError(BaseError):
    def __init__(self, message="URI Too Long", optional_message=None, data=None):
        super().__init__(414, message, optional_message, data)


class UnsupportedMediaTypeError(BaseError):
    def __init__(self, message="Unsupported Media Type", optional_message=None, data=None):
        super().__init__(415, message, optional_message, data)


class RangeNotSatisfiableError(BaseError):
    def __init__(self, message="Range Not Satisfiable", optional_message=None, data=None):
        super().__init__(416, message, optional_message, data)


class ExpectationFailedError(BaseError):
    def __init__(self, message="Expectation Failed", optional_message=None, data=None):
        super().__init__(417, message, optional_message, data)


class MisdirectedRequestError(BaseError):
    def __init__(self, message="Misdirected Request", optional_message=None, data=None):
        super().__init__(421, message, optional_message, data)


class UnprocessableEntityError(BaseError):
    def __init__(self, message="Unprocessable Entity", optional_message=None, data=None):
        super().__init__(422, message, optional_message, data)


class LockedError(BaseError):
    def __init__(self, message="Locked", optional_message=None, data=None):
        super().__init__(423, message, optional_message, data)


class FailedDependencyError(BaseError):
    def __init__(self, message="Failed Dependency", optional_message=None, data=None):
        super().__init__(424, message, optional_message, data)


class TooEarlyError(BaseError):
    def __init__(self, message="Too Early", optional_message=None, data=None):
        super().__init__(425, message, optional_message, data)


class UpgradeRequiredError(BaseError):
    def __init__(self, message="Upgrade Required", optional_message=None, data=None):
        super().__init__(426, message, optional_message, data)


class PreconditionRequiredError(BaseError):
    def __init__(self, message="Precondition Required", optional_message=None, data=None):
        super().__init__(428, message, optional_message, data)


class TooManyRequestsError(BaseError):
    def __init__(self, message="Too Many Requests", optional_message=None, data=None):
        super().__init__(429, message, optional_message, data)


class RequestHeaderFieldsTooLargeError(BaseError):
    def __init__(self, message="Request Header Fields Too Large", optional_message=None, data=None):
        super().__init__(431, message, optional_message, data)


class UnavailableForLegalReasonsError(BaseError):
    def __init__(self, message="Unavailable For Legal Reasons", optional_message=None, data=None):
        super().__init__(451, message, optional_message, data)


class InternalServerError(BaseError):
    def __init__(self, message="Internal Server Error", optional_message=None, data=None):
        super().__init__(500, message, optional_message, data)


class NotImplementedError(BaseError):
    def __init__(self, message="Not Implemented", optional_message=None, data=None):
        super().__init__(501, message, optional_message, data)


class BadGatewayError(BaseError):
    def __init__(self, message="Bad Gateway", optional_message=None, data=None):
        super().__init__(502, message, optional_message, data)


class ServiceUnavailableError(BaseError):
    def __init__(self, message="Service Unavailable", optional_message=None, data=None):
        super().__init__(503, message, optional_message, data)


class GatewayTimeoutError(BaseError):
    def __init__(self, message="Gateway Timeout", optional_message=None, data=None):
        super().__init__(504, message, optional_message, data)


class HTTPVersionNotSupportedError(BaseError):
    def __init__(self, message="HTTP Version Not Supported", optional_message=None, data=None):
        super().__init__(505, message, optional_message, data)


class VariantAlsoNegotiatesError(BaseError):
    def __init__(self, message="Variant Also Negotiates", optional_message=None, data=None):
        super().__init__(506, message, optional_message, data)


class InsufficientStorageError(BaseError):
    def __init__(self, message="Insufficient Storage", optional_message=None, data=None):
        super().__init__(507, message, optional_message, data)


class LoopDetectedError(BaseError):
    def __init__(self, message="Loop Detected", optional_message=None, data=None):
        super().__init__(508, message, optional_message, data)


class NotExtendedError(BaseError):
    def __init__(self, message="Not Extended", optional_message=None, data=None):
        super().__init__(510, message, optional_message, data)


class NetworkAuthenticationRequiredError(BaseError):
    def __init__(self, message="Network Authentication Required", optional_message=None, data=None):
        super().__init__(511, message, optional_message, data)
