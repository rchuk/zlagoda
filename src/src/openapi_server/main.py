import os

from dependency_injector import providers
from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from psycopg_pool import ConnectionPool

from openapi_server.containers import ApplicationContainer

from openapi_server.apis.customer_card_api import router as CustomerCardApiRouter
from openapi_server.apis.employee_api import router as EmployeeApiRouter
from openapi_server.apis.product_api import router as ProductApiRouter
from openapi_server.apis.product_archetype_api import router as ProductArchetypeApiRouter
from openapi_server.apis.product_category_api import router as ProductCategoryApiRouter
from openapi_server.apis.receipt_api import router as ReceiptApiRouter
from openapi_server.exceptions.app_exception_public import AppExceptionPublic

import openapi_server


def get_db_url() -> str:
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ["POSTGRES_HOST"]
    port = os.environ["POSTGRES_PORT"]
    name = os.environ["POSTGRES_NAME"]

    return f"postgresql://{user}:{password}@{host}:{port}/{name}"


def create_app() -> FastAPI:
    container = ApplicationContainer()
    container.repositories.db_pool.override(
        providers.Singleton(
            ConnectionPool,
            conninfo=get_db_url(),
            open=True
        )
    )
    container.wire(
        packages=[openapi_server.impl, openapi_server.services, openapi_server.repositories],
        modules=[__name__]
    )

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

    @inject
    @app.on_event("shutdown")
    async def close_pool(pool: ConnectionPool = Provide[ApplicationContainer.repositories.db_pool]):
        pool.close()

    return app


app = create_app()
