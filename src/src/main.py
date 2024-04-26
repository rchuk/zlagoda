from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from customer_card.router import router as CustomerCardRouter
from database import pool
from employee.router import router as EmployeeRouter
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


@app.on_event("startup")
async def open_pool():
    await pool.open()


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
