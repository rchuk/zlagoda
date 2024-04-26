from employee import repository
from employee.schemas import (
    EmployeeCriteria,
    EmployeeUpsertRequest,
    EmployeeResponse,
    EmployeeListResponse
)

from employee.converters import (
    upsert_request_to_model,
    model_to_response,
    model_list_to_response_list
)

from employee.validators import validate_model, validate_exists


async def add_employee(employee: EmployeeUpsertRequest) -> int:
    employee = await upsert_request_to_model(employee)
    await validate_model(employee)
    id = await repository.create(employee)
    return id


async def get_employee(id: str) -> EmployeeResponse:
    await validate_exists(id)
    result = await repository.read_one(id)
    result = await model_to_response(result)
    return result


async def list_employees(employee_criteria: EmployeeCriteria) -> EmployeeListResponse:
    result_list = await repository.read(employee_criteria)
    result_count = await repository.count(employee_criteria)
    result = await model_list_to_response_list(result_list, result_count)
    return result


async def update_employee(id: str, employee: EmployeeUpsertRequest) -> bool:
    await validate_exists(id)
    employee = await upsert_request_to_model(employee)
    employee.id = id
    await validate_model(employee)
    success = await repository.update(employee)
    return success


async def delete_employee(id: str) -> bool:
    await validate_exists(id)
    success = await repository.delete(id)
    return success
