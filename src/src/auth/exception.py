from fastapi import status

from exceptions import PublicError, ErrorDetails


class AccessError(PublicError):
    def __init__(self, msg: str):
        details = ErrorDetails(msg=msg, code=status.HTTP_401_UNAUTHORIZED)
        super().__init__(details)


class CredentialsError(PublicError):
    def __init__(self):
        details = ErrorDetails(msg="Неправильний логін чи пароль", code=status.HTTP_400_BAD_REQUEST)
        super().__init__(details)
