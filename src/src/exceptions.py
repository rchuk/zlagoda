from fastapi import status
from pydantic import BaseModel


class ErrorDetails(BaseModel):
    msg: str
    code: int


class PublicError(Exception):
    def __init__(self, details: ErrorDetails):
        super().__init__(details.msg)
        self.details = details


class ValidationError(PublicError):
    def __init__(self, msg):
        self.details = ErrorDetails(msg=msg, code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        super().__init__(self.details)
