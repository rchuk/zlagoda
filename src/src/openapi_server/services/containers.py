from dependency_injector import containers, providers

from openapi_server.services.customer_card.customer_card_merger import CustomerCardMerger
from openapi_server.services.customer_card.customer_card_service import CustomerCardService
from openapi_server.services.customer_card.customer_card_validator import CustomerCardValidator
from openapi_server.services.product_archetype.product_archetype_merger import ProductArchetypeMerger
from openapi_server.services.product_archetype.product_archetype_service import ProductArchetypeService
from openapi_server.services.product_archetype.product_archetype_validator import ProductArchetypeValidator
from openapi_server.services.product_category.product_category_merger import ProductCategoryMerger
from openapi_server.services.product_category.product_category_service import ProductCategoryService
from openapi_server.services.product_category.product_category_validator import ProductCategoryValidator


class ServicesContainer(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()

    product_category_merger = providers.Factory(ProductCategoryMerger)
    product_category_validator = providers.Factory(ProductCategoryValidator)
    product_category_service = providers.Factory(
        ProductCategoryService,
        repository=repositories.product_category_repository,
        merger=product_category_merger,
        validator=product_category_validator
    )

    product_archetype_merger = providers.Factory(ProductArchetypeMerger)
    product_archetype_validator = providers.Factory(
        ProductArchetypeValidator,
        product_category_repository=repositories.product_category_repository
    )
    product_archetype_service = providers.Factory(
        ProductArchetypeService,
        repository=repositories.product_archetype_repository,
        merger=product_archetype_merger,
        validator=product_archetype_validator
    )

    customer_card_merger = providers.Factory(CustomerCardMerger)
    customer_card_validator = providers.Factory(CustomerCardValidator)
    customer_card_service = providers.Factory(
        CustomerCardService,
        repository=repositories.customer_card_repository,
        merger=customer_card_merger,
        validator=customer_card_validator
    )
