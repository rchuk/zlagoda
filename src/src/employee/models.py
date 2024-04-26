from datetime import date
from decimal import Decimal

from pydantic import BaseModel

from employee.schemas import EmployeeRole


class Employee(BaseModel):
    id: str
    last_name: str
    first_name: str
    patronymic: str | None = None
    role: EmployeeRole
    salary: Decimal
    birth_date: date
    work_start_date: date
    phone_number: str
    city: str
    street: str
    zip_code: str
