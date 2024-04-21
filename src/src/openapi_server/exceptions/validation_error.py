from openapi_server.exceptions.app_exception_public import AppExceptionPublic


class ValidationError(AppExceptionPublic):
    def __init__(self, message: str):
        super().__init__(message)
