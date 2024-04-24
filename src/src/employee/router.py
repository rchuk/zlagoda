from typing import Annotated

from fastapi import (
    APIRouter,
    Body,
    Path,
)

from employee.models import (
    EmployeeCriteria,
    EmployeeUpsertRequest,
    EmployeeResponse,
    EmployeeListResponse
)

router = APIRouter()


@router.post("/api/employee")
async def create_employee(
    employee_upsert_request: Annotated[EmployeeUpsertRequest | None, Body()] = None,
) -> int:
    pass


@router.delete("/api/employee/{id}")
async def delete_employee(
    id: Annotated[int, Path()],
) -> bool:
    pass


@router.get("/api/employee/{id}", response_model=EmployeeResponse)
async def get_employee_by_id(
    id: Annotated[int, Path()]
) -> EmployeeResponse:
    pass


@router.post("/api/employee/list", response_model=EmployeeListResponse)
async def get_employee_list(
    employee_criteria: Annotated[EmployeeCriteria | None, Body()] = None
) -> EmployeeListResponse:
    pass


@router.put("/api/employee/{id}")
async def update_employee(
    id: Annotated[int, Path()],
    employee_upsert_request: Annotated[EmployeeUpsertRequest | None, Body()] = None
) -> bool:
    pass
