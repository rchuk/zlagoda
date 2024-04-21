from datetime import datetime

from dependency_injector import containers, providers

# from openapi_server.repositories.product_category_repository import ProductCategoryRepository
from openapi_server.repositories.in_memory_repository import InMemoryRepository

from openapi_server.entities.product_category_entity import ProductCategoryEntity
from openapi_server.entities.product_archetype_entity import ProductArchetypeEntity
from openapi_server.entities.customer_card_entity import CustomerCardEntity
from openapi_server.entities.employee_entity import EmployeeEntity
from openapi_server.entities.employee_role_entity_enum import EmployeeRoleEntityEnum


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

    employee_repository = providers.Singleton(
        InMemoryRepository,
        test_data=[
            EmployeeEntity(
                id=0,
                first_name="Дмитро",
                last_name="Запорожець",
                patronymic="Олександрович",
                role=EmployeeRoleEntityEnum.Manager,
                salary=25000,
                work_start_date=datetime(2020, 5, 1).date(),
                birth_date=datetime(2004, 12, 16).date(),
                phone_number="+380674400000",
                city="Київ",
                street="Якась вулиця",
                zip_code="01001"
            ),
            EmployeeEntity(
                id=2,
                first_name="Руслан",
                last_name="Омельчук",
                patronymic="Ігорович",
                role=EmployeeRoleEntityEnum.Cashier,
                salary=17000,
                work_start_date=datetime(2020, 11, 3).date(),
                birth_date=datetime(2004, 11, 24).date(),
                phone_number="+380664000000",
                city="Київ",
                street="Інша вулиця",
                zip_code="04210"
            )
        ]
    )
