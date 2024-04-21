from openapi_server.entities.customer_card_entity import CustomerCardEntity
from openapi_server.models.customer_card_view import CustomerCardView
from openapi_server.services.base.merger_base import MergerBase


class CustomerCardMerger(MergerBase[CustomerCardEntity, CustomerCardView]):
    def merge_create(self, entity: CustomerCardEntity, view: CustomerCardView):
        self.merge_main_fields(entity, view)

    def merge_edit(self, entity: CustomerCardEntity, view: CustomerCardView):
        self.merge_main_fields(entity, view)

    def merge_main_fields(self, entity: CustomerCardEntity, view: CustomerCardView):
        entity.first_name = view.first_name.strip()
        entity.last_name = view.last_name.strip()
        entity.patronymic = self._strip_optional(view.patronymic)
        entity.phone_number = view.phone_number.strip()
        entity.discount_percent = view.discount_percent
        entity.city = self._strip_optional(view.city)
        entity.street = self._strip_optional(view.street)
        entity.zip_code = self._strip_optional(view.zip_code)
