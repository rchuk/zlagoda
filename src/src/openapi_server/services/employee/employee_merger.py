from openapi_server.entities.employee_entity import EmployeeEntity
from openapi_server.entities.employee_role_entity_enum import EmployeeRoleEntityEnum
from openapi_server.exceptions.app_exception import AppException
from openapi_server.models.employee_role import EmployeeRole
from openapi_server.models.employee_view import EmployeeView
from openapi_server.services.base.merger_base import MergerBase


class EmployeeMerger(MergerBase[EmployeeEntity, EmployeeView]):
    def merge_create(self, entity: EmployeeEntity, view: EmployeeView):
        self._merge_main_fields(entity, view)

    def merge_edit(self, entity: EmployeeEntity, view: EmployeeView):
        self._merge_main_fields(entity, view)

    def _merge_main_fields(self, entity: EmployeeEntity, view: EmployeeView):
        entity.first_name = view.first_name.strip()
        entity.last_name = view.last_name.strip()
        entity.patronymic = self._strip_optional(view.patronymic)
        entity.role = self._map_role(view.role)
        entity.salary = view.salary
        entity.work_start_date = view.work_start_date
        entity.birth_date = view.birth_date
        entity.phone_number = view.phone_number.strip()
        entity.city = view.city.strip()
        entity.street = view.street.strip()
        entity.zip_code = view.zip_code.strip()

    @staticmethod
    def _map_role(role: EmployeeRole) -> EmployeeRoleEntityEnum:
        match role:
            case EmployeeRole.MANAGER:
                return EmployeeRoleEntityEnum.Manager
            case EmployeeRole.CASHIER:
                return EmployeeRoleEntityEnum.Cashier

        raise AppException("Unhandled EmployeeRole")
