from auth.schemas import (
    UserUpsertRequest,
    UserResponse,
    UserListResponse
)

from auth.models import User
from auth.utils import get_hash


async def upsert_request_to_model(user: UserUpsertRequest) -> User:
    return User.model_construct(
        login=user.login,
        password_hash=get_hash(user.password),
        role_id=user.role_id,
        employee_id=user.employee_id
    )


async def model_to_response(user: User) -> UserResponse:
    return UserResponse.model_construct(
        login=user.login,
        roleId=user.role_id,
        employeeId=user.employee_id
    )


async def model_list_to_response_list(user_list: list[User], count: int) -> UserListResponse:
    return UserListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in user_list]
    )
