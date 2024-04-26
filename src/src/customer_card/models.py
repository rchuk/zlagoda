from pydantic import BaseModel


class CustomerCard(BaseModel):
    id: str
    last_name: str
    first_name: str
    patronymic: str | None = None
    phone_number: str
    city: str | None = None
    street: str | None = None
    zip_code: str | None = None
    discount_percent: int
