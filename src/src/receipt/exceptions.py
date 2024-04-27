from fastapi import status

from exceptions import PublicError, ErrorDetails


class ReceiptNotFound(PublicError):
    def __init__(self):
        self.details = ErrorDetails(msg="Чеку з таким id не існує", code=status.HTTP_404_NOT_FOUND)
        super().__init__(self.details)
