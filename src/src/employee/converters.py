from employee.schemas import (
    EmployeeUpsertRequest,
    EmployeeResponse,
    EmployeeListResponse
)

from employee.models import Employee
from utils import float_to_decimal


async def upsert_request_to_model(employee: EmployeeUpsertRequest) -> Employee:
    return Employee.model_construct(
        last_name=employee.last_name,
        first_name=employee.first_name,
        patronymic=employee.patronymic,
        role=employee.role,
        salary=float_to_decimal(employee.salary),
        birth_date=employee.birth_date,
        work_start_date=employee.work_start_date,
        phone_number=employee.phone_number,
        city=employee.city,
        street=employee.street,
        zip_code=employee.zip_code,
    )


async def model_to_response(employee: Employee) -> EmployeeResponse:
    return EmployeeResponse.model_construct(
        id=employee.id,
        lastName=employee.last_name,
        firstName=employee.first_name,
        patronymic=employee.patronymic,
        role=employee.role,
        salary=float(employee.salary),
        birth_date=employee.birth_date,
        work_start_date=employee.work_start_date,
        phone_number=employee.phone_number,
        city=employee.city,
        street=employee.street,
        zipCode=employee.zip_code
    )


async def model_list_to_response_list(employee_list: list[Employee], count: int) -> EmployeeListResponse:
    return EmployeeListResponse.model_construct(
        totalCount=count,
        items=[await model_to_response(model) for model in employee_list]
    )
