from dependency_injector.wiring import Provide, inject

from openapi_server.apis.employee_api_base import BaseEmployeeApi
from openapi_server.containers import ApplicationContainer

from openapi_server.models.employee import Employee
from openapi_server.models.employee_criteria import EmployeeCriteria
from openapi_server.models.employee_list_response import EmployeeListResponse
from openapi_server.models.employee_view import EmployeeView
from openapi_server.services.employee.employee_service import EmployeeService


class EmployeeApi(BaseEmployeeApi):
    @inject
    def __init__(
        self,
        employee_service: EmployeeService = Provide[ApplicationContainer.services.employee_service]
    ):
        self._service = employee_service

    def create_employee(
        self,
        employee_view: EmployeeView,
    ) -> int:
        return self._service.create(employee_view)

    def delete_employee(
        self,
        id: int,
    ) -> bool:
        return self._service.delete(id)

    def get_employee_by_id(
        self,
        id: int,
    ) -> Employee:
        return self._service.get(id)

    def get_employee_list(
        self,
        employee_criteria: EmployeeCriteria,
    ) -> EmployeeListResponse:
        return EmployeeListResponse(
            total_count=self._service.count(employee_criteria),
            items=self._service.list(employee_criteria)
        )

    def get_employee_me(
        self,
    ) -> int:
        # TODO
        raise NotImplementedError()

    def update_employee(
        self,
        id: int,
        employee_view: EmployeeView,
    ) -> bool:
        return self._service.update(id, employee_view)
