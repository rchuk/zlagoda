from typing import Annotated

from pydantic import BaseModel, Field

from schemas import BaseCriteria, ListResponse


class CustomerCardBase(BaseModel):
    last_name: Annotated[str, Field(alias="lastName")]
    first_name: Annotated[str, Field(alias="firstName")]
    patronymic: str | None = None
    phone_number: Annotated[str, Field(alias="phoneNumber")]
    city: str | None = None
    street: str | None = None
    zip_code: Annotated[str | None, Field(alias="zipCode")] = None
    discount_percent: Annotated[int, Field(alias="discountPercent")]


class CustomerCardCriteria(BaseCriteria):
    ids: list[int] | None = None
    query: str | None = None
    last_name: Annotated[str | None, Field(alias="lastName")] = None
    phone_number: Annotated[str | None, Field(alias="phoneNumber")] = None


class CustomerCardUpsertRequest(CustomerCardBase):
    pass


class CustomerCardResponse(CustomerCardBase):
    id: int


class CustomerCardListResponse(ListResponse):
    items: list[CustomerCardResponse]
