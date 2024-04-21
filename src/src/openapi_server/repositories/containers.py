from dependency_injector import containers, providers

# from openapi_server.repositories.product_category_repository import ProductCategoryRepository

from openapi_server.repositories.in_memory_repository import InMemoryRepository
from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.entities.customer_card_entity import CustomerCardEntity


class RepositoryContainer(containers.DeclarativeContainer):
    product_category_repository = providers.Singleton(
        # ProductCategoryRepository,
        InMemoryRepository,
        test_data=[
            ProductCategoryEntity(
                id=0,
                name="Харчові продукти"
            ),
            ProductCategoryEntity(
                id=1,
                name="Косметика та парфумерія"
            )
        ]
    )

    product_archetype_repository = providers.Singleton(
        InMemoryRepository,
        test_data=[
            ProductArchetypeEntity(
                id=0,
                name="Яблука",
                category=0,
                manufacturer="Зібрані десь",
                description="Дуже гарні червоні яблука"
            ),
            ProductArchetypeEntity(
                id=1,
                name="Печиво шоколадне",
                category=0,
                manufacturer="Roshen",
                description="Печиво з шоколадною крихтою"
            ),
            ProductArchetypeEntity(
                id=2,
                name="Мило",
                category=1,
                manufacturer="Невідомо хто",
                description="Просто мило"
            )
        ]
    )

    customer_card_repository = providers.Singleton(
        InMemoryRepository,
        test_data=[
            CustomerCardEntity(
                id=0,
                first_name="Іван",
                last_name="Абрамов",
                patronymic="Ігорович",
                phone_number="+380974630000",
                discount_percent=20,
                city="Бровари",
                street="Головна",
                zip_code="55555"
            ),
            CustomerCardEntity(
                id=1,
                first_name="Артем",
                last_name="Гречка",
                patronymic="Віталійович",
                phone_number="+380996840184",
                discount_percent=0,
                city="Київ",
                street="Вулиція Гетьмана Данила",
                zip_code="04555"
            )
        ]
    )
