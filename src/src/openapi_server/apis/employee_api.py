# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.employee_api_base import BaseEmployeeApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_list_response import EmployeeListResponse
from openapi_server.models.employee_view import EmployeeView


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/api/employee",
    responses={
        200: {"model": int, "description": "Id of new employee"},
    },
    tags=["employee"],
    summary="Create a new employee",
    response_model_by_alias=True,
)
async def create_employee(
    employee_view: EmployeeView = Body(None, description=""),
) -> int:
    """Create a new employee"""
    return BaseEmployeeApi.subclasses[0]().create_employee(employee_view)


@router.delete(
    "/api/employee/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether employee was deleted"},
    },
    tags=["employee"],
    summary="Delete an employee by id",
    response_model_by_alias=True,
)
async def delete_employee(
    id: int = Path(..., description=""),
) -> bool:
    """Delete an employee by id"""
    return BaseEmployeeApi.subclasses[0]().delete_employee(id)


@router.get(
    "/api/employee/{id}",
    responses={
        200: {"model": Employee, "description": "Employee by id"},
    },
    tags=["employee"],
    summary="Get employee by id",
    response_model_by_alias=True,
)
async def get_employee_by_id(
    id: int = Path(..., description=""),
) -> Employee:
    """Get employee by id"""
    return BaseEmployeeApi.subclasses[0]().get_employee_by_id(id)


@router.post(
    "/api/employee",
    responses={
        200: {"model": EmployeeListResponse, "description": "List of employees"},
    },
    tags=["employee"],
    summary="Get list of employees",
    response_model_by_alias=True,
)
async def get_employee_list(
    employee_criteria: EmployeeCriteria = Body(None, description=""),
) -> EmployeeListResponse:
    """Get list of employees"""
    return BaseEmployeeApi.subclasses[0]().get_employee_list(employee_criteria)


@router.get(
    "/api/employee/me",
    responses={
        200: {"model": int, "description": "Employee id of self"},
    },
    tags=["employee"],
    summary="Get employee id of self",
    response_model_by_alias=True,
)
async def get_employee_me(
) -> int:
    """Get employee id of self"""
    return BaseEmployeeApi.subclasses[0]().get_employee_me()


@router.post(
    "/api/employee/{id}",
    responses={
        200: {"model": bool, "description": "Boolean whether employee was updated"},
    },
    tags=["employee"],
    summary="Update existing employee",
    response_model_by_alias=True,
)
async def update_employee(
    id: int = Path(..., description=""),
    employee_view: EmployeeView = Body(None, description=""),
) -> bool:
    """Update existing employee"""
    return BaseEmployeeApi.subclasses[0]().update_employee(id, employee_view)
