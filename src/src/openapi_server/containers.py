from dependency_injector import containers, providers

from openapi_server.repositories.containers import RepositoryContainer
from openapi_server.services.containers import ServicesContainer


class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(
        RepositoryContainer
    )

    services = providers.Container(
        ServicesContainer,
        repositories=repositories
    )
