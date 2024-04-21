from abc import ABC


class AppException(ABC, Exception):
    def __init__(self, message: str):
        super().__init__(message)
