from datetime import timedelta, datetime, timezone

from jose import jwt
from passlib.context import CryptContext

from auth.config import SECRET_KEY, ALGORITHM

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def verify_hash(plain: str, hash: str) -> bool:
    return password_context.verify(plain, hash)


async def get_hash(plain: str) -> str:
    return password_context.hash(plain)


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
