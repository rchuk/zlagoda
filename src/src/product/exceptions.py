from fastapi import status

from exceptions import PublicError, ErrorDetails


class ProductNotFound(PublicError):
    def __init__(self):
        self.details = ErrorDetails(msg="Продукта з таким upc не існує", code=status.HTTP_404_NOT_FOUND)
        super().__init__(self.details)