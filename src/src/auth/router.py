from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, Security
from fastapi.security import OAuth2PasswordRequestForm

from auth import service
from auth.config import ACCESS_TOKEN_EXPIRE_TIME
from auth.exception import CredentialsError
from auth.schemas import Token, UserResponse
from auth.utils import create_access_token
from auth.dependencies import current_user

router = APIRouter()


@router.post("/api/token")
async def login_for_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise CredentialsError()
    scopes = [await service.get_role(user.role_id)]
    access_token_expires = ACCESS_TOKEN_EXPIRE_TIME
    access_token = await create_access_token(
        data={"sub": user.login, "scopes": scopes},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/api/users/me")
async def get_user_me(
        user: Annotated[UserResponse, Security(current_user)]
) -> UserResponse:
    return user
