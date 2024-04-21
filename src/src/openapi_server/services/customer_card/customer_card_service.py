from openapi_server.entities.customer_card_entity import CustomerCardEntity
from openapi_server.models.customer_card import CustomerCard
from openapi_server.models.customer_card_view import CustomerCardView
from openapi_server.repositories.base.crud_repository_base import CrudRepositoryBase

from openapi_server.services.base.crud_service_base import CrudServiceBase
from openapi_server.services.base.merger_base import MergerBase
from openapi_server.services.base.validator_base import ValidatorBase


class CustomerCardService(CrudServiceBase[int, CustomerCardEntity, CustomerCardView, CustomerCard]):
    def __init__(
        self,
        repository: CrudRepositoryBase[id, CustomerCardEntity],
        merger: MergerBase[CustomerCardEntity, CustomerCardView],
        validator: ValidatorBase[CustomerCardEntity]
    ):
        super().__init__(
            repository, merger, validator,
            lambda: CustomerCardEntity.model_construct(id=-1),
            self._build_dto
        )

    @staticmethod
    def _build_dto(entity: CustomerCardEntity) -> CustomerCard:
        return CustomerCard(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            patronymic=entity.patronymic,
            phone_number=entity.phone_number,
            discount_percent=entity.discount_percent,
            city=entity.city,
            street=entity.street,
            zip_code=entity.zip_code
        )
