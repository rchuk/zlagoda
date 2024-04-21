from dependency_injector import containers, providers

from openapi_server.repositories.product_category_repository import ProductCategoryRepository


class RepositoryContainer(containers.DeclarativeContainer):
    product_category_repository = providers.Singleton(ProductCategoryRepository)
