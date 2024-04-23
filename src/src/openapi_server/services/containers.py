from dependency_injector import containers, providers

from openapi_server.services.customer_card.customer_card_merger import CustomerCardMerger
from openapi_server.services.customer_card.customer_card_service import CustomerCardService
from openapi_server.services.customer_card.customer_card_validator import CustomerCardValidator
from openapi_server.services.employee.employee_merger import EmployeeMerger
from openapi_server.services.employee.employee_service import EmployeeService
from openapi_server.services.employee.employee_validator import EmployeeValidator
from openapi_server.services.product.product_merger import ProductMerger
from openapi_server.services.product.product_service import ProductService
from openapi_server.services.product.product_validator import ProductValidator
from openapi_server.services.product_archetype.product_archetype_merger import ProductArchetypeMerger
from openapi_server.services.product_archetype.product_archetype_service import ProductArchetypeService
from openapi_server.services.product_archetype.product_archetype_validator import ProductArchetypeValidator
from openapi_server.services.product_category.product_category_merger import ProductCategoryMerger
from openapi_server.services.product_category.product_category_service import ProductCategoryService
from openapi_server.services.product_category.product_category_validator import ProductCategoryValidator
from openapi_server.services.receipt.receipt_merger import ReceiptMerger
from openapi_server.services.receipt.receipt_service import ReceiptService
from openapi_server.services.receipt.receipt_validator import ReceiptValidator
from openapi_server.services.receipt_item.receipt_item_merger import ReceiptItemMerger
from openapi_server.services.receipt_item.receipt_item_service import ReceiptItemService
from openapi_server.services.receipt_item.receipt_item_validator import ReceiptItemValidator


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

    employee_merger = providers.Factory(EmployeeMerger)
    employee_validator = providers.Factory(EmployeeValidator)
    employee_service = providers.Factory(
        EmployeeService,
        repository=repositories.employee_repository,
        merger=employee_merger,
        validator=employee_validator
    )

    product_merger = providers.Factory(ProductMerger)
    product_validator = providers.Factory(
        ProductValidator,
        product_repository=repositories.product_repository,
        product_archetype_repository=repositories.product_archetype_repository
    )
    product_service = providers.Factory(
        ProductService,
        repository=repositories.product_repository,
        merger=product_merger,
        validator=product_validator
    )

    receipt_item_merger = providers.Factory(
        ReceiptItemMerger,
        product_repository=repositories.product_repository,
        receipt_repository=repositories.receipt_repository
    )
    receipt_item_validator = providers.Factory(
        ReceiptItemValidator,
        product_repository=repositories.product_repository,
        receipt_repository=repositories.receipt_repository
    )
    receipt_item_service = providers.Factory(
        ReceiptItemService,
        repository=repositories.receipt_item_repository,
        merger=receipt_item_merger,
        validator=receipt_item_validator,
        product_repository=repositories.product_repository
    )

    receipt_merger = providers.Factory(
        ReceiptMerger,
        product_repository=repositories.product_repository,
        receipt_repository=repositories.receipt_repository
    )
    receipt_validator = providers.Factory(
        ReceiptValidator,
        receipt_repository=repositories.receipt_repository,
        employee_repository=repositories.employee_repository,
        customer_card_repository=repositories.customer_card_repository
    )
    receipt_service = providers.Factory(
        ReceiptService,
        repository=repositories.receipt_repository,
        merger=receipt_merger,
        validator=receipt_validator,
        receipt_item_service=receipt_item_service
    )
