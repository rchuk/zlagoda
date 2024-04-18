# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_view import EmployeeView


class BaseEmployeeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEmployeeApi.subclasses = BaseEmployeeApi.subclasses + (cls,)
    def count_employee(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> int:
        ...


    def create_employee(
        self,
        employee_view: EmployeeView,
    ) -> int:
        ...


    def delete_employee(
        self,
        id: int,
    ) -> bool:
        ...


    def get_employee_by_id(
        self,
        id: int,
    ) -> Employee:
        ...


    def get_employee_list(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> List[Employee]:
        ...


    def get_employee_me(
        self,
    ) -> int:
        ...


    def update_employee(
        self,
        id: int,
        employee_view: EmployeeView,
    ) -> bool:
        ...
