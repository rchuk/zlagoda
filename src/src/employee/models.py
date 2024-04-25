from datetime import date

from pydantic import BaseModel

from employee.schemas import EmployeeRole


class Employee(BaseModel):
    id: int
    last_name: str
    first_name: str
    patronymic: str | None = None
    role: EmployeeRole
    salary: int
    birth_date: date
    work_start_date: date
    phone_number: str
    city: str
    street: str
    zip_code: str
