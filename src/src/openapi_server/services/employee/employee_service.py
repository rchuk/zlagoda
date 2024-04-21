from openapi_server.entities.employee_entity import EmployeeEntity
from openapi_server.entities.employee_role_entity_enum import EmployeeRoleEntityEnum
from openapi_server.exceptions.app_exception import AppException
from openapi_server.models.employee import Employee
from openapi_server.models.employee_role import EmployeeRole
from openapi_server.models.employee_view import EmployeeView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class EmployeeService(CrudServiceBase[int, EmployeeEntity, EmployeeView, Employee]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, EmployeeEntity],
        merger: MergerBase[EmployeeEntity, EmployeeView],
        validator: ValidatorBase[EmployeeEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: EmployeeEntity.model_construct(id=-1),
            self._build_dto
        )

    @classmethod
    def _build_dto(cls, entity: EmployeeEntity) -> Employee:
        return Employee(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            patronymic=entity.patronymic,
            role=cls._build_role_enum_dto(entity.role),
            salary=entity.salary,
            work_start_date=entity.work_start_date,
            birth_date=entity.birth_date,
            phone_number=entity.phone_number,
            city=entity.city,
            street=entity.street,
            zip_code=entity.zip_code
        )

    @staticmethod
    def _build_role_enum_dto(role: EmployeeRoleEntityEnum) -> EmployeeRole:
        match role:
            case EmployeeRoleEntityEnum.Manager:
                return EmployeeRole.MANAGER
            case EmployeeRoleEntityEnum.Cashier:
                return EmployeeRole.CASHIER

        raise AppException("Unhandled EmployeeRoleEntityEnum")
