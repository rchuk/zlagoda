from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from openapi_server.containers import ApplicationContainer

from openapi_server.apis.customer_card_api import router as CustomerCardApiRouter
from openapi_server.apis.employee_api import router as EmployeeApiRouter
from openapi_server.apis.product_api import router as ProductApiRouter
from openapi_server.apis.product_archetype_api import router as ProductArchetypeApiRouter
from openapi_server.apis.product_category_api import router as ProductCategoryApiRouter
from openapi_server.apis.receipt_api import router as ReceiptApiRouter
from openapi_server.exceptions.app_exception_public import AppExceptionPublic

import openapi_server


def create_app() -> FastAPI:
    container = ApplicationContainer()
    # container.repositories.product_category_repository.override(
    #    providers.Singleton(ProductCategoryRepository)
    # )
    container.wire(packages=[openapi_server.impl, openapi_server.services, openapi_server.repositories])

    app = FastAPI(
        title="Zlagoda",
        description="API for systems used by the employees of Zlagoda shops",
        version="1.0.0",
    )
    app.container = container
    app.include_router(CustomerCardApiRouter)
    app.include_router(EmployeeApiRouter)
    app.include_router(ProductApiRouter)
    app.include_router(ProductArchetypeApiRouter)
    app.include_router(ProductCategoryApiRouter)
    app.include_router(ReceiptApiRouter)

    origins = [
        "http://localhost",
        "http://localhost:3000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    @app.exception_handler(AppExceptionPublic)
    async def public_exception_handler(request, exc: AppExceptionPublic):
        return PlainTextResponse(str(exc), status_code=400)

    return app


app = create_app()
