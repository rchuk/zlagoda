from datetime import datetime

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from auth.schemas import UserUpsertRequest
from customer_card.router import router as CustomerCardRouter
from database import pool
from auth import service as auth_service
from employee import service as employee_service
from employee.router import router as EmployeeRouter
from employee.schemas import EmployeeRole, EmployeeUpsertRequest
from exceptions import PublicError
from product.router import router as ProductRouter
from product_archetype.router import router as ProductArchetypeRouter
from product_category.router import router as ProductCategoryRouter
from receipt.router import router as ReceiptRouter
from auth.router import router as AuthRouter

from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
    title="Zlagoda",
    description="API for systems used by the employees of Zlagoda shops",
    version="1.0.0",
)

app.include_router(CustomerCardRouter)
app.include_router(EmployeeRouter)
app.include_router(ProductRouter)
app.include_router(ProductArchetypeRouter)
app.include_router(ProductCategoryRouter)
app.include_router(ReceiptRouter)
app.include_router(AuthRouter)

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

async def add_users():
    admin_login = "admin"
    admin_password = "admin"
    if await auth_service.get_user(admin_login) is None:
        await auth_service.add_user(UserUpsertRequest(login=admin_login, password=admin_password, roleId=1))
    manager_login = "manager"
    manager_password = "manager"
    if await auth_service.get_user(manager_login) is None:
        manager_id = await employee_service.add_employee(EmployeeUpsertRequest(lastName="manager",
                                                                  firstName="manager",
                                                                  role=EmployeeRole.MANAGER,
                                                                  salary=10000.,
                                                                  birthDate=datetime(year=2000, month=1, day=1).date(),
                                                                  workStartDate=datetime(year=2020, month=1, day=1).date(),
                                                                  phoneNumber="+380991331486",
                                                                  city="A",
                                                                  street="Abc",
                                                                  zipCode="ABC123"))
        await auth_service.add_user(UserUpsertRequest(login=manager_login, password=manager_password, roleId=2, employeeId=manager_id))
    cashier_login = "cashier"
    cashier_password = "cashier"
    if await auth_service.get_user(cashier_login) is None:
        manager_id = await employee_service.add_employee(EmployeeUpsertRequest(lastName="cashier",
                                                                               firstName="cashier",
                                                                               role=EmployeeRole.CASHIER,
                                                                               salary=7000.,
                                                                               birthDate=datetime(year=2002,
                                                                                                  month=1,
                                                                                                  day=1).date(),
                                                                               workStartDate=datetime(year=2022,
                                                                                                      month=1,
                                                                                                      day=1).date(),
                                                                               phoneNumber="+380991331487",
                                                                               city="B",
                                                                               street="Bcd",
                                                                               zipCode="BCD567"))
        await auth_service.add_user(UserUpsertRequest(login=cashier_login, password=cashier_password, roleId=3))


@app.on_event("startup")
async def on_startup():
    await pool.open()
    await add_users()


@app.on_event("shutdown")
async def close_pool():
    await pool.close()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=exc.status_code)


@app.exception_handler(PublicError)
async def public_exception_handler(request, exc):
    return PlainTextResponse(exc.details.msg, status_code=exc.details.code)
