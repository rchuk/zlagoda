from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, JWTError
from pydantic import ValidationError

from auth import service
from auth.config import SECRET_KEY, ALGORITHM
from auth.exception import AccessError
from auth.schemas import UserResponse, TokenData

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/token",
    scopes={
        "CASHIER": "Operations available to cashier.",
        "MANAGER": "Operations available to manager.",
        "ADMIN": "Operations available to admin."
    }
)


async def current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("sub")
        if login is None:
            raise AccessError("Помилка при перевірці облікових даних")
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, login=login)
    except (JWTError, ValidationError):
        raise AccessError("Помилка при перевірці облікових даних")
    user = await service.get_user(login)
    if user is None:
        raise AccessError("Помилка при перевірці облікових даних")
    if len(security_scopes.scopes) == 0:
        return user
    for scope in token_data.scopes:
        if scope in security_scopes.scopes:
            return user
    raise AccessError("Не достатньо прав для виконання цієї операції")
