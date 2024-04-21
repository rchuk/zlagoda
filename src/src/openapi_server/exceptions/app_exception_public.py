from openapi_server.exceptions.app_exception_base import AppExceptionBase


class AppExceptionPublic(AppExceptionBase):
    def __init__(self, message: str):
        super().__init__(message)
