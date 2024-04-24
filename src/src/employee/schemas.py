from datetime import date
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field

from schemas import BaseCriteria, ListResponse


class EmployeeRole(str, Enum):
    CASHIER = "CASHIER"
    MANAGER = "MANAGER"


class EmployeeBase(BaseModel):
    last_name: Annotated[str, Field(alias="lastName")]
    first_name: Annotated[str, Field(alias="firstName")]
    patronymic: str | None = None
    role: EmployeeRole
    salary: int
    birth_date: Annotated[date, Field(alias="birthDate")]
    work_start_date: Annotated[date, Field(alias="workStartDate")]
    phone_number: Annotated[str, Field(alias="phoneNumber")]
    city: str
    street: str
    zip_code: Annotated[str, Field(alias="zipCode")]


class EmployeeCriteria(BaseCriteria):
    ids: list[int] | None = None
    query: str | None = None
    role: EmployeeRole | None = None
    last_name: Annotated[str | None, Field(alias="lastName")] = None


class EmployeeUpsertRequest(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int


class EmployeeListResponse(ListResponse):
    items: list[EmployeeResponse]
