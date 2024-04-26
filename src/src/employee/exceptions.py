from exceptions import ErrorDetails, PublicError
from fastapi import status


class EmployeeNotFoundException(PublicError):
    def __init__(self):
        self.details = ErrorDetails(msg="Працівника з таким id не існує", code=status.HTTP_404_NOT_FOUND)
        super().__init__(self.details)
