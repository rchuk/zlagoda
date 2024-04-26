from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from employee.schemas import (
    EmployeeCriteria,
    EmployeeUpsertRequest,
    EmployeeResponse,
    EmployeeListResponse
)

from employee import service

router = APIRouter()


@router.post("/api/employee")
async def create_employee(
    employee_upsert_request: Annotated[EmployeeUpsertRequest | None, Body()] = None,
) -> str:
    return await service.add_employee(employee_upsert_request)


@router.delete("/api/employee/{id}")
async def delete_employee(
    id: Annotated[str, Path()],
) -> bool:
    return await service.delete_employee(id)


@router.get("/api/employee/{id}", response_model=EmployeeResponse)
async def get_employee_by_id(
    id: Annotated[str, Path()]
) -> EmployeeResponse:
    return await service.get_employee(id)


@router.post("/api/employee/list", response_model=EmployeeListResponse)
async def get_employee_list(
    employee_criteria: Annotated[EmployeeCriteria | None, Body()] = None
) -> EmployeeListResponse:
    return await service.list_employees(employee_criteria)


@router.put("/api/employee/{id}")
async def update_employee(
    id: Annotated[str, Path()],
    employee_upsert_request: Annotated[EmployeeUpsertRequest | None, Body()] = None
) -> bool:
    return await service.update_employee(id, employee_upsert_request)
