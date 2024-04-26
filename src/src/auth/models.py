from pydantic import BaseModel


class User(BaseModel):
    login: str
    password_hash: str
    role_id: int
    employee_id: str
