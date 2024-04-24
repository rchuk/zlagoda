from fastapi import FastAPI

from customer_card.router import router as CustomerCardRouter
from employee.router import router as EmployeeRouter
from product.router import router as ProductRouter
from product_archetype.router import router as ProductArchetypeRouter
from product_category.router import router as ProductCategoryRouter
from receipt.router import router as ReceiptRouter

from fastapi.middleware.cors import CORSMiddleware

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
