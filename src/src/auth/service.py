from auth import repository, converters, validators
from auth.schemas import UserResponse


async def get_user(login: str) -> UserResponse | None:
    user = await repository.read_one(login)
    if user is None:
        return None
    user = await converters.model_to_response(user)
    return user


async def authenticate_user(login: str, password: str) -> UserResponse | None:
    user = await repository.read_one(login)
    await validators.validate_credentials(user, login, password)
    user = await converters.model_to_response(user)
    return user


async def get_role(id: int) -> str:
    role = await repository.role_map(id)
    return role
