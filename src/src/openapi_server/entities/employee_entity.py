from datetime import date
from typing import Optional

from pydantic import BaseModel, StrictStr, StrictInt

from openapi_server.entities.employee_role_entity_enum import EmployeeRoleEntityEnum


class EmployeeEntity(BaseModel):
    id: StrictInt
    first_name: StrictStr
    last_name: StrictStr
    patronymic: Optional[StrictStr]
    role: EmployeeRoleEntityEnum
    salary: StrictInt
    work_start_date: date
    birth_date: date
    phone_number: StrictStr
    city: StrictStr
    street: StrictStr
    zip_code: StrictStr
