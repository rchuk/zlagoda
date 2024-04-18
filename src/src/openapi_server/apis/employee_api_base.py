# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_list_response import EmployeeListResponse
from openapi_server.models.employee_view import EmployeeView


class BaseEmployeeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEmployeeApi.subclasses = BaseEmployeeApi.subclasses + (cls,)
    def create_employee(
        self,
        employee_view: EmployeeView,
    ) -> int:
        """Create a new employee"""
        ...


    def delete_employee(
        self,
        id: int,
    ) -> bool:
        """Delete an employee by id"""
        ...


    def get_employee_by_id(
        self,
        id: int,
    ) -> Employee:
        """Get employee by id"""
        ...


    def get_employee_list(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> EmployeeListResponse:
        """Get list of employees"""
        ...


    def get_employee_me(
        self,
    ) -> int:
        """Get employee id of self"""
        ...


    def update_employee(
        self,
        id: int,
        employee_view: EmployeeView,
    ) -> bool:
        """Update existing employee"""
        ...
