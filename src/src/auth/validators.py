from auth.models import User
from auth.utils import verify_hash
from exceptions import ValidationError


async def validate_credentials(model: User, login: str, password: str) -> bool:
    if model is None:
        raise ValidationError("Користувача не існує")
    if model.login != login:
        raise ValidationError("Логіни повинні співпадати")
    if verify_hash(password, model.password_hash):
        raise ValidationError("Паролі повинні співпадати")
    return True