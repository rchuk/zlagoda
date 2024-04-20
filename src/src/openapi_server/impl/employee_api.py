from datetime import datetime
from typing import Dict

from openapi_server.apis.employee_api_base import BaseEmployeeApi

from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_list_response import EmployeeListResponse
from openapi_server.models.employee_role import EmployeeRole
from openapi_server.models.employee_view import EmployeeView


class EmployeeApi(BaseEmployeeApi):
    def __init__(self):
        self._employees: Dict[int, Employee] = {
            0: Employee(
                id=0,
                first_name="Дмитро",
                last_name="Запорожець",
                patronymic="Олександрович",
                role=EmployeeRole.MANAGER,
                salary=25000,
                work_start_date=datetime(2020, 5, 1).date().isoformat(),
                birth_date=datetime(2004, 12, 16).date().isoformat(),
                phone_number="+380674400000",
                city="Київ",
                street="Якась вулиця",
                zip_code="01001"
            ),
            2: Employee(
                id=2,
                first_name="Руслан",
                last_name="Омельчук",
                patronymic="Ігорович",
                role=EmployeeRole.CASHIER,
                salary=17000,
                work_start_date=datetime(2020, 11, 3).date().isoformat(),
                birth_date=datetime(2004, 11, 24).date().isoformat(),
                phone_number="+380664000000",
                city="Київ",
                street="Інша вулиця",
                zip_code="04210"
            )
        }

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
        return self._employees[id]


    def get_employee_list(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> EmployeeListResponse:
        # TODO: Handle paging
        return EmployeeListResponse(total_count=len(self._employees), items=list(self._employees.values()))


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
