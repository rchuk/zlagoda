from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field

from schemas import ListResponse, BaseCriteria


class UserRole(str, Enum):
    CASHIER = "CASHIER"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str | None = None
    scopes: list[str] = []


class UserBase(BaseModel):
    login: str
    role_id: Annotated[int, Field(alias="roleId")]
    employee_id: Annotated[str | None, Field(alias="employeeId")] = None


class UserCriteria(BaseCriteria):
    ids: list[str] | None = None


class UserUpsertRequest(UserBase):
    password: str


class UserResponse(UserBase):
    role: Annotated[str, Field(alias="roleId")]


class UserListResponse(ListResponse):
    items: list[UserResponse]
