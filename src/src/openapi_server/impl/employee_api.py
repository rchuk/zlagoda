from typing import List

from openapi_server.apis.employee_api_base import BaseEmployeeApi

from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_view import EmployeeView


class EmployeeApi(BaseEmployeeApi):
    def count_employee(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> int:
        return 666 # Test


    def create_employee(
        self,
        employee_view: EmployeeView,
    ) -> int:
        raise NotImplementedError()


    def delete_employee(
        self,
        id: int,
    ) -> bool:
        raise NotImplementedError()


    def get_employee_by_id(
        self,
        id: int,
    ) -> Employee:
        raise NotImplementedError()


    def get_employee_list(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> List[Employee]:
        raise NotImplementedError()


    def get_employee_me(
        self,
    ) -> int:
        raise NotImplementedError()


    def update_employee(
        self,
        id: int,
        employee_view: EmployeeView,
    ) -> bool:
        raise NotImplementedError()
