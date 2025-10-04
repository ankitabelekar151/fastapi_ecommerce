from fastapi import FastAPI
from app.account.routers import router as account_router
from app.product.routers.category import router as category_router
from app.product.routers.product import router as products_router
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.mount("/media", StaticFiles(directory="media"), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_router, prefix="/api/account", tags=["Account"])
app.include_router(category_router, prefix="/api/product-category", tags=["Product Category"])
app.include_router(products_router, prefix="/api/products", tags=["Products"])