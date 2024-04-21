from openapi_server.exceptions.app_exception import AppException


class AppExceptionPublic(AppException):
    def __init__(self, message: str):
        super().__init__(message)
