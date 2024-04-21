from dependency_injector import containers, providers

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
